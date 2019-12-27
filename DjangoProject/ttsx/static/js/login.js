$(function () {
    $("#loginBtn").click(function () {
        var username = $("#username").val();
        var password = $("#password").val();
        $.ajax({
            url: '../user/login',
            type: 'POST',
            data: {"username": username, "password": password},
            success: function (res) {
                if (res.code == '200') {
                    window.location.href = 'index.html'
                } else if (res.code == '401') {
                    $(".user_error").css("display", "block");
                    $(".user_error span").text(res.msg);
                } else if (res.code == '402') {
                    $(".pwd_error").css("display", "block");
                    $(".pwd_error span").text(res.msg);
                }
            }
        })
    })
})