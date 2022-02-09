#Lists Project

colors = ["Blue", "Red", "Yellow", "Purple", "Pink", "Green", "Orange", "Gold"]
luckyNumbers = [19, 21, 11, 99, 96, 2]

#print(colors)
#print(colors[1:4])

print(len(luckyNumbers))
colors.extend(luckyNumbers)
colors.append("Cereal")
colors.insert(2,"LOVE")
colors.remove("Gold")
print(colors.index(2))
print(colors.count("Green"))
luckyNumbers.sort()
print(colors)
print(luckyNumbers)

number = -9

if number > 0:
    print(f"{number} is greater than 0")
else:
    print(f"{number} is less than 0")