function IsEraseChecked() {
    return $("#erase-plot-button").hasClass("btn-primary")
}

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
        let counter = $("#result-count")
        let count = parseInt(counter.text(), 10)
        let increment = $("#increment-result-count-button")
        if (count >= 64) {
            increment.attr("disabled", true)
        } else {
            increment.attr("disabled", false)
        }

        let decrement = $("#decrement-result-count-button")
        if (count <= 1) {
            decrement.attr("disabled", true)
        } else {
            decrement.attr("disabled", false)
        }

        if (count > 9) {
            $(this).css("left", "87%")
        } else {
            $(this).css("left", "89%")
        }
    })
})