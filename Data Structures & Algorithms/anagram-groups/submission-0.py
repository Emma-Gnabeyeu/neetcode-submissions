class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]
        groups = defaultdict(list) # {sorted(strs[0]):[strs[0]]}
        for str_ in strs:
            key =''.join(sorted(str_))
            groups[key].append(str_)
        return list(groups.values())

        