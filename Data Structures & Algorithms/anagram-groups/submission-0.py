class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list);

        for str in strs:
            a = [0] * 26
            for c in str:
                a[ord(c) - ord('a')] += 1
            dic[tuple(a)].append(str)
        return list(dic.values())