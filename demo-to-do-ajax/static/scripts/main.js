$(document).ready(function() {
    // register click for every existing item
    $("button.done").click(function() {
        $.ajax({
            method: "POST",
            url: "/done",
            data: {
                id: $(this).attr("taskid")
            },
            success: function(data) {
                // move item from todo to done
            },
            error: function() {
                alert("There was an error with ajax");
            }
        });
    });

    $("button.delete").click(function() {
        var liNode = this.parentNode;
        $.ajax({
            method: "POST",
            url: "/delete",
            data: {
                id: $(this).attr("todoid")
            },
            success: function(response) {
                if (response['status'] == 'OK')
                    $(liNode).hide();
            }
        });
    });

    $("#addTask").click(function(eventObj) {
        if ($("#textBox").val() == "") {
            return;
        }

        $.ajax({
            method: "POST",
            url: "/new_task",
            data: {
                task: $("#textBox").val()
            },
            success: function(response) {
                $("#new-todos").append(response);
                $("#textBox").val("");
            }
        });
    });
});

function load() {
    $.ajax({
        method: "GET",
        url: "/tasks",
        success: function(response) {
            // var response = [
            //     {'id': 5, 'task': 'Fish n chips', 'done': 0}, 
            //     {'id': 10, 'task': 'asdasdasdasd', 'done': 0}
            // ]
            for (item in response) {
                $("#todos").append("<li>" + item['task'] + "</li>")
            }
        },
        error: function() {
            alert("error");
        }
    });
}