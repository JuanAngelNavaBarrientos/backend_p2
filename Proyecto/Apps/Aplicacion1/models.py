from django.db import models
import uuid
#Paso 1 se crea la máquna virtual con estos comandos: py -mvenv .\env
#Paso 2 entrar a la carpeta creada: cd env
#Paso 3 entrar a Scripts: cd Scripts
#Paso 4 activar el entorno: .\activate
#Paso 5 instalar todo lo que se necesite: pip install ...
#Paso 6 colocarse a la altura de la carpeta env: cd ..
#Paso 7 iniciar un proyecto django: django-admin startproject Proyecto
#Paso 8 entrar a la carpeta Proyecto: cd Proyecto
#Paso 9 crear una carpeta Apps: md Apps
#Paso 10 entrar en Apps: cd Apps
#Paso 11 iniciar una aplicación: django-admin startapp Aplicacion1
#Paso 12 ir a models.py e ingresar tanto tus librerías (de dónde importas) y tus clases/modelos 
#Paso 13 ir a admin.py y registrar tu(s) modelo(s): from .models import Video
#admin.site.register(Video)
#Paso 14 ir a settings.py para añadir nuestra aplicación en la sección INSTALLED_APPS
#'Apps.Aplicacion1'
#Cerciorarse que en apps.py aparezca de la misma forma.
#Paso 15 colocarse en el mismo nivel que manage.py
#Paso 16 En la terminal: python manage.py migrate para crear por defecto una base de datos db.sqlite3
#Paso 17 para crear el superusuario: python manage.py createsuperuser (juancho,nava.barrientos.juan.angel@gmal.com,123)
#Paso 18 para crear las migraciones  python manage.py makemigrations
#Paso 19 correr el servidor: python manage.py runserver http://127.0.0.1:8000/admin
#Paso 20 para termiar el servidor, ctrl-c o ctrl-break
#Paso 20 para salir de la máquina virtual: 
# Create your models here.
class Video(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    titulo=models.CharField(max_length=100)
    url=models.URLField(max_length=200)
    fecha_carga=models.DateField(auto_now=True)