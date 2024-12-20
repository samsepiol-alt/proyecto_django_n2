from django.urls import path
from .views import index
from .views import sign_in, sign_out, register
from .views import inmueble,crear_inmueble,editar_inmueble, eliminar_inmueble
from .views import profile, edit_profile, delete_profile
urlpatterns = [
    path('', index, name='index'),
    path('login/', sign_in, name='login'), #REQ01B
    path('logout/', sign_out, name='logout'),#REQ01B
    path('register/', register, name='register'),#REQ01B
    path('inmueble/', inmueble, name='inmueble'),
    path('inmueble/crear/', crear_inmueble, name='crear_inmueble'),
    path('inmueble/<int:id>/editar/', editar_inmueble, name="editar_inmueble"),
    path('inmueble/<int:id>/eliminar/', eliminar_inmueble, name='eliminar_inmueble'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/delete/', delete_profile, name='delete_profile'),
]
