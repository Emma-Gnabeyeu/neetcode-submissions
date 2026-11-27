class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_ = ""
        for str_ in strs:
            encode_+=str(len(str_)) + "%" + str_ # encode like , length+separator(%) + string itself
        print(encode_)
        return encode_ # "".join(len(s)).join("%")+strs

    def decode(self, s: str) -> List[str]:
        decode = []
        indx = 0
        while indx < len(s):
            init = indx
            while s[indx] != "%":
                indx+=1
            length = int(s[init:indx])
            decode.append(s[indx+1:indx+1+length])
            indx = indx + 1 + length
        return decode
