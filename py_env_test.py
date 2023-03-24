# PY_TEST_SCR.py

import os, sys, platform
from datetime import datetime
from random import randint
import socket
#from pip import _internal


current_datetime = datetime.now()
r = randint(0, 25)


print(f'| sys.v :: {sys.version} |')
print(f'| platform.v :: {platform.python_version()} |')
print(f'| Executable :: {os.path.dirname(sys.executable), sys.executable} |')
print(f'| randint :: {r} |')
print(f'| User @ Host :: {os.getlogin()}@{socket.gethostname()} |')

#print(os.system('ip a'))

from pathlib import Path

print(f"Path :: {Path(__file__).resolve()}")
print(f"Path :: {Path(__file__).resolve().parent} :: parent")
print(f"Path :: {Path(__file__).resolve().parent.parent} :: parent parent")

print(os.getenv("LOCAL_MACHINE_DEV"))
print(os.path.dirname(__file__))