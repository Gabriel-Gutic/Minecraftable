$(document).ready(function() {

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
                li.append(`<div id="item-line-` + items[i].id + `"></div>`)

                var div = $("#item-line-" + items[i].id);
                div.append(`<input class="form-check-input" type="radio" name="flexRadioDefault" id="radio-item-` + items[i].id + `">`)
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
        const id = $(this).attr("id")

        var list = id.split("-")
        const x = parseInt(list[1], 10)
        const y = parseInt(list[2], 10)

        var hover = $("#plot-hover-image")
        hover.css("top", y)
        hover.css("left", x)
        hover.css("opacity", 0.7);
    }).mouseout(function() {
        $("#plot-hover-image").css("opacity", 0);
    }).on("click", function() {
        console.log("Plot pressed!")
    })

    $("#search-item-input").on("input", function() {

        const text = $(this).val()
        $(".item-element").each(function(i, obj) {
            list = obj.id.split("-")

            var item_name = $("label-item-" + list[3]).val()
            console.log(item_name)
        })

    })
})

function FillListOfItems() {
    var list = $("#item-list")

    var items = $("#list-of-items").value;
    console.log(items)
    for (var i = 0; i < list.length; i++) {
        list.append(`<li id="list-group-item-{{item.id}}" class="list-group-item item-element d-flex justify-content-between align-items-center">
                        <div>
                            <input class="form-check-input" type="radio" name="flexRadioDefault" id="radio-item-{{item.id}}">
                            <label id="label-item-{{item.id}}" class="form-check-label" for="radio-item-{{item.id}}">
                                {{item.name}}
                            </label>
                        </div>
                        {% if item.image %}
                            <img id="item-image-{{item.id}}" src="{{item.image.url}}" class="item-image">
                        {% endif %}
                    </li>`)
    }
}