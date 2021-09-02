function SetTimer(minutes, seconds) {
    if (minutes <= 9)
        minutes = "0" + minutes;
    if (seconds <= 9)
        seconds = "0" + seconds;
    time = minutes + ":" + seconds;
    new_time = ""
    for (let i = 0; i < time.length; i++)
    {  
        if (time[i] == '1')
            new_time += " ";
        new_time += time[i];
    }    
        
    $("#timer-data").text(new_time);
}

$(document).ready(function(){

    $(".timer-increment").on("click", function(){
        let parts = $("#timer-data").text().split(":");
        minutes = parseInt(parts[0].replaceAll(" ", ""))
        seconds = parseInt(parts[1].replaceAll(" ", ""))

        if (minutes >= 99 && seconds >= 59)
            return;

        seconds++;
        if (seconds == 60)
        {
            seconds = 0;
            minutes++;
        }
        
        SetTimer(minutes, seconds);
    })

    $(".timer-decrement").on("click", function(){
        let parts = $("#timer-data").text().split(":");
        minutes = parseInt(parts[0].replaceAll(" ", ""))
        seconds = parseInt(parts[1].replaceAll(" ", ""))

        if (minutes <= 0 && seconds <= 1)
            return;

        if (seconds == 0)
        {   
            minutes--;
            seconds = 59;
        }
        else seconds--;

        SetTimer(minutes, seconds);
    })

    $("#timer-data").on("change", function(){
        type = $("#recipe-type-select").val();
        if (['smelting','smoking','blasting', 'campfire_cooking'].includes(type))
        {
            let left, top;
            if (type == "campfire_cooking")
            {
                left = "69.5%";
                top = "15.9%";
            }
            else
            {
                left = "71.2%";
                top = "15.4%";
            }

            $(this).css("left", left);
            $(this).css("top", top);

            $(this).removeClass("undisplayed-data");
        }    
        else 
            $(this).addClass("undisplayed-data");
    })
})