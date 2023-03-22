# DJ_PARSER

---

http://py2.ponomarev-aa.ru/


---

## INIT 

```
pip install -r requirements.txt

python -m pip install --upgrade pip
```

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