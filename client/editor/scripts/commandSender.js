const submitButton = document.getElementById("submitButton")

var ip = "http://71.167.25.60"
var port = "5000"

submitButton.addEventListener("click", () => {
  command = document.getElementById("command").value;
  document.getElementById("command").value = "";
  sendCommand(command);
});

function sendCommand(command) {
  url = ip + ":" + port + "/shell/" + command
  httpGetAsync(url)
}

function updateConsole(output) {
  document.getElementById("consoleOut").innerHTML = output;
}

function httpGetAsync(url)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            updateConsole(xmlHttp.responseText);
    }
    xmlHttp.open("GET", url, true);
    xmlHttp.send(null);
}

// Ignore - Prevents page from reloading after the submit button is clicked
var form = document.getElementById("consoleForm");
function handleForm(e) {e.preventDefault();}
form.addEventListener('submit', handleForm);
