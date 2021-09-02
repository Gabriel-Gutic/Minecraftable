$(document).ready(function()
{
    $("#reset-password-form").validate({
        rules: {
            password: {
                required: true,
                minlength: 8,
            },
            password_again: {
                required: true,
                equalTo: '#password-field',
            },
        },
        messages: {
            password: {
                required: "You need to fill out this field!",
                minlength: "Your password need to have at least 8 characters!",
            },
            password_again: {
                required: "You need to fill out this field!",
                equalTo: "Passwords don't match!",
            }
        }
    })
})