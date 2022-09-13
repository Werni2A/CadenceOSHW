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


def add_new_entry(connection: sqlite3.Connection, name: str, author: str, fork_url: str, orig_url: str) -> None:

    cursor = connection.cursor()

    sql_command = f"""
        SELECT id, name, author FROM repositories
        WHERE orig_url = "{orig_url}";
    """

    cursor.execute(sql_command)
    results = cursor.fetchall()

    if len(results) > 0:
        print(f"Repository for URL {orig_url} already exists, not adding it to database!")
        return

    sql_command = f"""
        INSERT INTO repositories (name, author, fork_url, orig_url)
        VALUES ("{name}", "{author}", "{fork_url}", "{orig_url}"); 
    """

    cursor.execute(sql_command)

    connection.commit()


if __name__ == "__main__":
    connection = sqlite3.connect("repos.db")

    # create_table(connection)

    # Add new entry
    name = "CadenceLibrary"
    author = "XiaoSenLuo"
    fork_url = "https://github.com/Werni2A/XiaoSenLuo_CadenceLibrary"
    orig_url = "https://github.com/XiaoSenLuo/CadenceLibrary"
    add_new_entry(connection, name, author, fork_url, orig_url)

    cursor = connection.cursor()

    # Print all entries
    cursor.execute("SELECT * FROM repositories")
    repos = cursor.fetchall()

    for repo in repos:
        print(repo)

    connection.commit()

    connection.close()