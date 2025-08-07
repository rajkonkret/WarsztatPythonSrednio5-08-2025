# longest() - znajduje najdłuzszy klucz w słowniku

class LongestKeyDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest


class LongestKeyDictMax(dict):
    def longest_key(self):
        return max(self.keys(), key=len, default=None)


art = LongestKeyDict()
art['tomasz'] = 12
art['abraham'] = 34
art['zen'] = 1
print(art.longest_key())  # abraham

art = LongestKeyDictMax()
art['tomasz'] = 12
art['abraham'] = 34
art['zen'] = 1
print(art.longest_key())  # abraham
assert "abraham" == art.longest_key()
# assert "zen" == art.longest_key() # AssertionError
