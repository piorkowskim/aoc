arr = []

with open('input.txt', 'r') as f:
    for line in f:
        arr.append(line.strip())

snack = 0
sum_calories = []

for calories in arr:
    if calories != '':
        snack += int(calories)
    else:
        sum_calories.append(snack)
        snack = 0

sum_calories = sorted(sum_calories, reverse=True)
print(sum(sum_calories[0:3]))
