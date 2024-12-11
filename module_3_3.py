def single_root_words(root_word, *other_words):
    same_words = []
    all_words = list(other_words)
    for i in range(len(all_words)):
        if root_word.lower() in all_words[i].lower() or all_words[i].lower() in root_word.lower():
            same_words.append(all_words[i])
    return (same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

single_root_words(result2)
