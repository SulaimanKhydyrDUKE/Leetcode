class Solution(object):
    def intToRoman(self, num):
        map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ret = ""

        if num/map["M"]>0 or num%map["M"]>=900:
            time = num/map["M"]
            while time > 0:
                num -= map["M"]
                ret+="M"
                time -=1
            if num%map["M"]>=900:
                ret+="CM"
                num-=900
            
        if num/map["D"]>0 or num%map["D"]>=400:
            time = num/map["D"]
            
            while time>0:
                num-=map["D"]
                ret+="D"
                time -=1
            if num%map["D"]>=400:
                ret+="CD"
                num -=400
        if num/map["C"]>0 or num%map["C"]>=90:
            time = num/map["C"]
            
            while time>0:
                num-=map["C"]
                ret+="C"
                time -=1
            if num%map["C"]>=90:
                ret += "XC"
                num -=90
        if num/map["L"]>0 or num%map["L"]>=40:
            time = num/map["L"]
            
            while time>0:
                ret+="L"
                num-=50
                time -=1
            if num%map["L"]>=40:
                num -= 40
                ret += "XL"
        if num/map["X"] > 0 or num%map["X"]==9:
            
            time = num/map["X"]
            while time>0:
                ret+="X"
                time-=1
                num-=10
            if num%map["X"]==9:
                num -= 9
                ret += "IX"
        if num/map["V"]>0 or num%map["V"]==4:
            
            time = num/map["V"]
            while time>0:
                num-=5
                ret+="V"
                time-=1
            if num%map["V"]==4:
                num -=4
                ret += "IV"
        while num>0:
            ret+="I"
            num-=1
        return ret




                
        
