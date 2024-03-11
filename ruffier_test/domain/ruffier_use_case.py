
def ruffier_index(p1, p2, p3):
    result = (4 * (p1 + p2 + p3) - 200) / 10
    return result

def bad_level(age):
    result = 21 - ((min(age, 15) - 7) / 2) * 1.5
    return result

def get_level(index, age):
    level = bad_level(age)

    if index > level:
        return "незадовільний"
    
    level -= 4

    if index > level:
        return "слабкий"
    
    level -= 5

    if index > level:
        return "задовільний"
    
    level -= 5.5

    if index > level:
        return "добрий"
    
    return "відмінний"
