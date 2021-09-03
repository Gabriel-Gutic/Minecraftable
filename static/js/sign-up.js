$(document).ready(function(){

    $("#regiter-form").validate({
        rules: {
            username: {
                required: true,
                minlength: 4,
            },
            email: {
                required: true,
                email: true,
            },
            password: {
                required: true,
                minlength: 8,
            },
            password_again: {
                equalTo: "#password-field",
            }
        },
        messages: {
            username: {
                required: "You need to enter a username!",
                minlength: "Your username must be at least 4 characters!",
            },
            email: {
                required: "You need to enter an email address!",
                email: "You need to enter a valid email address!",
            },
            password: {
                required: "You need to enter a password!",
                minlength: "Your password must be at least 8 characters!",
            },
            password_again: {
                equalTo: "Passwords don't match!",
            }
        }
    })

})