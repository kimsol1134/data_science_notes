def reverseVowels(s: str) -> str:
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    idx_list = []
    word_list = []
    for idx, word in enumerate(s) :
        if word in vowels:
            idx_list.append(idx)
            word_list.append(word)
    word_list = word_list[::-1]
    s = list(s)
    for i in range(len(idx_list)):
        s[idx_list[i]] = word_list[i]
    return ''.join(s)

print(reverseVowels("IceCreAm"))