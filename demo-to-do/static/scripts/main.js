$(document).ready(function() {
    /* $("div").on("click", "#delete", function() { //This event handler function is only triggered when a descendant of a div element with id of delete is clicked.
        var taskToDelete = $(this).parent() //We extract the parent of the delete button, which is the task to be deleted. 
        taskToDelete.remove() //We delete that extracted parent element using the remove() method.
    }); */

    $.ajax({
        type: "GET",
        url: '/',
        success: function(data) {
            console.log('success', data)
        }
    });

    $("#addTask2").click(function(eventObj) {
        if ($("#textBox2").val() == "") {
            alert("Task box is empty. Enter task first. ")
            return;
        }

        $.ajax({
            method: "POST",
            url: "/new_task",
            data: {
                task: $("#textBox2").val()
            },
            success: function(data) {
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
                    taskElement.fadeOut(200, function() {
                        taskElement.remove();
                    });
                });
                doneBtnElement.click(function() {
                    taskElement.fadeOut(200, function() {
                        $(".notCompleted").remove(taskElement);
                        $(".completed").append(taskElement);
                        taskElement.fadeIn(200);
                    });
                });

                /* var listItem = $("#textBox2").val();
                $(".ord_li").append("<li>" + listItem + "</li>"); */

                $("#textBox2").val(""); // clear out the text box
            },
            error: function(data) {
                alert("There was an error with ajax");
            }
        });
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
        $("li").hide("slow")
        console.log("Button clicked for hide.")
    });

    // Shows all list elements
    $("#show").click(function() {
        $("li").show("slow")
        console.log("Button clicked for show.")
    });

    // Change Website
    $("#website").click(function() {
        $("#site").attr("href", "https://www.google.com")
        $("#site").text("Google")
    });
});