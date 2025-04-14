from itertools import permutations

def solve_cryptoarithmetic(equation):
    words = equation.replace(" ", "").split("+")
    words[-1], result = words[-1].split("=")
    words.append(result)
    letters = set("".join(words))
    if len(letters) > 10:
        print("Too many unique letters")
        return
    letters = list(letters)
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if any(mapping[word[0]] == 0 for word in words):
            continue  # Leading digit cannot be zero
        numbers = [sum(mapping[char] * (10 ** i) for i, char in enumerate(word[::-1])) for word in words]
        if sum(numbers[:-1]) == numbers[-1]:
            print("Solution Found:")
            print({char: mapping[char] for char in sorted(mapping)})
            return
    print("No solution found")

equation = input("Enter cryptoarithmetic equation (e.g., SEND + MORE = MONEY): ")
solve_cryptoarithmetic(equation)
