$(document).ready(function() {

    const resize_object = new ResizeObserver(function(entries) {
        let rect = entries[0].contentRect;

        let width = rect.width;

        if (width < 975) {
            $(".col-image-logo").css("display", "none");
        } else {
            $(".col-image-logo").css("display", "inline");
        }
    });

    resize_object.observe(document.getElementById("base-row"));
})