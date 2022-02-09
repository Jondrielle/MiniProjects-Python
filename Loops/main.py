names = ["Jondrielle", "Raven", "Persephone"]
person = {
    "name": "Jondrielle",
    "age": 20,
    "gender": "Female"
}
numbers = [1, 3, 5, 6, 7, 9]
sum = 0

for name in names:
    print(name)

for value in person:
    print(person[value])

for number in numbers:
    sum = sum + number

print("The sum is: " + str(sum))
count = 0
while count <= 5:
    print(count)
    count += 1

i = 1
while i <= 10:
    print(i)
    i += 1

print("The while loop ended")

for name in "school":
    print(name)

print("For loop ended")