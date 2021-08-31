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
        let recipe = null
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
        } else if (select == "smithing") {
            let valid = true;
            $(".smithing-plot").each(function(i, obj) {
                has_image = $("#" + obj.id + "-image").length > 0;
                if (!has_image)
                    valid = false;
            })

            if (!valid) {
                Error("Not a valid recipe!")
                return
            }

            recipe = [
                $("#smithing-plot-base-image-data").text(),
                $("#smithing-plot-addition-image-data").text(),
            ]

            result = $("#smithing-plot-result-image-data").text()
        } 
        else if (select == "smelting" || select == "blasting" || select == "smoking")
        {
            popover_list = $("#furnace-plot-ingredient-image").data("popover-list");
            recipe = []

            popover_list.ForEach(function(i, obj)
            {
                let parts = obj.id.split("-")

                let type = parts[parts.length - 2]
                let id = parts[parts.length - 1]

                recipe.push(type + "~" + id);
            })
            let data = $("#furnace-plot-result-image-data");
            let valid = data.length > 0 && recipe.length > 0;

            if (!valid)
            {
                Error("Not a valid recipe!");
                return;
            }

            let timer = $("#timer-data").text().replaceAll(" ", "").split(":");
            let minutes = parseInt(timer[0], 10);
            let seconds = parseInt(timer[1], 10);

            timer = 60 * minutes + seconds; // Turn timer in seconds only

            let xp = $("#xp-data").text();
            result = data.text() + "!" + timer + "!" + xp;
        }
        else {
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