class Mother:

    tribe = "human"

    def run(self):
        print("달리는 능력")

    def attack(self):
        print("공격하는 능력")


class Son(Mother):
    def jump(self):
        print("점프하는 능력")

    ## 오버라이딩
    def run(self):
        print("아들만의 달리는 능력")

    ## super()
    def mother_run(self):
        super().run()

        print(super())
        # <super: <class 'Son'>, <Son object>>

        print(type(super()))
        # <class 'super'>


if __name__ == "__main__":
    son = Son()

    print(son.tribe)

    son.attack()
    son.jump()
    son.run()
    son.mother_run()