function cap_name(sentence) {
 let array = sentence.split("")
 let newarray = []
 for (let item of array) {
     if (item == item.toUpperCase()) {
         newarray.push(item.toLowerCase())
     } else {
         newarray.push(item.toUpperCase())
     }
 }
 console.log(newarray.join(""))
}

cap_name("The Quick Brown Fox")