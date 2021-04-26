    # Cars finder #

склонировать репозиторий, перейти в папку с ним

python -m venv

venv\Scripts\activate.bat

pip install -r requirements.txt

cd car

python manage.py runserver

http://127.0.0.1:8000/

http://127.0.0.1:8000/admin

(добавление машин из панели администратора)

логин:  guest

пароль: skillfaktory

P.S.: сочетание коробки передач с остальными параметрами поиска - должно точно совпадать с находящейся записью в базе (иначе поиск не даст результата)