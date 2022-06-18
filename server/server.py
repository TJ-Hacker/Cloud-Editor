import os
import subprocess
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

app = Flask(__name__)
CORS(app)

# Should receive a json object with the text to update in the 'data' parameter
@app.route("/create/<fileName>", methods = ['POST'])
def createFile(fileName):
    return "To Be Implemented..."

# Should recieve a json object with the file name and the path of the directory the file is in
@app.route("/retrieve/", methods = ['GET'])
def retrieveFile():
    directory = request.headers.get("directory")
    fileName = request.headers.get("fileName")

    try:
        file = open(directory + "/" + fileName, "r")
    except TypeError:
        return "Invalid/Missing header"
    except FileNotFoundError:
        return "File not found :("

    fileContent = file.read()
    file.close()

    response = Response(fileContent, 200, )
    response.headers["Access-Control-Allow-Origin"] = "*"
    return {"data": fileContent}

@app.route("/shell/<command>")
def sendCommand(command):
    output = formatOut(str(runCommand(command)))
    return "<p>" + output + "</p>"
