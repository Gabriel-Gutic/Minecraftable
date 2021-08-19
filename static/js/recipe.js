$(document).ready(function() {
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
            }
        $("#crafting-plot-result").attr("coords", 75.5 / 100 * width + "," + 32.3 / 100 * height + "," + 94.2 / 100 * width + "," + 67.6 / 100 * height);
    });

    images = document.getElementsByClassName("recipe-image");
    for (let i = 0; i < images.length; i++) {
        resize_object.observe(images[i]);
    }

    $.ajax({
        url: "",
        type: "GET",
        data: {
            'prepare-items': '',
        },
        success: function(data) {
            var list = $("#item-list")
            const items = data.items;
            for (var i = 0; i < items.length; i++) {
                const id = "list-group-item-" + items[i].id
                list.append(`<li id="` + id + `" class="list-group-item item-element d-flex justify-content-between align-items-center"></li>`)
                var li = $("#" + id)
                li.css("display", "none")
                li.append(`<div id="item-line-` + items[i].id + `"></div>`)

                var div = $("#item-line-" + items[i].id);
                div.append(`<input class="form-check-input" type="radio" name="item-radio-list" id="radio-item-` + items[i].id + `" value="` + items[i].id + `~` + items[i].image + `">`)
                div.append(`<label id="label-item-` + items[i].id + `" class="form-check-label ms-2" for="radio-item-{{item.id}}">
                                ` + items[i].name + `
                            </label>`);

                if (items[i].image != null) {
                    li.append(`<img id="item-image-` + items[i].id + `" src="` + items[i].image + `" class="item-image">`)
                }
            }
        }
    })

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
    }).on("click", function() {
        console.log("Plot pressed!")

        selected_item = $("input[type=radio][name=item-radio-list]:checked").val()
        if (selected_item == null) {
            console.log("Not any item slected");
        } else {
            let parts = selected_item.split("~");

            let item_id = parts[0];
            let item_image = parts[1];

            let id = $(this).attr("id");
            img_id = id + "-image"

            let hover_plot = $("#plot-hover-image");
            let x = hover_plot.css("left");
            let y = hover_plot.css("top");
            let hover_width = hover_plot.css("width");

            let exists = ($("#" + img_id).length) > 0;

            if (exists) {
                image = $("#" + img_id);
                image.attr("src", item_image);
            } else {
                $("#image-div").append(`<img id="` + img_id + `" src="` + item_image + `" class="plot-item-image">`)
                image = $("#" + img_id);
            }

            image.css("left", x);
            image.css("top", y);
            image.css("width", hover_width)
            image.css("height", hover_width)
        }
    })

    $("#search-item-input").on("input", function() {

        const text = $(this).val().toLowerCase();
        $(".item-element").each(function(i, obj) {
            list = obj.id.split("-")
            var item_name = $("#label-item-" + list[3]).text().toLowerCase();

            if (!item_name.includes(text)) {
                $("#list-group-item-" + list[3]).removeClass("d-flex")
            } else {
                $("#list-group-item-" + list[3]).addClass("d-flex")
            }
        })

    })
})