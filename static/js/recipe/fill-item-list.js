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
                var $li = $("#" + id)
                $li.css("display", "none")

                let item = new ElementList(items[i], 'item')
                $li.append(item.input)

                image = item.image
                if (image != null) {
                    $li.append(image)
                }
            }

            $("#item-list-finished").val("true").change();
        }
    })
})