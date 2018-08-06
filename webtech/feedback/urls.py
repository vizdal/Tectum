from django.contrib import admin
from django.urls import include,path
from feedback.views import feedback_form,save_feedback
from feedback.views import get_apartment_names

urlpatterns = [
	path('<int:user_id>/',feedback_form, name="Feedback Form"),
	path('save/',save_feedback,name="save feedback")
]