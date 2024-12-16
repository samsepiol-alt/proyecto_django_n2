from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User
#MANAGER PARA LA CLASE BASE

class ModelManager(models.Manager):
    #sobrecargar metodo para obtener objetos que esten activos
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class AllModelManager(models.Manager):
    #devuelve el metodo heredado sin modificar
    def get_queryset(self):
        return super().get_queryset()


#clase base para los modelos
class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ModelManager()
    class Meta:
        abstract = True



#Entidades mas fuertes que usuario

class Region(BaseModel):
    nombre = models.CharField(max_length=50, null=False, blank=False, unique=True)
    class Meta:
        verbose_name_plural ="Regiones"
    def __str__(self):
        return self.nombre


class Comuna(BaseModel):
    nombre = models.CharField(max_length=50, null=False, blank=False, unique=True)
    region = models.ForeignKey(Region, on_delete = models.RESTRICT)

    def __str__(self):
        return self.nombre

class Direccion(BaseModel):
    comuna = models.ForeignKey(Comuna, on_delete = models.RESTRICT)
    calle = models.CharField(max_length=100, null=False, blank=False)
    numero = models.CharField(max_length=8,null=False, blank=False)
    piso = models.IntegerField(null=True, blank=True)
    departamento = models.CharField(max_length=6,null=True, blank=True)
    class Meta:
        verbose_name_plural ="Direcciones"
        constraints = [
            models.UniqueConstraint(
                fields=['comuna', 'calle', 'numero', 'piso', 'departamento'],
                name='unique_direccion'
            )
        ]
    
    def __str__(self):
        return f'{self.calle} {self.numero}'




class Perfil(BaseModel):
    TIPO_CHOICE = (('landlord','Arrendador'),('tenant','Arrendatario'))
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    nombre2 = models.CharField(max_length=30, null=False, blank=True)
    apellido2 = models.CharField(max_length=30, null=False, blank=True)
    rut = models.CharField(max_length=10, unique=True, null=False, blank=False)
    direccion = models.ForeignKey(Direccion, on_delete= models.PROTECT)
    telefono = models.CharField(max_length=11,unique=True, null=False, blank=False)
    email = models.EmailField(max_length=50, unique=True)
    tipo_usuario = models.CharField(max_length=10, choices = TIPO_CHOICE, default="arrendatario")

    class Meta:
        verbose_name_plural ="Perfiles"


class Inmueble(BaseModel):
    TIPO_CHOICE =(('house','Casa'),('department','Departamento'),('plot','Parcela'))
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    m2_construidos = models.PositiveIntegerField()
    m2_totales = models.PositiveIntegerField()
    nro_est = models.PositiveIntegerField()
    nro_hab = models.PositiveIntegerField()
    nro_wc = models.PositiveIntegerField()
    direccion = models.OneToOneField(Direccion, on_delete=models.PROTECT)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    tipo_inmueble = models.CharField(max_length=20, choices=TIPO_CHOICE, default="Casa")
    propietario = models.ForeignKey(User, related_name="propietario", on_delete=models.PROTECT)
    is_disponible = models.BooleanField(default = True)
    #manager extra para modulo de administracion
    all_objects = AllModelManager()
    #definir el manager base para usarse en admin
    base_manager_name = "all_objects"


    def __str__(self):
        return self.nombre


class Foto(BaseModel):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    url = models.URLField(blank = False, null=False)


