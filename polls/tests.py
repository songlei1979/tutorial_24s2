import datetime

from django.test import TestCase
from django.utils import timezone

from polls.models import Question


# Create your tests here.
class Tests(TestCase):
    def test_question_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_question_was_published_recently_with_before_yesterday_question(self):
        time = timezone.now() + datetime.timedelta(days=-30)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_question_was_published_recently_with_yesterday_question(self):
        time = timezone.now() + datetime.timedelta(hours=-23)
        yesterday_question = Question(pub_date=time)
        self.assertIs(yesterday_question.was_published_recently(), True)
