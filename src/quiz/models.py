from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

from core.models import BaseModel


class Result(BaseModel):
    quiz = models.ForeignKey(to="quiz.Quiz", related_name="results", on_delete=models.CASCADE)
    user = models.ForeignKey(to=get_user_model(), related_name="results", on_delete=models.CASCADE)
    count_of_correct_answers = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.user.email} ({self.quiz.title})"


class Category(BaseModel):
    image = models.ImageField(upload_to="media/category/covers", null=True, blank=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return f"{self.name} ({self.id})"


class Quiz(BaseModel):
    QUESTION_MAX_COUNT = 5

    class LEVEL_CHOICES(models.IntegerChoices):
        BASIC = 0, "Basic"
        MEDIUM = 1, "Medium"
        ADVANCED = 2, "Advanced"

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(to="quiz.Category", related_name="quizzes", on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to="media/quiz/covers")
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES.choices, default=LEVEL_CHOICES.BASIC)

    def __str__(self):
        return f"{self.title} ({self.id})"

    def questions_count(self):
        return self.questions.count()


class Question(BaseModel):
    quiz = models.ForeignKey(to="quiz.Quiz", related_name="questions", on_delete=models.CASCADE)
    order_number = models.PositiveSmallIntegerField(validators=[MaxValueValidator(Quiz.QUESTION_MAX_COUNT)])
    text = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.text} ({self.order_number})"


class Choice(BaseModel):
    question = models.ForeignKey(to="quiz.Question", related_name="choices", on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({self.question.order_number})"
