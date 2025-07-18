# EduSystem

EduSystem adalah aplikasi manajemen sistem pendidikan berbasis web yang dibuat menggunakan framework **Django**.


## Fitur Utama

- Manajemen pengguna (Dosen, Mahasiswa)

## Teknologi yang Digunakan

- Python 3
- Django
- HTML & CSS (untuk antarmuka)
- PostgresSQL (database)

edusystem/
├── manage.py
├── edusystem/ # Konfigurasi proyek utama
├── core/ # Aplikasi inti
├── mainapp/ # Aplikasi utama (fitur-fitur edukasi)
    ├──templates/ # Folder HTML

## Cara Menjalankan Proyek
1. Jalankan Command prompt
   ```bash
   git clone https://github.com/username/edusystem.git
   cd edusystem/edusystem

2. Buat dan aktifkan virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate     # Untuk Linux/Mac
  venv\Scripts\activate        # Untuk Windows

3. Jalankan migrasi database:
  ```bash
  python manage.py makemigrations
  python manage.py migrate

4. Jalankan server:
  ```bash
  python manage.py runserver

