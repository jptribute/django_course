from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfoPerfil (models.Model):
    user = models.OneToOneField (User, on_delete=models.CASCADE) #La relacion UNO-A-UNO con User

    #clases adicionales

    sitio_de_portafolio = models.URLField(blank = True) #blank = True es del optional parameter
    foto_perfil = models.ImageField(upload_to = "profile_pics", blank = True )

    def __str__(self):
        return self.user.username
