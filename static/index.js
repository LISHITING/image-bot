
  $(function() {
      // ajax submit
    var submit_form = function(e) {
      $.getJSON('/query', {
        a: $('input[name="a"]').val(),
      }, function(data) {
        $( ".chatlog" ).prepend( '<i>Your intention is:<strong> ' + data.intention + '</strong> and your' +
            ' parameters is: <strong>'+  data.parameter + '</strong></i>' );
        $( ".chatlog" ).prepend( '<div class="robot"><p>Robot: ' + data.response + '</p></div>' );
        $( ".chatlog" ).prepend( '<div class="you"><p>You: ' + data.query + '</p></div>' );
        $( ".chatlog" ).prepend( '</hr>' );
        $('input[name=a]').focus().select();
      });
      return false;
    };

     $('#upload-file-btn').click(function() {
        var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/upload',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function(data) {
                $( ".chatlog" ).prepend( '<div class="robot"><p>Robot: Process done!</p></div>' );
            },
        });
    });

    // clean history
    var clean_content = function(){
        $( ".chatlog" ).empty();
    };

    $('a#calculate').bind('click', submit_form);
    $('a#clear').bind('click', clean_content);

    //press enter to submit
    $('input[type=text]').bind('keydown', function(e) {
      if (e.keyCode == 13) {
        submit_form(e);
      }
    });


    $('input[name=a]').focus();
  });