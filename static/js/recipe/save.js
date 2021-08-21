$(document).ready(function() {
    $("#save-button").on("click", function() {

        let name = $("#name-input").val()
        if (name == null || name.length == 0) {
            Error("Your recipe deserve a name!")
            return
        }

        let select = $("#recipe-type-select").find(":selected").val();

        switch (select) {
            case "crafting_shapeless":
                {
                    let valid = false

                    for (let i = 0; i < 3 && !valid; i++)
                        for (let j = 0; j < 3 && !valid; j++)
                            valid = ($("#crafting-plot-" + i + "-" + j + "-image").length) > 0

                    if (valid) {
                        valid = ($("#crafting-plot-result-image").length) > 0
                    }

                    if (!valid) {
                        Error("Not a valid recipe!")
                        return
                    }

                    recipe = [
                        null, null, null,
                        null, null, null,
                        null, null, null,
                    ]
                    for (let i = 0; i < 3; i++)
                        for (let j = 0; j < 3; j++) {
                            recipe[3 * i + j] = $("#crafting-plot-" + i + "-" + j + "-image-data").text();
                        }
                    result = $("#crafting-plot-result-image-data").text();
                }
                break;
        }

        $.ajax({
            headers: { "X-CSRFToken": Cookies.get("csrftoken") },
            url: "",
            type: "POST",
            dataType: 'json',
            data: {
                'new-recipe': '',
                'name': name,
                'type': select,
                'recipe': recipe,
                'result': result,
            },
            success: function(data) {
                window.location.href = '/Minecraftable/datapack/' + data.datapack_id + '/'
            }
        })
    })

})