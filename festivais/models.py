from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome


class Localizacao(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome


class Festival(models.Model):
    nome = models.CharField(max_length=40)
    bandas = models.ManyToManyField(Banda,related_name="bandas")
    localizacao = models.ForeignKey('Localizacao', on_delete=models.CASCADE, null=True, default=None,related_name="localizacao")
    image = models.ImageField(upload_to='festivais/images', null=True, blank=True)

    def __str__(self):
        return self.nome
