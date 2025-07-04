
'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.


Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 
Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
'''

#word1의 알파벳 하나씩 answer 짝수 인덱스에 넣기
#word2의 알파벳 하나씩 answer 홀수 인덱스에 넣기
#갯수가 다르면 나머지 쭉 넣기

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        for idx,w1 in enumerate(word1): # 짝수 인덱스에 w1 알파벳 하나씩 넣기
            answer.insert(2*idx,w1)
        for idx,w2 in enumerate(word2): # 홀수 인덱스에 w2 알파벳 하나씩 넣기
            answer.insert(2*idx+1,w2)
        return ''.join(answer) # 합치기

# two pointer로 개선

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 결과를 저장할 리스트 (append 사용)
        merged_string = []
        
        # 각 문자열의 현재 위치를 가리키는 포인터 (인덱스)
        p1 = 0
        p2 = 0
        
        # 두 문자열의 길이
        n1, n2 = len(word1), len(word2)
        
        # 두 문자열 모두 문자가 남아있는 동안 번갈아 가며 추가 (핵심 부분)
        while p1 < n1 and p2 < n2:
            merged_string.append(word1[p1])
            merged_string.append(word2[p2])
            p1 += 1 # word1 포인터 이동
            p2 += 1 # word2 포인터 이동
        
        # word1에 남은 문자가 있다면 모두 추가
        while p1 < n1:
            merged_string.append(word1[p1])
            p1 += 1
        
        # word2에 남은 문자가 있다면 모두 추가
        while p2 < n2:
            merged_string.append(word2[p2])
            p2 += 1
            
        # 리스트에 저장된 문자들을 하나의 문자열로 합쳐 반환
        return "".join(merged_string)