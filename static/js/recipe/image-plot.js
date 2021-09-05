function IsEraseChecked() {
    return $("#erase-plot-button").hasClass("btn-primary")
}

function SetHoverInPlot(plot_id) {
    let $hover = $("#plot-hover-image")
    SetImageRectForPlot($hover, $("#" + plot_id));
    $hover.css("opacity", 0.7);
}

function IsTagInPlot(plot_id) {
    $image = $("#" + plot_id + "-image")
    if ($image.length > 0) {
        $data = $("#" + plot_id + "-image-data")

        if ($data.text().includes("tag"))
            return true
    }
    return false
}

function IsListInPlot(plot_id) {
    return $("#" + plot_id).hasClass("recipe-list-plot");
}

function ShowList(plot_id) {
    $plot_image = $("#" + plot_id + "-image");
    if ($plot_image.length > 0) {
        popover_list = $plot_image.data("popover-list");
        if (popover_list) {
            if (IsListInPlot(plot_id)) {
                count = popover_list.Size();
                if (count <= 0)
                    return
                HidePopoversByClass("plot-list-popover");
            } else if (IsTagInPlot(plot_id)) {
                HidePopoversByClass("plot-tag-popover");
            }
            popover_list.Show();
            popover_list.OnMouseLeave(function() {
                setTimeout(function() {
                    if (!IsPopoverHovered()) {
                        popover_list.Hide();
                    }
                }, 300)
            });
        }
    }
}

function HideList(plot_id) {
    if (IsTagInPlot(plot_id) || IsListInPlot(plot_id)) {
        setTimeout(function() {
            if (!$(".popover:hover").length) {
                let $image = $("#" + plot_id + "-image")
                $image.popover("hide");
            }
        }, 200)
    }
}


$(document).ready(function() {

    $(".recipe-plot").mouseover(function() {
        const id = $(this).attr("id");
        SetHoverInPlot(id);
        ShowList(id);
    }).mouseout(function() {
        $("#plot-hover-image").css("opacity", 0);
        const id = $(this).attr("id");
        HideList(id);
    })

    $(".recipe-image-plot").on("click", function(event) {
        if (IsEraseChecked()) {
            let id = $(this).attr("id");
            img_id = id + "-image";

            let $this = $(this);
            $(".plot-image").each(function(i, obj) {
                if (obj.id.includes(img_id)) {
                    let $image = $("#" + img_id);
                    $image.popover("hide");

                    $this.popover('dispose');
                    $this.off("mouseenter");
                    $this.off("mouseleave");
                    obj.remove();

                    $("#" + obj.id + "-data").remove();
                }
            })
        } else {
            let $selected = $("input[type=radio][name=data-radio-list]:checked")
            SetElementInPlot($(this), $selected);
        }
    })

    $(".recipe-list-plot").on("click", function(event) {
        let $selected = $("input[type=radio][name=data-radio-list]:checked");
        if ($selected.length > 0) {
            AddElementInPlotList($(this).attr("id"), $selected);
            let popover_list = $("#" + $(this).attr("id") + "-image").data("popover-list");
            popover_list.OnMouseLeave(function() {
                setTimeout(function() {
                    if (!IsPopoverHovered()) {
                        popover_list.Hide();
                    }
                }, 300)
            });
        }
    })
})