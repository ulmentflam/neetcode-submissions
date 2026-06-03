class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings, group all anagrams together into sublists. 
        You may return the output in any order. 

        Let's do somthing trivial first. Let's classify each string as an anagram.

        Let's create a map that looks somthing like this.

        {
            "act": [
                "act",
                "cat"
            ]
        }
        We need a fucntion to convert "cat" to "act for dictionary insertion, so that when we get
        dict[fn("cat")] it stores it in it's proper corrasponding anagram. If it doesn't exist,
        we create a new anagram.

        Since the output can be in any order, we don't have to worry about sorting. 

        Let me do the scaffoldig for the loop, then I will define the proper function

        """

        def hash_ord(s: str) -> str:
            """
            This is a special hash that will return the same value if the string has the same characters.

            We can do somthing similar to one hot encoding. The order needs to be the same for each.
            """
            one_hot_chars: list = [0 for _ in range(26)]   # O(26) or O(1) memory space
            for c in s:
                one_hot_chars[ord(c) - ord('a')] += 1
            return str(one_hot_chars) # Computationally O(s) 
            
            
        classify_anagrams: dict[str, List[str]] = {}
        
        # This is asymptotically O(sS) where S is the length of the list and s is the lenght of the string 
        for s in strs:
            hashed_str = hash_ord(s) # This hash does change computational complexity by order of O(s) where s is the string
            if not classify_anagrams.get(hashed_str):
                classify_anagrams[hashed_str] = []
            classify_anagrams[hashed_str].append(s)
        
        return [l for l in classify_anagrams.values()]
        
