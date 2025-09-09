1. Tautan menuju aplikasi PWS : https://felicia-evangeline-kickncart.pbp.cs.ui.ac.id/ (Football shop dengan nama Kick n' Cart, ibarat pemain bola yang terus menendang bola utuk mencapai tujuannya yaitu mencetal gol, pembeli terus menelurusi toko ini hingga mencapai tujuannya yaitu mendapatkan barang yang ia inginkan)


-----------------------------------------------------------------------------------------------------------------------------------------------
2. Pertanyaan 1 : Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban : 
- Persiapan folder proyek dan virtual environment
Saya membuat sebuah direktori proyek bernama kickncart dan masuk ke dalamnya. Di direktori itu saya membuat virtual environment untuk mengisolasi dependensi proyek sehingga tidak bercampur dengan paket-paket di sistem. Setelah membuat virtual environment, saya mengaktifkannya agar semua instalasi paket dan perintah manage.py berjalan di lingkungan yang terkontrol.

- Instalasi Django dan inisiasi proyek
Dengan virtual environment aktif, saya menginstal Django. Kemudian saya menginisiasi proyek Django (root project) di dalam direktori kerja. Proyek ini berisi file konfigurasi global seperti settings.py, urls.py, dan file manajemen manage.py.

- Membuat aplikasi main dan mendaftarkan ke proyek
Di dalam proyek saya membuat aplikasi baru bernama main yang akan menampung semua kode untuk tugas Football Shop. Setelah folder aplikasi main dibuat, saya mendaftarkannya di INSTALLED_APPS pada settings.py agar Django mengenali aplikasi tersebut saat runtime dan saat proses migrasi.

- Menyiapkan view untuk halaman utama
Saya membuat fungsi view (dengan nama show_main) di main/views.py. Fungsi ini bertugas menyiapkan data yang akan ditampilkan. Selain daftar produk yang diambil dari database, saya juga memasukkan variabel identitas yang diminta tugas (NPM, nama, dan kelas). Variabel-variabel ini dikirim ke template melalui context agar bisa ditampilkan dinamis pada halaman.

- Menyiapkan template HTML sesuai ketentuan tugas
Saya membuat folder templates di dalam aplikasi main dan menaruh file main.html di sana. Di file template tersebut saya memasang placeholder template variables untuk npm, name, class serta struktur perulangan untuk menampilkan daftar produk. Dengan struktur ini, view hanya perlu me-render main.html dan Django akan menggabungkan context menjadi HTML yang bisa dilihat user. 

- Mengonfigurasi routing (urls.py)
Saya menambahkan file urls.py di aplikasi main yang memetakan root path ('') ke view show_main. Lalu pada urls.py di level proyek saya melakukan include ke main.urls sehingga halaman utama aplikasi bisa diakses melalui http://localhost:8000/. Dengan pemetaan ini, request pertama akan diteruskan ke view yang menyiapkan context dan template.

- Pengaturan template loader di settings
Di settings.py saya memastikan konfigurasi templating mengizinkan Django mencari template di dalam folder aplikasi. Nilai APP_DIRS saya pastikan aktif. Ini penting agar Django menemukan main.html yang terletak di main/templates/ tanpa perlu menambahkan path template manual.

- Sinkronisasi database (migrasi)
Setelah struktur aplikasi lengkap, saya menjalankan proses migrasi untuk mengaplikasikan perubahan struktur database yang diperlukan proyek (misal jika ada perubahan model). Proses ini memastikan database lokal siap menyimpan data yang diperlukan aplikasi.

- Menjalankan server lokal dan verifikasi
Dengan semua konfigurasi siap, saya menjalankan server development dan membuka http://localhost:8000/. Saya memeriksa tampilan seperti variabel NPM, nama, dan kelas harus tampil, serta daftar produk muncul sesuai data di database.

- Deployment ke PWS
Langkah deployment meliputi: membuat project di PWS, menyiapkan file environment produksi (.env.prod) dengan konfigurasi yang diminta, menambahkan domain PWS ke ALLOWED_HOSTS pada settings.py, lalu push kode ke repository dan menjalankan perintah deployment yang diberikan oleh PWS. Di dashboard PWS saya memastikan environment variables tersimpan (raw editor) dan menunggu status deployment berubah menjadi Running. Setelah itu saya buka URL PWS untuk memastikan aplikasi dapat diakses publik.

- Unit testing
Saya menulis beberapa pengujian unit sederhana untuk memeriksa aspek-aspek penting: halaman utama dapat diakses (status 200), halaman menggunakan template main.html, dan beberapa pengecekan fungsionalitas dasar lainnya. Pengujian dijalankan dengan perintah test bawaan Django untuk memastikan tidak ada regresi saat pengembangan lanjutan.

