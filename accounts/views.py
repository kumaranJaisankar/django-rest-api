from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter

from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
# from rest_framework.decorators import api_view,permission_classes 
# from django.contrib.auth.models import User
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.serializers import ModelSerializer
# from rest_framework.response import Response




class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = "http://127.0.0.1:8000/accounts/github/login/callback/"
    client_class = OAuth2Client



