$(document).ready(function(){

    $("#login-form").validate({
        rules: {
            username_email: {
                required: true,
            },
            password: {
                required: true,
            }
        },
        messages: {
            username_email: {
                required: "Please fill out this field",
            },
            password: {
                required: "Please fill out this field",
            }
        }
    })

})