//// Troubleshooting yang saya lakukan selama pengerjaan ////
- ImportError (tidak bisa import show_main)
Perbaikan: memastikan main/views.py mendefinisikan show_main, import di main/urls.py tepat (from .views import show_main), hapus nama file yang konflik, dan memastikan ada __init__.py di folder main/.

- TemplateDoesNotExist (main.html)
Perbaikan: memastikan file main.html ada di main/templates dan settings.py memakai APP_DIRS = True. Memastikan juga view memanggil path yang konsisten.


-----------------------------------------------------------------------------------------------------------------------------------------------
3. Pertanyaan 2 : Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawaban : 
- Bagan dapat di akses melalui link berikut : ristek.link/Soal-2
Alur kerja aplikasi Django dimulai ketika client mengirimkan request melalui browser. Request tersebut pertama kali masuk ke urls.py di level proyek, lalu diteruskan ke urls.py di dalam aplikasi yang sesuai. Dari sini, URL dipetakan ke fungsi tertentu di views.py.

Fungsi view akan menjalankan logika aplikasi, termasuk mengambil data dari models.py bila diperlukan. Data yang didapat kemudian dimasukkan ke dalam context dan diteruskan ke file template HTML. Template inilah yang merender data menjadi tampilan web yang dinamis.

Hasil render berupa file HTML lengkap lalu dikirim kembali ke browser sebagai response. Dengan demikian, urls.py berperan sebagai pemetaan, views.py mengendalikan logika, models.py menangani data, dan template HTML menampilkan hasil akhirnya kepada pengguna.


-----------------------------------------------------------------------------------------------------------------------------------------------
4. Pertanyaan 3 : Jelaskan peran settings.py dalam proyek Django!
Jawaban : 
File settings.py memiliki peran sebagai pusat konfigurasi dalam sebuah proyek Django. Semua pengaturan utama yang dibutuhkan untuk menjalankan aplikasi tersimpan di dalam file ini, sehingga settings.py bisa dianggap sebagai “otak” yang mengatur jalannya proyek.

Pertama, settings.py mengatur daftar aplikasi yang digunakan melalui bagian INSTALLED_APPS. Pada bagian ini, kita mendaftarkan aplikasi bawaan Django maupun aplikasi yang kita buat sendiri, seperti main. Dengan begitu, Django mengetahui aplikasi mana saja yang harus dijalankan.

Kedua, file ini juga mengatur konfigurasi database, mulai dari jenis database yang digunakan (misalnya SQLite, PostgreSQL, atau MySQL) hingga detail koneksinya. Hal ini memungkinkan Django untuk menghubungkan model dengan database sehingga data dapat disimpan dan diakses sesuai kebutuhan.

Selain itu, settings.py berperan dalam aspek keamanan proyek. Misalnya, terdapat variabel SECRET_KEY yang digunakan untuk proses enkripsi internal dan variabel DEBUG yang menentukan mode proyek, apakah sedang dalam tahap pengembangan atau sudah dipublikasikan. Pada mode produksi, nilai DEBUG harus diatur ke False demi mencegah kebocoran informasi penting.

Tidak hanya itu, file ini juga mengatur lokasi template dan file statis (CSS, JavaScript, gambar) agar tampilan aplikasi bisa dimuat dengan baik di browser. Pengaturan terkait bahasa, zona waktu, serta middleware yang digunakan dalam proyek juga diatur di sini.

Singkatnya, settings.py adalah pusat kendali dari sebuah proyek Django. Tanpa file ini, proyek tidak akan tahu aplikasi mana yang aktif, database apa yang digunakan, serta bagaimana perilaku aplikasi di lingkungan pengembangan maupun produksi.



-----------------------------------------------------------------------------------------------------------------------------------------------
5. Pertanyaan 4 : Bagaimana cara kerja migrasi database di Django?
Jawaban: 
Migrasi database di Django merupakan proses untuk menyelaraskan perubahan yang kita buat pada model dengan struktur tabel yang ada di database. Dengan adanya migrasi, kita tidak perlu mengubah database secara manual karena Django sudah menyediakan mekanisme otomatis untuk melakukan penyesuaian tersebut.

Secara garis besar, cara kerja migrasi terbagi menjadi dua tahap. Pertama, ketika kita menjalankan perintah makemigrations, Django akan membaca perubahan yang ada pada file model, lalu mencatatnya dalam sebuah file migrasi. File ini berisi instruksi mengenai perubahan yang harus dilakukan di database, seperti menambah tabel baru, menambahkan kolom, menghapus kolom, atau memodifikasi atribut tertentu. Tahap ini bisa dianggap sebagai “draft” atau rencana perubahan database.

Tahap kedua adalah menjalankan perintah migrate. Pada tahap ini, Django benar-benar mengeksekusi file migrasi yang sudah dibuat sebelumnya. Perintah ini akan menerapkan perubahan ke database sesuai dengan instruksi yang ada pada file migrasi, sehingga struktur tabel di database menjadi selaras dengan definisi model terbaru.

