from django.urls import reverse
from rest_framework.test import APITestCase
from apps.education.models import Direction, Faculty
from apps.common.models import Districts
from apps.application.models import Application
from django.contrib.auth.models import User
from datetime import datetime


class ApplicationAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_pass')

        self.faculty = Faculty.objects.create(title='Test Faculty')
        self.direction = Direction.objects.create(title='Test Direction', faculty=self.faculty)
        self.district = Districts.objects.create(title='Test District')

        self.application = Application.objects.create(
            user=self.user,
            first_name="John",
            last_name="Doe",
            passport="AB1234567",
            pinfl="12345678901234",
            gender="Male",
            birth_date=datetime(1990, 1, 1),
            direction=self.direction,
            status="Pending",
            district=self.district,
        )

        self.list_url = reverse('application_list')

    def test_application_creation_api(self):
        data = {
            "user": self.user.id,
            "first_name": "Jane",
            "last_name": "Smith",
            "passport": "CD7654321",
            "pinfl": "98765432109876",
            "gender": "Female",
            "birth_date": "1995-05-05",
            "direction": self.direction.id,
            "status": "Pending",
            "district": self.district.id,
        }

        response = self.client.post(self.list_url, data, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Application.objects.count(), 2)  # The initial one plus the new one
        self.assertEqual(Application.objects.last().first_name, "Jane")

    def test_application_list_api(self):
        response = self.client.get(self.list_url)
        r = response.json()
        count = r.get('count', 0)
        results = r.get('results', [])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(count, 1)
        if results:
            data = results[0]
            self.assertEqual(self.application.first_name, data['first_name'])
            self.assertEqual(self.application.last_name, data['last_name'])
        else:
            self.fail("Results list is empty.")
