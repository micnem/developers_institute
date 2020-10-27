let building = {
    number_levels : 4,
    number_of_apt_by_level : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants : ["Sarah", "Dan", "David"],
    number_of_rooms_and_rent:  {
        "Sarah": [3, 990],
        "Dan":  [4, 1000],
        "David": [1, 500],
    },
}

console.log(building.number_levels)
console.log(building.number_of_apt_by_level[1])
console.log(building.number_of_apt_by_level[3])
console.log(building.number_of_rooms_and_rent.Dan[0])

if(building.number_of_rooms_and_rent.Sarah[1]+building.number_of_rooms_and_rent.David[1]>building.number_of_rooms_and_rent.Dan[1]){
    console.log("Increase Dan's rental amount")
    building.number_of_rooms_and_rent.Dan[1] = 2000
    console.log(building.number_of_rooms_and_rent)
}
else{
    console.log("smaller")
}