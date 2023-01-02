from django.urls import reverse
from api_app.models import Email
from django.test import TestCase
from api_app.serializers import EmailSerializer

class BasicInviteTest(TestCase):
    @classmethod 
    def setUpTestData(cls):
        Email.objects.create(email="unittest@unittest.com")
    
    def test_if_invited(self):
        invite_ = Email.objects.create(email="neha@neha.com")
        serialized_data = EmailSerializer(invite_)
        data = {
            "email": "neha@neha.com"
        }
        response = self.client.post(reverse("invite_list_endpoint"), data)
        self.assertEqual(response.json()[0], serialized_data.data)
        
        
    def test_create_user(self):
       user_data = {
           "email" : "userdoesntexist@unittest.com",
           "user_name":"userdoesntexist",
           "password":"userdoesntexist",
           "password2":"userdoesntexist",
           "first_name":"Anukul",
           "last_name":"Unit Tests"
       }
       response = self.client.post(reverse("register_user"), data=user_data)       
       self.assertEqual(response.json(), {"response": "sorry your email address doesn't exist in invite list"})
       
    def test_invite_user(self):
        """
        Integration test of whole workflow of inviting, registering of new users by existing members.
        """
        user_data = {
           "email" : "unittest@unittest.com",
           "user_name":"unittest",
           "password":"unittest",
           "password2":"unittest",
           "first_name":"Anukul",
           "last_name":"Unit Tests"
        }
        # Register User
        self.client.post(reverse("register_user"), data=user_data)
        
        # Generating Access Token of Registered User
        login = self.client.post(reverse("token_obtain_pair"), {"email":"unittest@unittest.com", "password":"unittest"})
        token = login.json()['access'] 
        Header = {'HTTP_AUTHORIZATION': f'Bearer {token}'} 
       
        # User to be Invited 
        payload = {
            "email": "neha@neha.com"
        }
        
        # Inviting user by using registered user
        self.client.post(reverse("invite_to_bookxchange"), data=payload, **Header)
        
        # verifying if user is in invited_list
        response = self.client.post(reverse("invite_list_endpoint"), data=payload)
        self.assertEqual(response.json()[0]['email'], payload['email'])
