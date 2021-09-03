$(document).ready(function(){
    $ipp = $("#input-profile-picture-div");
    $ipp.inputPicture("input-profile-picture");

    inputPicture = $ipp.inputPicture()

    inputPicture.SetDefaultImage(media_url + "users/user-no-image.png")
    inputPicture.RemoveImage();

    if (user_image)
        inputPicture.SetImage(media_url + user_image);
    inputPicture.OnChange(function(temp_path){
        inputPicture.Upload({
            headers: { "X-CSRFToken": Cookies.get("csrftoken") },
            url: "",
            success: function(data){
                data = JSON.parse(data);

                inputPicture.SetImage(data.url)
            }
        });
    })


    $("#email-change-button").on("click", function(){

        $.ajax({
            url: "",
            type: "GET",
            data: {
                'change-email': '',
            },
            success: function(data){
                if (data.error == undefined) 
                {
                    $(".modal-title").text("Change Email");
                    $("#email-send-modal").modal("show");
                    return;
                }

                Error(data.error);
            }
        })
    })

    $("#password-change-button").on("click", function(){

        $.ajax({
            url: "",
            type: "GET",
            data: {
                'change-password': '',
            },
            success: function(data){
                if (data.error == undefined) 
                {
                    $(".modal-title").text("Change Password")
                    $("#email-send-modal").modal("show");
                    return;
                }

                Error(data.error);
            }
        })
    })
})