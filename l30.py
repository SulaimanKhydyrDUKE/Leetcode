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

        
