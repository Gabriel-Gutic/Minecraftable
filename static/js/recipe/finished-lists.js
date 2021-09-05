$(document).ready(function() {

    $(".finished-list").on("change", function() {
        ok1 = $("#item-list-finished").val()
        ok2 = $("#tag-list-finished").val()

        if (ok1 == "true" && ok2 == "true") {
            FillRecipeData()
        }
    })

})