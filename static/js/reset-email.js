$(document).ready(function()
{
    $("#reset-email-form").validate({
        rules: {
            email: {
                required: true,
            },
        },
        messages: {
            email: {
                required: "You need to specify an email address!",
            },
        }
    })
})