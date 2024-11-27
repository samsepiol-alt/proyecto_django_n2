import json
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from inmobiliaria.models import Region, Comuna, Direccion, TipoUsuario, InmuebleTipo, Inmueble, Perfil
from datetime import datetime
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Importar datos dummy en la base de datos"



    def handle(self, *args, **kwargs):
        # Abrir el archivo JSON
        with open('requerimientos/datos_dummy.json', 'r') as file:
            data = json.load(file)
        
        #crear regiones
        for region_data in data['regiones']:
            region, created = Region.objects.get_or_create(
                id=region_data['id'],
                nombre=region_data['nombre']
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Región "{region.nombre}" creada.'))
        # crear comunas
        for comuna_data in data['comunas']:
            comuna, created = Comuna.objects.get_or_create(
                id=comuna_data['id'],
                nombre=comuna_data['nombre'],
                region_id=comuna_data['region_id']
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Comuna "{comuna.nombre}" creada.'))

        # crear direcciones
        for direccion_data in data['direcciones']:
            direccion, created = Direccion.objects.get_or_create(
                id=direccion_data['id'],
                comuna_id=direccion_data['comuna_id'],
                calle=direccion_data['calle'],
                numero=direccion_data['numero'],
                piso= direccion_data.get('piso', None),
                departamento=direccion_data.get('departamento',None ) 
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Dirección "{direccion}" creada.'))

        # crear tipos de usuario
        for tipo_usuario_data in data['tipos_usuario']:
            tipo_usuario, created = TipoUsuario.objects.get_or_create(
                id=tipo_usuario_data['id'],
                nombre=tipo_usuario_data['nombre']
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Tipo de usuario "{tipo_usuario.nombre}" creado.'))

        # crear usuarios
        for usuario_data in data['usuarios']:
            usuario, created = User.objects.get_or_create(
                username=usuario_data['username'],
                password = make_password("python2024"),
                first_name=usuario_data['first_name'],
                last_name=usuario_data['last_name']
            )
            if created:
            
                usr = User.objects.get(id=usuario.id)
                self.stdout.write(self.style.SUCCESS(f'Usuario "{usuario.username}" creado.'))
            perfil, created = Perfil.objects.get_or_create(
                usuario = usr,
                nombre2=usuario_data['nombre2'],
                apellido2=usuario_data['apellido2'],
                rut=usuario_data['rut'],
                direccion_id=usuario_data['direccion_id'],
                telefono=usuario_data['telefono'],
                email=usuario_data['email'],
                tipo_usuario_id=usuario_data['tipo_usuario_id']
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Perfil del Usuario "{usuario.username}" creado.'))



        #crear tipos de inmueble
        for tipo_inmueble_data in data['tipos_inmueble']:
            tipo_inmueble, created = InmuebleTipo.objects.get_or_create(
                id=tipo_inmueble_data['id'],
                nombre=tipo_inmueble_data['nombre']
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Tipo de inmueble "{tipo_inmueble.nombre}" creado.'))


        # crear inmuebles
        for inmueble_data in data['inmuebles']:
            inmueble, created = Inmueble.objects.get_or_create(
                id=inmueble_data['id'],
                nombre=inmueble_data['nombre'],
                descripcion=inmueble_data['descripcion'],
                m2_construidos=inmueble_data['m2_construidos'],
                m2_totales=inmueble_data['m2_totales'],
                nro_est=inmueble_data['nro_est'],
                nro_hab=inmueble_data['nro_hab'],
                nro_wc=inmueble_data['nro_wc'],
                direccion_id=inmueble_data['direccion_id'],
                comuna_id=inmueble_data['comuna_id'],
                arrendatario_id=inmueble_data['arrendatario_id'],
                fecha=inmueble_data['fecha'],
                precio=inmueble_data['precio'],
                tipo_inmueble_id=inmueble_data['tipo_inmueble_id'],
                propietario_id=inmueble_data['propietario_id'],
                is_disponible=inmueble_data['is_disponible']
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Inmueble "{inmueble.nombre}" creado.'))
        


        # crear superusuario
        nuevo_usuario = Usuario(
            username='admin',  
            first_name='Juan',
            last_name='Perez',
            email='sysadmin@mail.com',  
            is_staff =True,
            is_superuser = True
        )

        #generar una contraseña
        psw = make_password("python2024")
        nuevo_usuario.set_password(psw)  
        
        nuevo_usuario.save()


        self.stdout.write(self.style.SUCCESS("superusuario creado y guardado correctamente."))

        self.stdout.write(self.style.SUCCESS('Datos dummy importados exitosamente.'))
