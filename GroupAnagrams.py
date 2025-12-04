class Solution(object):
    def groupAnagrams(self, strs):
        # Map that contains the sorted word and indexes
        map = {}
        for s in range(len(strs)):
            b = ''.join(sorted(strs[s]))
            if b not in map:
                l = list()
                l.append(s)
                map[b] = l
            else:
                map[b].append(s)

        # looping through the map, reading the values, joiing them together, and printing thenm out
        ret = []*len(strs)
        for key, value in map.items():
            it = 0
            temp = list()
            for i in value:
                temp.append(strs[i])
            ret.append(temp)
            it+=1
        return ret
