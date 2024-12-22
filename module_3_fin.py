def calculate_structure_sum(*args):
    sum = 0
    for element in args:
        if isinstance(element, str):
            sum += len(element)
        elif isinstance(element, int):
            sum += element
        elif isinstance(element, float):
            sum += element
        elif isinstance(element, bool):
            sum += element
        elif isinstance(element, list):
            sum += calculate_structure_sum(*element)
        elif isinstance(element, tuple):
            sum += calculate_structure_sum(*element)
        elif isinstance(element, set):
            sum += calculate_structure_sum(*element)
        elif isinstance(element, dict):
            sum += calculate_structure_sum(*tuple(element.items()))
    return sum


data_structure = [
    [1, 2, 4],
    {'a': 2, 'b': 7},
    (6, {'cube': 7, 'drum': 11}),
    "Hello",
    ((), [{(6, 'Urban', ('Urban2', 42))}])
]
result = calculate_structure_sum(data_structure)
print(result)