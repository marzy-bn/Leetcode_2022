class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse = {'a':".-",'b':"-...",'c':"-.-.",
                      'd':"-..",'e':".",'f':"..-.",
                      'g':"--.",'h':"....",'i':"..",
                      'j':".---",'k':"-.-",'l':".-..",
                      'm':"--",'n':"-.",'o':"---",'p':".--.",
                      'q':"--.-",'r':".-.",'s':"...",'t':"-",
                      'u':"..-",'v':"...-",'w':".--",'x':"-..-",
                      'y':"-.--",'z':"--.."}
        out = set()
        for word in words:
            mapped = ""
            for letter in word:
                mapped += morse[letter]
            out.add(mapped)
        
        return len(out)
            