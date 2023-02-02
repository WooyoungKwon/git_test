# 10.9
class Bear:

    def __init__(self):
        self.eat = 'berries'

    def eats(self):
        return self.eat


class Rabbit:
    def __init__(self):
        self.eat = 'clover'

    def eats(self):
        return self.eat


class Octothorpe:
    def __init__(self):
        self.eat = 'campers'

    def eats(self):
        return self.eat


bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()

print(bear.eats(), rabbit.eats(), octothorpe.eats())


# 10.10
class Laser:
    def __init__(self):
        self.name = 'disintegrate'

    def does(self):
        return self.name


class Claw:
    def __init__(self):
        self.name = 'crush'

    def does(self):
        return self.name


class SmartPhone:
    def __init__(self):
        self.name = 'ring'

    def does(self):
        return self.name


class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        print(self.laser.does(), self.claw.does(), self.smartphone.does())


robot = Robot()
robot.does()