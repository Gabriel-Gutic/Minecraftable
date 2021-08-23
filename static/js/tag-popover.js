function SetTagPopover(element, content, timeout = 200) {
    element.popover('dispose');
    element.popover({
        trigger: "manual",
        placement: "right",
        html: true,
        content: content,
    }).off("mouseenter").on("mouseenter", function() {
        let this_ = $(this)
        $(".popover").popover('hide');
        this_.popover("show")
        $(".popover").on("mouseleave", function() {
            this_.popover('hide');
        });
    }).off("mouseleave").on("mouseleave", function() {
        let this_ = $(this)
        setTimeout(function() {
            if (!$(".popover:hover").length) {
                this_.popover("hide");
            }
        }, timeout)
    })
}