from django.core.exceptions import ValidationError
from django.test import TestCase

from quiz.models import Quiz
from quiz.utils.samples import sample_question, sample_quiz


class TestQuizModel(TestCase):
    def setUp(self):
        self.test_quiz = sample_quiz(title="test_quiz")
        self.questions_count = Quiz.QUESTION_MAX_COUNT
        for order_number in range(self.questions_count):
            sample_question(quiz=self.test_quiz, order_number=order_number)

    def tearDown(self) -> None:
        self.test_quiz.delete()

    def test_questions_count(self):
        self.assertEqual(self.questions_count, self.test_quiz.questions_count())

    def test_quiz_title_limit(self):
        with self.assertRaises(ValidationError):
            sample_quiz(title="A" * 7000)

        self.assertEqual(Quiz.objects.count(), 1)
