class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ','')
        number = number.replace('-','')
        
        output = ''
        count = len(number)
        remain = count % 3
        print(remain)
        
        if remain == 0:
            last = number[len(number)-3:]
            end = len(number)-3

        if remain == 2:
            last = number[len(number)-2:]
            end = len(number)-2
        
        if remain == 1:
            last = number[len(number)-4:len(number)-2] + '-' + number[len(number)-2:]
            end = len(number)-4
        
        for i,num in enumerate(number[:end]):
            output += num
            if (i+1)%3 == 0:
                output += '-'    
            count -= 1
        
        output += last
        
        
        
        return output