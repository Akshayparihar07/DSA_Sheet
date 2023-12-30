class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) == 1: return True
        dic = {}
        for word in words:
            for char in word:
                if char in dic:
                    dic[char] += 1
                else: dic[char] = 1

        for char, count in dic.items():
            if  count % len(words) != 0:
                return False
        return True
