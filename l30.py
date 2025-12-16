#Failed this one at 2/3 because I couldn't generate all permutations of the words. Sliding window with a hashmap apprently can suffice
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        concat = {""}# Apprently this is a dictionary
        #concat = set() #is the right way
        #Run a for loop that runs continuesly updating concat by having a temporary set that all cominations of the words.
        for i in range(len(words)):
            word = words[i]
            print(word)
            temp_concat = set()
            #for k in concat: apprently a for loop doesn't run for a set
            for k in concat:
                temp_concat.add(k + word)
                temp_concat.add(word + k)
            concat = temp_concat
            print(concat)
        # Run a loop that checks for for character match by two pointers. Save indexes, return them. 
        ind = set()
        for i in concat:
            inf = s.find(i)
            b = 0
            while s[b:len(s)].find(i)!=-1:
                inf=s[b:len(s)].find(i)
                ind.add(inf+b)
                b+=inf+1
        
        return list(ind)

# Solution that works, but is extremely slow = 9 seconds, beats only 5% of submissions
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        map = {}
        for i in words:
            if i in map:
                map[i] = map[i]+1
            else:
                map[i] = 1
        word = len(words[0])
        siz = word*len(words)
        l, r = 0, siz-1
        ret = set()
        
        while r<len(s):
            temp_map = map.copy()
            window = s[l:r+1]
     
            count = 0
            t, p = 0, word
       
            while p<r+2:
                wee = window[t:p]
                if wee in temp_map and temp_map[wee] != 0:
                
                    count+=1
                    temp_map[wee]-=1
                    t+=word
                    p+=word
                else:
                    t+=word
                    p+=word
                    break
            if count==len(words):
                ret.add(l)
            count = 0
            l+=1
            r+=1
            
            
        return list(ret)

        

        
