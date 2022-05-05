function addFormField() {
    var id = document.getElementById("id").value;
    $("#divTxt").append(
      "<p id='row" +
        id +
        "'><label for='txt" +
        id +
        "'>Field " +
        id +
        "&nbsp;&nbsp;<input type='text' size='20' name='txt[]' id='txt" +
        id +
        "'>&nbsp;&nbsp<a href='#' onClick='removeFormField(\"#row" +
        id +
        "\"); return false;'>Remove</a><p>"
    );
  
    id = id - 1 + 2;
    document.getElementById("id").value = id;
  }
  
  function removeFormField(id) {
    $(id).remove();
  }
  