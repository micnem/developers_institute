brand = {
    "name":"Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France":"Blue", "Spain":"Red", "US":["pink","green"]}
}

brand["number_stores"] = 2
brand["country_creation"] = "Spain"

if "international_competitors" in brand.keys():
    brand["international_competitors"].append("desigual")
brand.pop("creation_date")

print(brand)
print("\n")
print(brand["major_color"]["US"])
print(len(brand))
print(brand.keys())
print(f"The major colours in the U.S.A are: {brand['major_color']['US']}")
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)

print(brand)