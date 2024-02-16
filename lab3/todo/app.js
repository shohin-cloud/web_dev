document.getElementById('add-todo').addEventListener('click', function() {
    const input = document.getElementById('todo-input');
    const text = input.value.trim();

    if(text !== "") {
        addTodoItem(text);
        input.value = ''; 
    }
});

function addTodoItem(text) {
    const ul = document.getElementById('todo-list');
    const li = document.createElement('li');
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.addEventListener('change', function() {
        if(this.checked) {
            li.classList.add('completed');
        } else {
            li.classList.remove('completed');
        }
    });

    const span = document.createElement('span');
    span.textContent = text;

    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Delete';
    deleteBtn.addEventListener('click', function() {
        ul.removeChild(li);
    });

    li.appendChild(checkbox);
    li.appendChild(span);
    li.appendChild(deleteBtn);
    ul.appendChild(li);
}