Selain itu, Django juga menyimpan riwayat migrasi yang sudah dijalankan di dalam sebuah tabel khusus bernama django_migrations. Dengan cara ini, Django bisa melacak migrasi apa saja yang sudah diterapkan dan memastikan bahwa migrasi tidak dijalankan dua kali.

Dengan adanya sistem migrasi ini, proses pengembangan menjadi lebih fleksibel. Setiap kali kita mengubah model, kita cukup membuat migrasi dan menjalankannya tanpa harus menulis query SQL secara manual. Hal ini membuat pengelolaan database menjadi lebih efisien, konsisten, dan mudah dikelola, terutama ketika bekerja dalam tim.



-----------------------------------------------------------------------------------------------------------------------------------------------
6. Pertanyaan 5 : Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Jawaban : 
Menurut saya, alasan Django dijadikan framework awal dalam pembelajaran karena sifatnya yang cukup lengkap sekaligus ramah bagi pemula. Django sudah menyediakan banyak fitur bawaan seperti sistem autentikasi, pengelolaan database dengan ORM, dan juga admin panel. Dengan begitu, mahasiswa tidak perlu menulis semuanya dari nol dan bisa lebih cepat memahami konsep dasar pengembangan web.

Selain itu, Django menggunakan pola arsitektur Model-View-Template (MVT) yang menurut saya cukup jelas dalam memisahkan data, logika, dan tampilan. Hal ini membantu mahasiswa untuk belajar menulis kode dengan terstruktur sejak awal, sehingga tidak bingung ketika proyek semakin besar.

Dari sisi dokumentasi dan komunitas, Django juga sangat kuat. Saya merasa ini memudahkan mahasiswa untuk mencari referensi atau solusi saat menemui masalah. Jadi, walaupun mungkin ada framework lain yang lebih populer untuk industri tertentu, menurut saya Django tetap ideal sebagai titik awal karena bisa melatih dasar-dasar logika, keteraturan kode, dan konsep web development secara menyeluruh.

Singkatnya, Django dipilih bukan hanya karena “mudah digunakan”, tapi juga karena bisa melatih pola pikir yang benar dalam membangun aplikasi web, yang nantinya akan berguna saat mempelajari framework lain atau masuk ke dunia kerja.



-----------------------------------------------------------------------------------------------------------------------------------------------
7. Pertanyaan 6 : Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Jawaban : 
Menurut saya, materi pada Tutorial 1 sudah cukup membantu dalam memahami dasar pembuatan aplikasi Django. Penjelasan pada tutorial disusun secara runtut, dimulai dari pembuatan proyek dan aplikasi, kemudian dilanjutkan ke konfigurasi URL, pembuatan view, penggunaan template, hingga migrasi database. Alur ini memudahkan saya dalam mengikuti langkah demi langkah ketika mengerjakan tugas.

Bagian yang menurut saya paling bermanfaat adalah penjelasan mengenai struktur proyek dan aplikasi. Pada awalnya saya cukup bingung membedakan peran direktori proyek dengan aplikasi, terutama ketika harus menentukan letak file urls.py, views.py, dan templates. Setelah membaca tutorial, saya jadi lebih paham bagaimana alurnya dan mengapa file urls.py di tingkat proyek berbeda fungsi dengan urls.py di dalam aplikasi.

Selain itu, bagian migrasi database juga cukup jelas. Tutorial menjelaskan alur penggunaan perintah makemigrations dan migrate, sehingga saya bisa lebih memahami bahwa proses tersebut sebenarnya adalah cara Django menyamakan definisi model dengan struktur database. Hal ini langsung berguna ketika saya membuat model produk di aplikasi saya.

Kemudian, bagian template juga sangat membantu. Dari tutorial, saya belajar bagaimana cara menampilkan variabel yang dikirimkan dari view ke dalam HTML, serta bagaimana menuliskan perulangan dengan sintaks template Django. Konsep ini sangat penting karena pada tugas saya, saya harus menampilkan variabel identitas (NPM, nama, kelas) serta daftar produk dari database.

Secara keseluruhan, menurut saya Tutorial 1 sudah bagus sebagai pengantar. Materinya cukup lengkap untuk mahasiswa yang baru pertama kali menggunakan Django, dan contoh yang diberikan relevan dengan kebutuhan tugas. Dengan mengikuti alur di tutorial, saya bisa menyelesaikan tugas dengan lebih terstruktur dan memahami keterkaitan antara model, view, template, dan URL routing.


-----------------------------------------------------------------------------------------------------------------------------------------------
REFERENSI
- PBP Tutorial 0
- PBP Tutorial 1
- Django documentation
- YouTube channel Marcellinus Yoseph