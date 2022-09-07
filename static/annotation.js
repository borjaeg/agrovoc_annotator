$(document).ready(function () {
  $('#annotation-loading').hide();
  $('#input_sentence').keypress(function (event) {
    var keycode = (event.keyCode ? event.keyCode : event.which);
    if (keycode == '13') {
      var input_sentence = $('#input_sentence').val()
      $("#annotation").empty();
      $('#annotation-loading').show();
      //178.128.198.118
      $.getJSON("http://localhost:5555/annotate/" + input_sentence, function (result) {
        $('#annotation-loading').hide();
        $.each(result.annotation, function (i, tag) {
          $("#annotation").append(input_sentence.split(" ")[i] + " <b>(" + tag + ")<b> ");
        });
      });
    }
  });
});