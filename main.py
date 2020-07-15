class Cat:
    def __init__(self, name, bowl = None):
        self.name = name
        self.bowl = bowl
        # print("{}: I am here".format(self.name))

    def meow(self):
        return "{}: Meow\n".format(self.name)

    def eat(self):
        if self.bowl == None:
            return "There isn't bowl\n"
        else:
            if self.bowl.isdec():
                return "Nice food\n"
            else:
                return "I am hungry\n"


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
    with open("output.txt", "w") as file:
        cat = Cat("Cleo")
        file.write(cat.meow())
        file.write(cat.eat())

        bowl_for_milisa = Bowl(5)
        file.write("Bowl volume is {}\n".format(bowl_for_milisa.getvolume()))

        cat2 = Cat("Milisa", bowl_for_milisa)
        file.write(cat2.meow())
        file.write(cat2.eat())

        file.write("Bowl volume is {}\n".format(bowl_for_milisa.getvolume()))

        file.flush()