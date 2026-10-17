"""Ручний прогін вашого запиту без тестів.

Використання:  python try_it.py <номер_задачі> [--explain]
Скрипт створює тимчасову схему, завантажує схему й дані вашого набору (за VARIANT у файлі variants/variant_NN.py),
виконує запит із вашої функції (у задачі 9 обидва запити) і друкує назви стовпців та рядки результату.
З параметром --explain додатково друкує план виконання (EXPLAIN ANALYZE): так можна порівняти запити.
Тимчасова схема видаляється наприкінці.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "tests"))

import pgutil  # noqa: E402
from conftest import load  # noqa: E402
from schemas import SCHEMAS  # noqa: E402


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args or not args[0].isdigit():
        print(__doc__)
        return 1
    task = int(args[0])
    explain = "--explain" in sys.argv
    mod = load(task)
    variant = getattr(mod, "VARIANT", 0)
    if not variant or (variant - 1) // 3 + 1 != task:
        print(f"Вкажіть у variant_{task:02d}.py змінну VARIANT зі значенням {3 * task - 2}-{3 * task}.")
        return 1
    set_no = (variant - 1) % 3 + 1
    names = ["query_exists", "query_join"] if task == 9 else ["query"]
    db = pgutil.Db()
    try:
        db.run(SCHEMAS[set_no])
        for name in names:
            sql = getattr(mod, name)()
            print(f"=== {name}()")
            cols, rows = db.query(sql)
            print(" | ".join(cols))
            for row in rows:
                print(" | ".join("NULL" if v is None else str(v) for v in row))
            print(f"--- рядків: {len(rows)}")
            if explain:
                print("--- план виконання")
                for (line,) in db.rows("EXPLAIN (ANALYZE, COSTS OFF, TIMING OFF) " + sql):
                    print(line)
    except pgutil.ScriptError as error:
        print("Помилка SQL:", error)
        return 1
    except NotImplementedError:
        print("Функцію ще не реалізовано.")
        return 1
    finally:
        db.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
