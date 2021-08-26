function GetCurrentImageRect() {
    let image_rect = null
    $(".recipe-image-rect").each(function(i, obj) {
        let id = obj.id.replace("-rect", "")
        let image = $("#" + id)
        if (!image.hasClass("undisplayed-data")) {
            image_rect = $("#" + obj.id).text().split(",");
        }
    })
    return image_rect
}

function ResizePlotImage(plot, new_width, x, y) {
    let image = $("#" + plot.attr("id") + "-image")
    if (image.length > 0) {
        image.css("max-width", new_width)
        image.css("max-height", new_width)

        let width = image.width()
        let height = image.height()

        image.css("left", x + (new_width - width) / 2.0);
        image.css("top", y + (new_width - height) / 2.0);
    }
}

$(document).ready(function() {

    const resize_object = new ResizeObserver(function(entries) {
        for (let entry of entries) {
            let image_id = entry.target.id
            let rect = entry.contentRect;

            const width = rect.width;
            const height = rect.height;
            if (image_id.includes("crafting")) {

                $("#crafting-recipe-image-rect").text(width + "," + height);

                let lu = [] //Left Up Corner Coords
                let rd = [] //Right Down Corner Coords

                //Margin and SquareWidth in pixels
                const margin = 5.55 / 100 * width;
                const square_width = 14.0 / 100 * width;
                const image_width = 12.0 / 100 * width;

                lu.push(margin);
                lu.push(margin + square_width);
                lu.push(margin + 2 * square_width);

                const point = margin + 12.22 / 100 * width;
                rd.push(point);
                rd.push(point + square_width);
                rd.push(point + 2 * square_width);

                for (let i = 0; i < 3; i++)
                    for (let j = 0; j < 3; j++) {
                        area = $("#crafting-plot-" + i + "-" + j);
                        area.attr("coords", lu[j] + "," + lu[i] + "," + rd[j] + "," + rd[i]);

                        ResizePlotImage(area, image_width, lu[j], lu[i])
                    }
                let plot = $("#crafting-plot-result")
                plot.attr("coords", 75.5 / 100 * width + "," + 32.3 / 100 * height + "," + 94.2 / 100 * width + "," + 67.6 / 100 * height);
                ResizePlotImage(plot, image_width, 78.8 / 100 * width, 37.9 / 100 * height)
            } else if (image_id.includes("furnace")) {

                $("#furnace-recipe-image-rect").text(width + "," + height);
                let image_width = 12.0 / 100 * width;

                let plot = $("#furnace-plot-result")
                plot.attr("coords", 68.7 / 100 * width + "," + 39 / 100 * height + "," + 87 / 100 * width + "," + 69 / 100 * height);
                ResizePlotImage(plot, image_width, 72 / 100 * width, 44 / 100 * height)
            } else if (image_id.includes("smithing")) {
                $("#smithing-recipe-image-rect").text(width + "," + height);
                let image_width = 12.0 / 100 * width;

                let plot = $("#smithing-plot-base")
                plot.attr("coords", 7 / 100 * width + "," + 56 / 100 * height + "," + 24 / 100 * width + "," + 87 / 100 * height);
                ResizePlotImage(plot, image_width, 9.8 / 100 * width, 59.5 / 100 * height)

                plot = $("#smithing-plot-addition")
                plot.attr("coords", 40 / 100 * width + "," + 56 / 100 * height + "," + 57 / 100 * width + "," + 87 / 100 * height);
                ResizePlotImage(plot, image_width, 42.8 / 100 * width, 59.5 / 100 * height)

                plot = $("#smithing-plot-result")
                plot.attr("coords", 77 / 100 * width + "," + 56 / 100 * height + "," + 94 / 100 * width + "," + 87 / 100 * height);
                ResizePlotImage(plot, image_width, 79.8 / 100 * width, 59.5 / 100 * height)
            }
        }

    });

    images = document.getElementsByClassName("recipe-image");
    for (let i = 0; i < images.length; i++) {
        resize_object.observe(images[i]);
    }
})