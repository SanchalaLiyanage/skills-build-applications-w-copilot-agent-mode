from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username="testuser", email="testuser@example.com", password="password")

    def test_user_creation(self):
        response = self.client.post('/api/users/', {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_team_creation(self):
        team = Team.objects.create(name="Test Team")
        team.members.add(self.user)
        self.assertEqual(team.name, "Test Team")

    def test_activity_creation(self):
        activity = Activity.objects.create(user=self.user, activity_type="Running", duration="01:00:00")
        self.assertEqual(activity.activity_type, "Running")

    def test_leaderboard_entry(self):
        leaderboard = Leaderboard.objects.create(user=self.user, score=100)
        self.assertEqual(leaderboard.score, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name="Test Workout", description="Test Description")
        self.assertEqual(workout.name, "Test Workout")