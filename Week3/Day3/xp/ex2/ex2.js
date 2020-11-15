//define functions

// ondrop="dragDrop(event)"
function dragDrop(event){
    event.preventDefault();
    let data = event.dataTransfer.getData("text")
    console.log("data: ", data);

    let box = document.getElementById(data);
    event.target.appendChild(box);
}
// ondragover="allowDrop(event)"
function allowDrop(event){
    event.preventDefault();
}

  
//   dragStart(event)  
function dragStart(event){
    console.log("target:",  event.target);
    console.log("id: ",  event.target.id );// id: square1
    event.dataTransfer.setData("text", event.target.id);
}
function dragEnd(event){
    //change colour
    let boxy = document.getElementById("square1");
    boxy.style.backgroundColor = "black";
    //change text to "dropped!"
   boxy.style.color = "red";
   boxy.innerHTML = "Dropped!";
}