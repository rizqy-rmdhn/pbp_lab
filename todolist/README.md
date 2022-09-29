# To Do List
Nama: Muhammad Rizqy Ramadhan

NPM: 2106632182

Kelas: PBP-F

Kode Asdos: DRY

Deployment link : [https://tugas2pbpkiram.herokuapp.com/todolist](https://tugas2pbpkiram.herokuapp.com/todolist)

## Kegunaan CSRF Token

CSRF token atau {% csrf_token %} memiliki fungsi sebagai pelindung user dari ancaman _Cross Site Request Forgery_ atau pemalsuan request. _Cross Site Request Forgery_ merupakan suatu ancaman di mana pelaku akan membuat korban melakukan proses request yang bisa jadi tidak diinginkan kepada suatu website. Cara kerja hal tersebut adalah dengan menambahkan token pada setiap request yang dikirim user dan dilakukan pengecekan. Contoh kasus CSRF misalnya, pada suatu website user secara tidak sengaja mengklik sebuah hyperlink dengan alamat "http&#65279;://bankpalsu.com/transfer.do?acct=PelakuA&jumlah=100" untuk mentransfer 100 USD ke PelakuA. Tanpa adanya perlindungan CSRF, ketika user mengklik link tersebut, maka request user akan diproses dan uang akan ditransfer. Sehingga, jika tidak ada CSRF token atau {% csrf_token %} pada elemen '\<form>', maka website berpotensi mengalami ancaman CSRF.

## Pembuatan Form secara Manual
  
Form dapat dibuat secara manual tanpa menggunakan generator seperti {{ form.as_table }}. Generator {{ form.as_table }} atau generator lainnya pada dasarnya akan merender form secara otomatis sesuai dengan tagnya. Untuk {{ form.as_table }} akan merender form sebagai tabel dengan tag <tr>.
  
Untuk membuat form dapat dibuat secara manual memanfaatkan tag <input> yang kemudian diisi dengan parameter/attribute "name" dan "type" sesuai kebutuhan. Parameter type akan menentukan tipe input/form yang ditampilkan, sedangkan parameter name akan membuat nama form tersebut. Contoh penggunaannya adalah \<input type="text" id="fname" name="fname">. Kita juga dapat memanfaatkan tag \<form> untuk menandakan elemen-elemen form yang berisikan berbagai input. Contohnya
  
\<form>
  \<label for="fname">First name:</label><br>
  \<input type="text" id="fname" name="fname"><br>
  \<label for="lname">Last name:</label><br>
  \<input type="text" id="lname" name="lname">
\</form>

## Penjelasan Alur Submisi Data dari Form
  
1. User memasukkan data pada form melalui input dan mengklik submit
2. Form tersebut akan mengirim data melalui request POST atau GET sesuai setting form. Namun, pada umumnya adalah request POST.
3. Fungsi views yang sesuai pada server akan memproses input tersebut sesuai dengan input dan parameter. 
4. Sesuai fungsi views yang memproses, sebuah object akan dibuat dengan attribute sesuai input dari user. 
5. Object tersebut akan disimpan melalui method ".save()" atau dapat disave/create dengan method Model.objects.create() dengan parameter yang sesuai. 
6. Untuk mengakses data object yang telah disimpan tadi dapat melalui method Model.objects.all() atau jika ingin menampilkan sesuai filter (dalam tugas ini adalah user) dapat memanfaatkan method Model.objects.filter(user=request.user) 
7. Data tersebut diassign dalam dictionary bernama context, 
8. Fungsi views akan mengirim context ke file HTML melalui fungsi render()
9. Data dapat diakses sebagai variabel di template HTML

## Proses Pengerjaan
  
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
