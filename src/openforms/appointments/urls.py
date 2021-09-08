from django.urls import path

from .views import VerifyCancelAppointmentLinkView

app_name = "appointments"

urlpatterns = [
    path(
        "<str:base64_submission_uuid>/<str:token>/verify",
        VerifyCancelAppointmentLinkView.as_view(),
        name="appointments-verify-cancel-appointment-link",
    )
]
