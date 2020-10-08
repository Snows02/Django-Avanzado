"""Users views."""

# Django REST Framework
from rest_framework import status
from rest_framework.views import APIView

# Serializers
from cride.users.serializer import UserLoginSerializer

class UserLoginAPIView(APIView):
    """User login API View."""

    def post(self, request, *args, **kwargs):
        """Handle HTTp POST request."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        data = {
            'status': 'ok',
            'token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
