from django.conf.urls import path
from django.contrib import admin
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.views.generic import TemplateView, RedirectView

from collection.backends import MyRegistrationView
from collection import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/',
        TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/',
        TemplateView.as_view(template_name='contact.html'), name='contact'),

    path('things/', RedirectView.as_view(pattern_name='browse', permanent=True)),
    path('things/<slug>/', views.thing_detail, name='thing_detail'),
    path('things/<slug>/edit/', views.edit_thing, name='edit_thing'),

    path('browse/', RedirectView.as_view(pattern_name='browse', permanent=True)),
    path('browse/name/',
        views.browse_by_name, name='browse'),
    path('browse/name/<initial>/',
        views.browse_by_name, name='browse_by_name'),

    path('accounts/password/reset/', password_reset,
        {'template_name': 'registration/password_reset_form.html'}, name="password_reset"),
    path('accounts/password/reset/done/', password_reset_done,
        {'template_name': 'registration/password_reset_done.html'}, name="password_reset_done"),
    path('accounts/password/reset/<uidb64>/<token>/', password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'}, name="password_reset_confirm"),
    path('accounts/password/done/', password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name="password_reset_complete"),

    path('accounts/register/',
        MyRegistrationView.as_view(), name='registration_register'),
    path('accounts/create_thing/',
        views.create_thing, name='registration_create_thing'),

    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
]
