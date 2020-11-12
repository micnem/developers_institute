now = 2020
def get_age(birth_year):
    age = now - birth_year
    return age


def can_retire(gender, birth_year):
    if gender == "M":
        if get_age(birth_year) >= 67:
            return True
        else:
            return False
    else:
        if get_age(birth_year) >= 62:
            return True
        else:
            return False
    

if not can_retire("M", 1997):
    print("too early")
else:
    print("you can retire")