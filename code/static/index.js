$(function () {

    var submit_form = function (e) {
        var a = $('input[name="a"]').val();
        if (a == '') {
            $("#query-error").fadeIn();

            return false
        } else {
            $("#query-error").fadeOut();
            $.getJSON('/query', {
                a: a
            }, function (data) {
                $(".chatlog").prepend('<i class="conversation query-info" style="display: none">Your intention' +
                    ' is:<strong>' +
                    ' ' + data.intention + '</strong>' +
                    ' and' +
                    ' your' +
                    ' parameters is: <strong>' + data.parameter + '</strong></i>');
                $(".chatlog").prepend('<div class="conversation robot" style="display: none"><p><span' +
                    ' class="chatname">Robot:</span> </br>' + data.response + '</p></div>');
                $(".chatlog").prepend('<div class="conversation user" style="display: none"><p><span' +
                    ' class="chatname">You:</span></br>' + data.query + '</p></div>');
                $(".conversation").slideDown();
                $('input[name=a]').focus().select();
            });
        }
        return false;
    };


    $('#upload-file-btn').click(function () {
        var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: '/upload',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            beforeSend: function () {
                $(".chatlog").prepend('<div class="robot conversation" style="display: none"><p><span class="chatname">Robot:</span></br>' +
                    ' Analyzing</p></div>');
                $(".btn").prop('disabled', true);
                $(".conversation").slideDown();
            },
            success: function (data) {
                $(".btn").prop('disabled', false);
                $("#upload-file-btn").prop('disabled', true);
                $(".chatlog").prepend('<div class="robot conversation" style="display: none"><p><span class="chatname">Robot:</span>' +
                    ' </br> Analyze' +
                    ' done!</p></div>');
                $(".conversation").slideDown();
            },
        });
    });

    // clean history
    var clean_content = function () {
        $(".chatlog").empty();
    };

    var show_help = function () {
        $(".chatlog").prepend('<div class="robot conversation" style="display: none"><p><span class="chatname">Robot:</span></br> You can' +
            ' ask me what' +
            ' I can see from the' +
            ' picture</p><p>You can also ask me how many objects or check if one kind of object exist.</p></div>');
        $(".conversation").slideDown();
    }

    var upload_change = function () {
        var filename = this.value;
        console.log(filename);
        var lastIndex = filename.lastIndexOf("\\");
        if (lastIndex >= 0) {
            filename = filename.substring(lastIndex + 1);
        }
        $(".chatlog").prepend('<i>File chosen: <strong> ' + filename + '</strong></i>');
        $("#upload-file-btn").prop('disabled', false);
    }

    $('#imagefile').change(upload_change)

    $('#calculate').bind('click', submit_form);

    $('#help').bind('click', show_help);

    $('#clear').bind('click', clean_content);

    //press enter to submit
    $('input[type=text]').bind('keydown', function (e) {
        if (e.keyCode == 13) {
            submit_form(e);
        }
    });

    $('input[name=a]').focus();
});