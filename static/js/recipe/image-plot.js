function SetHoverInPlot(plot_id) {
    hover = $("#plot-hover-image")
    let image_rect = GetCurrentImageRect();

    const width = parseInt(image_rect[0]);
    const height = parseInt(image_rect[1]);

    const element_width = 12.22 / 100 * width;
    const margin = 5.70 / 100 * width;
    const square_width = 14.0 / 100 * width;

    if (plot_id == "crafting-plot-result") {
        hover.css("left", 78.8 / 100 * width);
        hover.css("top", 37.9 / 100 * height)
    } else if (plot_id.includes("crafting-plot")) {
        var list = plot_id.split("-");
        const x = parseInt(list[2], 10);
        const y = parseInt(list[3], 10);

        hover.css("top", margin + x * square_width);
        hover.css("left", margin + y * square_width);
    } else if (plot_id == "furnace-plot-result") {
        hover.css("left", 72 / 100 * width);
        hover.css("top", 44 / 100 * height)
    }

    hover.css("width", element_width);
    hover.css("height", element_width);
    hover.css("opacity", 0.7);
}

$(document).ready(function() {
    $(".recipe-image-plot").mouseover(function() {
        const id = $(this).attr("id");
        SetHoverInPlot(id);
    }).mouseout(function() {
        $("#plot-hover-image").css("opacity", 0);
    }).on("click", function(event) {
        if (IsEraseChecked()) {
            let id = $(this).attr("id");
            console.log(id)
            img_id = id + "-image";

            this_ = $(this)
            $(".plot-item-image").each(function(i, obj) {
                if (obj.id.includes(img_id)) {
                    this_.popover('dispose');
                    this_.off("mouseenter");
                    this_.off("mouseleave");
                    obj.remove();

                    $("#" + obj.id + "-data").remove();
                }
            })
        } else {
            let selected = $("input[type=radio][name=data-radio-list]:checked")
            SetElementInPlot($(this), selected);
        }
    })
})