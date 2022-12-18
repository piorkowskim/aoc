import string

point = [" "]
arr = []
score = 0
i = 0
for letter in string.ascii_letters:
    point.append(letter)

with open('input.txt', 'r') as f:
    for line in f:
        arr.append(line.strip())

for i in range(0,len(arr),3):
    first, second, third = arr[i], arr[i+1], arr[i+2]
    common = list(set(first)&set(second)&set(third))
    score += point.index(common[0])
print(score)