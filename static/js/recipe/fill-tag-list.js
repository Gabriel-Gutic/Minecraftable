$(document).ready(function() {
    $.ajax({
        url: "",
        type: "GET",
        data: {
            'prepare-tags': '',
        },
        success: function(data) {
            var list = $("#tag-list")
            const tags = data.tags;
            for (var i = 0; i < tags.length; i++) {
                tag_id = tags[i].id
                const id = "list-group-tag-" + tag_id
                list.append(`<li id="` + id + `" class="list-group-item tag-element d-flex justify-content-between align-items-center"></li>`)
                var li = $("#" + id)
                li.css("display", "none")
                li.append(`<div id="tag-line-` + tag_id + `"></div>`)

                var div = $("#tag-line-" + tag_id);
                div.append(`<input class="form-check-input" type="radio" name="data-radio-list" id="radio-tag-` + tag_id + `" value="` + tag_id + `~` + tags[i].image + `">`)
                div.append(`<label id="label-tag-` + tag_id + `" class="form-check-label ms-2" for="radio-tag-` + tag_id + `">
                                ` + tags[i].name + `
                            </label>`);

                if (tags[i].image != null) {
                    image_id = "tag-image-" + tag_id
                    li.append(`<img id="` + image_id + `" src="` + tags[i].image + `" class="tag-image element-image">`)

                    let content = `<ul id="tag-` + tag_id + `-list-items" class="list-group object-list mt-3 border border-light border-2">`

                    items = tags[i].items
                    for (let i = 0; i < items.length; i++) {
                        content += `
                        <li id="tag-` + tag_id + `-list-item-` + items[i].id + `" class="list-group-item d-flex justify-content-between align-items-center">
                            ` + items[i].name + `
                            <img id="image-tag-` + tag_id + `-list-item-` + items[i].id + `" src="` + items[i].image + `" class="element-image ms-2">
                        </li>`
                    }

                    content += `</ul>`

                    SetTagPopover($("#" + image_id), content);
                }
            }

            $("#tag-list-finished").val("true").change();
        }
    })
})