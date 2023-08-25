import unittest

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.status import (HTTP_200_OK, HTTP_401_UNAUTHORIZED,
                                   HTTP_403_FORBIDDEN)
from rest_framework.test import APIClient

from quiz.utils.samples import sample_question, sample_quiz


class TestAPI(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.quiz = sample_quiz(level=1, title="Test", description="Some description")
        self.question = sample_question(quiz=self.quiz, order_number=1)

        self.user = get_user_model().objects.create(email="test_api@example.com")
        self.user.set_password("qwerty1234")
        self.user.save()

    def test_question_details(self):
        self.client.force_authenticate(user=self.user)

        result = self.client.get(
            reverse("api:question_details", kwargs={"pk": self.quiz.pk, "order": self.question.order_number})
        )
        self.assertEqual(result.status_code, HTTP_200_OK)
        self.assertEqual(result.data, {"id": 1, "order_number": 1, "text": "Text for testing", "choices": []})

    @unittest.skip("")
    def test_question_details_no_access(self):
        result = self.client.get(
            reverse("api:question_details", kwargs={"pk": self.quiz.pk, "order": self.question.order_number})
        )
        self.assertEqual(result.status_code, HTTP_401_UNAUTHORIZED)

    def test_quiz_list_forbidden(self):
        self.client.force_authenticate(user=self.user)

        result = self.client.get(reverse("api:quiz_list"))
        self.assertEqual(result.status_code, HTTP_403_FORBIDDEN)
