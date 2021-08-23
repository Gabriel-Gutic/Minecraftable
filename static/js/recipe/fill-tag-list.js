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


                tag = new ElementList(tags[i], 'tag')
                li.append(tag.input)

                image = tag.image
                if (image != null) {
                    li.append(image)

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

                    SetTagPopover($("#tag-image-" + tags[i].id), content);
                }
            }

            $("#tag-list-finished").val("true").change();
        }
    })
})