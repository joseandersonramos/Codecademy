# School Catalogue Project
# José Anderson Ramos Aquino

# School class
class School:
  def __init__(self, name, level, numberOfStudents=0):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def __repr__(self):
    return 'A {level} school named {name} with {numberOfStudents} students'.format(level=self.level, name=self.name, numberOfStudents=self.numberOfStudents)

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents
  
  def set_numberOfStudents(self, numberOfStudents):
    self.numberOfStudents = numberOfStudents

# Primary School class
class PrimarySchool(School):
  def __init__(self, name, numberOfStudents=0, pickupPolicy="Pickup after 3pm"):
    super().__init__(name, 'primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def get_pickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    return super().__repr__() + '. ' + self.pickupPolicy + '.'

# High School class
class HighSchool(School):
  def __init__(self, name, numberOfStudents=0, sportsTeams=None):
    super().__init__(name, 'high', numberOfStudents=0)

    if sportsTeams == None:
      self.sportsTeams = ['basketball', 'tennis']
    else:
      self.sportsTeams = sportsTeams
  
  def get_sportsTeams(self):
    return self.sportsTeams
  
  def __repr__(self):
    return 'Our sports teams are: {}'.format(self.sportsTeams)
    
hs = HighSchool('Anderson High', 400)
print(hs)

