arr = []

with open('input.txt', 'r') as f:
    for line in f:
        arr.append(line.strip())
sum = 0
sum_calories = []
for calories in arr:
    if calories != '':
        sum +=int(calories)
    else:
        sum_calories.append(sum)
        sum = 0
print(sorted(sum_calories, reverse=True)[0])
