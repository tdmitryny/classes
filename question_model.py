class Question:
    def __init__(self, text, answer):
            self.text = text
            self.answer = answer


ques = Question("Who?", "What")
print(ques.text)