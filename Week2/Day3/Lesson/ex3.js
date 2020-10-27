var names= ["john", "sarah", 23, "Rudolf",34]

for(let i=0; i < names.length; i++){
    
    if(isNaN(names[i])==true){
        if(names[i].charAt(0).toUpperCase()==true){
        console.log(names[i]);}
        else{names[i]= names[i].charAt(0).toUpperCase() + names[i].slice(1)};
        // console.log(names)
    }
    else {
        console.log("not string");
    }
    console.log(names[i])
}



