let body = document.getElementsByTagName("body");
let para = document.createElement("P");
para.innerText = "Hello this is a paragraph that can be moved around. Hopefully, the size of the font will change accordingly."
para.setAttribute("draggable","true")
para.setAttribute("ondragstart", "dragStart(event)");
para.setAttribute("ondragend", "dragEnd(event)");
document.body.appendChild(para);

//defining functions

// dragStart

function dragStart(event){
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
    event.target.style.fontSize = (x/100) + "px";
    console.log ("dragend" + "X: " + event.clientX  + " Y: " +  event.clientY );
}

