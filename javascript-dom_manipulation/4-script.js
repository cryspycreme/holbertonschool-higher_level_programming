add_item = document.getElementById("add_item");
// get a reference to the class 'my_list'
const ul = document.querySelector(".my_list");

// Append the new paragraph to the 'app' div
add_item.addEventListener('click', function() {
    // create a new element
    let list_item = document.createElement("li");
    // set the text content of the element
    list_item.textContent = 'Item';
    ul.appendChild(list_item);
})
