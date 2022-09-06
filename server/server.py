import os
import subprocess
import json

# from flask import Flask
from flask import *
from flask_cors import CORS

def formatOut(res):
    res = res[2:len(res)]
    res = replaceSubStr(res, "\\n", "\n")
    res = replaceSubStr(res, "\\r", "")
    res = replaceSubStr(res, "\\\\", "\\")

    return res[0:(len(res)-1)]

def replaceSubStr(str, sub, repl):
    while sub in str:
        str = str[0:str.index(sub)] + repl + str[(str.index(sub)+len(sub)):len(str)]
    return str

def runCommand(cmd):
    return subprocess.check_output(["C:\Windows\System32\WindowsPowerShell\\v1.0\powershell.exe", cmd], shell=True)

def is_safe_path(basedir, path, follow_symlinks=True):
    # Credit to: https://security.openstack.org/guidelines/dg_using-file-paths.html
    if follow_symlinks:
        matchpath = os.path.realpath(path)
    else:
        matchpath = os.path.abspath(path)
    return basedir == os.path.commonpath((basedir, matchpath))


app = Flask(__name__)
CORS(app)

@app.route("/tree/", methods = ["GET"])
def getDirectoryContent():
    directory = request.headers.get("directory")
    dirList = []


    return {"data" : dirList}

# Creates a file / or updates one
@app.route("/create/", methods = ["POST"])
def createFile():
    directory = request.headers.get("directory")
    fileName = request.headers.get("fileName")

    finalPath = directory + "/" + fileName

    if not is_safe_path(os.getcwd(), finalPath):
        return Response(None, 403)

    data = json.loads(request.data)

    fileContent = str(data["data"])

    with open(finalPath, "w") as file:
        file.write(fileContent)

    return str(data["data"])

# Returns the content of a specified file
@app.route("/retrieve/", methods = ["GET"])
def retrieveFile():
    directory = request.headers.get("directory")
    fileName = request.headers.get("fileName")

    finalDir = directory + "/" + fileName

    if not is_safe_path(os.getcwd(), finalDir):
        return Response(None, 403)

    try:
        file = open(directory + "/" + fileName, "r")
    except TypeError:
        return Response("Invalid/Missing header", 405)
    except FileNotFoundError:
        return Response("File not Found :(", 404)

    fileContent = file.read()
    file.close()

    # TO DO - implement Responses
    # response = Response(fileContent, 200, )
    # response.headers["Access-Control-Allow-Origin"] = "*"

    return {"data": fileContent}

@app.route("/shell/", methods = ["POST"])
def sendCommand():
    return "To Be Implemented..."
