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
                li.css("display", "none")
                li.append(`<div id="item-line-` + items[i].id + `"></div>`)

                var div = $("#item-line-" + items[i].id);
                div.append(`<input class="form-check-input" type="radio" name="data-radio-list" id="radio-item-` + items[i].id + `" value="` + items[i].id + `~` + items[i].image + `">`)
                div.append(`<label id="label-item-` + items[i].id + `" class="form-check-label ms-2" for="radio-item-` + items[i].id + `">
                                ` + items[i].name + `
                            </label>`);

                if (items[i].image != null) {
                    image_id = "item-image-" + items[i].id
                    li.append(`<img id="` + image_id + `" src="` + items[i].image + `" class="item-image element-image">`)
                }
            }

            $("#item-list-finished").val("true").change();
        }
    })
})