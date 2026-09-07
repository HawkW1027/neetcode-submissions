class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        empty_set = set()
        for s in strs:
            empty_set.add(tuple(sorted(s)))
        empty_list = list(empty_set)
        result: list[list[str]] = [[] for _ in range(len(empty_list))]
        for s in strs:
            for i in range(len(empty_list)):
                if tuple(sorted(s))==empty_list[i]:
                    result[i].append(s)
                    break
        return result     

