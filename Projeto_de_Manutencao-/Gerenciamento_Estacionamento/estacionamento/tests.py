from django.test import TestCase

# Create your tests here.


class UserTestCase(TestCase):
    """ Test Case example """

    def setUp(self) -> None:
        self.name = "user_test_case"

    def test_user(self):
        self.assertEqual(1, 1)
