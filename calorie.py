from temperature import Temperature


class Calorie:
    """Represents optimal calorie a person needs to take today"""

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return result


if __name__ == "__main__":
    temperature = Temperature(country='italy', city='rome').get()
    calorie = Calorie(temperature=temperature, weight=70, height=175, age=32)
    print(calorie.calculate())
