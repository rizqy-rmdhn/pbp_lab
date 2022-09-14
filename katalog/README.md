Nama: Muhammad Rizqy Ramadhan

NPM: 2106632182

Kelas: PBP - F

Kode Asdos: DRY

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

![bagan_request_response_django drawio](https://user-images.githubusercontent.com/87021641/190053310-3124e853-6d1f-4a38-a2e1-d8bae49013b8.png)

Pada implementasinya, Django menerapkan arsitektur MVT (Model-Views-Template). Arsitektur MVT mempunyai tiga komponen utama, yaitu Model, View, dan Template.

Sebuah View pada arsitektur Django adalah bagian yang akan menangani permintaan dari web dan mengembalikan suatu respons. Respons tersebut bisa berbentuk konten HTML dari suatu situs web, sebuah _redirect_, pesan error 404, sebuah gambar, dan sebagainya. Penerapan View pada Django umumnya dilakukan di berkas views.py Berkas views.py untuk menerapkan bagian View biasanya berbentuk suatu function. 

Model adalah sumber informasi dari data pada web. Model pada Django mengandung _fields_ dan _behaviours_ dari data yang disimpan. Implementasi model pada Django diterapkan pada berkas models.py. Berkas models.py adalah berkas yang berfungsi untuk mendefinisikan tabel database dan relasi diantaranya. 

Sebagai _web framework_, Django membutuhkan suatu cara untuk menghasilkan HTML secara dinamis. Dari hal tersebut, Django menggunakan Template. Suatu template pada Django biasanya mengandung bagian statis dari output HTML yang diinginkan dan juga beberapa syntax spesial untuk membantu menampilkan konten secara dinamis. Implementasi Template pada Django digunakan pada berkas html pada folder template.

Cara kerja penanganan permintaan (_request_) client ke web aplikasi berbasis Django dan responsnya berawal dari client yang mengirimkan HTTP request kepada server. HTTP request tersebut akan diproses oleh urls.py Berkas urls.py akan melakukan _routing_ antara views yang menangani request tersebut dengan suatu URL. Dengan kata lain URL tersebut akan dipetakan kepada views yang sesuai. Selanjutnya, setelah dilakukan routing, request akan diteruskan kepada view yang sesuai di berkas views.py.Berkas views.py adalah berkas yang akan menangani request dari client dan menentukan data apa yang perlu dipakai dari database melalui berkas models.py. Selain itu, berkas view function juga dapat mengupdate data model dari models.py tersebut sesuai request client. Kemudian data tersebut diproses dan berkas views.py akan menentukan apa yang akan ditampilkan pada _display_ atau _interface_ pengguna menggunakan berkas html pada template. Berkas html tersebut juga akan menampilkan konten sesuai view function dan juga dapat membaca data dari function tersebut. Selanjutnya, setelah memproses hal-hal yang telah disebutkan, views.py akan mengirimkan HTTP response berupa tampilan kepada client sesuai request.

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Sebuah virtual environment adalah sebuah Python environment, di mana Python interpreter, libraries, dan scripts yang telah diinstalasi pada virtual environment tersebut, sehingga hal-hal tersebut terisolasi dari virtual environment lain. Alasan kita menggunakan virtual environment adalah untuk membantu kita dalam menjaga ketergantungan (_dependencies_) dari proyek yang berbeda.

Kita tetap dapat membuat suatu aplikasi web berbasis Django tanpa menggunakan virtual environment. Meskipun demikian, hal tersebut tidak mudah untuk dilakukan.

4. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
