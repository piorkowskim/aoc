import string

arr = []
point = [" "]
score = 0
i = 0
for letter in string.ascii_letters:
    point.append(letter)

with open('input.txt', 'r') as f:
    for line in f:
        arr.append(line.strip())

print(arr)
for compartments in arr:
    first, second = arr[i][:len(arr[i])//2], arr[i][len(arr[i])//2:]
    common = list(set(first)&set(second))
    score += point.index(common[0])
    i += 1
print(score)

