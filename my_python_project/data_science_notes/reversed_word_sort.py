def reverse(word):
    return ''.join(reversed(word))

fruits = ['cherry', 'apple', 'banana']
sort_by_last = sorted(fruits, key=reverse)

print(sort_by_last)