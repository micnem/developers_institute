
// Assigning attributes to all boxes

let boxes = document.getElementsByClassName("box")
for(let box of boxes){
    box.setAttribute("draggable", "true");
    box.setAttribute("ondragstart", "dragStart(event)");
    box.setAttribute("ondragend", "dragEnd(event)");
}

// Defining functions

// dragStart

function dragStart(event){
    event.target.style.backgroundColor = "green";
    console.log ("drag " +  "X: " + event.clientX  + " Y: " +  event.clientY);
}
//dragEnd

function dragEnd(event){
    let x = event.clientX;
    let y = event.clientY;
    console.log(event)
    event.target.style.left = x + "px";
    event.target.style.top = y + "px";
    event.target.style.position = "absolute"; //Necessary
    console.log ("dragend" + "X: " + event.clientX  + " Y: " +  event.clientY );
}
