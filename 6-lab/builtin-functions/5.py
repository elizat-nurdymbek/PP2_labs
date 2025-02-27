def all_true_elements(t):
    return all(t)

user_input = input("Enter tuple elements separated by spaces (e.g., True 3): ")

tuple_values = tuple(map(eval, user_input.split()))

print(all_true_elements(tuple_values))
