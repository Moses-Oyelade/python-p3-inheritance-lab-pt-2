class Student:

    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")
        
    def raise_hand(self):
        print("Pick me!")
        

student1=Student()

student1.hello()
student1.raise_hand()

class ChattyStudent(Student):
    
    def hello(self):
        Student.hello(self)
        self.hello = ("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")
        print(self.hello)
        
    def raise_hand(self):
        for i in range(10):
            super().raise_hand()
        
special_stud = ChattyStudent()
special_stud.__dict__
special_stud.hello()
special_stud.raise_hand()
