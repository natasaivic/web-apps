$(document).ready(function() {
    // var newListItem = $("<li> Fourth </li>")

    // What is the difference between next two blocks? 
    var childElements = $("ul").children();
    childElements.append("Fourth...");

    $("li").append("Sixt");

    // Appends at the end, it does not become a part of the list. Not an element created.  
    $("ul").append("55");
    $("#unord_li").append("Fourth");
    $("#unord_li").append("Fifth");

    // Set hovet for each item
    $("li").hover(function() {
            $("li").css("color", "red");
        },
        function() {
            $("li").css("color", "black");
        });


    // Hides all list elements
    $("#hide").click(function() {
        $("li").hide()
    });

    // Shows all list elements
    $("#show").click(function() {
        $("li").show()
    });

    // Change Website
    $("#website").click(function() {
        $("#site").attr("href", "https://www.google.com")
        $("#site").text("Google")
    });
});