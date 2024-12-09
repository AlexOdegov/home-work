calls = 0
def count_cals():
    global calls
    calls += 1
def string_info(string):
    string_1 = str(string)
    facts = (len(string_1), string_1.upper(), string_1.lower())
    count_cals()
    return facts
def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_cals()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            facts = True
            break
        else:
            facts = False
            continue
    return facts
print(string_info('Detroit Red Wins'))
print(string_info('Colorado Avalanche'))
print(is_contains('Urban',['ban', 'BaNan', 'urBAN']))
print(is_contains('cycle',['recycling', 'cyclic']))


