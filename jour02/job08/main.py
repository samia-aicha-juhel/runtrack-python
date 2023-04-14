def string(type, saison):
     if type == "fruits" and saison == "hiver":
        return "orange, mandarine et kiwi"
     elif type == "fruits" and saison == "été":
         return "poire, fraise et cassis"
     elif type == "legume" and saison == "hiver":
        return "carotte, topinambour et endive"
     elif type == "legume" and saison == "été":
        return "artichaut, aubergine et navet"
     

print(string("fruits", "hiver"))
print(string("fruits", "été"))
print(string("legume", "hiver"))
print(string("legume", "été"))