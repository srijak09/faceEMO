# facial_emotion_recognition/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emotion_recognition/', include('emotion_recognition.urls')),  # Include the emotion_recognition URLs
    path('', include('emotion_recognition.urls')),  # Direct root URL to emotion_recognition URLs
]
