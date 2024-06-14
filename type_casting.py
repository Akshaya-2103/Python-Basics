class Person:
    def init(self, name, age, gender, ht_no):
        self.name = name
        self.age = age
        self.gender = gender
        self.ht_no = ht_no
        
    def speak(self):
        print(f"Hi my name is {self.name} and my age is {self.age}.")
        print(f"My gender is {self.gender} and my hall ticket number is {self.ht_no}.")
        
    def major(self):
        if int(self.age)>18:
            print("I am eligible for voting.")
        else:
            print("I am not eligible for voting.")

Radhika = Person("Radhika","21","Female","2203A51L81")
Radhika.speak()
Radhika.major()
