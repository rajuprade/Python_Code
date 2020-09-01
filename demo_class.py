class Employee:
  def __init__(self, name, age):
        self.name = name
        self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name, "and age is " + str(self.age))
    mystring= "Hello my name is {}."
    print(mystring.format(self.age))

p1 = Employee("RAJ", 36)
p1.myfunc()
