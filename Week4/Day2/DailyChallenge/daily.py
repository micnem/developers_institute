bday = input("Type in Bday DD/MM/YYYY: ")
age =  2020 - int((bday.split("/")[2]))
print(age)
digit = age%10
candles = "i"*digit

print(f"     ___{candles}___\n   |:H:a:p:p:y:|\n __|___________|__\n|^^^^^^^^^^^^^^^^^|\n|:B:I:R:T:H:D:A:Y:|\n|                 |\n ~~~~~~~~~~~~~~~~~~")