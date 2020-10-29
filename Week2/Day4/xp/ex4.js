var str = 'The Quick Brown Fox';
var arr = str.split("");

function swapper(array){
    for(i in arr){
    if(arr[i] = arr[i].toUpperCase()){
       arr[i] = arr[i].toLowerCase();
    }
    else{
        arr[i] = arr[i].toUpperCase();
    }
}
console.log(arr);
}
swapper(arr)
