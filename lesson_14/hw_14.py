class Student:
    def __init__(self, name, last_name, age, rating):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.rating = rating

    def change_rating(self, new_rating):
        self.rating = new_rating


student = Student("Artur", "Sclar", 20, 8.5)

print(f'Name:', student.name,
      '\n'"Last name:", student.last_name,
      '\n'"Age:", student.age,
      '\n'"Rating:", student.rating)

student.change_rating(9.2)

print("\nAfter change raiting:"
      '\n'"Raiting:", student.rating)
