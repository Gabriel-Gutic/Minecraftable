function ResizeArea($area, $base_image)
{
    let width = $base_image.width();
    let height = $base_image.height();

    if (width == 0 || height == 0)
        return;

    let previousWidth = $base_image.data("previous-width");
    let previousHeight = $base_image.data("previous-height");

    let old_coords = $area.attr("coords").split(",");
    let new_coords = "";
    for (let i = 0; i < old_coords.length; i+=2)
    {
        console.log(previousWidth);
        new_coords += parseFloat(old_coords[i]) * width / previousWidth + ",";
        new_coords += parseFloat(old_coords[i+1]) * height / previousHeight;
        if (i + 2 < old_coords.length)
            new_coords += ",";
    }

    $area.attr("coords", new_coords);
}

function ResizeAreaById(area_id, $base_image)
{
    $area = $("#" + area_id);
    ResizeArea($area, $base_image);
}

function GetCurrentImageRect() {
    $image = $(".recipe-image").not(".undisplayed-data")
    return {
        width: parseFloat($image.width()),
        height: parseFloat($image.height()),
    }
}

function GetCurrentImageId()
{
    return $(".recipe-image").not(".undisplayed-data").attr("id");
}

function ResizePlotImageById(plot_id, $base_image)
{
    let width = $base_image.width();
    let height = $base_image.height();
    let $plot_image = $("#" + plot_id + "-image");
    if (width == 0 || height == 0)
    {
        $plot_image.addClass("undisplayed-data");
        return;
    }
    $plot_image.removeClass("undisplayed-data");
    let previousWidth = $base_image.data("previous-width");
    let previousHeight = $base_image.data("previous-height");

    if ($plot_image.length > 0) {
        let old_width = parseFloat($plot_image.css("max-width"));
        let old_height = parseFloat($plot_image.css("max-height"));

        $plot_image.css("max-width", old_width * width / previousWidth);
        $plot_image.css("max-height", old_height * height / previousHeight);

        let old_left = parseFloat($plot_image.css("left"));
        let old_top = parseFloat($plot_image.css("top"));

        $plot_image.css("left", old_left * width / previousWidth);
        $plot_image.css("top", old_top * height / previousHeight);
    }
}


function ResizePlotImage($plot, $base_image) {
    ResizePlotImageById($plot.attr("id"), $base_image);
}

function GetPlotImageRect(plot)
{
    const rect = GetCurrentImageRect();

    let coords = plot.attr("coords").split(",")
    for (let i = 0; i < coords.length; i++)
        coords[i] = parseFloat(coords[i])

    const plot_width = coords[2] - coords[0];

    let id = GetCurrentImageId();
    let image_width = null;
    let left = coords[0];
    let top = coords[1];
    if (id.includes("stonecutter") || id.includes("campfire")) 
    {
        image_width = 17.0 / 100 * rect.width;
    }
    else 
    {
        left++;
        top++;
        image_width = 12.0 / 100 * rect.width;
    }
    
    return {
        width: image_width,
        height: image_width,
        left: left + (plot_width - image_width) / 2.0,
        top: top + (plot_width - image_width) / 2.0, 
    }
}

function SetImageRectForPlot($image, $plot, addition_function = () => {})
{
    var func = () => {
        addition_function();
        let rect = GetPlotImageRect($plot)

        $image.css("max-width", rect.width);
        $image.css("max-height", rect.height);

        let new_width = parseFloat($image.css("width"));
        let new_height = parseFloat($image.css("height"));

        let max = rect.width;

        $image.css("left", rect.left + (max - new_width) / 2.0);
        $image.css("top", rect.top + (max - new_height) / 2.0);
    }

    $image.on("load", func);

    if ($image.prop("complete") && $image.prop("naturalHeight") !== 0)
    {
        $image.trigger("load");
    }
}

function ResizeFont($parent, $base_image)
{
    let height = $base_image.height();
    if (height == 0)
        return;
    let previousHeight = $base_image.data("previous-height");

    let old_font_size = parseFloat($parent.css("font-size"));
    $parent.css("font-size", old_font_size * height / previousHeight);
}

