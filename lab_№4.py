class Human:
    default_name = 'Duke'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = 'bomj'

    def info(self):
        print (self.name, self.age, self.__money, self.__house)

    def earn_money(self, money):
        self.__money += money

    def buy_house(self, house, discount):
        if self.__money >= house.final_price(discount):
            self.__make_deal(house, discount)
            print('средств хватило')
        else:
            print('недостаточно средств')

    def __make_deal(self, house, discount):
        self.__money -= house.final_price(discount)
        self.__house = house

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)


class House:
    def __init__(self, area=10, price=10):
        self.__area = area
        self.__price = price

    def final_price(self, discount=100):
        return self.__price * (100 - discount) / 100

class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)


Human.default_info()
hum = Human('Charlie', 48)
hum.info()
building = SmallHouse(1000)
hum.buy_house(building, 10)
hum.earn_money(100000)
hum.buy_house(building, 10)
hum.info()

