import uvicorn

if __name__ == '__main__':
    uvicorn.run("dj_parser.asgi:application", reload=True)