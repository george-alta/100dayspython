NZ_cities = ["Auckland", "Dunedin", "Chistchurch"]
Letters = ["A","B","C","D","E","F"]

print (Letters[0])
print (NZ_cities[2])

NZ_cities[2] = "Otautahi"

print(NZ_cities)

# append adds elements at the end

NZ_cities.append("Nelson")
print(NZ_cities)
#extend to add several elements (but if there are several it has to be a list)
NZ_cities.extend(["Wanaka","Wellington","Hamilton","Rotorua"])

print(NZ_cities)

#pop returns the [n] element and removes it from the list