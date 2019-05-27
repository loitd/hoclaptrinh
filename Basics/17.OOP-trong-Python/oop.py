# ------------------------------------------------------------
# OOP Example for Youtube.com/c/tranducloi
# ------------------------------------------------------------
# Không có khai báo public/protected/private trong python
class Human(object):
    # global attribute
    liveon = 'Earth'
    # Constructor
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
    # sample method
    def say(self, msg):
        print("{0} saying {1} from {2}".format(self.name, msg, self.location))
    
    # sample private/hidden/mangle method
    def __show(self):
        print("__SHowing {0}".format(self.name))

# Asian is a subclass of Human
class Asian(Human):
    # Overwrite __init__ method of parent class
    def __init__(self, name, age):
        return super().__init__(name, age, "Asia")

if __name__ == "__main__":
    john = Human("John", 30, "Moon")
    john.say("youtube.com/c/tranducloi")
    # john.__show()
    print(john)

    lan = Asian("Lan", 29)
    lan.say("youtube.com/c/tranducloi")

    # check for instance
    print(isinstance(lan, (Human)))

    # Test global attribute
    print("We're living on? {0}".format(Human.liveon))
    
    # Test global attribute on children
    print("We're living on? {0}".format(Asian.liveon))