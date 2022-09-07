$(document).ready(function(){
    $('#input_sentence').keypress(function(event){
        var keycode = (event.keyCode ? event.keyCode : event.which);
        if(keycode == '13'){
          var input_sentence = $('#input_sentence').val()
          $("#annotation").empty();
          $.getJSON("http://localhost:5555/annotate/" + input_sentence, function(result){
            $.each(result.annotation, function(i, tag){
              $("#annotation").append(input_sentence.split(" ")[i] + " (" + tag + ") ");
            });
          });
        }
      });
  });