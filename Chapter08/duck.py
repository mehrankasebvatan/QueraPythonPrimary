def find_winner(n):
    people = list(range(1, n + 1))
    current_index = 0
    while len(people) > 1:
        next_index = (current_index + 1) % len(people)
        people.pop(next_index)
        current_index = next_index
    return people[0]


n = int(input())
winner = find_winner(n)
print(winner)
