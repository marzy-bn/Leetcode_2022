class Solution:
    def interpret(self, command: str) -> str:
        
        output = ""
        idx = 0
        while idx < len(command):
            if command[idx] == 'G':
                output += 'G'
                idx += 1
            elif command[idx] == '(' and command[idx+1] == ')':
                output += 'o'
                idx += 2
            elif command[idx] == '(' and command[idx+1] == 'a' and command[idx+2] == 'l' and command[idx+3] == ')':
                output += 'al'
                idx += 4
        return output
                        
                    
                
                
                