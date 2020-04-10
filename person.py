# This code creates a Person class which is the basis for the SpartaTrainee class.
# It has a method that ensures the user only inputs a valid name (i.e. made of alphabetical letters only)
# It has one other method in it which uses the formatting function


class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def check_name_has_letters_only(self):
        if self.first_name.isalpha() and self.last_name.isalpha():
            return "Person object successfully created"
        else:
            return "Invalid name entry"

    def introduce(self):
        return "Hi, my name is {} {}".format(self.first_name, self.last_name)


if __name__ == '__main__':
    John = Person("John", "Doe")
    print(John.check_name_has_letters_only())
    print(John.introduce())
