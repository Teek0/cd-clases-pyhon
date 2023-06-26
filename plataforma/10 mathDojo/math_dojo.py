class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        for n in range(0,len(nums)):
            self.result+=nums[n]
        self.result += num
        return self
    def subtract(self, num, *nums):
        for n in range(0,len(nums)):
            self.result-=nums[n]
        self.result -= num
        return self
    def result(self):
        print(self.result)

md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	

rd = MathDojo()
y = rd.add(6).add(2,2,14,4).add(3,1).result
print(y)
y = rd.subtract(6).subtract(2,2,14,4).subtract(3,1).result
print(y)
