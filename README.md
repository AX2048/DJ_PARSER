# DJ_PARSER

---

http://py2.ponomarev-aa.ru/


---

## INIT 

```
python -m venv venv_parser

.\venv_parser\Scripts\activate

python -m pip install --upgrade pip

pip install -r requirements.txt
```

## RUN 

Запустить проект можно в разделе "Запуск и отладка" -> "Django_debug"

## Docker

```
docker build . -t dj_parser:0.0.1
```

```
REPOSITORY                        TAG       IMAGE ID       CREATED          SIZE
dj_parser                         0.0.1     22f357475b73   22 seconds ago   1.74G
```

```
docker run -d --rm --name dj_parser-test -p 8080:8000 dj_parser:0.0.1
```

http://localhost:8080/

---