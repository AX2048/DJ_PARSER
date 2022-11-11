import os, sys, platform
from datetime import datetime

print('sys.v :: ', sys.version)
print('platform.v :: ', platform.python_version())
print('')
print('cwd :: ', os.getcwd())
print('Executable :: ', os.path.dirname(sys.executable), sys.executable)
print('')

current_datetime = datetime.now()
print('DT :: ', current_datetime)

file = open("/home/alex/Documents/CODE/PY/otus.txt", "a")
file.write(f"sys.v :: {sys.version}\nplatform.v :: {platform.python_version()}\ncwd :: {os.getcwd()}\nExecutable :: {os.path.dirname(sys.executable)}, {sys.executable}\nDT :: {current_datetime} \n\n")
file.close()