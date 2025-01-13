class Employee:
    def __init__(self, name, work_id, length_of_work):
        self.name = name
        self.work_id = work_id
        self.length_of_work = length_of_work

    def get_info(self):
        return str(self.name) + ". Стаж работы: " + str(self.length_of_work) + " мес."

class Manager(Employee):
    def __init__(self, name, department, work_id, length_of_work):
        Employee.__init__(self, name, work_id, length_of_work)
        self.department = department

    def get_info(self):
        return Employee.get_info(self) + " Менеджер отдела " + self.department + "."

    def manage_project(self):
        ...

class Technician(Employee):
    def __init__(self, name, specialization, work_id, length_of_work):
        Employee.__init__(self, name, work_id, length_of_work)
        self.specialization = specialization

    def get_info(self):
        return Employee.get_info(self) + " " + self.specialization + "."

    def perform_maintenance(self):
        ...

class TechManager(Manager, Technician):
    def __init__(self, name, specialization, department, work_id, length_of_work, team):
        self.name = name
        self.specialization = specialization
        self.length_of_work = length_of_work
        self.department = department
        self.work_id = work_id
        self.length_of_work
        self.team = team

    def get_info(self):
            return Employee.get_info(self) + " Специальность: " + self.specialization + ". Отдел: " + self.department + "."

    def get_team_info(self):
        print("Технический менеджер команды: " + self.get_info() + ".")
        for employee in self.team:
            print(employee.get_info())

    def add_employee(self, employee):
        self.team.append(employee)


techman = TechManager("Олег", "физик-ядерщик", "не помню", 374, 25, list([Employee("Витя", 102, 2)]))
freelancer = Employee("Аноним", 997, 0)

techman.add_employee(freelancer)

print(techman.get_team_info())
