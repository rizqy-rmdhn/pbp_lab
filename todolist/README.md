# To Do List
Nama: Muhammad Rizqy Ramadhan

NPM: 2106632182

Kelas: PBP-F

Kode Asdos: DRY

Deployment link : [https://tugas2pbpkiram.herokuapp.com/todolist](https://tugas2pbpkiram.herokuapp.com/todolist)

## Tugas 4

### Kegunaan CSRF Token

CSRF token atau {% csrf_token %} memiliki fungsi sebagai pelindung user dari ancaman _Cross Site Request Forgery_ atau pemalsuan request. _Cross Site Request Forgery_ merupakan suatu ancaman di mana pelaku akan membuat korban melakukan proses request yang bisa jadi tidak diinginkan kepada suatu website. Cara kerja hal tersebut adalah dengan menambahkan token pada setiap request yang dikirim user dan dilakukan pengecekan. Contoh kasus CSRF misalnya, pada suatu website user secara tidak sengaja mengklik sebuah hyperlink dengan alamat "http&#65279;://bankpalsu.com/transfer.do?acct=PelakuA&jumlah=100" untuk mentransfer 100 USD ke PelakuA. Tanpa adanya perlindungan CSRF, ketika user mengklik link tersebut, maka request user akan diproses dan uang akan ditransfer. Sehingga, jika tidak ada CSRF token atau {% csrf_token %} pada elemen '\<form>', maka website berpotensi mengalami ancaman CSRF.

### Pembuatan Form secara Manual
  
Form dapat dibuat secara manual tanpa menggunakan generator seperti {{ form.as_table }}. Generator {{ form.as_table }} atau generator lainnya pada dasarnya akan merender form secara otomatis sesuai dengan tagnya. Untuk {{ form.as_table }} akan merender form sebagai tabel dengan tag <tr>.
  
Untuk membuat form dapat dibuat secara manual memanfaatkan tag <input> yang kemudian diisi dengan parameter/attribute "name" dan "type" sesuai kebutuhan. Parameter type akan menentukan tipe input/form yang ditampilkan, sedangkan parameter name akan membuat nama form tersebut. Contoh penggunaannya adalah \<input type="text" id="fname" name="fname">. Kita juga dapat memanfaatkan tag \<form> untuk menandakan elemen-elemen form yang berisikan berbagai input. Contohnya
  
\<form>
  \<label for="fname">First name:</label><br>
  \<input type="text" id="fname" name="fname"><br>
  \<label for="lname">Last name:</label><br>
  \<input type="text" id="lname" name="lname">
\</form>

### Penjelasan Alur Submisi Data dari Form
  
1. User memasukkan data pada form melalui input dan mengklik submit
2. Form tersebut akan mengirim data melalui request POST atau GET sesuai setting form. Namun, pada umumnya adalah request POST.
3. Fungsi views yang sesuai pada server akan memproses input tersebut sesuai dengan input dan parameter. 
4. Sesuai fungsi views yang memproses, sebuah object akan dibuat dengan attribute sesuai input dari user. 
5. Object tersebut akan disimpan melalui method ".save()" atau dapat disave/create dengan method Model.objects.create() dengan parameter yang sesuai. 
6. Untuk mengakses data object yang telah disimpan tadi dapat melalui method Model.objects.all() atau jika ingin menampilkan sesuai filter (dalam tugas ini adalah user) dapat memanfaatkan method Model.objects.filter(user=request.user) 
7. Data tersebut diassign dalam dictionary bernama context, 
8. Fungsi views akan mengirim context ke file HTML melalui fungsi render()
9. Data dapat diakses sebagai variabel di template HTML

### Proses Pengerjaan
  
1. Memanfaatkan repositori tugas PBP yang sudah tersedia, membuka project dan aktivasi venv.
2. Membuat app baru bernama todolist dengan command python manage.py startapp todolist
3. Menambahkan app baru ke dalam INSTALLED_APPS pada settings.py pada folder project kita, yaitu folder project_django
4. Membuat file urls.py pada folder todolist yang nantinya akan berisikan routing dari view app todolist
5. Melakukan routing todolist ke `project_django/urls.py` dengan menambahkan path('todolist/', include('todolist.urls')) pada urlpatterns di urls.py folder project_django
6. Membuat model Task pada models.py dengan attribute sesuai ketentuan, yaitu user, date, title, description, dan is_finished. Attribute user merupakan attribute foreignkey.
7. Buat views sesuai kebutuhan yaitu untuk kegiatan register, login, logout, halaman utama, membuat task, mengupdate task, dan mendelete task. 
8. Membuat file .html pada folder template di app todolist sesuai views dan kebutuhan. 
9. Menambahkan routing views dari todolist ke todolist/urls.py pada urlpattern dengan bantuan path().  
10. Push repository ke github dan melakukan deploy ke Heroku 
11. Melakukan CreateSuperUser untuk membuat akun admin dan menambahkan data dummy. 

## Tugas 5
  
### Perbedaan, kelebihan, dan kekurangan dari inline, internal, dan external CSS
  
  1. Inline CSS adalah cara penggunaan CSS dengan properti dan attribute CSS berada dalam tag HTML dalam satu baru (inline). Implementasi setiap tag akan berbeda pada tiap HTML. 
- Kelebihannya adalah prioritasnya utama. Sangat efisien untuk pembuatan style sebab berkas CSS tidak perlu dibuat atau ditulis dalam berkas HTML.
- Kekurangannya akan mengurangi readability dan tidak cocok untuk style elemen yang berulang. 

2. Internal CSS merupakan implementasi CSS dengan cara mengumpulkan properti dan attribute CSS di dalam berkas HTML, tepatnya pada head HTML. Setiap berkas HTML akan memiliki style yang berbeda. 
- Kelebihannya merupakan readability lebih bagus dari inline CSS dan cocok untuk mengubah banyak elemen pada suatu halaman HTML yang berbeda dengan halaman lain. Kemudian, tidak perlu membuat berkas CSS. 
- Kekurangannya adalah prioritas di bawah inline CSS. Lebih lanjut lagi, bagian head HTML akan penuh dengan properti CSS, sehingga dapat mengurangi readability dan kemudahan akses berkas HTML.

3. External CSS merupkan implementasi CSS dengan pembuatan berkas CSS terpisah  yang properti dan attrbute CSS serta tag HTML. Berkas CSS perlu disematkan pada berkas HTML memanfaatkan tag <link>. Setiap tag HTML dapat dikustomisasi sekali pada seluruh berkas HTML yang menyematkan berkas CSS yang sama.
- Kelebihannya adalah readability sangat bagus sebab pendefinisian style pada berkas yang berbeda. Selanjutnya, jika beberapa page HTML memanfaatkan style yang sama, maka sangat efisien untuk menggunakan external CSS.
- Kekurangannya, di sisi lain, prioritasnya paling rendah dan penulisan kode perlu memerhatikan dua berkas.
 
### Tag HTML5
  - <#html>: Mendefine root file HTML
- <#body>: Mendefine bagian body file HTML
- <#head>: Mendefine bagian head file HTML
- <#header>: Mendefine bagian header file HTML
- <#footer>: Mendefine footer pada sebuah dokumen HTML
- <#div>: Mendefine sebuah divisi pada dokumen HTML
- <#nav>: Mendefine link navigasi
- <#style>: Mendefine style HTML di Head dokumen HTML
- <#title> Mendefine judul dokumen HTML
- <#h1> sampai <#h6>: Menampilkan header HTML (memiliki ukuran huruf yang berbeda, <#h1> memiliki huruf terbesar)
- <#a>: Mendefine Hyperlink
- <#b>: Menampilkan teks bold
- <#p>: Menampilkan paragraf
- <#hr>: Membuat garis mendatar atau horizontal
- <#textare>: Mendefine multi-line input text
- <#iframe>: Menampilkan url dalam inline frame
- <#img>: Menampilkan gambar pada file HTML
- <#label>: Mendefine label untuk kontrol input
- <#table>: Mendefine table
- <#td>: Mendefine cell dalam table
- <#th>: Mendefine cell teratas pada table
- <##button>: Membuat tombol pada file HTML
- <#ul>: Mendefine daftar yang tidak berurutan
- <#object>: Mendefine sebuah object pada file HTML
- <#caption>: Mendefine caption atau judul suatu tabel
- <#form>: Mendefine form HTML pada dokumen HTML
- <#embed>: Memasukkan aplikasi eksternal ke dalam dokumen HTML
- <#audio>: Memasukkan audio ke dalam file HTML
- <#video>: Memasukkan video ke dalam dokumen HTML
- <#code>: Mendefine teks sebagai code pemrograman
- <#script>: Tempat menaruh script pada dokumen HTML
  
### Tipe CSS Selector
  
1. Simple selector adalah selector sederhana yang memilih elemen berdasarkan nama, id, atau class pada dokumen HTML. Jenis-jenisnya terdapat tiga buah: id selector, element selector, dan class selector
  a. id selector merupakan selector yang memanfaatkan id di tag HTML sehingga perlu didefinisikan 
  b. Element selector merupakan selector yang memanfaatkan tag HTML
  c. Class selector merupakan selector dengan memanfaatkan class pada tag HTML sehingga perlu didefinisikan terlebih dahulu
  
2. Combinator selector merupakan selector yang memilih kombinasi/kumpulan elemen menurut hubungannya. Jenis-jenisnya terdapat empat jenis, yaitu descendant selector, child selector, adjacent sibling selector, general sibling selector.
  
  a. Descendant selector adalah selector yang memilih semua elemen turunan (descendant) dari suatu elemen tertentu.
  b. Child selector adalah selector yang memilih semua elemen child dari suatu elemen tertentu
  c. Adjacent sibling selector adalah selector yang memilih semua elemen yang posisinya berada setelah suatu elemen dengan parent yang sama.
  d. General sibling selector adalah selector yang memilih semua elemen sibling berikutnya dari elemen tertentu
  
3. Pseudo-class selector merupakan selector dengan pemilihan elemen menurut suatu keadaan. Terdapat tujuh jenis pseudo-class selector
  a. :active adalah pemilih semua elemen yang aktif
  b. :checked adalah pemilih semua elemen yang telah dicentang
  c. :disabled adalah pemilih semua elemen yang dinonaktifkan (disabled)
  d. :enabled adalah pemilih semua elemen yang diaktifkan (enabled)
  e. :link adala pemilih semua link yang belum terkunjungi
  f. :hover adalah pemilih semua elemen dengan kursor di atasnya
  g. :visited -adalah pemilih link yang terkunjungi
  
4. Atribute selector merupakan pemilih elemen menurut nama atributnya atau nilai atributnya

### Proses Pengerjaan
  - Mengkustomisasi tampilan page login, register, todolist, dan create_task dengan menggunakan CSS dan bantuan framework Bootstrap
- Objects Task yang ditampilkan tidak menjadi table, tetapi dalam bentuk Card untuk setiap task.
- Membuat page login, register, todolist, dan create_task menjadi responsive sehingga tampilan web tidak rusak ketika digunakan pada device yang berbeda.
