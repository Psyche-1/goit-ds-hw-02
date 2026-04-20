import faker
from random import randint
import sqlite3


DATABASE = 'tasks.db'
NUMBER_USERS = 10
NUMBER_TASKS = 20

def generate_fake_data(number_users, number_tasks) -> tuple():
    fake_users = []
    fake_tasks = []
    statuses = [('new',), ('in progress',), ('completed',)]
    fake_data = faker.Faker()

    for _ in range(number_users):
        fake_users.append((fake_data.name(), fake_data.email()))

    for _ in range(number_tasks):
        fake_tasks.append((fake_data.sentence(nb_words=4), fake_data.paragraph(nb_sentences=3), randint(1, len(statuses)), randint(1, number_users)))

    return fake_users, fake_tasks, statuses


def insert_data_to_db(users, tasks, statuses) -> None:
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        sql_to_users = """INSERT INTO users(fullname, email)
                          VALUES (?, ?)"""
        cur.executemany(sql_to_users, users)

        sql_to_statuses = """INSERT INTO status(name)
                              VALUES (?)"""
        cur.executemany(sql_to_statuses, statuses)

        sql_to_tasks = """INSERT INTO tasks(title, description, status_id, user_id)
                          VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_tasks, tasks)

        con.commit()


if __name__ == "__main__":
    users, tasks, statuses = generate_fake_data(NUMBER_USERS, NUMBER_TASKS)
    insert_data_to_db(users, tasks, statuses)
