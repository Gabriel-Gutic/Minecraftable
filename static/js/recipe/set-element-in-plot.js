function SetElementInPlot(plot, element, show_popover = true) {
    let value = element.val()

    if (value == null) {
        console.log("Not any item selected");
    } else {
        let type = null
        if (element.attr("id").includes("item"))
            type = "item"
        else if (element.attr("id").includes("tag")) {
            if (plot.attr("id").includes("result")) {
                Error("The result can not be a tag!")
                return
            }
            type = "tag";

            let parts = element.attr("id").split("-")
            let popover = bootstrap.Popover.getInstance(document.getElementById("tag-image-" + parts[2]))
            SetTagPopover(plot, popover._config.content, 300)
            if (show_popover == true)
                plot.popover('show')
        }

        parts = value.split("~");

        let element_id = parts[0];
        let element_image = parts[1];

        let id = plot.attr("id");
        img_id = id + "-image";

        let hover_plot = $("#plot-hover-image");
        let x = parseInt(hover_plot.css("left"), 10);
        let y = parseInt(hover_plot.css("top"), 10);
        let hover_width = hover_plot.width();

        let exists = ($("#" + img_id).length) > 0;

        if (exists) {
            image = $("#" + img_id);
            image.attr("src", element_image);
            $("#" + img_id + "-image").text(type + `~` + element_id)
        } else {
            $("#image-div").append(`<img id="` + img_id + `" src="` + element_image + `" class="plot-item-image">`)
            $("#image-div").append(`<p id="` + img_id + `-data" class="undisplayed-data">` + type + `~` + element_id + `</p>`)
            image = $("#" + img_id);
        }

        image.css("max-width", hover_width)
        image.css("max-height", hover_width)

        let width = image.width()
        let height = image.height()

        image.css("left", x + (hover_width - width) / 2.0);
        image.css("top", y + (hover_width - height) / 2.0);
    }
}