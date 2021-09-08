function SetElementInPlotByData(plot_id, data) //Data format: type~id
{
    let parts = data.split("~")
    let type = parts[0];
    let id = parts[1];

    let element = BinarySearchElement(type, id)

    if (element != null) {
        SetElementInPlot($("#" + plot_id), element, false)
    }
}

function SetResultInPlot(plot_id, result_id, count = "") {
    SetElementInPlotByData(plot_id, "item~" + result_id)
    $("#result-count").text(count == "" ? "1" : count).change()
}

function SetTimerFromData(data) 
{
    let timer = data;

    const minutes = parseInt(timer / 60, 10);
    const seconds = timer % 60;

    SetTimer(minutes, seconds);
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
            success: function(data) 
            {
                let name = data.name;
                $("#name-input").val(name)
                $("#type-select").SetType(data.type);

                setTimeout(function() {
                    if (data.type == "crafting_shapeless") 
                    {
                        let ingredients = data.ingredients

                        for (let i = 0; i < ingredients.length; i++) {
                            let nr = Math.trunc(i / 3)
                            SetElementInPlotByData("crafting-plot-" + nr + "-" + (i - nr * 3), ingredients[i])
                        }
                        SetResultInPlot("crafting-plot-result", data.result, data.count)
                    } 
                    else if (data.type == "crafting_shaped") 
                    {
                        crafting = data.crafting

                        for (var i = 0; i < crafting.length; i++)
                            for (var j = 0; j < crafting[i].length; j++) {
                                if (crafting[i][j] != "")
                                    SetElementInPlotByData("crafting-plot-" + i + "-" + j, crafting[i][j])
                            }

                        SetResultInPlot("crafting-plot-result", data.result, data.count)
                    } 
                    else if (data.type == "smithing") 
                    {
                        SetElementInPlotByData("smithing-plot-base", data.base)
                        SetElementInPlotByData("smithing-plot-addition", data.addition)
                        SetResultInPlot("smithing-plot-result", data.result)
                    } 
                    else if (["smelting", "smoking", "blasting"].includes(data.type))
                    {
                        SetTimerFromData(data.cooking_time)
                        SetXP(data.xp);

                        let ingredients = data.ingredients;
                        for (var i = 0; i < ingredients.length; i++)
                        {
                            let element = BinarySearchElement(ingredients[i][0], ingredients[i][1]);
                            AddElementInPlotList("furnace-plot-ingredient", element, false);
                        }

                        SetResultInPlot("furnace-plot-result", data.result)
                    }
                    else if (data.type == "stonecutting")
                    {
                        let ingredients = data.ingredients;
                        for (var i = 0; i < ingredients.length; i++)
                        {
                            let element = BinarySearchElement(ingredients[i][0], ingredients[i][1]);
                            AddElementInPlotList("stonecutter-plot-ingredient", element, false);
                        }

                        SetResultInPlot("stonecutter-plot-result", data.result, data.count);
                    }
                    else if (data.type == "campfire_cooking")
                    {
                        SetTimerFromData(data.cooking_time)

                        let ingredients = data.ingredients;
                        for (var i = 0; i < ingredients.length; i++)
                        {
                            let element = BinarySearchElement(ingredients[i][0], ingredients[i][1]);
                            AddElementInPlotList("campfire-plot-ingredient", element, false);
                        }

                        SetResultInPlot("campfire-plot-result", data.result);
                    }
                }, 10)
            }
        })

    }
}