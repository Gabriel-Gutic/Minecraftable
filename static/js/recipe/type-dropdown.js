function SetItemType($item)
{
    let $button = $("#type-select-button");
    $button.find('div').remove();
    let $div = $item.find("div").clone();
    $button.append($div);

    let type = $item.data("type");
    $("#type-select-data").val(type).change();
}

$(document).ready(function(){

    $("#type-select-data").on("change", function(){
        let type = $(this).val();
        $(".recipe-image").addClass("undisplayed-data");

        if (type == "crafting_shapeless" || type == "crafting_shaped") 
        {
            $("#crafting-recipe-image").removeClass("undisplayed-data");
        } 
        else if (type == "smelting" || type == "smoking" || type == "blasting") 
        {
            $("#furnace-recipe-image").removeClass("undisplayed-data");
        } 
        else if (type == "smithing") 
        {
            $("#smithing-recipe-image").removeClass("undisplayed-data"); 
        } 
        else if (type == "campfire_cooking") 
        {
            $("#campfire-recipe-image").removeClass("undisplayed-data");
        } 
        else if (type == "stonecutting") 
        {
            $("#stonecutter-recipe-image").removeClass("undisplayed-data");
        } 
        else 
        {
            console.error("Invalid type " + type + " selected!");
        }

        $(".cooking-data").trigger("change");
        $("#result-count").trigger("change");
    });

    $.fn.SetType = function(type){
        $(".type-item").each(function(i, obj){
            let $item = $(obj);
    
            if ($item.data("type") == type)
            {
                SetItemType($item);
            }
        })
    };

    $("#type-select").SetType('crafting_shapeless');

    $(".type-item").on("click", function(){
        SetItemType($(this));
    })
})