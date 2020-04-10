# The following class uses SpartaTrainee as its base via multilevel inheritance
# It overrides the graduation_date method from SpartaTrainee to apply it to the whole Batch than just to one trainee (polymorphism)
# Depending on the stream, when the list_all_trainees method is called, it returns the relevant list

from student import SpartaTrainee


class Batch(SpartaTrainee):

    data_trainees = ["Weiyee", "Gigi", "Jonny", "Andy"]
    other_trainees = ["Mike", "Jason", "Kyle"]

    def __init__(self, first_name, last_name, stream, start_date):
        super().__init__(first_name, last_name, stream)
        self.start_date = start_date

    def add_student(self):
        if self.check_name_has_letters_only():
            if self.stream.lower() == "data":
                self.data_trainees.append(self.first_name)
            else:
                self.other_trainees.append(self.first_name)
        else:
            return "Invalid name entry"

    def list_all_trainees(self):
        if self.stream.lower() == "data":
            return self.data_trainees
        else:
            return self.other_trainees

    def graduation_date(self):
        return "{} batch graduates {} weeks from {}".format(self.stream, self.number_of_weeks_training(), self.start_date)


if __name__ == '__main__':
    CJ = Batch("CJ", "De Guzman", "Data", "24/04/2020")
    Alex = Batch("Alex", "Brown", "DevOps", "10/04/2020")

    CJ.add_student()
    Alex.add_student()
    print(CJ.list_all_trainees())
    print(Alex.list_all_trainees())

    print(CJ.introduce())
    print(CJ.number_of_weeks_training())
    print(CJ.graduation_date())
    print(CJ.check_trainer())
    print(CJ.list_all_modules())
