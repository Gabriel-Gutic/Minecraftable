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

                switch (data.type) {
                    case "crafting_shapeless":
                        {
                            let ingredients = data.ingredients
                            let k = 0;

                            for (let i = 0; i < ingredients.length; i++) {
                                parts = ingredients[i].split("~")

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
                                    let nr = Math.trunc(k / 3)
                                    let plot_id = "crafting-plot-" + (k - nr * 3) + "-" + nr
                                    SetHoverInPlot(plot_id)
                                    SetElementInPlot($("#" + plot_id), element, false)
                                    k++;
                                }
                            }
                            result_id = data.result
                            console.log(result_id)
                            var list = $(".item-element")
                            item_id = BinarySearchUnorderedList(list, result_id, 0, list.length)

                            element = $("#radio-item-" + item_id)
                            plot_id = "crafting-plot-result"
                            SetHoverInPlot(plot_id)
                            SetElementInPlot($("#" + plot_id), element)
                            $("#crafting-recipe-image").trigger("resize");
                        }
                        break;
                }
            }
        })

    } else {
        $("#recipe-type-select").val("crafting_shapeless")
    }
}