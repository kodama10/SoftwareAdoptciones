from django.db import models

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    especie = models.CharField(max_length=50, choices=[('perro', 'Perro'), ('gato', 'Gato')])
    raza = models.CharField(max_length=100)
    estado_salud = models.TextField()
    comportamiento = models.TextField()
    foto = models.ImageField(upload_to='fotos_animales/')
    disponible = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

class SolicitudAdopcion(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    nombre_adoptante = models.CharField(max_length=100)
    email_adoptante = models.EmailField()
    telefono_adoptante = models.CharField(max_length=20)
    direccion = models.TextField()
    estado = models.CharField(
        max_length=20,
        choices=[('en revisión', 'En Revisión'), ('aprobada', 'Aprobada'), ('rechazada', 'Rechazada')],
        default='en revisión'
    )
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud de {self.nombre_adoptante} para {self.animal.nombre}"
