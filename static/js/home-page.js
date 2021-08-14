$(document).ready(function() {

    $(".delete-button").on("click", function() {

        var datapack_id = $(this).attr("id").split("-")[0]
        datapack_name = $("#" + datapack_id + "-name").text();

        console.log("Delete datapack " + datapack_name)

        $("#delete-modal-body").text("You are about to delete the '" + datapack_name + "' datapack. Are you sure?")

        $("#deleted-datapack-id").text(datapack_id)
        $("#delete-modal").modal("show");
    })

    $("#confirm-delete-button").on("click", function() {

        $.ajax({
            headers: { "X-CSRFToken": Cookies.get("csrftoken") },
            type: "POST",
            url: "#",
            dataType: 'json',
            data: {
                "datapack-delete": "",
                "datapack-id": $("#deleted-datapack-id").text()[0],
            },
            success: function() {
                console.log("Datapack deleted!")
                location.reload();
            }
        })

    })

})