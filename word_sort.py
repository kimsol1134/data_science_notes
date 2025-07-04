'''
1. 글자수 짧은게 우선
2. 글자수 같으면 사전순
'''

N = int(input())

words = []
for _ in range(N):
    word = input()
    words.append(word)
words = list(set(words))
words.sort(key=lambda x : (x, len(x))) # 튜플로 길이순 정렬 과 알파벳 정렬


for i in range(len(words)):
    print(words[i])