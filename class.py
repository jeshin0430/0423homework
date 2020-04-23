class Fourcal:
    def __init__(self, name, age, university):
        self.name = name
        self.age = age
        self.university = university
        self.add_num = 0
        self.sub_num = 0
        self.gob_num = 0
        self.div_num = 0

    def add(self, num1, num2):
        self.add_num += 1
        return num1 + num2

    def sub(self, num1, num2):
        self.sub_num += 1
        return num1 - num2

    def gob(self, num1, num2):
        self.gob_num += 1
        return num1 * num2

    def div(self, num1, num2):
        self.div_num += 1
        if num2 == 0:
            return "0으로 못나눕니다"
        else:
            return num1 / num2

    def showcount(self):
        print("덧셈: %d" % self.add_num)
        print("뺄셈: %d" % self.sub_num)
        print("곱셉: %d" % self.gob_num)
        print("나눗셈: %d" % self.div_num)

calculator1 = Fourcal('정현', 25, '고려대')
print(calculator1.div(5,0))
print(calculator1.div(10,2))
print(calculator1.gob(5,3))
print(calculator1.gob(5,0))
calculator1.showcount()