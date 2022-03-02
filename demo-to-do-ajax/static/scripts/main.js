$(document).ready(function() {
    // register click for every existing item
    $("button.done").click(function() {
        var liNode = this.parentNode;
        $.ajax({
            method: "POST",
            url: "/done",
            data: {
                id: $(this).attr("todoid")
            },
            success: function(response) {
                // move item from todo to done
                if (response['status'] == 'OK') {
                    $(liNode).hide();
                    $("#complete-todos").append(liNode);
                } else { console.log("ERROW WITH APPENDING ITEM TO DONE LIST") }
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
                var li = $('<li class="list_item"></li>')
                li.html($("#textBox").val())

                var doneBtn = $('<button class="done fas fa-check" todoid="' + response + '"></button>');
                li.append(doneBtn);
                doneBtn.click(function() {
                    $.ajax({
                        method: "POST",
                        url: "/done",
                        data: {
                            id: $(this).attr("todoid")
                        },
                        success: function(response) {
                            // move item from todo to done
                            if (response['status'] == 'OK') {
                                $("#new-todos").remove(li);
                                $("#complete-todos").append(li);
                            } else {
                                console.log("ERROW WITH APPENDING ITEM TO DONE LIST");
                            }
                        },
                        error: function() {
                            alert("There was an error with ajax");
                        }
                    });
                });

                var deleteBtn = $('<button class="delete fas fa-trash-alt" todoid="' + response + '"></button>');
                deleteBtn.click(function() {
                    $.ajax({
                        method: "POST",
                        url: "/delete",
                        data: {
                            id: $(this).attr("todoid")
                        },
                        success: function(response) {
                            if (response['status'] == 'OK')
                                $(li).hide();
                        }
                    });
                });
                li.append(deleteBtn);

                $("#new-todos").append(li);
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