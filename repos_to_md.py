import sqlite3

from markdownTable import markdownTable


if __name__ == "__main__":

    connection = sqlite3.connect("repos.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM repositories")

    repos = cursor.fetchall()

    connection.close()

    rows = []

    for repo in repos:

        columns = ["ID", "Name", "Author", "Fork URL", "Original URL"]
        repo = dict(zip(columns, repo))

        repo.pop("ID")

        rows += [repo]

    rows = sorted(rows, key = lambda row: row["Name"])

    md_str = markdownTable(rows).setParams(row_sep = "markdown", quote = False).getMarkdown()

    with open("repos_table.md", "w") as f:
        f.write(md_str)