
function chooseFile() {
  document.getElementById("fileInput").click();
}




// function chooseFile() {
//     document.getElementById("fileInput").click();
//   }

document.getElementById("fileInput").addEventListener("change", function() {
      document.getElementById("upload-form").submit();
});
