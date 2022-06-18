var ip = "http://127.0.0.1"
var port = "5000"

const getFile = async () => {
  let dir = document.getElementById("filePath").value
  let name = document.getElementById("fileName").value

  // const response = await fetch(ip + ":" + port + "/retrieve/", {
  //   method: 'GET',
  //   headers: {
  //     "directory": dir,
  //     "fileName" : name
  //   }
  // });
  // let resp = await response;
  // console.log(resp.json())

  fetch(ip + ":" + port + "/retrieve/", {
    method: 'GET',
    headers: {
      "directory": dir,
      "fileName" : name
    }
  }).then(response => response.json()).then(data => {loadDataToEditor(data["data"]);})

}

// Ignore - Prevents page from reloading after the submit button is clicked
var form = document.getElementById("fileChooser");
function handleForm(e) {e.preventDefault();}
form.addEventListener('submit', handleForm);
