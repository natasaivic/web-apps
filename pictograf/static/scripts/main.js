$(document).ready(function() {
    $("a.test").click(function() {
        $.ajax({
            method: "POST",
            url: "/addlikeTEST",
            data: {
                id: $(this).attr('href')
            },
            success: function(response) {
                if (response['status'] == 'OK') {
                    console.log("Error in uploading DOM.")
                    $("a.test").hide

                } else { console.log("ERRRRRRROR") }
            },
            error: function() {
                alert("There was an error with ajax");
            }
        });
    });
    $("a.addlike_class").click(function() {
        var post_id = $(this).attr('likeid');
        $.ajax({
            method: "POST",
            url: "/unlike/" + post_id,
            data: {
                id: post_id
            },
            success: function(response) {
                if (response['status'] == 'OK') {
                    $("a.addlike_class").hide
                }
            },
            error: function() {
                alert("There was an error with ajax");
            }
        });
    });
    $("a.removelike_class").click(function() {
        $.ajax({
            method: "POST",
            url: "/addlike/" + post_id,
            data: {
                id: $(this).attr("likeid")
            },
            success: function(response) {
                if (response['status'] == 'OK') {
                    $("a.removelike_class").hide
                }
            },
            error: function() {
                alert("There was an error with ajax");
            }
        });
    });

});