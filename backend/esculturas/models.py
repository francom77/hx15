# encoding:utf-8
from django.db import models

#la clase escultura guarda un id de la api soportada por nuestra app
class Escultura(models.Model):

    id_api = models.CharField(max_length=60, blank=True)

    def __unicode__(self):

        return self.id_api

#relaciona la id de la api con una de las imagenes que conforman el objeto 360
class Imagen(models.Model):

    id_api = models.ForeignKey(Escultura)
    imagen = models.ImageField(upload_to='360images')

    def __unicode__(self):

        return self.id_api.id_api

