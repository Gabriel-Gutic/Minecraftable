$(document).ready(function() {
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

    $("#search-tag-input").on("input", function() {

        const text = $(this).val().toLowerCase();
        $(".tag-element").each(function(i, obj) {
            list = obj.id.split("-")
            var tag_name = $("#label-tag-" + list[3]).text().toLowerCase();

            if (!tag_name.includes(text)) {
                $("#list-group-tag-" + list[3]).removeClass("d-flex")
            } else {
                $("#list-group-tag-" + list[3]).addClass("d-flex")
            }
        })

    })
})