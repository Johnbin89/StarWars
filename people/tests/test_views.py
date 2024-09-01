from django.test import TestCase
import decimal
from people.models import StarWarsCharacter
import json

# Get user model from settings
from django.contrib.auth import get_user_model

User = get_user_model()


class PeopleViewSetTest(TestCase):
    def setUp(self):
        # Create two users
        test_user1 = User.objects.create_user(
            username="testuser1", password="testuser1pass"
        )
        test_user2 = User.objects.create_user(
            username="testuser2", password="testuser2pass"
        )

        test_user1.save()
        test_user2.save()

        # Create 10 StarWarsCharacter objects
        for i in range(10):
            StarWarsCharacter.objects.create(
                name=f"TestName-{i}",
                height=175,
                mass=decimal.Decimal(10),
                hair_color="random",
                skin_color="random",
                eye_color="random",
                birth_year=decimal.Decimal(50.2),
                gender="male",
                home_world_name="planet",
            )

    def test_people_view(self):
        response = self.client.get("/api/people/")
        self.assertEqual(response.status_code, 200)
        
    def test_all_listed(self):
        response = self.client.get("/api/people/")
        count = StarWarsCharacter.objects.all().count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count, len(response.data))

    def test_favorites_protected(self):
        response = self.client.get("/api/people/favorites/")
        self.assertEqual(response.status_code, 401)

    def post_favorites(self):
        self.client.login(username="testuser1", password="testuser1pass")
        response = self.client.post(
            "/api/people/favorites/",
            json.dumps([1, 4, 10]),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["added_count"], 3)
        added_ids = [character[0] for character in response.data["characters"]]
        self.assertEqual(added_ids, [1, 4, 10])

    def get_favorites(self):
        self.client.login(username="testuser1", password="testuser1pass")
        response = self.client.get("/api/people/favorites/")
        found_ids = [character["id"] for character in response.data]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(found_ids, [1, 4, 10])

    def test_post_get_favorites(self):
        self.post_favorites()
        self.get_favorites()

