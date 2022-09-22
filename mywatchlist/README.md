# My Watchlist
Nama: Muhammad Rizqy Ramadhan

NPM: 2106632182

Kelas: PBP-F

Kode Asdos: DRY

Deployment link : [https://tugas2pbpkiram.herokuapp.com/mywatchlist](https://tugas2pbpkiram.herokuapp.com/mywatchlist)

# Perbedaan JSON, XML, dan HTML
* JSON atau JavaScript Object Notation merupakan suatu format yang menggunakan teks yang mudah dibaca manusia untuk menyimpan dan mentransmit data. Data tersebut berisikan attribute yang tersusun dalam pasangan key dan value. 
* XML atau Extensible Markup Language merupakan suatu bahasa markup yang berfungsi untuk menyimpan dan mengirim data. XML menggunakan tag juga seperti HTML, tetapi bukan tag yang sudah didefinisikan sebelumnya seperti HTML. 
* HTML atau HyperText Markup Language adalah suatu bahasa markup yang memanfaatkan tanda-tanda (_tag_) untuk menyatakan kode-kode agar halaman tersebut dapat ditampilkan. Meskipun demikian, HTML dapat dilakukan untuk penyajian data web. 

# Alasan diperlukan data delivery dalam pengimplementasian platform
Pada suatu aplikasi web, client berkomunikasi dengan server. Client akan melakukan request kepada server dan server akan mengirimkan respons sebagai balasan. Dalam pengiriman response tersebut terjadi pengiriman data dari server ke client. Hal tersebut didasarkan karena client ingin menampilkan tampilan dengan data yang sesuai. Format pengiriman data tersebut dapat berupa HTML, JSON, dan XML. 

# Langkah-langkah implementasi
1. Pertama masuk ke dalam project yang sama dengan sebelumnya. Kemudian masuk ke dalam venv dan melakukan perintah "python manage.py startapp mywatchlist" untuk membuat app mywatchlist. Lalu menambahkan mywatchlist ke dalam INSTALLED_APPS pada berkas settings.py
2. Pembuatan model baru pada models.py pada app mywatchlist, yaitu MyWatchList dengan field watched, title, rating, release_date, dan review sesuai ketentuan.
3. Lalu membuat 10 data untuk objek MyWatchList melalui fixtures, initial_mywatchlist_data.json
4. Kemudian membuat views yang bersesuaian, yaitu menyajikan data dalam HTML, JSON, dan XML sesuai request client.
5. Berikutnya membuat urls.py di app mywatchlist dan menambahkan urlpatterns sebagai berikut.
  urlpatterns = [
    path('html/', show_mywatchlist_html, name='show_mywatchlist_html'),
    path('xml/', show_mywatchlist_xml, name='show_mywatchlist_xml'),
    path('json/', show_mywatchlist_json, name='show_mywatchlist_json'),
    path('json/<int:id>', show_mywatchlist_json_by_id, name='show_mywatchlist_json_by_id'),
    path('xml/<int:id>', show_mywatchlist_xml_by_id, name='show_mywatchlist_xml_by_id'),
    ]
6. Selanjutnya menambahkan "path('mywatchlist/', include('mywatchlist.urls'))" pada urls.py di project repository, yaitu django_project. Tujuannya adalah melakukan routing url di mywatchlist kepada view yang bersesuaian.
7. Mengubah Procfile untuk melakukan loaddata objek MyWatchList dan melakukan deploy ke Heroku

# Screenshots Postman
1. HTML
![image](https://user-images.githubusercontent.com/87021641/191641391-23f0b854-e5bb-4811-85a1-14930774f688.png)


2. JSON
![image](https://user-images.githubusercontent.com/87021641/191641430-18005879-b75c-44bd-9d45-4108ce5a5f63.png)


3. XML
![image](https://user-images.githubusercontent.com/87021641/191641464-7679176b-eb7a-4978-9aa0-8db7d7140166.png)
