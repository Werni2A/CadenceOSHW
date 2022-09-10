import sqlite3


def create_table(connection: sqlite3.Connection) -> None:
    cursor = connection.cursor()

    sql_command = """
        CREATE TABLE repositories (
            id       INTEGER      PRIMARY KEY AUTOINCREMENT NOT NULL,
            name     VARCHAR(127) NOT NULL,
            author   VARCHAR(127) NOT NULL,
            fork_url VARCHAR(127) NOT NULL,
            orig_url VARCHAR(127) NOT NULL
        );
    """

    cursor.execute(sql_command)

    connection.commit()


if __name__ == "__main__":
    connection = sqlite3.connect("repos.db")

    # create_table(connection)

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM repositories")
    repos = cursor.fetchall()

    for repo in repos:
        print(repo)

    connection.commit()

    connection.close()