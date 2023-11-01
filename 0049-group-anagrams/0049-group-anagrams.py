class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grouped_angram = {}
        
        for word in strs:
            sorted_str = ''.join(sorted(word))
            
            if sorted_str in grouped_angram:
                grouped_angram[sorted_str].append(word)
            else:
                grouped_angram[sorted_str] = [word]

        return list(grouped_angram.values())
            