Nama: Muhammad Rizqy Ramadhan

NPM: 2106632182

Kelas: PBP - F

Kode Asdos: DRY

Link Heroku: [https://tugas2pbpkiram.herokuapp.com/](https://tugas2pbpkiram.herokuapp.com/katalog/)

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

![bagan_request_response_django drawio](https://user-images.githubusercontent.com/87021641/190053310-3124e853-6d1f-4a38-a2e1-d8bae49013b8.png)

Pada implementasinya, Django menerapkan arsitektur MVT (Model-Views-Template). Arsitektur MVT mempunyai tiga komponen utama, yaitu Model, View, dan Template.

Sebuah View pada arsitektur Django adalah bagian yang akan menangani permintaan dari web dan mengembalikan suatu respons. Respons tersebut bisa berbentuk konten HTML dari suatu situs web, sebuah _redirect_, pesan error 404, sebuah gambar, dan sebagainya. Penerapan View pada Django umumnya dilakukan di berkas views.py Berkas views.py untuk menerapkan bagian View biasanya berbentuk suatu function. 

Model adalah sumber informasi dari data pada web. Model pada Django mengandung _fields_ dan _behaviours_ dari data yang disimpan. Implementasi model pada Django diterapkan pada berkas models.py. Berkas models.py adalah berkas yang berfungsi untuk mendefinisikan tabel database dan relasi diantaranya. 

Sebagai _web framework_, Django membutuhkan suatu cara untuk menghasilkan HTML secara dinamis. Dari hal tersebut, Django menggunakan Template. Suatu template pada Django biasanya mengandung bagian statis dari output HTML yang diinginkan dan juga beberapa syntax spesial untuk membantu menampilkan konten secara dinamis. Implementasi Template pada Django digunakan pada berkas html pada folder template.

Cara kerja penanganan permintaan (_request_) client ke web aplikasi berbasis Django dan responsnya berawal dari client yang mengirimkan HTTP request kepada server. HTTP request tersebut akan diproses oleh urls.py Berkas urls.py akan melakukan _routing_ antara views yang menangani request tersebut dengan suatu URL. Dengan kata lain URL tersebut akan dipetakan kepada views yang sesuai. Selanjutnya, setelah dilakukan routing, request akan diteruskan kepada view yang sesuai di berkas views.py.Berkas views.py adalah berkas yang akan menangani request dari client dan menentukan data apa yang perlu dipakai dari database melalui berkas models.py. Selain itu, berkas view function juga dapat mengupdate data model dari models.py tersebut sesuai request client. Kemudian data tersebut diproses dan berkas views.py akan menentukan apa yang akan ditampilkan pada _display_ atau _interface_ pengguna menggunakan berkas html pada template. Berkas html tersebut juga akan ditampilkan  konten sesuai view function. Selanjutnya, setelah memproses hal-hal yang telah disebutkan, views.py akan mengirimkan HTTP response berupa tampilan kepada client sesuai request.

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Sebuah virtual environment adalah sebuah Python environment, di mana Python interpreter, libraries, dan scripts yang telah diinstalasi pada virtual environment tersebut, sehingga hal-hal tersebut terisolasi dari virtual environment lain. Alasan kita menggunakan virtual environment adalah untuk membantu kita dalam menjaga ketergantungan (_dependencies_) dari proyek yang berbeda. 

Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Meskipun demikian, hal tersebut akan sulit untuk dicapai. Sebagai contoh, selama waktu berlalu, modul dan libraries yang dipakai akan diperbarui atau berubah. Karena kita tidak menggunakan virtual environment, maka hal tersebut tidak diisolasi. Sehingga, setiap kali ada perubahan, kita harus menyesuaikan hal-hal tersebut sesuai perubahan. Hal tersebut dilakukan karena bisa saja aplikasi web yang dibuat tidak _compatible_.

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

  1) Membuat views.py

     Pertama, saya membuat fungsi view berupa show_catalog() pada views.py. Fungsi tersebut menerima HTTP request dari user. Kemudian, fungsi tersebut akan mengambil semua data CatalogItem dari models.py yang tersimpan dalam list_barang. Fungsi tersebut juga menyimpan data untuk ditampilkan melalui katalog.html dalam bentuk dictionary bernama context. Dictionary tersebut menyimpan data CatalogItem tadi, nama saya, dan NPM saya. Kemudian fungsi akan mengembalikan fungsi render untuk me-render katalog.html dengan data yang disebutkan sebelumnya.
     
  2) Routing HTML
 
     Routing HTML dilakukan melalui berkas urls.py. dengan mendaftar URL pattern baru. Hal tersebut dilakukan dengan memanfaatkan fungsi path(). Fungsi tersebut melakukan routing fungsi view yang sesuai kepada URL pattern yang dimasukkan. Dalam hal ini, path('', show_catalog, name='show_catalog') akan melakukan routing fungsi view show_catalog() ke URL pattern .../katalog/.
    
  3) Mapping data ke HTML
  
     Mapping data ke HTML dilakukan di berkas katalog.html dengan memanfaatkan data yang tersimpan pada function view yang sesuai, yaitu show_catalog(). For loop akan melakukan iterasi pada setiap object CatalogItem pada QuerySet yang sudah disimpan pada function view. Kemudian, attribute-attribute dari tiap CatalogItem akan ditampilkan, yaitu item_name, item_price, item_stock, description, rating, dan item_url.
  
  4) Deploy ke Heroku

     Deployment ke Heroku saya lakukan eprtama kali dengan melakukan add, commit, dan push Django project saya untuk menyimpan perubahan-perubahan yang telah saya lakukan ke github. Kemudian, saya membuat aplikasi baru di Heroku. Selanjutnya, saya mencatat API key dan juga nama aplikasi Heroku saya untuk disimpan pada secrets di repository github saya. Kemudian, dpl.yml akan membcara API key dan nama aplikasi Heroku. Setelahnya, workflow akan dijalankan dan deployment akan dilaksanakan. 
