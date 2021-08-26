function SetResultInPlot(plot_id, result_id, count = "") {
    var list = $(".item-element")
    item_id = BinarySearchUnorderedList(list, result_id, 0, list.length)

    element = $("#radio-item-" + item_id)
    SetHoverInPlot(plot_id)
    $("#plot-hover-image").css("opacity", 0);
    SetElementInPlot($("#" + plot_id), element)
    $("#result-count").text(count).change()
}

function SetElementInPlotByData(plot_id, data) //Data format: type~id
{
    let parts = data.split("~")
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
        SetHoverInPlot(plot_id)
        $("#plot-hover-image").css("opacity", 0);
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
                    SetResultInPlot("crafting-plot-result", data.result, data.count)
                } else if (data.type == "crafting_shaped") {
                    crafting = data.crafting

                    for (var i = 0; i < crafting.length; i++)
                        for (var j = 0; j < crafting[i].length; j++) {
                            SetElementInPlotByData("crafting-plot-" + i + "-" + j, crafting[i][j])
                        }

                    SetResultInPlot("crafting-plot-result", data.result, data.count)
                } else if (data.type == "smithing") {
                    SetElementInPlotByData("smithing-plot-base", data.base)
                    SetElementInPlotByData("smithing-plot-addition", data.addition)
                    SetResultInPlot("smithing-plot-result", data.result)
                }
            }
        })

    } else {
        $("#recipe-type-select").val("crafting_shapeless").change()
    }
}