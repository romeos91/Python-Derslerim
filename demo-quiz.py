class quiz:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()
q1 = quiz("What is the capital of France?", "Paris")   
user_answer = input(q1.question + " ")
if q1.check_answer(user_answer):
    print("Correct!")
else:
    print("Wrong! The correct answer is:", q1.answer)
