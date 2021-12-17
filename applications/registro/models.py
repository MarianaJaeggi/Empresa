from django.db import models

# Create your models here.

class Docente(models.Model):
    """Model definition for Empleado."""

    Materia = (

        ('Lengua','Lengua'),
        ('Programación','Programación'),
        ('Matemáticas','Matemáticas'),
        ('Práctica','Práctica'),
        ('Sistemas','Sistemas'),
        ('Base de datos','Base de datos'),
        ('Modelado','Modelado'),
        ('Arquitectura','Arquitectura'),
        ('Redes','Redes'),
    )

    last_name = models.CharField("Apellido", max_length=50)
    first_name = models.CharField("Nombres", max_length=50)
    full_name = models.CharField('Nombre completo',max_length=150, blank = True)
    age = models.IntegerField("Edad")
    course = models.CharField("Materia", max_length=50, choices=Materia)
    avatar = models.ImageField('Imagen', upload_to='registro', height_field=None, width_field=None, max_length=None, blank = True)
    

    #Imagen de perfil

    class Meta:
        """Meta definition for Empleado."""

        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        ordering = ['last_name','first_name']

    def _str_(self):

        """Unicode representation of Empleado."""
        return self.last_name + ', ' + self.first_name
 

class NoDocente(models.Model):
    """Model definition for Empleado."""

    Oficina= (

        ('Finanzas','Finanzas'),
        ('RRHH','RRHH'),
        ('Comercial','Comercial'),
        ('Marketing','Marketing'),
        ('Soporte','Soporte'),
        ('Administración','Administración'),
        ('Contabilidad','Contabilidad'),
        ('Mantenimiento','Mantenimiento'),
        ('Gestión','Gestión'),
    )

    last_name = models.CharField("Apellido", max_length=50)
    first_name = models.CharField("Nombres", max_length=50)
    full_name = models.CharField('Nombre completo',max_length=150, blank = True)
    age = models.IntegerField("Edad")
    office = models.CharField("Oficina", max_length=50, choices = Oficina)
    avatar = models.ImageField('Imagen', upload_to='registro', height_field=None, width_field=None, max_length=None, blank = True)

    #Imagen de perfil

    class Meta:
        """Meta definition for Empleado."""

        verbose_name = 'No Docente'
        verbose_name_plural = 'No Docentes'
        ordering = ['last_name','first_name']

    def _str_(self):
        """Unicode representation of Empleado."""
        return self.last_name + ', ' + self.first_name
       
