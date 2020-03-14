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

        self.director_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik16RkdRME00UXpSR09VUkVNRU5CUkRnNU1UVXdSRE5FUVRjMVFqZEVORU13TWpCR01FWXpPQSJ9.eyJpc3MiOiJodHRwczovL3VpYXR6dS5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQ1OTU4NDMwNzYxODE1NDg4MDIiLCJhdWQiOlsiY29mZmUiLCJodHRwczovL3VpYXR6dS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTgxNzc3NTczLCJleHAiOjE1ODE4NjM5NzMsImF6cCI6Ik4zNWUwRWdwZERLN1czSmdTekFDYjdhSzY1OVRBWVA1Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6ZHJpbmtzIiwiZ2V0OmFjdG9ycyIsImdldDpkcmlua3MtZGV0YWlsIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOmRyaW5rcyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDpkcmlua3MiXX0.bFUxeisaWw70KLElnMTS6Q1wNtGkQQ5y2ESUpdy3sfE6lxNOzGdQEqOH5N2OSTxnHRlp8mTyYrUzz1c-z5Vvr6z01o2fbSfsN3ekDih-nAAnxDy9qg-nyzjLD6R4kzPyCOOZJ-UDkm-jHRXeH6dvnBLE4movccVLYZ_ppkVsoPJoFGmiSdmfWjF3FE1HYHazs5i-V28l5ZajL56GbBcD_H1UXgwvoMarHXV6DOADMeV4io9nUDVSe0uoI3dTb9kmOt0C26_4hnN2uE4qy7dtFDXYJTa7egkQYFnD7K-Zttm2tjd7v0aOgDDITacQBlHDf0uB9VMHMMsY1wmjk0PbZg'
        self.producer_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik16RkdRME00UXpSR09VUkVNRU5CUkRnNU1UVXdSRE5FUVRjMVFqZEVORU13TWpCR01FWXpPQSJ9.eyJpc3MiOiJodHRwczovL3VpYXR6dS5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTEwMDc0MjczMzI0NTgwODgxODciLCJhdWQiOlsiY29mZmUiLCJodHRwczovL3VpYXR6dS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTgxNzc3NDY0LCJleHAiOjE1ODE4NjM4NjQsImF6cCI6Ik4zNWUwRWdwZERLN1czSmdTekFDYjdhSzY1OVRBWVA1Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJnZXQ6bW92aWVzIiwicG9zdDptb3ZpZXMiXX0.X9y9hCPVRfZOtOOnXKszx3c-yOcIRklYy7hDVtdSpL0boPv19hM7j7LoDw3CY4ut2t1H7L5UgaeRa7wzOc8qSUZfUlDFMdiUA7fipVoaevm8wY7tjh59-QLB26sgiggmMYQsqGiLonck0gCN01NY14XQPbIx8qdu6MvR85H5oTs1iyTvJ64nhjMPR6nsXojAPqsVq_7y16m4UHL7bkq-KpRB_IZoM_lRVuBIKQCuYxKejaKZxle8pOQOOqCDiwgJN9mfc0WwD0iMboAP9kBBdpgq-GbvZwfRjxOuRP3p2RcRURgTOHrkwssuX2eBmo01YA6W0f_Z8iu7fLgqmqiVMw'

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
        self.assertEqual(response.status_code, 200)

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
