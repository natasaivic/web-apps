$(document).ready(function() {
    /* $("div").on("click", "#delete", function() {
        var taskToDelete = $(this).parent()
        taskToDelete.remove()
    }); */

    $("#addTask2").click(function(eventObj) {
        if ($("#textBox2").val() != "") {
            var taskElement = $("<div></div>")
            taskElement.addClass("task")
            taskElement.text($(".textBox2").val())

            var deleteBtnElement = $("<button id=\"delete\"></button>");
            deleteBtnElement.addClass("fas fa-trash-alt delete");

            var doneBtnElement = $("<button id='done'> </button>")
            doneBtnElement.addClass("fas fa-check")

            // the new task element, along with its children button elements, is added to the DOM tree
            taskElement.append(deleteBtnElement, doneBtnElement)
            $(".notCompleted").append(taskElement)
            deleteBtnElement.click(function() {
                taskElement.remove()
            });

            /* var listItem = $("#textBox2").val();
            $(".ord_li").append("<li>" + listItem + "</li>"); */

            $("#textBox2").val(""); // clear out the text box
        } else {
            alert("Task box is empty. Enter task first. ")
        }
    });

    // var newListItem = $("<li> Fourth </li>")

    // What is the difference between next two blocks? 
    var childElements = $("ul").children();
    childElements.append("Fourth...");

    $("li").append("Sixt");

    // Appends at the end, it becomes a part of the list. Not an element created, unless you append with an element tag.  
    $("ul").append("<li>55</li>");
    $("#unord_li").append("<li>Fourth</li>");
    $("#unord_li").append("<li>Fifth</li>");

    $(".div2").append("<input id=\"textBox1\" placeholder=\"Enter task here\">");
    $(".div2").append("<button id=\"addButton1\">Add new list item</button>")
    $("#addButton").click(function(eventObj) {
        if ($("#textBox1").val() == "") {
            alert("Text Box is empty. Type in new list item.")
        } else {
            var item = $("#textBox1").val();
            $("ul").append("<li>" + item + "</li>");
        }
        $("#textBox").val("");
    });

    // Set hover for each item
    $(".hov1").hover(function() {
            $(".hov1").css("color", "red");
        },
        function() {
            $(".hov1").css("color", "black");
        });

    $(".hov2").hover(function() {
        $(".hov2").css("color", "blue")
    }, function() {
        $(".hov2").css("color", "black")
    })

    $(".hov3").hover(function() {
        $(".hov3").css("color", "green")
    }, function() {
        $(".hov3").css("color", "black")
    })

    // Hides all list elements
    $("#hide").click(function() {
        $("li").hide()
        console.log("Button clicked for hide.")
    });

    // Shows all list elements
    $("#show").click(function() {
        $("li").show()
        console.log("Button clicked for show.")
    });

    // Change Website
    $("#website").click(function() {
        $("#site").attr("href", "https://www.google.com")
        $("#site").text("Google")
    });
});