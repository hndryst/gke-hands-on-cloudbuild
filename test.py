import pytest
import requests
from rest import app

with app.test_client() as test_client:

    def postRequest(task_id, task):
        return test_client.post(f"/task/{task_id}", data={"task": task}).status_code

    def getRequest(task_id):
        return test_client.get(f"/task/{task_id}").status_code

    def deleteRequest(task_id):
        return test_client.delete(f"/task/{task_id}").status_code

    def getHealthzRequest():
        return test_client.get("/healthz").status_code

    class TestREST:
        def test_post(self):
            # positive
            assert postRequest("1", "turn off the light") == 201
            assert postRequest("2", "buy groceries") == 201
            # negative
            assert postRequest("1", "turn on the light") == 409

        def test_get(self):
            # positive
            assert getRequest(1) == 200
            assert getRequest(2) == 200
            # negative
            assert getRequest(6) == 404

        def test_delete(self):
            # positive
            assert deleteRequest(1) == 204
            assert deleteRequest(2) == 204
            # negative
            assert deleteRequest(4) == 404

        def test_get_after_delete(self):
            assert getRequest(1) == 404

        def test_get_healthz(self):
            # positive
            assert getHealthzRequest() == 200
