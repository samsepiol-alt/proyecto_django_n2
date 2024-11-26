from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
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
        constraints = [
            models.UniqueConstraint(
                fields=['comuna', 'calle', 'numero', 'piso', 'departamento'],
                name='unique_direccion'
            )
        ]
    
    def __str__(self):
        return f'{self.calle} {self.numero}'



class TipoUsuario(BaseModel):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


#clase base para los usuarios
class Usuario(AbstractUser):
    
    nombre2 = models.CharField(max_length=30, null=False, blank=True)
    apellido2 = models.CharField(max_length=30, null=False, blank=True)
    rut = models.CharField(max_length=10, unique=True, null=False, blank=False)
    direccion = models.ForeignKey(Direccion, on_delete= models.RESTRICT)
    telefono = models.CharField(max_length=11,unique=True, null=False, blank=False)
    email = models.EmailField(max_length=50, unique=True)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.PROTECT)
    updated_at = models.DateTimeField(auto_now=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_set',  # Nombre único para la relación inversa
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permissions_set',  # Nombre único para la relación inversa
        blank=True
    )
    




class InmuebleTipo(BaseModel):
    nombre = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nombre


class Inmueble(BaseModel):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    m2_construidos = models.PositiveIntegerField()
    m2_totales = models.PositiveIntegerField()
    nro_est = models.PositiveIntegerField()
    nro_hab = models.PositiveIntegerField()
    nro_wc = models.PositiveIntegerField()
    direccion = models.OneToOneField(Direccion, on_delete=models.PROTECT)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT)
    arrendador = models.ForeignKey(Usuario, related_name='anfitrion', on_delete=models.PROTECT)
    arrendatario = models.ForeignKey(Usuario, related_name='visitante', on_delete=models.PROTECT)
    fecha = models.DateTimeField(null = False)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    tipo_inmueble = models.ForeignKey(InmuebleTipo, on_delete=models.PROTECT)
    propietario = models.ForeignKey(Usuario, related_name="propietario", on_delete=models.PROTECT)
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


