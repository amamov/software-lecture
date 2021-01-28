class Robot:

    """ Robot Class """

    # Class Variable
    population = 0

    def __init__(self, name, age):  # 생성자
        self.name = name  # Instanse Variable
        self.age = age  # Instanse Variable
        Robot.population += 1

    # Instance Method
    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")

    # Instance Method
    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")
        print(f"I am {self.age} years old.")

    # Class Method
    @classmethod
    def how_many(cls):
        print(f"We have {cls.population} robots.")

    # Class Method
    @classmethod
    def is_name_amamov(cls, instance):
        if instance.name == "amamov":
            print("This robot name is amamov")
        else:
            print("This robot name is not amamov")


if __name__ == "__main__":
    rob1 = Robot(name="Siri", age=6)

    Robot.how_many()

    rob2 = Robot(name="GiGA Genie", age=4)
    rob3 = Robot(name="amamov", age=15)

    Robot.how_many()

    rob1.say_hi()

    Robot.is_name_amamov(rob2)
    Robot.is_name_amamov(rob3)

    rob1.die()

    Robot.how_many()
