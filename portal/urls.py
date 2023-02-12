from django.contrib import admin
from django.urls import path
from turism import views

urlpatterns = [
    path("", views.index, name="home"),
]

handler404 = "turism.views.page_not_found_view"
handler403 = "turism.views.page_forbidden"
handler400 = "turism.views.page_bad_request"
# handler500 = "messenger.views.page_internal_server"