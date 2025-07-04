'''
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
'''

#GCD 존재하려면 str1,str2 둘다 반복문자이거나 아니면 str1자체가 str2의 반복문자여야함.
#반복문자인지 확인하려면 두문자열의 길이의 최대공약수를 구하고
#최대공약수의 약수의 길이만큼의 문자열의 배수가 원래 문자열이 되야함.

class Solution:

    def gcd(self,a, b):
        while b: #b가 0이 될때까지 반복
            a, b = b, a % b 
        return a

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == len(str2):
            if str1 == str2 :
                return str1
            else :
                return ""
        gcd = self.gcd(len(str1),len(str2))

        for i in range(gcd,0,-1):
            if len(str1) > len(str2):
                if str1 == (len(str1)//i)*str2[:i] and str2 == (len(str2)//i)*str2[:i]:
                    return str2[:i]
            if len(str1) < len(str2):
                if str2 == (len(str2)//i)*str1[:i] and str1 == (len(str1)//i)*str1[:i]:
                    return str1[:i]
            else :
                return ""