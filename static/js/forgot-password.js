$(document).ready(function(){

    $("#reset-form").validate({
        rules: {
            recoverydata: {
                "required": true,
            }
        },
        messages: {
            recoverydata: "Please provide your username or your email address!",
        }
    });

    $("#send-button").on("click", function(){
        if ($("#reset-form").valid())
        {
            $.ajax({
                url: "",
                type: "GET",
                data: {
                    "text": $("#recovery-data").val(),
                },
                success: function(data){
                    if (data.error != undefined)
                    {
                        console.error(data.error);
                        Error(data.error);
                    }
                    else
                        window.location.replace("/Minecraftable/recovery-email-send/");
                }
            })
        }
    })

})