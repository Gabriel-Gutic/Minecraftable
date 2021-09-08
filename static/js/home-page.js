$(document).ready(function() {

    for (const type of ['datapack', 'tag'])
    {
        let modalObject = $("#modal-" + type).modalObject(type + "-delete-modal");
        modalObject.SetTitle("Be careful!");
        modalObject.AddButton({
            id: "confirm-" + type + "-delete-button",
            classes: "btn btn-danger",
            text: "Yes",
        });

        modalObject.AddButton({
            id: "cancel-" + type + "-delete-button",
            classes: "btn btn-secondary",
            text: "No",
        });
        modalObject.SetButtonForClose("cancel-" + type + "-delete-button");
    }

    $(".datapack-delete-button").on("click", function() {
        var datapack_id = $(this).attr("id").split("-")[0]
        let $li = $(this).parent().parent();
        datapack_name = $li.clone()    //clone the element
                          .children() //select all the children
                          .remove()   //remove all the children
                          .end()  //again go back to selected element
                          .text();

        let modalObject = $("#modal-datapack").modalObject();
        modalObject.Get$Body().text("You are about to delete the '" + datapack_name + "' datapack. Are you sure?");
        $("#deleted-datapack-id").text(datapack_id);
        modalObject.Show();
    })
    
    $("#confirm-datapack-delete-button").on("click", function() {
        let modalObject = $("#modal-datapack").modalObject();
        $.ajax({
            headers: { "X-CSRFToken": Cookies.get("csrftoken") },
            type: "POST",
            url: "",
            dataType: 'json',
            data: {
                "datapack-delete": "",
                "datapack-id": $("#deleted-datapack-id").text(),
            },
            success: function(data) {
                console.log("Datapack deleted!")
                $("#datapack-item-" + data.datapack_id).remove();
                modalObject.Hide();
            }
        })
    })

    $(".tag-delete-button").on("click", function() {
        var tag_id = $(this).attr("id").split("-")[0]
        let $li = $(this).parent().parent();
        tag_name = $li.find(".left-div").text();

        let modalObject = $("#modal-tag").modalObject();
        modalObject.Get$Body().text("You are about to delete the '" + tag_name + "' tag. Are you sure?");
        $("#deleted-tag-id").text(tag_id);
        modalObject.Show();
    })
    
    $("#confirm-tag-delete-button").on("click", function() {
        let modalObject = $("#modal-tag").modalObject();
        $.ajax({
            headers: { "X-CSRFToken": Cookies.get("csrftoken") },
            type: "POST",
            url: "",
            dataType: 'json',
            data: {
                "tag-delete": "",
                "tag-id": $("#deleted-tag-id").text(),
            },
            success: function(data) {
                console.log("Tag deleted!")
                $("#tag-item-" + data.tag_id).remove();
                modalObject.Hide();
            }
        })
    })

    $(".download-datapack").on("click", function() {
        $li = $(this).parent().parent();
        let datapack_id = parseInt($li.attr("id").split("-")[2], 10);

        $.ajax({
            url: "/datapack/" + datapack_id + "/download/",
            type: "GET",
            success: function(data) {
                var element = document.createElement('a');
                element.style.display = "none";
                element.setAttribute('href', data.zip_url);
                element.setAttribute('download', data.zip_name);
                document.body.appendChild(element);
                element.click();
                document.body.removeChild(element);

                $.ajax({
                    url: "/datapack/download/complete/" + data.zip_name + "/",
                    type: "GET",
                    success: function(data) {
                        console.log("Downloaded successfully!")
                    }
                })
            }
        })
    })

})