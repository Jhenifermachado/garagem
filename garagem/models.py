from django.db import models

class Marca(models.Model):

    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome.upper()


class Acessorio(models.Model):

    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao.title()

    class Meta:
        verbose_name_plural = "Acessórios"
        verbose_name = "Acessório"


class Categoria(models.Model):

    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao.title()
    
class Modelo(models.Model):
    nome = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.marca} {self.nome} {self.categoria}"



class Cor(models.Model):

    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao.title()

    class Meta:
        verbose_name_plural = "Cores"





class Veiculo(models.Model):

    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT)
    acessorios = models.ManyToManyField(Acessorio)
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0.0
    )

    def __str__(self):
        return f"{self.modelo.marca} {self.modelo.nome} {self.ano} {self.cor}"

    class Meta:
        verbose_name_plural = "Veículos"
        verbose_name = "Veículo"