function SetTagPopover(element, content) {
    element.popover({
        trigger: "manual",
        placement: "right",
        html: true,
        content: content,
    }).on("mouseenter", function() {
        let this_ = $(this)
        this_.popover("show")
        $(".popover").on("mouseleave", function() {
            this_.popover('hide');
        });
    }).on("mouseleave", function() {
        let this_ = $(this)
        setTimeout(function() {
            if (!$(".popover:hover").length) {
                this_.popover("hide");
            }
        }, 200)
    })
}