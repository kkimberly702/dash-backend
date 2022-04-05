from django.urls import path, include
from .views.users import SignUp, SignIn, SignOut, ChangePassword
from .views.items import ItemsView, ItemView


urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
    path('items/', ItemsView.as_view(), name='items'),
    path('item/<int:pk>/', ItemView.as_view(), name='items'),
]
