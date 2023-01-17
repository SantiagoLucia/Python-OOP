import sqlite3

conn = sqlite3.connect("sales.db")

conn.execute("""CREATE TABLE Sales (
                salesperson text,
                amt currency,
                year integer,
                model text,
                new boolean
                )""")

datos = [
    ('Tim', 16000, 2010, 'Honda Fit', 'true'),
    ('Tim', 9000, 2006, 'Ford Focus', 'false'),
    ('Gayle', 8000, 2004, 'Dodge Neon', 'false'),
    ('Gayle', 28000, 2009, 'Ford Mustang', 'true'),
    ('Gayle', 50000, 2010, 'Lincoln Navigator', 'true'),
    ('Don', 20000, 2008, 'Toyota Prius', 'false')
]

conn.executemany(
    "INSERT INTO Sales(salesperson, amt, year, model, new) values (?,?,?,?,?)", datos
    )

conn.commit()
conn.close()