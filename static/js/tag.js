function isValidName(name) 
{
    return !name.match(/[^a-z0-9_]/);
}

$(document).ready(function()
{
    $("#search-input").on("input", function()
    {
        let text = $(this).val().toLowerCase();

        let list = $(".item-label")
        for (let i = 0; i < list.length; i++)
        {
            let $element = $("#" + list[i].id);
            item_name = $element.text().toLowerCase();
            if (!item_name.includes(text))
                $element.parent().parent().addClass("undisplayed-data");
            else
                $element.parent().parent().removeClass("undisplayed-data");
        }
    })

    inputPicture = $("#image-div").inputPicture("input-image");
    inputPicture.SetSquare();
    inputPicture.SetText("Select Image");



    inputPicture.SetDefaultImage("/media/select-image.jpg");
    inputPicture.RemoveImage();

    $tag_data = $("#tag-data");
    if ($tag_data.length > 0)
    {
        url = $tag_data.text().split("?")[1];
        inputPicture.SetImage(url);
    }

    inputPicture.OnChange(function(temp_path){
        inputPicture.SetImage(temp_path);
    })

    $("#save-button").on("click", function()
    {
        let name = $("#name-input").val();
        if (!isValidName(name) || name == "")
        {
            alert("Please enter a valid name! Only lowercase letters, numbers and underscores are allowed!")
            return;
        }    
        
        let list = $(".check-item:checked");
        if (list.length == 0)
        {
            alert("You need to select at least one item!")
            return;
        }  

        let items = []
        for (let i = 0; i < list.length; i++)
        {
            items.push(list[i].id.split("-")[2]);
            console.log(items);
        }
        
        data = {
            "create": "",
            "name": name,
            "items": items,
        }

        $tag_data = $("#tag-data");
        if ($tag_data.length > 0)
        {
            delete data.create;
            data['update'] = "";
            data['tag-id'] = parseInt($tag_data.text().split("?")[0], 10);

        }    
        
        if (inputPicture.HaveImage())
        {
            inputPicture.Upload({
                headers: { "X-CSRFToken": Cookies.get("csrftoken") },
                url: "/Minecraftable/tag/update/",
                data: data,
                success: function(data)
                {
                    if (!!data.error)
                    {
                        Error(data.error);
                        return;
                    }
                    window.location.replace("/Minecraftable/home/");
                }
            })
        }
        else if ($tag_data.length > 0)
        {
            $.ajax({
                headers: { "X-CSRFToken": Cookies.get("csrftoken") },
                url: "/Minecraftable/tag/update/",
                type: "POST",
                data: data,
                success: function(data){
                    if (!!data.error)
                    {
                        Error(data.error);
                        return;
                    }
                    window.location.replace("/Minecraftable/home/");
                }
            })
        }
        else
        {
            alert("Please select an image!")
        }
    })
})