

from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    TemplateView,
    UpdateView,
    DeleteView,
)


from django.urls import reverse_lazy
from .models import Docente
from .models import NoDocente
from .forms import DocenteForm
from .forms import NoDocenteForm




#Listado de los Docentes
class DocenteListViewAll(ListView):
    model = Docente
    template_name = "registro/listadocente.html"
    ordering = 'last_name'
    context_object_name = 'lista'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Docente.objects.filter(
            last_name__icontains =  palabra_clave 

        )
        return lista
     




#Listado de los No-Docentes
class NoDocenteListViewAll(ListView):
    model = NoDocente
    template_name = "registro/listanodocente.html"
    ordering = 'last_name'
    context_object_name = 'lista'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = NoDocente.objects.filter(
            last_name__icontains =  palabra_clave 

        )
        return lista






#Buscar  Docentes por Apellido

class DocenteListViewBuscar(ListView):
    model = Docente
    template_name = "registro/buscarporapellido.html"
    context_object_name = 'lista'
    

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Docente.objects.filter(
            last_name =  palabra_clave 

        )
        return lista


#Buscar  Docentes por Materia

class DocenteListViewBuscarPorMateria(ListView):
    model = Docente
    template_name = "registro/buscarpormateria.html"
    context_object_name = 'lista'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Docente.objects.filter(
            course =  palabra_clave 

        )
        return lista




#Buscar  NoDocentes por Apellido

class NoDocenteListViewBuscar(ListView):
    model = NoDocente
    template_name = "registro/buscarporapellidonodocente.html"
    context_object_name = 'lista'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = NoDocente.objects.filter(
            last_name =  palabra_clave 

        )
        return lista


#Buscar  NoDocentes por Oficina

class NoDocenteListViewBuscarPorOficina(ListView):
    model = NoDocente
    template_name = "registro/buscarporoficina.html"
    context_object_name = 'lista'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = NoDocente.objects.filter(
            office =  palabra_clave 

        )
        return lista




#Detalle Docente con PK

class DocenteDetailView(DetailView):
    model = Docente
    template_name = "registro/detalle.html"
    context_object_name = 'detalleSi'


#Detalle NoDocente con PK

class NoDocenteDetailView(DetailView):
    model = NoDocente
    template_name = "registro/detallenodocente.html"
    context_object_name = 'detalleNo'



class SuccessView(TemplateView):
    template_name = "registro/exitodocente.html"



#Alta un Docente

class DocenteCreateView(CreateView):
    model = Docente
    template_name = "registro/altadocente.html"
    form_class = DocenteForm

    success_url = reverse_lazy('registro_app:listar-docentes')

    

    def form_valid(self, form):
        docente = form.save(commit=False)
        docente.full_name= docente.first_name + ' ' + docente.last_name
        docente.save()
        return super(DocenteCreateView, self).form_valid(form)


#Modificar un Docente

class DocenteUpdateView(UpdateView):
    model = Docente
    template_name = "registro/update.html"
    form_class = DocenteForm




    success_url = reverse_lazy('registro_app:listar-docentes')

    def form_valid(self, form):
        docente = form.save(commit=False)
        docente.full_name= docente.first_name + ' ' + docente.last_name
        docente.save()
        return super(DocenteUpdateView, self).form_valid(form)



#Eliminar un Docente

class DocenteDeleteView(DeleteView):
    model = Docente
    template_name = "registro/delete.html"
    success_url = reverse_lazy('registro_app:listar-docentes')



    #Alta NO Docente




class NoDocenteCreateView(CreateView):
    model = NoDocente
    template_name = "registro/altanodocente.html"
    form_class = NoDocenteForm

    success_url = reverse_lazy('registro_app:listar-nodocentes')

    

    def form_valid(self, form):
        nodocente = form.save(commit=False)
        nodocente.full_name= nodocente.first_name + ' ' + nodocente.last_name
        nodocente.save()
        return super(NoDocenteCreateView, self).form_valid(form)


 #Modificar un NO Docente


class NoDocenteUpdateView(UpdateView):
    model = NoDocente
    template_name = "registro/updatenodocente.html"
    form_class = NoDocenteForm

    success_url = reverse_lazy('registro_app:listar-nodocentes')

    

    def form_valid(self, form):
        nodocente = form.save(commit=False)
        nodocente.full_name= nodocente.first_name + ' ' + nodocente.last_name
        nodocente.save()
        return super(NoDocenteUpdateView, self).form_valid(form)



#Eliminar un NO Docente

class NoDocenteDeleteView(DeleteView):
    model = NoDocente
    template_name = "registro/deletenodocente.html"
    success_url = reverse_lazy('registro_app:listar-nodocentes')


class VistaPrincipal(TemplateView):
    template_name = "index.html"