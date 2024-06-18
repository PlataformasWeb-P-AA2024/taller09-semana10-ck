from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30)
    twitter = models.CharField(max_length=30, blank=True)
    campeonatos = models.ManyToManyField('Campeonato', through='CampeonatoEquipos', related_name='equipos_participantes')

    def __str__(self):
        return "%s - %s - %s" % (self.nombre, self.siglas, self.twitter)


class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    posicion = models.CharField(max_length=30)
    numero = models.IntegerField()
    sueldo = models.FloatField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s - %s - %d - %f" % (self.nombre, self.posicion, self.numero, self.sueldo)


class Campeonato(models.Model):
    nombre = models.CharField(max_length=30)
    auspiciante = models.CharField(max_length=30)
    equipos = models.ManyToManyField('Equipo', through='CampeonatoEquipos', related_name='campeonatos_participados')

    def __str__(self):
        return "%s - %s" % (self.nombre, self.auspiciante)


class CampeonatoEquipos(models.Model):
    anio = models.IntegerField()
    equipo = models.ForeignKey(Equipo, related_name='campeonatosequipo', on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, related_name='campeonatosequipo', on_delete=models.CASCADE)

    def __str__(self):
        return "Campeonatos: Campeonato(%s) / Equipo(%s) / año(%d)" % (self.campeonato, self.equipo.nombre, self.anio)
