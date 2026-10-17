"""Виконання перевірок зі специфікацій (specs.py): результат запиту студента порівнюється з еталонним набором рядків."""
import inspect
import re
from decimal import Decimal

import pytest

import pgutil
from schemas import SCHEMAS


def fail(message):
    pytest.fail(message, pytrace=False)


def norm(value):
    if value is None:
        return None
    if isinstance(value, Decimal):
        return format(value, "f")
    return str(value)


def norm_rows(rows):
    return [tuple(norm(v) for v in row) for row in rows]


def call(mod, name, task, set_no):
    """Викликає функцію варіанта. Еталон приймає номер набору; студентська функція без параметрів
    працює для набору, що випливає з константи VARIANT."""
    fn = getattr(mod, name, None)
    if fn is None:
        fail(f"У файлі варіанта немає функції {name}()")
    if inspect.signature(fn).parameters:
        return fn(set_no)
    variant = getattr(mod, "VARIANT", 0)
    if not variant:
        fail("Змінну VARIANT не задано: впишіть номер свого варіанта (1-30) на початку файла")
    if (variant - 1) // 3 + 1 != task:
        fail(f"VARIANT = {variant} не відповідає задачі {task}: файл variant_{task:02d}.py призначений "
             f"для варіантів {3 * task - 2}-{3 * task}")
    if (variant - 1) % 3 + 1 != set_no:
        pytest.skip("перевірка іншого набору даних")
    try:
        return fn()
    except NotImplementedError:
        fail(f"Функція {name}() ще не реалізована (NotImplementedError)")


def strip_sql(sql):
    """Прибирає коментарі й текстові літерали, стискає пробіли, переводить у верхній регістр."""
    text = re.sub(r"/\*.*?\*/", " ", sql, flags=re.S)
    text = re.sub(r"--[^\n]*", " ", text)
    text = re.sub(r"'(?:[^']|'')*'", "''", text)
    text = re.sub(r"\s+", " ", text).strip().rstrip(";").strip()
    return text.upper()


def need_query(value, name):
    if not isinstance(value, str) or not value.strip():
        fail(f"{name}() має повертати непорожній рядок з одним запитом SELECT або WITH")
    clean = strip_sql(value)
    if ";" in clean:
        fail(f"{name}() має повертати один запит (без зайвих команд після крапки з комою)")
    if not re.match(r"(SELECT|WITH|\()", clean):
        fail(f"{name}() має повертати запит, що починається зі SELECT або WITH")
    return value


def check_form(sql, rules):
    clean = strip_sql(sql)
    for rule in rules:
        kind, rx = rule[0], rule[1]
        if kind == "need" and not re.search(rx, clean, re.S):
            fail("Запит не відповідає вимозі до конструкції: " + rule[2])
        if kind == "forbid" and re.search(rx, clean, re.S):
            fail("Запит використовує заборонену тут конструкцію: " + rule[2])
        if kind == "min" and len(re.findall(rx, clean)) < rule[2]:
            fail("Запит не відповідає вимозі до конструкції: " + rule[3])
        if kind == "max" and len(re.findall(rx, clean)) > rule[2]:
            fail("Запит не відповідає вимозі до конструкції: " + rule[3])


def run_case(db, mod, task, set_no, spec, chk):
    db.run(SCHEMAS[set_no])
    for sql in chk["setup"]:
        db.run(sql)
    name = chk["func"]
    text = need_query(call(mod, name, task, set_no), name)
    if chk["form"]:
        check_form(text, chk["form"])
        return
    try:
        cols, rows = db.query(text)
    except pgutil.ScriptError as error:
        fail(f"Запит завершився помилкою {error}")
    want_cols = [c.lower() for c in chk["cols"]]
    if [c.lower() for c in cols] != want_cols:
        fail(f"Перевірка «{chk['id']}»: очікувались стовпці {want_cols}, отримано {[c.lower() for c in cols]}. "
             "Назви й порядок стовпців задано в картці варіанта (використайте AS).")
    got, want = sorted(norm_rows(rows), key=repr), sorted(norm_rows(chk["expect"]), key=repr)
    if got != want:
        missing = [r for r in want if r not in got]
        extra = [r for r in got if r not in want]
        lines = [f"Перевірка «{chk['id']}»: очікувалось рядків {len(want)}, отримано {len(got)}."]
        if missing:
            lines.append("Бракує: " + "; ".join(map(str, missing[:3])) + (" ..." if len(missing) > 3 else ""))
        if extra:
            lines.append("Зайві або інші: " + "; ".join(map(str, extra[:3])) + (" ..." if len(extra) > 3 else ""))
        if len(got) == len(want) and not missing and not extra:
            lines.append("Кількість збігається, але набори різні (можливі дублікати).")
        fail("\n".join(lines))
