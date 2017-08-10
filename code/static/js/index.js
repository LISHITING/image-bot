$(function () {

    var submit_form = function () {
        var a = $('input[name="a"]').val();
        if (a == '') {
            $("#query-error").fadeIn();
            return false
        } else {
            $("#query-error").fadeOut();
            $.getJSON('/query', {
                a: a
            }, function (data) {
                $(".chatlog").prepend("<i class=\"conversation query-info\" style=\"display: none\">Your intention" +
                    " is:<strong> " + data.intention + "</strong> and" + ' your' + ' parameters is: <strong>' + data.parameter + '</strong></i>');
                $(".chatlog").prepend("<div class=\"conversation robot\" style=\"display: none\"><p><span" +
                    " class=\"chatname\">Robot:</span> </br>" + data.response + '</p></div>');
                $(".chatlog").prepend("<div class=\"conversation user\" style=\"display: none\"><p><span" +
                    " class=\"chatname\">You:</span></br>" + data.query + '</p></div>');
                $(".conversation").slideDown();
                $('input[name=a]').focus().select();
            });
        }
        return false;
    };

    var upload_file = function () {
        var form_data = new FormData($('#upload-file')[0]);
        console.log(form_data);
        $.ajax({
            type: 'POST',
            url: '/upload',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            beforeSend: function () {
                $(".chatlog").prepend("<div class=\"robot conversation\" style=\"display: none\"><p><span" +
                    " class=\"chatname\">Robot:</span></br> Wait a second ... </p></div>");
                $(".btn").prop('disabled', true);
                $("#imagefile").prop('disabled', true);
                $("#imagefile-label").prop('disabled', true);
                $(".conversation").slideDown();
            },
            success: function (data) {
                $(".btn").prop('disabled', false);
                $("#imagefile").prop('disabled', false);
                $("#imagefile-label").prop('disabled', false);
                $("#upload-file-btn").prop('disabled', true);
                if (data.status == 'success') {
                    $(".chatlog").prepend("<div class=\"robot conversation\" style=\"display: none\"><p><span" +
                        " class=\"chatname\">Robot:</span> </br> Done!</p></div>");
                } else {
                    $(".chatlog").prepend("<div class=\"robot conversation\" style=\"display: none\"><p><span" +
                        " class=\"chatname\">Robot:</span> </br> <span style = \"color: red\">Upload failed!</span>" +
                        " </p> <p>Only support .jpg .png format.</p></div>");
                }
                $(".conversation").slideDown();
            }
        });
    };

    var clean_content = function () {
        $('#query').val('');
        $(".chatlog").empty();
    };

    var show_help = function () {
        $(".chatlog").prepend("<div class=\"robot conversation\" style=\"display: none\"><p><span" +
            " class=\"chatname\">Robot:</span></br> Hello, You can ask me what I can see from the picture. You can" +
            " also ask me how many objects or check if one kind of object exist. But you should first choose an" +
            " image to upload.</p></div>");
        $(".conversation").slideDown();
    };

    var readURL = function (input) {
        if (input.files && input.files[0]) {
            var filename = input.value;
            console.log(filename);
            var lastIndex = filename.lastIndexOf("\\");
            if (lastIndex >= 0) {
                filename = filename.substring(lastIndex + 1);
            }
            if (filename != '') {
                $(".chatlog").prepend('<i>File chosen: <strong> ' + filename + '</strong></i>');
                $("#upload-file-btn").prop('disabled', false);
            }
            var reader = new FileReader();
            reader.onload = function (e) {
                $(".chatlog").prepend(' <img id="preview" class="img-thumbnail " src="#" /></br>');
                $('#preview').attr('src', e.target.result);
            };

            reader.readAsDataURL(input.files[0]);
        }
    };

    show_help()

    $('#imagefile').change(function () {
        readURL(this)
    });

    $('#upload-file-btn').click(upload_file);

    $('#calculate').click(submit_form);

    $('#help').click(show_help);

    $('#clear').click(clean_content);

    //press enter to submit
    $('input[type=text]').bind('keydown', function (e) {
        if (e.keyCode == 13) {
            submit_form(e);
        }
    });

    $('input[name=a]').focus();
});