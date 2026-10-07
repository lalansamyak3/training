f = open("notes.txt", "r")
print(f.read())
f.close()

"""open is used to open the file in read mode having file name and also having the r in read mode 
"""


"""when you open a file python creates a resource connection that needs to be closed at time"""
"""
Mode	Meaning
r	Read-only to read from the file
w	Write: write to the file. It will create a new file and write in it or
     if file already exists then remove the previous content and add new content
a	Append: to add new content without disturbing the existing one
x	Create new file or fail if already exist
b	Binary: read in binary mode
t	Text: to read the text file normally or default mode is text only
+	Read + Write: to read as well as write to the file
"""
# r+: read + write mode

# we can see that saam.txt was not existing previously but in write mode it create and written content there
"""write=create(if not exist create and write)+overwrite(if exist)"""
g = open("saaam.txt", "w")
g.write("ninik")
g.close()

# appending using a mode
r = open("saaam.txt", "a")
r.write("\nnnknknkn")
r.close()
# open saam.txt and see new content been appended there


# create a new file and fail if already exist
# so saam.txt is created
"""
n = open("saam.txt", "x")
n.close()
"""

# it is used for the pdf images, video, audio,
z = open("images.jpg", "rb")
data = z.read()
z.close()


g1 = open("saam.txt", "r+")
g1.write("nnkn")
g1.close()


"""read with parameter now"""
rt = open("saam.txt", "r")
print(rt.read(3))
rt.close()
# only to read first 3 characters only not more than that


"""Readline(): only used to read one line only"""
py = open("saam.txt", "r")
print(py.readline())
# only print single line at a time
print(py.readline())
py.close()

"""Readlines(parameter) with parameter"""
i = open("saam.txt", "r")
print(i.readline(2))  # first 2 characters of first line
print(i.readline(2))  # first 2 characters of second line
i.close()


################## CONTEXT MANAGER ########################################################

"""CONTEXT MANAGER WITH STATEMENTS IT AUTOMATICALLY CLOSES THE FILE WHEN WITH STATEMENTS EXECUTES
we don't need close explicitly"""

with open("saam.txt", "r") as f:
    data = f.read()
print(data)

"""
benefits of using context manager is that:
normally if exception occur before f.close() it will never close the connection while context manager
closes the connections automatically

f = open("notes.txt", "r")
print(f.read())
# any error occur here so connection will not be closed
f.close()
"""

# writing with write
with open("saam.txt", "w") as f:
    f.write("hellioji\n")
    f.write("buhnik\n")


# WRITELINES: we need \n so data is added by continuously changing line
l1 = ["njnknknkn\n", "ijjmkljml\n", "nkjmk\n"]
with open("saam.txt", "w") as o:
    o.writelines(l1)


###################################################################################################################################
################ SEEK #############################################

"""File pointer: when you read a file it maintains a current position called the file pointer"""
"""you can see the position of pointer using tell() only"""
# tell() to see the position of pointer using tell() (tell the position of pointer)
# seek() it is used to move the file pointer
# seek(0) to move the file pointer to the starting only
# seek(2) position from the end
# seek(1) position from the current one
# seek() it is used to move the pointer to the starting

with open("saam.txt", "r") as f:
    print(f.tell())
    f.read(5)
    print(f.tell())

with open("notes.txt", "r") as f:

    print(f.read(5))

    print(f.read(5))


with open("notes.txt", "r") as f:

    print(f.read(5))
    f.seek(0)
    print(f.read(5))


###################################################################################################
"""PATHLIB"""
#### Pathlib: it is used to work with files in cross-platform way, work with files and folders in a clean,
# cross-platform way
# 1) exists(): to see file exists or not
# 2) is_file() or is_dir(): to see whether it is file or directory
# 3) create directory(): using mkdir()
# 4) read_text() to read the file
# 5) write_text() to write to the file
# 6) get info from the file like name of the file (name), data using (stem) and .txt, .jpg using (suffix)

from pathlib import Path

path = Path("data") / "users" / "user.txt"
print(path)


# 1) to see a file exist or not give true or false to see whether the file exist or not
file = Path("saam.txt")
print(file.exists())

# 2) to see whether it is file or directory
print(file.is_file())
print(file.is_dir())

# 3) to create a directory
# file.mkdir()

# 4) read_text(): to read a file
# file = Path("sam.txt")
print(file.read_text())

# 5) write_text()
file.write_text("huhn")
print(file.read_text())

# 6) to get the details of the file using name to get name of the file, suffix to get format and
# stem to get the data
print(file.name)
print(file.stem)
print(file.suffix)

# previous instead of pathlib we were using os.path.join()
###################################################################################################


