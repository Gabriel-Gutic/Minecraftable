$(document).ready(function(){
    setTimeout(function(){
    $("#erase-plot-button").on("click", function() {
        let class_name = "btn-primary";

        if ($(this).hasClass(class_name)) {
            $(this).removeClass(class_name);
        } else {
            $(this).addClass(class_name);
            $("input[type=radio][name=data-radio-list]:checked").prop("checked", false);
        }
        
    })

    $("input[type=radio][name=data-radio-list]").on("change", function() {
        let class_name = "btn-primary";

        let $erase = $("#erase-plot-button");

        if ($erase.hasClass(class_name)) 
        {
            $erase.removeClass(class_name);
        }
    })
    }, 1000);
})