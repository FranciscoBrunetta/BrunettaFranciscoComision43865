from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',index, name="inicio"),

    path('ourcreator/',ourcreator, name="ourcreator"),

    path('wine_form/',wineForm, name="wine_form"),
    path('wine_form2/',wineForm2, name="wine_form2"),

    path('search_categoria/',searchCategoria, name="search_categoria"),
    path('search2/',search2, name="search2"),

    path('wines/',WineList.as_view(), name="wines"),
    path('create_wine/', WineCreate.as_view(), name="create_wine"),
    path('detail_wine/<int:pk>/', WineDetail.as_view(), name="detail_wine"),
    path('update_wine/<int:pk>/', WineUpdate.as_view(), name="update_wine"),
    path('delete_wine/<int:pk>/', WineDelete.as_view(), name="delete_wine"),


    path('beers/',BeerList.as_view(), name="beers"),
    path('create_beer/', BeerCreate.as_view(), name="create_beer"),
    path('detail_beer/<int:pk>/', BeerDetail.as_view(), name="detail_beer"),
    path('update_beer/<int:pk>/', BeerUpdate.as_view(), name="update_beer"),
    path('delete_beer/<int:pk>/', BeerDelete.as_view(), name="delete_beer"),

    path('spirits/',SpiritList.as_view(), name="spirits"),
    path('create_spirit/', SpiritCreate.as_view(), name="create_spirit"),
    path('detail_spirit/<int:pk>/', SpiritDetail.as_view(), name="detail_spirit"),
    path('update_spirit/<int:pk>/', SpiritUpdate.as_view(), name="update_spirit"),
    path('delete_spirit/<int:pk>/', SpiritDelete.as_view(), name="delete_spirit"),

    path('sparkling/',SparklingList.as_view(), name="sparkling"),
    path('create_sparkling/', SparklingCreate.as_view(), name="create_sparkling"),
    path('detail_sparkling/<int:pk>/', SparklingDetail.as_view(), name="detail_sparkling"),
    path('update_sparkling/<int:pk>/', SparklingUpdate.as_view(), name="update_sparkling"),
    path('delete_sparkling/<int:pk>/', SparklingDelete.as_view(), name="delete_sparkling"),

    path('whisky/',WhiskyList.as_view(), name="whisky"),
    path('create_whisky/', WhiskyCreate.as_view(), name="create_whisky"),
    path('detail_whisky/<int:pk>/', WhiskyDetail.as_view(), name="detail_whisky"),
    path('update_whisky/<int:pk>/', WhiskyUpdate.as_view(), name="update_whisky"),
    path('delete_whisky/<int:pk>/', WhiskyDelete.as_view(), name="delete_whisky"),

    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('register/', register, name="register"),

    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]