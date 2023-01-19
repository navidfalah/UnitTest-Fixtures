from typing import Optional
from django.conf import settings
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from user_auth.models import User


USER_FIXTURE_ADDRESS = "user_auth/fixtures/user_fixtures.yaml"



class HamgramAPIClient(APIClient):
    def credentials(self, user: User, http_authorization_header: str = "Bearer ", **kwargs):
        access_token = AccessToken.for_user(user)
        access = str(access_token)
        super().credentials(HTTP_AUTHORIZATION=http_authorization_header + access, **kwargs)
        return


class HamgramAPITestCase(APITestCase):
    client_class = HamgramAPIClient
    fixtures = [USER_FIXTURE_ADDRESS]
    client_phone: Optional[str] = "09930731973"

    def setUp(self) -> None:
        if USER_FIXTURE_ADDRESS in self.fixtures and self.client_phone:
            self.user = User.objects.get(phone=self.client_phone)
            self.client.credentials(user=self.user)

