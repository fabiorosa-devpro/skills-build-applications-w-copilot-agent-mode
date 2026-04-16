from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient

from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):

        client = MongoClient('localhost', 27017)
        db = client[settings.DATABASES['default']['NAME']]

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Teams
        teams = [
            {"_id": ObjectId(), "name": "Marvel"},
            {"_id": ObjectId(), "name": "DC"}
        ]
        db.teams.insert_many(teams)

        # Users
        users = [
            {"_id": ObjectId(), "name": "Superman", "email": "superman@dc.com", "team": "DC"},
            {"_id": ObjectId(), "name": "Batman", "email": "batman@dc.com", "team": "DC"},
            {"_id": ObjectId(), "name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
            {"_id": ObjectId(), "name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"_id": ObjectId(), "name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
            {"_id": ObjectId(), "name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"}
        ]
        db.users.insert_many(users)
        db.users.create_index([("email", 1)], unique=True)

        # Activities
        activities = [
            {"_id": ObjectId(), "user": "Superman", "activity": "Flight", "duration": 120},
            {"_id": ObjectId(), "user": "Batman", "activity": "Martial Arts", "duration": 90},
            {"_id": ObjectId(), "user": "Iron Man", "activity": "Suit Training", "duration": 100},
            {"_id": ObjectId(), "user": "Wonder Woman", "activity": "Lasso Practice", "duration": 80},
            {"_id": ObjectId(), "user": "Captain America", "activity": "Shield Throw", "duration": 70},
            {"_id": ObjectId(), "user": "Black Widow", "activity": "Espionage", "duration": 60}
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {"_id": ObjectId(), "user": "Superman", "score": 1000},
            {"_id": ObjectId(), "user": "Iron Man", "score": 950},
            {"_id": ObjectId(), "user": "Batman", "score": 900},
            {"_id": ObjectId(), "user": "Wonder Woman", "score": 850},
            {"_id": ObjectId(), "user": "Captain America", "score": 800},
            {"_id": ObjectId(), "user": "Black Widow", "score": 750}
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {"_id": ObjectId(), "user": "Superman", "workout": "Strength Training", "reps": 50},
            {"_id": ObjectId(), "user": "Iron Man", "workout": "Tech Lifting", "reps": 40},
            {"_id": ObjectId(), "user": "Batman", "workout": "Endurance", "reps": 45},
            {"_id": ObjectId(), "user": "Wonder Woman", "workout": "Amazon Circuit", "reps": 35},
            {"_id": ObjectId(), "user": "Captain America", "workout": "Shield Pushups", "reps": 30},
            {"_id": ObjectId(), "user": "Black Widow", "workout": "Stealth Moves", "reps": 25}
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
