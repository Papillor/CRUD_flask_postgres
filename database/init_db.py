import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="bookstore",
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'])

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 'pages_num integer NOT NULL,'
                                 'review text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Little Women',
             'Louisa May Alcott',
             296,
             'N/A')
            )


cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('La sombra del viento',
             'Carlos Ruiz Zafón',
             569,
             'N/A')
            )

conn.commit()

cur.close()
conn.close()