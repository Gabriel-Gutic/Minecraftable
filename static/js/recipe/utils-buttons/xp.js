function GetXP()
{
    return parseInt($("#xp-data").text());
}

function SetXP(value)
{
    $xp_data = $("#xp-data")
    $xp_data.text(value);
    $xp_data.trigger("change");
}

$(document).ready(function()
{
    $("#furnace-xp-increment").on("click", function()
    {
        xp = GetXP();
        if (xp >= 999)
            return;
        xp++;
        SetXP(xp);
    })

    $("#furnace-xp-decrement").on("click", function()
    {
        xp = GetXP();
        if (xp <= 0)
            return;
        xp--;
        SetXP(xp);
    })
    $("#xp-data").on("change", function()
    {
        let type = $("#type-select-data").val();
        if (['smelting','smoking','blasting'].includes(type))
        {    
            xp = GetXP();
            if (xp < 10)
                $(this).css("left", "72%")
            else if (xp < 100)
            {
                $(this).css("left", "68%");
            } 
            else
            {
                $(this).css("left", "64%");
            }

            $(this).removeClass("undisplayed-data");
        }
        else 
            $(this).addClass("undisplayed-data");
    })
})