magicians = ["WandMan", "MagicMan", "TrickMan", "El Wando", "Her Royal Wandwoman"]

# def show_magicians():
#     print(magicians)

# show_magicians()
# great_magicians = []
# def make_great():
#     for magician in magicians:
#         great_magicians.append(magician +"The great")
#     return magicians
# print(make_great())

new_magicians = ["The Great " + e  for e in magicians]

print(new_magicians)

   