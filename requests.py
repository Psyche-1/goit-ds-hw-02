import sqlite3
from pprint import pprint

DATABASE = 'tasks.db'

def execute_query(sql: str) -> list:
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

if __name__ == '__main__':
    sql = """
    SELECT *
    FROM tasks
    WHERE user_id = 1
    """
    # pprint(execute_query(sql))

    sql = """
    SELECT *
    FROM tasks
    WHERE status_id IN (SELECT id
    FROM status
    WHERE name = 'new')
    """
    # pprint(execute_query(sql))

    sql = """
    UPDATE tasks SET status_id = 2 WHERE id = 1
    """
    # execute_query(sql)

    sql = """
    SELECT *
    FROM users
    WHERE id NOT IN (SELECT user_id
    FROM tasks
    )
    """
    # pprint(execute_query(sql))

    sql = """
    INSERT INTO tasks (title, description, status_id, user_id)
    VALUES ('Homework', 'Add new task for specific user', 1, 1)
    """
    # execute_query(sql)

    sql = """
    SELECT *
    FROM tasks
    WHERE status_id NOT IN (SELECT id
    FROM status
    WHERE name = 'completed')
    """
    # pprint(execute_query(sql))

    sql = """
    DELETE FROM tasks
    WHERE id = 20
    """
    # execute_query(sql)

    sql = """
    SELECT *
    FROM users
    WHERE email LIKE 'handerson@example.com'
    """
    # pprint(execute_query(sql))

    sql = """
    UPDATE users SET fullname = 'Noname Nonamenko' WHERE fullname = 'Cynthia Miller'
    """
    # execute_query(sql)

    sql = """
    SELECT COUNT(id) as total_tasks, status_id
    FROM tasks
    GROUP BY status_id
    """
    # pprint(execute_query(sql))

    sql = """
    SELECT *
    FROM tasks
    WHERE user_id IN (SELECT id
    FROM users
    WHERE email LIKE '%@example.com')
    """
    # pprint(execute_query(sql))

    sql = """
    SELECT *
    FROM tasks
    WHERE description = ''
    """
    # pprint(execute_query(sql))

    sql = """
    SELECT u.id, u.fullname, u.email, t.id, t.title, t.description AS task
    FROM users AS u
    INNER JOIN tasks AS t ON u.id = t.user_id
    WHERE t.status_id IN (SELECT id
    FROM status
    WHERE name = 'in progress')
    """
    # pprint(execute_query(sql))

    sql = """
    SELECT u.id, u.fullname, u.email, COUNT(t.user_id) as total_tasks
    FROM users AS u
    LEFT JOIN tasks AS t ON u.id = t.user_id
    GROUP BY u.id
    """
    # pprint(execute_query(sql))
