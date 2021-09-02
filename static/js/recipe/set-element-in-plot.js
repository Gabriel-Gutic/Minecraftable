function SetPopoverFromTagId(image, tag_id, extra_classes = "", classForTrigger = "", show_popover = true) {
    tag_image = $("#tag-image-" + tag_id);
    let popover_list = tag_image.data("popover-list")

    new_popover_list = new PopoverList({
        parent: image,
        id: image.attr("id") + "-popover",
        popover_classes: extra_classes})
    new_popover_list.SetContent(popover_list.GetContent())

    if (classForTrigger != "") {
        new_popover_list.SetPredifinedTrigger(classForTrigger);

        new_popover_list.OnShow(function() {
            $("." + classForTrigger).on("mouseleave", function() {
                new_popover_list.Hide();
            });
        })
    }

    if (show_popover == true)
        new_popover_list.Show();
}

function SetPopoverFromTagRadio(image, tag_radio, show_popover = true, extra_classes = "", classForTrigger = "") {

    let parts = tag_radio.attr("id").split("-")
    SetPopoverFromTagId(image, parts[2], show_popover, extra_classes, classForTrigger);
}

function SetElementInPlot(plot, element, show_popover = true) {
    let value = element.val()

    if (value == null) {
        console.log("No item selected!");
        return;
    }

    let type = null
    if (element.attr("id").includes("item"))
        type = "item"
    else if (element.attr("id").includes("tag")) {
        if (plot.attr("id").includes("result")) {
            Error("The result can not be a tag!")
            return
        }
        type = "tag";
    }
    parts = value.split("~");
    let element_id = parts[0];
    let element_image = parts[1];
    let id = plot.attr("id");
    img_id = id + "-image";

    let exists = ($("#" + img_id).length) > 0;
    if (exists) {
        var image = $("#" + img_id);
        let popover_list = image.data("popover-list");
        if (popover_list) 
        {
            popover_list.Hide();
            delete popover_list
        }
        image.remove();
        $("#" + img_id + "-data").remove();
    } 
    $("#image-div").append(`<img id="` + img_id + `" src="` + element_image + `" class="plot-image">`)
    $("#image-div").append(`<p id="` + img_id + `-data" class="undisplayed-data">` + type + `~` + element_id + `</p>`)
    var image = $("#" + img_id);
    if (type == "tag") {
        SetPopoverFromTagRadio(image, element, "plot-tag-popover", "plot-tag-popover", show_popover)
    }
    
    SetImageRectForPlot(image, plot);
}


function AddElementInPlotList(plot_id, element, show_popover = true) {
    let image = $("#" + plot_id + "-image")
    let popover_list = image.data("popover-list")

    let element_attr_id = element.attr("id")
    type = null
    if (element_attr_id.includes("item")) {
        type = "item"
    } else if (element_attr_id.includes("tag")) {
        type = "tag"
    } else {
        console.error("Invalid element: " + element_attr_id)
    }

    let value = element.val().split("~")
    let element_id = value[0]
    let element_image = value[1]

    searched_value = type + "-" + element_id

    if (popover_list.GetContent().includes(searched_value)) {
        return
    }

    let label_id = element.attr("id").replace("radio", "label")
    let element_name = $("#" + label_id).text()

    let extra_classes = ""
    if (type == "tag") {
        extra_classes = "popover-list-element-tag"
    }

    popover_list.AddElement({
        type: type, 
        id: element_id, 
        name: element_name, 
        image: element_image, 
        extra_classes: extra_classes,});
    if (show_popover)
        popover_list.Show();
}

function SetPopoverListSettings(popover_list)
{
    popover_list.SetSpecialComponent(function(type, id){
        return `<i id="` + this.GetId() + `-` + type + `-` + id + `-delete` + `" class="`+ this.GetId() + `-delete fas fa-trash-alt"></i>`
    })
    popover_list.OnShow(function() {
        popover_list.OnMouseLeaveParent(function() {
            popover_list.Hide();
        });

        $(".popover-list-element-tag").each(function(i, obj) {
            let image = $("#" + obj.id + "-image")
            let parts = obj.id.split("-")
            let tag_id = parts[parts.length - 1]
            SetPopoverFromTagId(image, tag_id, "popover-list-element-tag-popover", "popover-list-element-tag-popover", false)

            let popover_tag = image.data("popover-list")
            popover_tag.OnShow(function() {
                popover_tag.OnMouseLeave(function() {
                    popover_tag.Hide();
                    if (!popover_list.IsHovered()) {
                        popover_list.Hide();
                    }
                })
            })
        })

        $("." + popover_list.GetId() + "-delete").on("click", function(e) {
            let attr_id = $(this).attr("id");
            let parts = attr_id.split("-")
            let nr = parts.length

            let type =  parts[nr - 3]
            let id = parts[nr - 2]
                popover_list.RemoveElement(type, id);
            if (popover_list.Size() == 0) 
                popover_list.Hide()
            else popover_list.Show();
        })
    })
}
$(document).ready(function() {
    let furnace_popover_list = new PopoverList({
        parent: $("#furnace-plot-ingredient-image"),
        id: "furnace-plot-ingredient-popover",
        popover_classes: "plot-list-popover"});
    
    SetPopoverListSettings(furnace_popover_list);

    let stonecutter_popover_list = new PopoverList({
        parent: $("#stonecutter-plot-ingredient-image"),
        id: "stonecutter-plot-ingredient-popover",
        popover_classes: "plot-list-popover"
    });

    SetPopoverListSettings(stonecutter_popover_list);

    let campfire_popover_list = new PopoverList({
        parent: $("#campfire-plot-ingredient-image"),
        id: "campfire-plot-ingredient-popover",
        popover_classes: "plot-list-popover"
    });

    SetPopoverListSettings(campfire_popover_list);
})
