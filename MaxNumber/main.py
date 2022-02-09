#This program finds the largest number in a list

list = [1,30,394,0,495,1]

max = 0
for number in list:
    if max < number:
        max = number

print(max)