$(document).ready(function() {
    $(".recipe-image-plot").mouseover(function() {
        const id = $(this).attr("id");

        let image_rect = $("#image-rect").text().split(",");
        const width = parseInt(image_rect[0]);
        const height = parseInt(image_rect[1]);

        const hover_width = 12.22 / 100 * width;
        const margin = 5.70 / 100 * width;
        const square_width = 14.0 / 100 * width;

        var hover = $("#plot-hover-image");

        if (id == "crafting-plot-result") {
            hover.css("left", 78.8 / 100 * width);
            hover.css("top", 37.9 / 100 * height)
        } else if (id.includes("crafting-plot")) {
            var list = id.split("-");
            const x = parseInt(list[2], 10);
            const y = parseInt(list[3], 10);

            hover.css("left", margin + x * square_width);
            hover.css("top", margin + y * square_width);
        }


        hover.css("width", hover_width);
        hover.css("height", hover_width);
        hover.css("opacity", 0.7);
    }).mouseout(function() {
        $("#plot-hover-image").css("opacity", 0);
    }).on("click", function(event) {


        let selected = $("input[type=radio][name=data-radio-list]:checked")
        selected_value = selected.val()

        if (selected_value == null) {
            console.log("Not any item selected");
        } else {
            $(this).popover('dispose')

            let type = null
            if (selected.attr("id").includes("item"))
                type = "item"
            else if (selected.attr("id").includes("tag")) {
                if ($(this).attr("id").includes("result")) {
                    Error("The result can not be a tag!")
                    return
                }
                type = "tag";

                let parts = selected.attr("id").split("-")
                let popover = bootstrap.Popover.getInstance(document.getElementById("tag-image-" + parts[2]))
                SetTagPopover($(this), popover._config.content)
                $(this).popover('show')
            }

            parts = selected_value.split("~");

            let element_id = parts[0];
            let element_image = parts[1];

            let id = $(this).attr("id");
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
    }).on("contextmenu", function() {
        let id = $(this).attr("id");
        img_id = id + "-image";

        $(".plot-item-image").each(function(i, obj) {
            if (obj.id.includes(img_id)) {
                obj.remove();

                $("#" + obj.id + "-data").remove();
            }
        })
        return false;
    })
})