from django import forms 
from .models import Docente 
from .models import NoDocente 



class DocenteForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Docente
        fields = (
            
            'last_name',
            'first_name',
            'age',
            'course',  
            'avatar',
            
        )

     

class NoDocenteForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = NoDocente
        fields = (
            
            'last_name',
            'first_name',
            'age',
            'office',
            'avatar',
        )

       