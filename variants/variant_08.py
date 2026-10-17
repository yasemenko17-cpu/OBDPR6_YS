"""Задача 8. CTE: покроковий запит.

Опис і умови: student.md, розділ «Опис задач», задача 8; картка вашого варіанта.
Відкриті тести: pytest -k "T08"
"""

# Впишіть номер свого варіанта (22-24).
VARIANT = 23

def query():
    return """
    WITH cat_sales AS (
        SELECT c.name, SUM(p.quantity) AS taken
        FROM category c
        JOIN product pr ON pr.category_id = c.id
        JOIN purchase p ON p.product_id = pr.id
        GROUP BY c.id, c.name
    ),
    total_sales AS (
        SELECT SUM(taken) AS total FROM cat_sales
    )
    SELECT 
        cs.name, 
        cs.taken, 
        ROUND(100.0 * cs.taken / ts.total, 1) AS share
    FROM cat_sales cs
    CROSS JOIN total_sales ts
    ORDER BY cs.taken DESC;
    """