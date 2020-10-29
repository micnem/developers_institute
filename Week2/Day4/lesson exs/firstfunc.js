//defining a function
function workingWithArray (list, name) {
    for(i in list){
        console.log("my name is " + name + " and my favourite color is " + list[i])
    }
}
//calling a function
workingWithArray(["blue", "red", "yellow"], "David")