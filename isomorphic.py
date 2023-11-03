'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        x=set(i for i in s)
        y=set(i for i in t)
        if len(x) != len(y):
            return False
        x=dict()
        y=dict()
        k=0
        for i in range(len(s)):
            if s[i] not in x:
                x[s[i]]=k
            if t[i] not in y:
                y[t[i]]=k
            elif s[i] in x :
                if x[s[i]] == y[t[i]]:
                    k=k+1
                    continue
                else:
                    return False
            k=k+1
        return True     
            