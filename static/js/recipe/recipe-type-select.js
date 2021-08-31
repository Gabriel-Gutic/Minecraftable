$(document).ready(function() {

    $("#recipe-type-select").on("change", function() {
        selected = $(this).val();
        $(".recipe-image").addClass("undisplayed-data");
        if (selected == "crafting_shapeless" || selected == "crafting_shaped") {
            $("#crafting-recipe-image").removeClass("undisplayed-data");
        } else if (selected == "smelting" || selected == "smoking" || selected == "blasting") {
            
            $("#furnace-recipe-image").removeClass("undisplayed-data");
        } else if (selected == "smithing") {
            $("#smithing-recipe-image").removeClass("undisplayed-data");
        } else if (selected == "campfire_cooking") {
            $("#campfire-recipe-image").removeClass("undisplayed-data");
        } else if (selected == "stonecutting") {
            $("#stonecutter-recipe-image").removeClass("undisplayed-data");
        } else {
            console.error("Invalid type " + selected + " selected!");
        }

        $(".cooking-data").trigger("change");
        $("#result-count").trigger("change");
    })

})