Nama: Muhammad Rizqy Ramadhan
NPM: 2106632182
Kelas: PBP - F
Kode Asdos: DRY

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
![bagan_request_response_django drawio](https://user-images.githubusercontent.com/87021641/190053310-3124e853-6d1f-4a38-a2e1-d8bae49013b8.png)
Pada implementasinya, Django menerapkan arsitektur MVT (Model-Views-Template)
urls.py 
views.py adalah file yang akan menangani request dari client dan menentukan data apa yang perlu dipakai dari database. Kemudian data tersebut diproses dan file views.py akan menentukan apa yang akan ditampilkan pada _display_ atau _interface_ pengguna menggunakan file html pada template.
(kalo ada), terus nentuin apa yang
mau ditampilin di views
models.py adalah file yang berfungsi untuk mendefinisikan tabel database dan relasi diantaranya. Setiap model yang didefinisikan memiliki attribute.
berkas html

3. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
4. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
