from django.contrib.auth import get_user_model
from django.test import TestCase
from restaurants.models import Restaurant
from reviews.models import Review


class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            nickname='testuser', email='test@example.com', password='password1234'
        )
        self.restaurant = Restaurant.objects.create(
            name='Test Restaurant',
            description='Test Description',
            address='123 Test St',
            contact='Phone: 010-0000-0000'
        )
        self.data = {
            'user': self.user,
            'restaurant': self.restaurant,
            'title': 'Test Review Title',
            'comment': 'Tasty Yammy Yammy~'
        }

    def test_create_review(self):
        review = Review.objects.create(**self.data)

        self.assertEqual(review.title, self.data['title'])
        self.assertEqual(review.comment, self.data['comment'])
        self.assertEqual(review.user, self.data['user'])
        self.assertEqual(review.restaurant, self.data['restaurant'])


