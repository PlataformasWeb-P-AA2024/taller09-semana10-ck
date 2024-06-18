from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    siglas = models.CharField(max_length=30, blank=True)
    twitter = models.CharField(max_length=30, blank=True)
    campeonato = models.ManyToManyField('Campeonato', through='CampeonatoEquipos')
  # el campo puede
                                                            # ser vacio
    def __str__(self):
        return "%s - %s - %s" % (self.nombre,
                self.siglas,
                self.twitter)


class Jugador(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    posicion = models.CharField(max_length=30, unique=True)
    numero = models.IntegerField(max_length=30, unique=True)
    sueldo = models.FloatField(max_length=30, unique=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s - %s - %d - %f" % (self.nombre,
                self.posicion,
                self.numero,
                self.sueldo)
    

class Campeonato(models.Model):
    nombre = models.CharField(max_length=30, unique=True)
    auspiciante = models.CharField(max_length=30, blank=True)
    equipos = models.ManyToManyField('Equipo', through='CampeonatoEquipos')

                                                                # ser vacio
    def __str__(self):
        return "%s - %s" % (self.nombre,
                self.auspiciante)


class CampeonatoEquipos(models.Model):
    """
    """
    anio = models.CharField(max_length=30, unique=True)
    equipo = models.ForeignKey(Equipo, related_name='campeonatosequipo',
            on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, related_name='campeonatosequipo',
            on_delete=models.CASCADE)

    def __str__(self):
        return "Campeonatos: Campeoanto(%s) - Equipo(%s)" % \
                (self.campeonato, self.equipo.nombre)

