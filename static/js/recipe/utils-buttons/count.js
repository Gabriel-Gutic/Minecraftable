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
        let counter = $("#result-count")
        let count = parseInt(counter.text(), 10)
        counter.text(count + 1).change()
    })

    $("#decrement-result-count-button").on("click", function() {
        let counter = $("#result-count")
        let count = parseInt(counter.text(), 10)
        counter.text(count - 1).change()
    })

    $("#result-count").on("change", function() {
        let selected = $("#recipe-type-select").val()

        let increment = $("#increment-result-count-button")
        let decrement = $("#decrement-result-count-button")

        if (selected == "crafting_shapeless" || selected == "crafting_shaped" || selected == "stonecutting") {
            $("#result-count").removeClass("undisplayed-data");
            increment.attr("disabled", false)
            decrement.attr("disabled", false)
        } else {
            $("#result-count").addClass("undisplayed-data");
            increment.attr("disabled", true)
            decrement.attr("disabled", true)
            return
        }
        let top = null
        let left = null
        if (selected == "crafting_shapeless" || selected == "crafting_shaped") {
            top = "50%"
            left = 89
        } else {
            top = "63%"
            left = 86
        }
        $(this).css("top", top)

        let counter = $("#result-count")
        let count = parseInt(counter.text(), 10)
        if (count >= 64) {
            increment.attr("disabled", true)
        } else {
            increment.attr("disabled", false)
        }

        if (count <= 1) {
            decrement.attr("disabled", true)
        } else {
            decrement.attr("disabled", false)
        }

        if (count > 9) {
            left -= 3
        }
        $(this).css("left", left + "%")
    })


    
})