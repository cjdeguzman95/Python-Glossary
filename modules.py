# This code creates a SpartaModules class which is the basis for the SpartaTrainee class
# It has a hard-coded list of modules taught at Sparta Global
# The add_module method is encapsulated so that only authorised people can add modules to the list
# It uses an IF statements to check whether an object is a Sparta Module and also returns the length of a module if it is


class SpartaModules:

    sparta_modules_list = ["Business Week", "SQL", "Agile", "Python", "Machine Learning", "Tableau"]

    def __init__(self, module_name):
        self.module_name = module_name

    def _add_module(self):
        self.sparta_modules_list.append(self.module_name)

    def check_if_sparta_module(self):
        if self.module_name in self.sparta_modules_list:
            return True
        else:
            return False

    def module_length(self):
        if self.check_if_sparta_module():
            if self.module_name.lower() == "python":
                return "This module is 2 weeks long"
            else:
                return "This module is 1 week long"
        else:
            return "Unknown: this is not a Sparta module"

    def list_all_modules(self):
        return self.sparta_modules_list


if __name__ == '__main__':
    python = SpartaModules("Python")
    print(python.check_if_sparta_module())
