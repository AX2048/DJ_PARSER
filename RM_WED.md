# WEB

python -m venv venv_parser
python3 -m venv venv_parser

.\venv_parser\Scripts\activate
source venv_parser/bin/activate

python -m pip install --upgrade pip
python3 -m pip install --upgrade pip

pip install -r requirements.txt

---

.\manage.py runserver 

python -m uvicorn dj_parser.asgi:application

---

python manage.py migrate