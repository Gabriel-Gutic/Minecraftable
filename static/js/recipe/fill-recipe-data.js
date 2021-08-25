function SetCraftingResult(result_id, count = "") {
    var list = $(".item-element")
    item_id = BinarySearchUnorderedList(list, result_id, 0, list.length)

    element = $("#radio-item-" + item_id)
    plot_id = "crafting-plot-result"
    SetHoverInPlot(plot_id)
    SetElementInPlot($("#" + plot_id), element)
    $("#result-count").text(count).change()
    $("#crafting-recipe-image").trigger("resize").change();
}

function SetElementInCraftingPlot(data, i, j) {
    parts = data.split("~")
    let type = parts[0];
    let id = parts[1];

    let element = null
    if (type == "item") {
        var list = $(".item-element")
        let item_id = BinarySearchUnorderedList(list, id, 0, list.length)

        element = $("#radio-item-" + item_id)

    } else if (type == "tag") {
        var list = $(".tag-element")
        let tag_id = BinarySearchUnorderedList(list, id, 0, list.length)

        element = $("#radio-tag-" + tag_id)
    }

    if (element != null) {
        let plot_id = "crafting-plot-" + i + "-" + j
        SetHoverInPlot(plot_id)
        SetElementInPlot($("#" + plot_id), element, false)
    }

}

function FillRecipeData() {


    recipe_id = $("#recipe-id").text()

    if (recipe_id != "None") {
        $.ajax({
            url: "",
            type: "GET",
            data: {
                'fill-recipe-data': '',
            },
            success: function(data) {
                let name = data.name;
                $("#name-input").val(name)
                $("#recipe-type-select").val(data.type).change()


                if (data.type == "crafting_shapeless") {
                    let ingredients = data.ingredients

                    for (let i = 0; i < ingredients.length; i++) {
                        let nr = Math.trunc(i / 3)
                        SetElementInCraftingPlot(ingredients[i], nr, (i - nr * 3))
                    }
                    SetCraftingResult(data.result, data.count)
                } else if (data.type == "crafting_shaped") {
                    crafting = data.crafting

                    for (var i = 0; i < crafting.length; i++)
                        for (var j = 0; j < crafting[i].length; j++) {
                            SetElementInCraftingPlot(crafting[i][j], i, j)
                        }

                    SetCraftingResult(data.result, data.count)
                }
            }
        })

    } else {
        $("#recipe-type-select").val("crafting_shapeless").change()
    }
}