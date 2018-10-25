from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

# Create your views here.

@api_view(["POST"])
@permission_classes([AllowAny])
def verify_mt(request):
    try:
        
        return
    except Exception, e:
        return