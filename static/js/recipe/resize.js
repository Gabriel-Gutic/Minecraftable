function ResizeArea(area, base_image)
{
    let width = base_image.width();
    let height = base_image.height();

    if (width == 0 || height == 0)
        return;

    let previousWidth = base_image.data("previous-width");
    let previousHeight = base_image.data("previous-height");

    old_coords = area.attr("coords").split(",");
    new_coords = "";
    for (let i = 0; i < old_coords.length; i+=2)
    {
        new_coords += parseFloat(old_coords[i]) * width / previousWidth + ",";
        new_coords += parseFloat(old_coords[i+1]) * height / previousHeight;
        if (i + 2 < old_coords.length)
            new_coords += ",";
    }

    area.attr("coords", new_coords);
}

function ResizeAreaById(area_id, base_image)
{
    area = $("#" + area_id);
    ResizeArea(area, base_image);
}

function GetCurrentImageRect() {
    image = $(".recipe-image").not(".undisplayed-data")
    return {
        width: parseFloat(image.width()),
        height: parseFloat(image.height()),
    }
}

function ResizePlotImage(plot, base_image) {
    let width = base_image.width();
    let height = base_image.height();
    let plot_image = $("#" + plot.attr("id") + "-image");
    if (width == 0 || height == 0)
    {
        plot_image.addClass("undisplayed-data");
        return;
    }
    plot_image.removeClass("undisplayed-data");
    let previousWidth = base_image.data("previous-width");
    let previousHeight = base_image.data("previous-height");

    if (plot_image.length > 0) {
        old_width = parseFloat(plot_image.css("max-width"));
        old_height = parseFloat(plot_image.css("max-height"));

        plot_image.css("max-width", old_width * width / previousWidth);
        plot_image.css("max-height", old_height * height / previousHeight);

        old_left = parseFloat(plot_image.css("left"));
        old_top = parseFloat(plot_image.css("top"));

        plot_image.css("left", old_left * width / previousWidth);
        plot_image.css("top", old_top * height / previousHeight);
    }
}

function ResizePlotImageById(plot_id, base_image)
{
    plot = $("#" + plot_id);
    ResizePlotImage(plot, base_image);
}

function GetPlotImageRect(plot)
{
    const rect = GetCurrentImageRect();

    let coords = plot.attr("coords").split(",")
    for (let i = 0; i < coords.length; i++)
        coords[i] = parseFloat(coords[i])

    const plot_width = coords[2] - coords[0];
    const image_width = 12.0 / 100 * rect.width;

    const left = coords[0] + 1;
    const top = coords[1] + 1;

    return {
        width: image_width,
        height: image_width,
        left: left + (plot_width - image_width) / 2.0,
        top: top + (plot_width - image_width) / 2.0, 
    }
}

function SetImageRectForPlot(image, plot)
{
    rect = GetPlotImageRect(plot)

    image.css("left", rect.left);
    image.css("top", rect.top);

    image.css("width", rect.width);
    image.css("height", rect.height);
}

function ResizeFont(parent, base_image)
{
    let width = base_image.width();
    if (width == 0)
        return;
    let previousWidth = base_image.data("previous-width");

    old_font_size = parseFloat(parent.css("font-size"));
    parent.css("font-size", old_font_size * width / previousWidth);
}
$(document).ready(function() {
    const resize_object = new ResizeObserver(function(entries) {
        for (let entry of entries) {
            let image_id = entry.target.id
            let rect = entry.contentRect;

            const width = rect.width;
            const height = rect.height;

            let image = $("#" + image_id)
            if (image_id.includes("crafting")) {

                $(".crafting-area").each(function(i, obj){
                    ResizeAreaById(obj.id, image);
                    ResizePlotImageById(obj.id, image);
                })
            } else if (image_id.includes("furnace")) {

                $(".furnace-area").each(function(i, obj){
                    ResizeAreaById(obj.id, image);
                    ResizePlotImageById(obj.id, image);
                })

                $(".furnace-button").each(function(i, obj){
                    ResizeAreaById(obj.id, image)
                })

                ResizeFont($("#timer-data"), image);
                ResizeFont($("#xp-data"), image);
            } else if (image_id.includes("smithing")) {

                $(".smithing-area").each(function(i, obj){
                    ResizeAreaById(obj.id, image);
                    ResizePlotImageById(obj.id, image);
                })
            }


            if (width > 0 && height > 0) {
                image.data("previous-width", width);
                image.data("previous-height", height);
            }
        }

    });

    images = document.getElementsByClassName("recipe-image");
    for (let i = 0; i < images.length; i++) {
        $("#" + images[i].id).data("previous-width", images[i].naturalWidth)
        $("#" + images[i].id).data("previous-height", images[i].naturalHeight)

        resize_object.observe(images[i]);
    }
})