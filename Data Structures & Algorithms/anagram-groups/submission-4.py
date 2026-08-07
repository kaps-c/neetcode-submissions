class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            frequencies = {
            "a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0,
            "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0,
            "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0
            }
            for character in word:
                if character in frequencies:
                    frequencies[character] += 1
            
            key_list = frequencies.values()
            key = ','.join([str(count) for count in key_list])

            if key not in hashmap:
                hashmap[key] = []

            hashmap[key].append(word)

        output = list(hashmap.values())

        return output




