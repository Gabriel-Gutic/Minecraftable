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
        let rect = entries[0].contentRect;

        const width = rect.width;
        const height = rect.height;

        $("#image-rect").text(width + "," + height);

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
                area.attr("coords", lu[i] + "," + lu[j] + "," + rd[i] + "," + rd[j]);

                let image = $("#crafting-plot-" + i + "-" + j + "-image")
                if (image.length > 0) {
                    ResizePlotImage(image, image_width, lu[i], lu[j])
                }
            }
        $("#crafting-plot-result").attr("coords", 75.5 / 100 * width + "," + 32.3 / 100 * height + "," + 94.2 / 100 * width + "," + 67.6 / 100 * height);
        image = $("#crafting-plot-result-image")
        if (image.length > 0) {
            x = 78.8 / 100 * width
            y = 37.9 / 100 * height
            ResizePlotImage(image, image_width, x, y)
        }
    });

    images = document.getElementsByClassName("recipe-image");
    for (let i = 0; i < images.length; i++) {
        resize_object.observe(images[i]);
    }

})