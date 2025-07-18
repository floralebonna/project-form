from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('mahasiswa', 'Mahasiswa'),
        ('dosen', 'Dosen'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"
    
class Materi(models.Model):
    judul = models.CharField(max_length=100)
    file = models.FileField(upload_to='materi/')
    upload_by = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'dosen'})
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul

class Absensi(models.Model):
    mahasiswa = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'mahasiswa'})
    tanggal = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.mahasiswa.username} - {self.tanggal} - {'Hadir' if self.status else 'Tidak Hadir'}"

class Tugas(models.Model):
    mahasiswa = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'mahasiswa'})
    file = models.FileField(upload_to='tugas/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tugas oleh {self.mahasiswa.username} pada {self.uploaded_at.strftime('%Y-%m-%d')}"