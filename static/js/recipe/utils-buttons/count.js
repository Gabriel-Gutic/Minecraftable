$(document).ready(function() {

    $("#erase-plot-button").on("click", function() {
        class_name = "btn-primary"

        if ($(this).hasClass(class_name)) {
            $(this).removeClass(class_name);
        } else {
            $(this).addClass(class_name);
        }

    })

    $("#increment-result-count-button").on("click", function() {
        let $counter = $("#result-count");
        let count = parseInt($counter.text(), 10);
        $counter.text(count + 1).change();
    })

    $("#decrement-result-count-button").on("click", function() {
        let $counter = $("#result-count");
        let count = parseInt($counter.text(), 10);
        $counter.text(count - 1).change();
    })

    $("#result-count").on("change", function() {
        let selected = $("#recipe-type-select").val()
        
        let $increment = $("#increment-result-count-button")
        let $decrement = $("#decrement-result-count-button")
        
        let $counter = $(this)
        if (selected == "crafting_shapeless" || selected == "crafting_shaped" || selected == "stonecutting") {
            $counter.removeClass("undisplayed-data");
            $increment.attr("disabled", false)
            $decrement.attr("disabled", false)
        } else {
            $counter.addClass("undisplayed-data");
            $increment.attr("disabled", true)
            $decrement.attr("disabled", true)
            return
        }

        let top = null
        let left = null
        let count = parseInt($counter.text(), 10)

        if (selected == "crafting_shapeless" || selected == "crafting_shaped") {
            top = "53%"
            left = 89
            if (count > 9) {
                left -= 4;
            }
        } else {
            top = "66%"
            left = 85
            if (count > 9) {
                left -= 5;
            }
        }
        $counter.css("top", top)
        $counter.css("left", left + "%")

        if (count >= 64) {
            $increment.attr("disabled", true)
        } else {
            $increment.attr("disabled", false)
        }

        if (count <= 1) {
            $decrement.attr("disabled", true)
        } else {
            $decrement.attr("disabled", false)
        }
    })
})