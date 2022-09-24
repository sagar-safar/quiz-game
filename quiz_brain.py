class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_no<len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        ans = input(f"Q.{self.question_no} : {current_question.text} (True/False)? ")
        if ans == current_question.answer:
            self.score += 1
            print("you got it right!")

        else:
            print("That's wrong")
        print(f"The correct answer is : {current_question.answer}")
        print(f"your current score is : {self.score}")



