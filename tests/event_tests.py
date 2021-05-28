import json
from levelupapi.models.gameType import GameType
from levelupapi.models.game import Game
from rest_framework import status
from rest_framework.test import APITestCase
# from levelupapi.models import GameType


class EventTests(APITestCase):
    def setUp(self):
        """
        Create a new account and create sample category
        """
        url = "/register"
        data = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "bio": "Love those gamez!!"
        }
        # Initiate request and capture response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Store the auth token
        self.token = json_response["token"]

        # Assert that a user was created
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # SEED DATABASE WITH ONE GAME TYPE
        # This is needed because the API does not expose a /gametypes
        # endpoint for creating game types
        game_type = GameType()
        game_type.label = "Board Game"
        game_type.save()

        self.game = Game()
        self.game.game_type_id = 1
        self.game.skill_level = 5
        self.game.title = "Monopoly"
        self.game.maker = "Milton Bradley"
        self.game.number_of_players = 4
        self.game.gamer_id = 1
        self.game.save()



    def test_create_event(self):
        """
        Ensure we can create a new game.
        """
        # DEFINE GAME PROPERTIES
        url = "/events"
        data = {
            "time": "10:00",
            "date": "2021-22-5",
            "description": "asdf",
            "gameId": 1
        }

        # Make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was created
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["time"], data["time"])
        self.assertEqual(json_response["date"], data["date"])
        self.assertEqual(json_response["description"], data["description"])
        self.assertEqual(json_response["game"]["id"], data["gameId"])