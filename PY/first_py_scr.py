import os, sys, platform
from datetime import datetime
from random import randint


en_alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
en_ikato = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "Xray", "Yankee", "Zulu"]
current_datetime = datetime.now()
r = randint(0, 25)


print(f'| sys.v :: {sys.version} | platform.v :: {platform.python_version()} | cwd :: {os.getcwd()} | Executable :: {os.path.dirname(sys.executable), sys.executable} | DT :: {current_datetime} | randint :: {r} |\n')

e = 9999

print(len(str(e)))

current_dateTime = datetime.now()
print(f'{current_dateTime.year}-{str(current_dateTime.month).zfill(2)}-{str(current_dateTime.day).zfill(2)}_{str(current_dateTime.hour).zfill(2)}:{str(current_dateTime.minute).zfill(2)}:{str(current_dateTime.second).zfill(2)}::{str(current_dateTime.microsecond).zfill(6)}')


print(r)
rmm = en_alfabet[r]
rnn = str(en_ikato[r]).zfill(8)

#yo = str(current_dateTime.year + str(current_dateTime.month).zfill(2) + str(current_dateTime.day).zfill(2) + "_" + str(current_dateTime.hour).zfill(2) + "-" + str(current_dateTime.minute).zfill(2) + "-" + str(current_dateTime.second).zfill(2) + "__" + str(current_dateTime.microsecond).zfill(6))
yo = str(str(current_dateTime.year).zfill(4) + str(current_dateTime.month).zfill(2) + str(current_dateTime.day).zfill(2) + "_" + str(current_dateTime.hour).zfill(2) + "-" + str(current_dateTime.minute).zfill(2) + "-" + str(current_dateTime.second).zfill(2) + "_" + str(current_dateTime.microsecond).zfill(6) + "_" + rnn)

print(yo)
print(len(yo))


file = open("/home/alex/Documents/CODE/PY/otus.txt", "a")
file.write(f"sys.v :: {sys.version}\nplatform.v :: {platform.python_version()}\ncwd :: {os.getcwd()}\nExecutable :: {os.path.dirname(sys.executable)}, {sys.executable}\nDT :: {current_datetime}\nYO :: {yo}\n\n")
file.close()