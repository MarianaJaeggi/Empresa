
from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'registro_app'


urlpatterns = [


    #Listar
    path('listar-docentes/', views.DocenteListViewAll.as_view(), name='listar-docentes'),


    path('listar-nodocentes/', views.NoDocenteListViewAll.as_view(), name='listar-nodocentes'),



    #Busquedas Docentes

    path('buscarporapellido/', views.DocenteListViewBuscar.as_view(), name='buscarporapellido'),

    path('buscarpormateria/', views.DocenteListViewBuscarPorMateria.as_view(), name='buscarpormateria'),

     #Busquedas No Docentes
     
    path('buscarporapellidonodocente/', views.NoDocenteListViewBuscar.as_view(), name='buscarporapellidonodocente'),

    path('buscarporoficina/', views.NoDocenteListViewBuscarPorOficina.as_view(), name='buscarporoficina'),

    #Detalle Docente

    path('detalle/<pk>', views.DocenteDetailView.as_view(), name='detalle'),

     #Detalle No Docente

    path('detallenodocente/<pk>', views.NoDocenteDetailView.as_view(), name='detallenodocente'),



    #Mensaje a usuario: creado/modificado/eliminado con exito

    path('exito/', views.SuccessView.as_view(), name='exito'),



    #Alta Docente

    path('alta/', views.DocenteCreateView.as_view(), name='alta'),


    #Modificacion Docente

    path('update/<pk>/', views.DocenteUpdateView.as_view(), name='update'),


    #Eliminar Docente

    path('delete/<pk>/', views.DocenteDeleteView.as_view(), name='delete'),



     #Alta NO Docente

    path('altanodocente/', views.NoDocenteCreateView.as_view(), name='altanodocente'),



     #Modificacion NO Docente

    path('updatenodocente/<pk>/', views.NoDocenteUpdateView.as_view(), name='updatenodocente'),


      #Eliminar NoDocente

    path('deletenodocente/<pk>/', views.NoDocenteDeleteView.as_view(), name='deletenodocente'),

    path('', views.VistaPrincipal.as_view(), name="index"),
]