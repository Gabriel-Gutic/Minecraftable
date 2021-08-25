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

$(document).ready(function() {
    function ResizePlotImage(image, new_width, x, y) {
        image.css("max-width", new_width)
        image.css("max-height", new_width)

        let width = image.width()
        let height = image.height()

        image.css("left", x + (new_width - width) / 2.0);
        image.css("top", y + (new_width - height) / 2.0);
    }
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

                        let image = $("#crafting-plot-" + i + "-" + j + "-image")
                        if (image.length > 0) {
                            ResizePlotImage(image, image_width, lu[j], lu[i])
                        }
                    }
                $("#crafting-plot-result").attr("coords", 75.5 / 100 * width + "," + 32.3 / 100 * height + "," + 94.2 / 100 * width + "," + 67.6 / 100 * height);
                image = $("#crafting-plot-result-image")
                if (image.length > 0) {
                    x = 78.8 / 100 * width
                    y = 37.9 / 100 * height
                    ResizePlotImage(image, image_width, x, y)
                }
            } else if (image_id.includes("furnace")) {

                $("#furnace-recipe-image-rect").text(width + "," + height);
                let image_width = 12.0 / 100 * width;

                $("#furnace-plot-result").attr("coords", 68.7 / 100 * width + "," + 39 / 100 * height + "," + 87 / 100 * width + "," + 69 / 100 * height);
                let image = $("#furnace-plot-result-image")
                if (image.length > 0) {
                    x = 70 / 100 * width
                    y = 41 / 100 * height
                    ResizePlotImage(image, image_width, x, y)
                }
            }
        }

    });

    images = document.getElementsByClassName("recipe-image");
    for (let i = 0; i < images.length; i++) {
        resize_object.observe(images[i]);
    }
})