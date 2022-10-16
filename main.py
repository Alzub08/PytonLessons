class Human:
  def __init__(self):
    self.name = 'None'
    self.age = 0
    self.gender = 'None'
  def introduse(self):
    print('Hello my name is', self.name)
  def add_info(self):
    self.name = input('Name: ')
    self.age = input('Age: ')
    self.gender = input('Gender: ')

obj = Human()
obj.introduse()
obj.add_info()
obj.introduse()