
# Horus Aizat Exam

## Deskripsi

Repositori ini merupakan aplikasi web **full-stack** yang terdiri dari dua bagian utama:

* **Backend**: Dibangun menggunakan **FastAPI**, terhubung dengan basis data **MySQL**, dan menggunakan **Alembic** untuk migrasi database.
* **Frontend**: Dikembangkan menggunakan **Vite + Vue 3** serta menggunakan **Tailwind CSS** untuk tampilan yang modern dan responsif.

---

## Prasyarat

Pastikan perangkatmu sudah menginstal:

* [Python 3.10+](https://www.python.org/)
* [Node.js (versi LTS)](https://nodejs.org/)
* [MySQL](https://www.mysql.com/)
* [npm](https://www.npmjs.com/) atau [yarn](https://yarnpkg.com/)

---

## Panduan Instalasi dan Menjalankan Aplikasi

### Backend (FastAPI + MySQL + Alembic)

1. Buka terminal dan arahkan ke folder backend:

   ```bash
   cd backend
   ```

2. Buat dan aktifkan virtual environment (opsional, namun disarankan):

   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. Instal semua dependensi Python:

   ```bash
   pip install -r requirements.txt
   ```

4. Rename `.env.example` jadi `.env` , buat nama database mysqlnya `horus_aizat_db` lalu atur koneksi database di file `.env` , misalnya:

   ```
   DATABASE_URL=mysql+pymysql://root:password@localhost/horus_aizat_db
   ```

5. Jalankan migrasi Alembic untuk membuat tabel database:

   ```bash
   alembic upgrade head
   ```

6. Jalankan server FastAPI:

   ```bash
   pyhton run.py
   ```

7. Buka dokumentasi API (Swagger) di browser:

   ```
   http://localhost:8000/docs
   ```

---

### Frontend (Vite + Vue 3 + Tailwind CSS)

1. Buka terminal baru dan masuk ke folder frontend:

   ```bash
   cd frontend
   ```

2. Instal dependensi frontend:

   ```bash
   npm install
   ```

   atau

   ```bash
   yarn install
   ```

3. Jalankan server pengembangan frontend:

   ```bash
   npm run dev
   ```

   atau

   ```bash
   yarn dev
   ```

4. Buka aplikasi di browser melalui alamat:

   ```
   http://localhost:5173
   ```

---
