function HidePopoversByClass(className) {
    $("." + className).each(function(i, obj) {
        $("#" + obj.id).popover("hide");
    })
}

function IsPopoverHovered(className = "") {
    if (className == "")
        return $(".popover:hover").length > 0;
    return $("." + className + ".popover:hover").length > 0;
}