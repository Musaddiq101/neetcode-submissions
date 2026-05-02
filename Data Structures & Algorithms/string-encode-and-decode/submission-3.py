class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            l = len(word)
            s += str(l)+"#"+word
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        j = 0
        length = i-j+1
        while i < len(s):
            print(str(length) + " " + str(i) + s[i])
            if s[i].isdigit():
                i += 1
            elif s[i] == '#':
                length = int(s[j:i])
                print(length)
                # if length == 0:
                #     return [""]
                i = i+1
                ans.append(s[i:i+length])
                #print(ans)
                i += length
                j = i
            
        return ans