$(document).ready(function() {
    
    $("#result-count").data("crafting-font-size", 15.0 / 100 * parseInt($("#crafting-recipe-image").prop("naturalHeight"), 10) + "px");
    $("#result-count").data("stonecutter-font-size", 20.0 / 100 * parseInt($("#stonecutter-recipe-image").prop("naturalHeight"), 10) + "px");
    $("#result-count").css("font-size", $("#result-count").data("crafting-font-size"));

    $("#timer-data").data("furnace-font-size", 10.1 / 100 * parseInt($("#furnace-recipe-image").prop("naturalHeight"), 10) + "px")
    $("#timer-data").data("campfire-font-size", 9.7 / 100 * parseInt($("#campfire-recipe-image").prop("naturalHeight"), 10) + "px")
    const resize_object = new ResizeObserver(function(entries) {
        for (let entry of entries) {
            let image_id = entry.target.id
            let rect = entry.contentRect;

            const width = rect.width;
            const height = rect.height;

            if (image_id.includes("furnace"))
                $("#furnace-plot-ingredient-image").removeClass("undisplayed-data");
            else 
                $("#furnace-plot-ingredient-image").addClass("undisplayed-data");

            if (image_id.includes("stonecutter"))
                $("#stonecutter-plot-ingredient-image").removeClass("undisplayed-data");
            else 
                $("#stonecutter-plot-ingredient-image").addClass("undisplayed-data");

            let $result_count = $("#result-count");
            let $timer_data = $("#timer-data");
            let $image = $("#" + image_id);
            if (image_id.includes("crafting")) {

                $(".crafting-area").each(function(i, obj){
                    ResizeAreaById(obj.id, $image);
                    ResizePlotImageById(obj.id, $image);
                })
                
                if (width > 0)
                {
                    $result_count.css("font-size", $result_count.data("crafting-font-size"));
                    ResizeFont($result_count, $image);
                    $result_count.data("crafting-font-size", $result_count.css("font-size"));
                }
            } 
            else if (image_id.includes("furnace")) {

                $(".furnace-area").each(function(i, obj){
                    ResizeAreaById(obj.id, $image);
                    ResizePlotImageById(obj.id, $image);
                })

                $(".furnace-button").each(function(i, obj){
                    ResizeAreaById(obj.id, $image)
                })

                if (width > 0)
                {
                    $timer_data.css("font-size", $timer_data.data("furnace-font-size"));
                    ResizeFont($timer_data, $image);
                    $timer_data.data("furnace-font-size", $timer_data.css("font-size"));
                }
                ResizeFont($("#xp-data"), $image);
            } 
            else if (image_id.includes("smithing")) {

                $(".smithing-area").each(function(i, obj){
                    ResizeAreaById(obj.id, $image);
                    ResizePlotImageById(obj.id, $image);
                })
            }
            else if (image_id.includes("campfire"))
            {
                $(".campfire-area").each(function(i, obj){
                    ResizeAreaById(obj.id, $image);
                    ResizePlotImageById(obj.id, $image);
                })
                
                $(".campfire-button").each(function(i, obj){
                    ResizeAreaById(obj.id, $image)
                })

                if (width > 0)
                {
                    $timer_data.css("font-size", $timer_data.data("campfire-font-size"));
                    ResizeFont($("#timer-data"), $image);
                    $timer_data.data("campfire-font-size", $timer_data.css("font-size"));
                }
            }
            else if (image_id.includes("stonecutter"))
            {
                $(".stonecutter-area").each(function(i, obj){
                    ResizeAreaById(obj.id, $image);
                    ResizePlotImageById(obj.id, $image);
                })  

                if (width > 0) 
                {
                    $result_count.css("font-size", $result_count.data("stonecutter-font-size"));
                    ResizeFont($("#result-count"), $image);
                    $result_count.data("stonecutter-font-size", $result_count.css("font-size"));
                }
            }


            if (width > 0 && height > 0) {
                $image.data("previous-width", width);
                $image.data("previous-height", height);
            }
        }

    });

    images = document.getElementsByClassName("recipe-image");
    for (let i = 0; i < images.length; i++) 
    {
        let $image = $(images[i]);
        images[i].onload = function () {
            $image.data("previous-width", images[i].naturalWidth);
            $image.data("previous-height", images[i].naturalHeight);

            resize_object.observe(images[i]);
        }

        if (images[i].complete && images[i].naturalWidth !== 0) {
            $image.trigger("load");
        }
    }

    const resize_dropdown = new ResizeObserver(function(entries){
        for (const entry of entries) {
            let rect = entry.contentRect;
            const width = rect.width;

            $("#type-list").css("width", width + 50);
        }
    })

    resize_dropdown.observe(document.getElementById("type-select-button"));
})