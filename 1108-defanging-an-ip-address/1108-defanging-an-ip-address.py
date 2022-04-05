class Solution:
    def defangIPaddr(self, address: str) -> str:
        out = ""
        for element in address:
            if element is not '.':
                out += element
            else:
                out += '[.]'
        return out