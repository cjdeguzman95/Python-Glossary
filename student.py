# This code uses abstraction and multiple inheritance to create the SpartaTrainee class
# Uses an IF statement to check the Trainee is trained by Isabella and also returns the Trainee's training duration
# Has a method that outputs the Trainee's graduation date

from person import Person
from modules import SpartaModules


class SpartaTrainee(Person, SpartaModules):

    def __init__(self, first_name, last_name, stream):
        super().__init__(first_name, last_name)
        self.stream = stream

    def check_trainer(self):
        if self.stream.lower() == "data":
            return "{} is trained by Isabella".format(self.first_name)
        else:
            return "{} is not trained by Isabella".format(self.first_name)

    def number_of_weeks_training(self):
        if self.stream.lower() == "data":
            return 8
        elif self.stream.lower() == "ba":
            return 6
        else:
            return 10

    def graduation_date(self):
        return "{} graduates in {} weeks".format(self.number_of_weeks_training())


if __name__ == '__main__':
    Jane = SpartaTrainee("Jane", "Doe", "Devops")
    print(Jane.introduce())
    print(Jane.check_trainer())
    print(Jane.number_of_weeks_training())
    print(Jane.list_all_modules())
