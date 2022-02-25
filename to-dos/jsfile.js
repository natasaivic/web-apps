var createTodo = function(todo) {
    let li = document.createElement('li');

    let label = document.createElement('label');
    label.innerHTML = todo;
    let checkbox = document.createElement('input');
    checkbox.type = "checkbox";

    let deleteButton = document.createElement('button');
    deleteButton.innerHTML = "Delete";
    deleteButton.className = "delete";

    //nest todo elements in list item
    li.appendChild(checkbox);
    li.appendChild(label);
    li.appendChild(deleteButton);
    return li;
}

var addButton = document.getElementById('add');

addButton.onclick = function() {
    // store the button's parent element (.addTodo <div>) in a variable
    var parent = this.parentNode;
    // store the input, which is the *first* child element of the .addTodo <div>
    var addTextInput = parent.children[0];
    if (addTextInput.value === "") {
        return;
    } else {
        //add todo
        createTodo(addTextInput.value);
        //reset input 
        addTextInput.value = "";
    }

}