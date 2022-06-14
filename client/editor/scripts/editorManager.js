var editor = ace.edit("textEditor");
editor.setTheme("ace/theme/dracula");
editor.session.setMode("ace/mode/python");

editor.setValue("print(\"Hello World!\")")


// Keyboard shortcuts

document.onkeydown = (e) => {
  if (e.ctrlKey && (e.key === "s" || e.key === "S")) {
    e.preventDefault();
    saveCurrentFile();
  }
}

function saveCurrentFile() {
  // Do the saving stuff here
}
