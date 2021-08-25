$(document).ready(function() {

    $("#recipe-type-select").on("change", function() {
        selected = $(this).val();
        if (selected == "crafting_shapeless" || selected == "crafting_shaped") {
            $(".recipe-image").addClass("undisplayed-data");
            $("#crafting-recipe-image").removeClass("undisplayed-data");
        } else if (selected == "smelting" || selected == "smoking" || selected == "blasting") {
            $(".recipe-image").addClass("undisplayed-data");
            $("#furnace-recipe-image").removeClass("undisplayed-data");
        }
    })

})