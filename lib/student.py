class Student:
    def __init__(self, first_name="First", last_name="Last"):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = []
    def learn(self,information):
        self.knowledge.append(information)

    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")
    pass

class ChattyStudent(Student):
    def hello(self):
        print(
    "Hey there! I'm so excited to learn stuff.\n"
    "How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? "
    "You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died..."
)
    def raise_hand(self):
        for _ in range(10):
            print("Pick me!")

    pass


