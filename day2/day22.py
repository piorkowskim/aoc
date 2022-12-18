def fight_outcome(enemy, player):
    # A, B, C
    # X, Y, Z = rock, paper, scissors
    # 1, 2, 3 for shape and 0, 3, 6 for outcome
    if enemy == "A":
        if player == "X":
            return 3
        elif player == "Y":
            return 3+1
        elif player == "Z":
            return 6+2
    elif enemy == "B":
        if player == "X":
            return 1
        elif player == "Y":
            return 3+2
        elif player == "Z":
            return 6+3
    elif enemy == "C":
        if player == "X":
            return 2
        elif player == "Y":
            return 3+3
        elif player == "Z":
            return 6+1




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
