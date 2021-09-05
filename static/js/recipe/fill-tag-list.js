$(document).ready(function() {
    $.ajax({
        url: "",
        type: "GET",
        data: {
            'prepare-tags': '',
        },
        success: function(data) {

            var $list = $("#tag-list")
            const tags = data.tags;
            for (let i = 0; i < tags.length; i++) {
                let tag_id = tags[i].id
                const id = "list-group-tag-" + tag_id
                $list.append(`<li id="` + id + `" class="list-group-item tag-element d-flex justify-content-between align-items-center"></li>`)
                var $li = $("#" + id)
                $li.css("display", "none")


                let tag = new ElementList(tags[i], 'tag')
                $li.append(tag.input)

                let image = tag.image
                if (image != null) {
                    $li.append(image)

                    items = tags[i].items

                    let $image = $("#tag-image-" + tags[i].id)
                    let popover_list = new PopoverList({
                        parent: $image,
                        id: "tag-" + tag_id + "-popover",
                        popover_classes: "tag-list-element-popover",
                    });
                    for (let j = 0; j < items.length; j++) {
                        popover_list.AddElement({
                            type:  "item",
                            id:    items[j].id, 
                            name:  items[j].name, 
                            image: items[j].image,
                        })
                    }
                    popover_list.SetPredifinedTrigger("tag-list-element-popover")
                }
            }

            $("#tag-list-finished").val("true").change();
        }
    })
})