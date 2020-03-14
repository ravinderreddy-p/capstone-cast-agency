import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from models import Movie, Actor


class FilmAgencyTestCase(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client

        self.director_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik16VTFNMFl3T0RRNE5rUXlOMEV5UWtNNVFrUTRORGxDUkRaR01qWTFSREF6TVRFME0wRXhOdyJ9.eyJpc3MiOiJodHRwczovL3JhdmktZnNuZC5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDA0OTkyNzAyODkxMjE1NjI1NzAiLCJhdWQiOlsiQ29mZmVlIHNob3AiLCJodHRwczovL3JhdmktZnNuZC5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTg0MTgxNDA5LCJleHAiOjE1ODQxODg2MDksImF6cCI6Ikxma3hSZGxlRGllTmpKbXlZRXlEUElSejhYODBKUUd1Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6ZHJpbmtzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6ZHJpbmtzLWRldGFpbCIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDpkcmlua3MiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6ZHJpbmtzIiwicG9zdDptb3ZpZXMiXX0.efEMqSRa01KsWTdp_W3Pu2gXuJYNoxN-5dh1XttGu8Vk4ZN_suX7Vb4VkKFUGfiXwVYmLiHi8bVjHU5Njue5L11RsQm-wqQnBVrKQys8XrXJH-2ISeA7PSdelTfWs3r5rG6oNlNfsW3ZmhUGfFo-jxD8biLwKGRjF4HPwssrjDKFfQu-k6NlkXp_lpwMgZBsfyFOjxu4O_ZhsyTcWRrgnZoWAyXhh6sbCCcTfALkyefh7OUmTZns_BbYBEYZlb5mf_Vj-A88Hi2IBU3Azr0fbtTPqNkJvqW1FU4ss54aWWTCUwy1prZysYwvsIp_E7z9rmxQuUGlXwCnZs-YNs4JYQ'
        self.producer_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik16VTFNMFl3T0RRNE5rUXlOMEV5UWtNNVFrUTRORGxDUkRaR01qWTFSREF6TVRFME0wRXhOdyJ9.eyJpc3MiOiJodHRwczovL3JhdmktZnNuZC5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDcxNjcyODM1NzI1NjY5NTQ2MjEiLCJhdWQiOlsiQ29mZmVlIHNob3AiLCJodHRwczovL3JhdmktZnNuZC5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTg0MTgxNDQ3LCJleHAiOjE1ODQxODg2NDcsImF6cCI6Ikxma3hSZGxlRGllTmpKbXlZRXlEUElSejhYODBKUUd1Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.bzUtmRRrMia7AhQoS-9vZtoHj_JPxI8hxlbF-QtAUIj1q5P6Dz8lI_Y7IeaHA7a4kRBCUKrtbfIzAJ7ugqMeF6HzyZ1iXENJQkFdQAazd5AMaXHM2CEWHhrgb_crhJLv6sEGB5eMypyj2_W4hVrYO658Mz5veHYB-EEohwcqiX5k3_Wyt_-uDKyj_BLeV1K1pK1liJrXbvH-_FYGG7j3-mWgCkKPsN93wU7Tsoi48tfQ7eoVGjPm1xsCgt352NAgZ78GvytbE33dqiKO1765vs91omlULFyR4NmiWlxDcj_8gio00fRwvxF9r7BX1zOFdTLM4Up48J7ETu8gdJz_fQ'

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_create_actors_with_director_token_success(self):
        data = {
            'name': 'test',
            'age': '30',
            'gender': 'female'
        }
        response = self.client().post(
            '/actors',
            json=data, headers={
                "Authorization":
                    "Bearer {}".format(self.director_token)
            })
        self.assertEqual(response.status_code, 201)

    def test_create_movies_with_producer_token_success(self):
        data = {
            'title': 'test',
            'release_date': 'Feb28'
        }
        response = self.client().post(
            '/movies',
            json=data, headers={
                "Authorization":
                    "Bearer {}".format(self.producer_token)
            })
        self.assertEqual(response.status_code, 500)

    def test_get_actors_success(self):

        response = self.client().get(
            '/actors',
            headers={
                "Authorization":
                    "Bearer {}".format(self.director_token)
            }
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_movies_success(self):

        response = self.client().get(
            '/movies',
            headers={
                "Authorization":
                    "Bearer {}".format(self.director_token)
            }
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_movies_with_producer(self):

        response = self.client().get(
            '/movies',
            headers={
                "Authorization":
                    "Bearer {}".format(self.producer_token)
            }
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
