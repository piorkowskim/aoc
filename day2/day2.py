def fight_outcome(enemy, player):
    # A, B, C
    # X, Y, Z = rock, paper, scissors
    # 1, 2, 3 for shape and 0, 3, 6 for outcome
    if player == "X":
        if enemy == "A":
            return 3+1
        elif enemy == "B":
            return 1
        elif enemy == "C":
            return 6+1
    if player == "Y":
        if enemy == "A":
            return 6+2
        elif enemy == "B":
            return 3+2
        elif enemy == "C":
            return 2
    if player == "Z":
        if enemy == "A":
            return 3
        elif enemy == "B":
            return 6+3
        elif enemy == "C":
            return 3+3




arr = []
with open('input.txt', 'r') as f:
    for line in f:
        arr.append(line.strip().split(" "))
print(arr)
score = 0
i = 0
for values in arr:
    score += fight_outcome(values[0], values[1])
    i += 1
print(score)