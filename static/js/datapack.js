$(document).ready(function()
{
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

    $(".delete-button").on("click", function(){

        let $li = $(this).parent().parent();
        let recipe_name = $li.clone()    //clone the element
                            .children() //select all the children
                            .remove()   //remove all the children
                            .end()  //again go back to selected element
                            .text();
        let recipe_id = $li.attr("id").split("-")[1];

        $("#deleted-recipe-id").text(recipe_id);
        modalObject.Get$Body().text("You are about to delete the '" + recipe_name + "' recipe. Are you sure?")

        modalObject.Show();
    })

    $("#confirm-delete-button").on("click", function() {
        $.ajax({
            headers: { "X-CSRFToken": Cookies.get("csrftoken") },
            type: "POST",
            url: "",
            dataType: 'json',
            data: {
                "recipe-delete": "",
                "recipe-id": $("#deleted-recipe-id").text(),
            },
            success: function(data) {
                console.log("Recipe deleted!")
                $("#recipe-" + data.recipe_id).remove();
                modalObject.Hide();
            }
        })
    })
})