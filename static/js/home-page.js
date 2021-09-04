$(document).ready(function() {

    let modalObject = $("#modal-div").modalObject("delete-modal");
    modalObject.SetTitle("Be careful!");
    modalObject.AddButton({
        id: "confirm-delete-button",
        classes: "btn btn-danger",
        text: "Yes",
    });

    modalObject.AddButton({
        id: "cancel-delete-button",
        classes: "btn btn-secondary",
        text: "No",
    });
    modalObject.SetButtonForClose("cancel-delete-button");

    $(".delete-button").on("click", function() {

        var datapack_id = $(this).attr("id").split("-")[0]
        let li = $(this).parent().parent();
        datapack_name = li.clone()    //clone the element
                          .children() //select all the children
                          .remove()   //remove all the children
                          .end()  //again go back to selected element
                          .text();

        console.log("Delete datapack " + datapack_name)

        modalObject.Get$Body().text("You are about to delete the '" + datapack_name + "' datapack. Are you sure?");
        $("#deleted-datapack-id").text(datapack_id)
        modalObject.Show();
    })
    
    $("#confirm-delete-button").on("click", function() {
        $.ajax({
            headers: { "X-CSRFToken": Cookies.get("csrftoken") },
            type: "POST",
            url: "#",
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

})