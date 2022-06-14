const fileButton = document.getElementById("fileSubmitButton");

var chosenFilePath;

fileButton.addEventListener("click", () => {
  chosenFilePath = document.getElementById("filePath").value;
  getFileData(chosenFilePath);
  // sendCommand("Test-Path " + chosenFilePath);
});

function getFileData (filePath) {
  console.log("Chosen path:" + filePath);
  url = ip + ":" + port + "/create/" + filePath;
  saveCurrentFile();
  // httpGetAsync(url, loadDataToEditor);
}


var fileform = document.getElementById("fileChooser");
fileform.addEventListener('submit', handleForm);
