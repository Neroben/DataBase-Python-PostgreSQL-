import psycopg2
conn = psycopg2.connect(database="postgres",
    user="Alina",
    password="")

cursor = conn.cursor()

# Р’С‹РїРѕР»РЅСЏРµРј Р·Р°РїСЂРѕСЃ.


sql_statement = """
INSERT INTO genre(name)
VALUES('Р РѕРјР°РЅ');
"""

#results = cursor.fetchall()
try:
    cursor.execute("""
INSERT INTO genre(name)
VALUES('Р РѕРјР°РЅ');
""")
except psycopg2.DatabaseError as err:
        print("РћС€РёР±РєР°:", err)
        conn.rollback()
else:
    conn.commit()

cursor.execute("""
SELECT DISTINCT r.reader_id, r.full_name, b.name, a.name
FROM form f, book b, book b2, reader r, reader r2, genre g, genre g2, genre_book gb,  genre_book gb2, author a, authors_book ab
WHERE ((r.reader_id <> f.reader_id and
      b.isbn = f.book_id and
      f.reader_id = r2.reader_id and
      (r.sex = r2.sex or
      @(DATE_PART('year',r.birth_date) - DATE_PART('year', r2.birth_date)) <= 5)) or
      (r.reader_id = f.reader_id and
      b2.isbn = f.book_id and
      g.genre_id = gb.genre_id and
      gb.book_id = gb2.book_id and
      --b.genre = b2.genre and
      b.isbn <> f.book_id)) and
      b.isbn = ab.book_id and
      ab.author_id = a.author_id and
      r.reader_id <> f.reader_id
ORDER BY r.reader_id;""")

try:
    result = cursor.fetchone()
    reader_name = result[1]
except psycopg2.DatabaseError as err:
    print("РћС€РёР±РєР°:", err)
else:
    print("Р РµРєРѕРјРµРЅРґР°С†РёРё РґР»СЏ С‡РёС‚Р°С‚РµР»СЏ", result[1], ":")
    while result:
        if result[1] != reader_name:
            print("\nР РµРєРѕРјРµРЅРґР°С†РёРё РґР»СЏ С‡РёС‚Р°С‚РµР»СЏ", result[1], ":")
            reader_name = result[1]
        print('"', end="")
        print(result[2], end="")
        print('"', result[3])
        result = cursor.fetchone()

# Закрываем подключение
cursor.close()
conn.close()