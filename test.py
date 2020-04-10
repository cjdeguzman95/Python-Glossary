# The following test bed checks that all the methods from all the programmes work as they should

import unittest
from person import Person
from modules import SpartaModules
from student import SpartaTrainee
from batch import Batch


class TestSparta(unittest.TestCase):
    test_person_class = Person(",.;/", 1255)
    test_batch_class = Batch("John", "Smith", "Devops", "24/03/20")
    test_sparta_modules_class = SpartaModules("not a sparta module")
    test_sparta_trainee_class = SpartaTrainee("Jane", "Doe", "Data")

    def test_name_checker(self):
        self.assertEqual(self.test_person_class.check_name_has_letters_only(), "Invalid name entry")

    def test_module_checker(self):
        self.assertFalse(self.test_sparta_modules_class.check_if_sparta_module())

    def test_module_length_method(self):
        self.assertEqual(self.test_sparta_modules_class.module_length(), "Unknown: this is not a Sparta module")

    def test_training_duration_counter(self):
        self.assertEqual(self.test_sparta_trainee_class.number_of_weeks_training(), 8)

    def test_list_trainees(self):
        self.assertEqual(self.test_batch_class.list_all_trainees(), ["Mike", "Jason", "Kyle"])


if __name__ == '__main__':
    unittest.main()
