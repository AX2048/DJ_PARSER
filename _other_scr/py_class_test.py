class Person:
   def init(self, name, age, gender):
      self.name = name
      self.age = age
      self.gender = gender

   def greet(self):
      print("Hello, my name is {}".format(self.name))

   def introduce(self):
      print("I am {} years old and I am a {}".format(self.age, self.gender))

###

Person1 = Person()
Person1.name = 'Alex'
Person1.age = 24
Person1.gender = 'Men'

Person1.greet()
Person1.introduce()

Person2 = Person()
Person2.name = 'Ahav'
Person2.age = 55
Person2.gender = 'Men'

Person2.greet()
Person2.introduce()

###
