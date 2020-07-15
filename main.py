class Cat:
    def __init__(self, name, bowl = None):
        self.name = name
        self.bowl = bowl
        print("{}: I am here".format(self.name))

    def meow(self):
        print("{}: Meow".format(self.name))

    def eat(self):
        if self.bowl == None:
            print("There isn't bowl")
        else:
            if self.bowl.isdec():
                print("Nice food")
            else:
                print("I am hungry")


class Bowl:
    def __init__(self, volume):
        self.volume = volume

    def isdec(self):
        if self.volume > 0:
            self.volume -= 1
            return True
        else:
            return False
    
    def getvolume(self):
        return self.volume



if __name__ == "__main__":
    cat = Cat("Cleo")
    cat.meow()
    cat.eat()

    bowl_for_milisa = Bowl(5)
    print("Bowl volume is {}".format(bowl_for_milisa.getvolume()))

    cat2 = Cat("Milisa", bowl_for_milisa)
    cat2.meow()
    cat2.eat()

    print("Bowl volume is {}".format(bowl_for_milisa.getvolume()))