"""JSON"""
# json: to see the json data we use json.dump for write to the json file and
# json.load(): to read the content of the json file
import json

with open("users.json", "r") as f:
    data = json.load(f)

print(data)


use = [{"name": "Samyal", "age": 12}, {"name": "Samyal", "age": 12}]
with open("users.json", "w") as file:
    json.dump(use, file, indent=4)


###########################################################################################################
"""Context manager"""
"""
Context manager: it is not only used for file
files
database connections
locks
network resources
temporary resources
transactions
it used for the resources that need setup -> use -> cleanup
it basically uses __enter__ to enter the file and __exit__ to exit the file
so with is just created from __enter__ and __exit__ so we can create our own
with or context manager using __enter__ and __exit__
"""
"""flow is __enter__ -> with block executes -> __exit__"""


class MyContext:
    def __enter__(self):
        print("entering")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("exiting")


with MyContext():
    print("hey its with block")

"""context manager provide benefits that even if exception comes it will close the connections automatically"""


##################################################################################################
"""LOGGING"""
"""logging: we always use print but production application need logging instead of print"""
"""print() only for the printing"""
"""but logging() for severity, timestamp, loggername, message, file output, configuration"""
"""logging levels debug() info() warning() error() critical()"""

# 1)
"""debug() detail info useful during development"""
import logging as logger

logger.debug("start payment calculation")

# 2) info(): normal application events
logger.info("user successfully registered")

# 3) warning now
logger.warning("api response is slower than expected")

# 4) error
logger.error("it is an error fail to process the payments")

# 5) critical
logger.critical("critical failures")

# 6) create a logger
logger = logger.getLogger(__name__)
logger.info("application started")

# 7) logging exceptions now

try:
    m = 10 / 0
except ArithmeticError as e:
    logger.exception("calculation failed")

# 8)
import logging

logging.basicConfig(filename="app.log", level=logging.INFO)

logger = logging.getLogger(__name__)

logger.info("Application started")
logger.error("Something failed")
"""password
API key
JWT secret
database password
credit card data
private tokens


never log the abive things """
######################################################################################################3
"""Enviroment variabbles"""
""" you should never expos ethe api keys and db imfo into the source code as it will be uploaded in the github 
so ur api key gets exposed so instaed use enviroment varibale s"""
from dotenv import load_dotenv
import os

api_key = os.getenv("API_Key")
# .env-> load_dotenv()->applicatuion configuration it is convinent for local devlopemnet
"""never commit .env you should keep it in gitignore so it is never commited 
.env->gitignore ->git ignores it -> doesnt enetr the repositoy
env contains apikey ,db config et etc
"""
########################################################################################################3
"""never ever commit the secrets key as if you commit the secret key 
using git add
git commit 
git push 
then it is tored in the github 
even if you delete the line of key it will still be there in the 
you can see it in the old commit  never comit the secret key is much better than 
deleteimg it ater after being commited """
##############################################################################################################
"""GITIGNORE """
"""
# Environment
.env

# Virtual environment
.venv/
venv/

# Python cache
__pycache__/
*.pyc

# IDE
.vscode/
.idea/
"""
# basic gitignore conatisns these things
""" working and use of .env files
normally we add,commit then push the code but .env we put or mention in gitignore so git doesnt commit it 
as .env contains api keys or secrets  so another devloper dont get your .env but they get the template 
.env.examples  which just have Api_key .... menas onlythe field with novalue in it so .env.example is commited but .env is never commited 
"""
"""so .env.example only shows the necessary field or enviroment variables so another devloper can create or genrate api key and put there '
when another dev do git clone it only gets .env.examples


python not directly read .env file it needs python-dotenv for it 



"""


#######################################################################################################################################
""".env
venv/
.venv/
__pycache__/
*.pyc
.idea/
.vscode/                 ← often ignored, depending on team
.DS_Store 
never get commited in git """


"""main.py
database.py
models.py
routers/
services/
requirements.txt:all the installation it is passed to another dev so it can use pip insrtll -r requiremnets.txt
README.md:all the things about the project like the structure of the project ,technoogy,flow of the project 
.gitignore-contains .env,venv,pychache etc 
.env.example-conatisns field of .env without value so other devloper get that this are needed here 
Dockerfile
docker-compose.yml      ← depending on whether it contains secrets
alembic.ini
alembic/
tes
ts/
they are commited to git 
"""

"""supoose ther are 3 devlopers are there in 3 devlper everyone hacve the same source code but they have there own .env """
"""In production level appliactioon you dont need to creave .env 
basically the cloud platform provide ther own .env file 

"""
