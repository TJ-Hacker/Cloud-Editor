var editor = ace.edit("textEditor");
editor.setTheme("ace/theme/dracula");
editor.session.setMode("ace/mode/python");

editor.setValue("");


// Keyboard shortcuts

document.onkeydown = (e) => {
  if (e.ctrlKey && (e.key === "s" || e.key === "S")) {
    e.preventDefault();
    saveCurrentFile();
  }
}

function loadDataToEditor(data) {
  editor.setValue(data);
}

function saveCurrentFile() {
  console.log("A:SKLJDFHLK:AJSHDF");
  data = editor.getValue()
  var xhr = new XMLHttpRequest();
  var url = "http://71.167.25.60:5000/create/dumbFile.txt";
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
        console.log(JSON.parse(xhr.responseText));
    }
  };
  var sD = JSON.stringify({"data": data});
  xhr.send(sD);
  console.log(data)
}
