import unittest

from Flask_App import Flask_App

def test_home(self):
        response = self.client.get("/", data={"content": " Displays the index page accessible at '/' "})
        assert response.status_code == 200
        assert "POST method called" == response.get_data(as_text=True)
def test_operation(self):
        response = self.client.post("/"),
        assert response.status_code == 200
            


