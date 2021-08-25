$(document).ready(function() {
    $("#save-button").on("click", function() {

        let result_count = "None"
        let name = $("#name-input").val()
        name = name.trim()
        if (name == null || name.length == 0) {
            Error("Your recipe deserve a name!")
            return
        } else {
            for (let i = 0; i < name.length; i++) {
                let char = name[i]
                if (!(IsLetter(char) && char == char.toLowerCase() || IsNumeric(char) || char == '_')) {
                    Error("The name can contains only lowercase letters, numbers and underline!")
                    return
                }
            }
        }

        let select = $("#recipe-type-select").find(":selected").val();

        //Crafting recipes
        if (select == "crafting_shapeless" || select == "crafting_shaped") {
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
            result_count = $("#result-count").text()
            result = $("#crafting-plot-result-image-data").text() + "!" + result_count;
        } else {
            console.log("Invalid recipe type!")
            return
        }

        recipe_id = $("#recipe-id").text()
        $.ajax({
            headers: { "X-CSRFToken": Cookies.get("csrftoken") },
            url: "",
            type: "POST",
            dataType: 'json',
            data: {
                'recipe_id': recipe_id,
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