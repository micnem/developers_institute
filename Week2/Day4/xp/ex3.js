var name = "Ryan Singh"
var split_name = name.split(" ");
var first_name = split_name[0];
var last_name = split_name[1];



function abbrev(name){
    var abbrevname = last_name.substring(0,last_name.length - (last_name.length-1));
    console.log(first_name + " " + abbrevname + ".")
}
abbrev("Ryan Singh")