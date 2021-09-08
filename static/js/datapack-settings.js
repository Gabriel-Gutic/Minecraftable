$(document).ready(function() {
    console.log("Datapack Settings");

    $(".datapack-field").on('input', function() {

        console.log("'" + $(this).attr('id') + "'" + " element changed!");
        console.log("New value: " + $(this).val());

        $('#save-button').attr('disabled', false);
    });

    $("#save-button").on('click', function() {

        $.ajax({
            type: "GET",
            url: "",
            data: {
                "changed-settings": "",
                "name": $("#name-field").val(),
                "description": $("#description-field").val(),
                "version": $("#version-field").val(),
            },
            success: function() {
                $('#save-button').attr('disabled', true);
            }
        })

    })
})