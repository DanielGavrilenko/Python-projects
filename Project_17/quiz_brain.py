class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        player_answer = input(f"{current_question.text} (True/False):")
        self.check_answer(player_answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    def check_answer(self, player_answer):
        if player_answer == self.question_list[self.question_number].answer:
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong")
        print(f"The correct answer was: {self.question_list[self.question_number].answer}")
        print(f"Your current score {self.score}/{self.question_number+1}")
        print()
