### Flights

<<<<<<< HEAD
Данный проект является неким небольшим интерфейсом к учебной базе данных PostgreSQL: <https://postgrespro.ru/education/demodb>. Данные в базе напоминают реальные, чтобы с ними было интересно работать.
=======
Данный проект является неким небольшим интерфейсом к учебной базе данных PostgreSQL: https://postgrespro.ru/education/demodb. Данные в базе напоминают реальные, чтобы с ними было интересно работать.
>>>>>>> c949d53373f3806453c853e66fe06092589491a0

---

**Требования:**  
Python версии 3.6 и выше.  
Также необходимо установить Flask в качестве основного фреймворка и flask-paginate для пагинации (разбивка на страницы).

```
pip install Flask
pip install flask-paginate
```

flask-paginate требует подключения Bootstrap, поэтому в стили подключена Bootstrap 5.2.2 через cdn.jsdelivr.net.

---
**Запуск программы:**
1. Необходимо развернуть СУБД PostreSQL (локально или удалённо) или воспользоваться уже установленным где-либо вариантом.
<<<<<<< HEAD
2. Разворачивание учебной базы описано здесь: <https://postgrespro.ru/docs/postgrespro/9.6/demodb-bookings-installation.html>
=======
2. Разворачивание учебной базы описано здесь: https://postgrespro.ru/docs/postgrespro/9.6/demodb-bookings-installation.html
>>>>>>> c949d53373f3806453c853e66fe06092589491a0
3. В корне проекта создать файл "config.py", в котором прописать данные для подключения к БД в следующем формате:
```
database = '<db_name>'
user = '<db_user>'
password = '<user_password>'
host = '<db_host>'
port = '<db_port>'
```
<<<<<<< HEAD
4. Для подключения к PostgreSQL из Python необходимо установить библиотеку psycopg2.
На Windows я устанавливал её командой  
`pip install psycopg2`,  
на Ubuntu:  
`pip install psycopg2-binary`.
5. В консоли перейти в каталог проекта и запустить проект командой  
=======
4. В консоли перейти в каталог проекта и запустить проект командой  
>>>>>>> c949d53373f3806453c853e66fe06092589491a0
`python main.py`