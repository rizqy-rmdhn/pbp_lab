# To Do List
Nama: Muhammad Rizqy Ramadhan

NPM: 2106632182

Kelas: PBP-F

Kode Asdos: DRY

Deployment link : [https://tugas2pbpkiram.herokuapp.com/todolist](https://tugas2pbpkiram.herokuapp.com/todolist)

## Tugas 6

##  Perbedaan _asynchronous programming_ dengan _synchronous programming_.

### Asynchronous programming

Sesuai namanya, program akan berjalan asinkronus. Dengan kata lain, program akan berjalan secara tidak urut. Dalam kasus ini, program akan berjalan secara bersamaan atau paralel tanpa menunggu program sebelumnya diselesaikan.

### Synchronous programming

Sesuai namanya, program akan berjalan sinkronus. Dengan kata lain, program akan berjalan secara terurut. Hal ini menyebabkan tidak ada program yang berjalan secara pararel (bersamaan). Program sebelumnya akan diselesaikan terlebih dahulu sebelum menjalankan program selanjutnya.


## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma _Event-Driven Programming_. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

_Event-Driven Programming_ merupakan paradigma proraman yang mengimplementasikan _event_ sebagai penentu alur kerja program. _Event_ tersebut berbeda-beda dan tergantung user.

Contoh penerapannya pada Tugas 6 adalah ketika user melakukan _event_ klik _button_ _udpate_ atau _delete_, yang mana function AJAX yang sesuai akan dieksekusi.

##   Jelaskan penerapan <i>asynchronous programming</i> pada AJAX.

AJAX menerapkan _asynchronous programming_ contohnya melalui XMLHttpRequest. Hal tersebut akan membuat web server menukar data yang terjadi secara paralel. Akibatnya setelah server selesai mengirim respons, data akan langsung tampil pada layar.

##   Jelaskan bagaimana cara kamu mengimplementasikan <i>checklist</i> di atas.

### AJAX GET

1. Membuat view baru get_json(request) yang akan mendapatkan data Task dalam JSON

2. Membuat view baru show_json(request) yang akan menampilkan data Task (todolist) user login menggunakan AJAX dan JSON.

3. Membuat routing url yang sesuai sesuai spesifikasi kepada kedua views baru tersebut

4. Menyisipkan script berupa function untuk menampilkan detail Task pada bagian Card dari data JSON

### AJAX POST

1. Membuat view baru create_task_json(request) yang akan membuat Task baru dan mengembalikan redirect halaman yang menggunakan JSON

2. Membuat elemen button yang akan merujuk pada suatu modal pada template HTML memanfaatkan Bootstrap.

3. Membuat routing url yang sesuai sesuai spesifikasi kepada kedua views baru tersebut

4. Menyisipkan script berupa function untuk mendapatkan input judul dan deskripsi pada modal, kemudian ketika user menutup modal akan langsung menampilkan data yang ditambahkan.

Untuk AJAX POST, pertama buat dahulu routing dan function seperti tugas-tugas terdahulu sesuai dengan spesifikasi soal yang berguna untuk menghasilkan data.<br>
