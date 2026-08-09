class employee:
   def __init__(self,employee_id,emp_name):
      self.emp_name=emp_name
      self.employee_id=employee_id

   def display(self):
      print(self.emp_name)

class devel(employee):
   def __init__(self, name, language):
        super().__init__(name)
        self.language = language
   def work(self):
        print("Writing", self.language)


d = devel("Sahib", "Python")
d.display()