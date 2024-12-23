class person :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_info(self):
        print(f"my name is {self.name} and my age is {self.age}")  
        
        
class student :
    def __init__(self, college, student_id):
        self.college = college 
        self.student_id = student_id  
    def show_std_info(self):
        print(f"my college is {self.college} and my student ID = {self.student_id}")
        
        
class employee(person, student) :
    def __init__(self, name, age ,college, student_id, job, salary):        
        super().__init__(name,age)  
        student.__init__(self, college, student_id)
        self.job = job
        self.salary = salary    
    def show_emp_info(self):
        print(f"my job is {self.job} and my salary = {self.salary}")
    def show_all_info(self) :
         p1.show_info()
         p1.show_std_info()
         p1.show_emp_info()   
        
        
p1 = employee("mohamed", 20, "MNU", 20230271, "IOT enginner",30000) 
p1.show_all_info()

                                         