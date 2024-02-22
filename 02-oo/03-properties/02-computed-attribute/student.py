# Write your code here

class BMICalculator:
    def __init__(self, weight_in_kg, height_in_m):
        self.__weight_in_kg = weight_in_kg
        self.__height_in_m = height_in_m
        
    @property
    def weight(self):
        return self.__weight_in_kg

    @property
    def height(self):
        return self.__height_in_m
    
    @property
    def bmi(self):
        return self.weight / self.height**2
    
    @property
    def category(self):
        if self.bmi < 18.5:
            return "underweight"
        elif self.bmi > 25:
            return "overweight"
        else:
            return "normal"
        
person1 = BMICalculator(65.5, 1.75)
print(person1.bmi)