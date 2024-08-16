from django.db import models

class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=400, default='')
    eliminada = models.BooleanField(default=False)

class SubTarea(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField(max_length=400, default='')
    eliminada = models.BooleanField(default=False)
    tarea_id = models.ForeignKey(Tarea, related_name='subtarea', on_delete=models.CASCADE)



