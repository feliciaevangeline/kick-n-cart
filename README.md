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


-----------------------------------------------------------------------------------------------------------------------------------------------
=============== TUGAS 3 ===============
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Jawaban : 
Data delivery diperlukan karena sebuah platform hampir selalu melibatkan pertukaran informasi antara server dan pengguna. Server menyimpan serta mengolah data, sementara pengguna mengakses data tersebut melalui aplikasi web atau mobile. Tanpa adanya mekanisme pengiriman data, informasi yang ada di server tidak akan bisa sampai ke pengguna, dan masukan dari pengguna juga tidak bisa dikirim kembali ke server. Dengan kata lain, data delivery menjadi penghubung utama yang membuat platform bisa berfungsi secara interaktif.

Selain itu, data delivery juga membantu agar pertukaran data berjalan teratur dengan format standar seperti JSON atau XML. Dengan adanya format ini, data yang dikirim lebih mudah dibaca, diproses, dan ditampilkan oleh aplikasi, bahkan bisa digunakan kembali oleh sistem lain. Mekanisme ini juga memungkinkan platform menampilkan data secara real-time, terhubung dengan layanan eksternal, dan lebih mudah dikembangkan. Jadi, data delivery bisa dianggap sebagai fondasi penting agar platform tidak hanya berjalan secara lokal, tetapi juga bisa berinteraksi dengan pengguna maupun sistem lain secara luas.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Jawaban :
Menurut saya, JSON lebih baik dibandingkan XML karena formatnya jauh lebih sederhana dan mudah dipahami. JSON hanya menggunakan struktur key-value yang ringkas, sehingga data lebih cepat diproses dan tidak banyak memakan ruang. Berbeda dengan XML yang penuh dengan tag pembuka dan penutup, sehingga terasa lebih ribet ketika dibaca maupun digunakan.

Saya juga melihat JSON lebih populer karena lebih sesuai dengan kebutuhan aplikasi web dan mobile saat ini. Hampir semua framework modern mendukung JSON secara langsung, terutama karena JSON sangat erat kaitannya dengan JavaScript. Hal ini membuat pengembangan aplikasi jadi lebih praktis dan efisien. Walaupun XML masih ada manfaatnya, terutama di sistem lama atau yang butuh validasi ketat, saya pribadi lebih memilih JSON karena lebih ringan, cepat, dan sesuai dengan tren teknologi saat ini.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Jawaban :
Method is_valid() pada form Django dipakai untuk mengecek apakah data yang dimasukkan lewat form sudah sesuai dengan aturan yang berlaku. Misalnya, sistem akan memeriksa apakah nilai harga berupa angka, apakah kolom nama produk tidak kosong, atau apakah URL yang dimasukkan berbentuk link yang valid. Kalau semua syarat sudah terpenuhi, maka is_valid() akan mengembalikan nilai benar, sedangkan jika ada data yang salah, form akan dianggap tidak valid dan error bisa langsung ditampilkan ke pengguna.

Penggunaan method ini penting supaya data yang tersimpan di database tetap rapi dan konsisten. Tanpa adanya validasi ini, data yang salah atau tidak sesuai bisa saja tersimpan, misalnya stok bernilai negatif atau link gambar yang tidak bisa dibuka. Hal seperti ini bisa merusak sistem dan bikin data jadi kacau. Dengan adanya is_valid(), proses validasi jadi lebih praktis karena Django sudah otomatis melakukan pengecekan tanpa perlu menulis kode tambahan untuk setiap field.

4.  Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Jawaban :
CSRF token dibutuhkan pada form di Django untuk mencegah serangan Cross-Site Request Forgery (CSRF). Token ini berfungsi sebagai kode unik yang diberikan pada setiap form dan akan divalidasi oleh server ketika form dikirim. Dengan adanya token tersebut, server dapat memastikan bahwa permintaan benar-benar berasal dari pengguna yang sah melalui aplikasi, bukan dari sumber eksternal yang berusaha menyamar.

Apabila CSRF token tidak digunakan, aplikasi menjadi rentan terhadap manipulasi request. Penyerang dapat membuat halaman berbahaya yang secara diam-diam mengirimkan permintaan ke server dengan identitas pengguna tanpa sepengetahuannya, misalnya mengubah data, menghapus informasi, atau melakukan transaksi. Kondisi ini dapat dimanfaatkan untuk merugikan pengguna maupun merusak integritas aplikasi.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban :
Berdasarkan checklist yang diberikan, langkah pertama yang saya lakukan adalah membuat skeleton menggunakan base.html agar halaman-halaman lain dapat menggunakan kerangka yang sama. Setelah itu, saya menambahkan form melalui forms.py menggunakan ModelForm yang terhubung ke model Product, sehingga proses input data produk bisa dilakukan lebih mudah. Pada tahap berikutnya, saya membuat beberapa fungsi views, seperti show_main untuk menampilkan daftar produk, create_product untuk menambahkan produk baru, serta show_product untuk menampilkan detail produk tertentu. Saya juga menambahkan views tambahan untuk kebutuhan data delivery, yaitu show_json, show_xml, show_json_by_id, dan show_xml_by_id yang dibuat dengan memanfaatkan serializers untuk mengubah data model menjadi format JSON dan XML.

Langkah selanjutnya adalah membuat routing pada urls.py agar semua views tersebut dapat diakses melalui endpoint tertentu. Untuk bagian template, saya menambahkan main.html sebagai halaman utama yang berisi daftar produk dengan tombol “Add” dan “Detail”, lalu membuat create_product.html sebagai halaman input produk baru, serta product_detail.html untuk menampilkan detail produk. Setelah semuanya selesai, saya mencoba mengakses data dari endpoint JSON dan XML menggunakan Postman untuk memastikan data dapat ditampilkan dengan benar. Dalam proses ini, saya tidak hanya mengikuti tutorial secara mentah-mentah, tetapi juga menyesuaikan dengan kebutuhan tugas, sehingga dapat memahami fungsi setiap bagian dan alur implementasinya.

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Jawaban :
Menurut saya, tutorial 2 sudah sangat jelas dan membantu dalam memahami konsep dasar pembuatan aplikasi Django. Penjelasan yang diberikan membuat langkah-langkah mudah diikuti, sehingga proses belajar terasa lebih terarah. Dari materi yang sudah dijelaskan di tutorial, saya jadi lebih terbantu untuk mengerjakan tugas 3 karena sudah memiliki gambaran alur pengerjaan yang sesuai.

7. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
Jawaban :
ristek.link/postman-t3

Referensi : 
- website GeeksforGeeks
- tutorial 2 PBP
- website Telkom University
- website Coding Studio

=============== TUGAS 4 ===============
1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
Jawaban :
Django AuthenticationForm adalah sebuah form bawaan yang disediakan oleh Django untuk menangani proses autentikasi pengguna ketika login. Form ini sudah terintegrasi dengan sistem autentikasi Django sehingga mampu memvalidasi input username dan password berdasarkan data yang tersimpan di database. AuthenticationForm juga sudah memiliki mekanisme validasi error apabila pengguna salah memasukkan data. Kelebihan dari AuthenticationForm adalah praktis karena tidak perlu membuat form autentikasi dari awal, aman karena sudah mengikuti standar keamanan Django, serta efisien untuk implementasi cepat. Namun, AuthenticationForm memiliki kekurangan dari sisi fleksibilitas, karena jika pengembang membutuhkan tampilan login yang lebih kompleks atau ingin menambahkan field khusus, maka diperlukan penyesuaian tambahan. AuthenticationForm lebih sering dipakai sebagai dasar yang kemudian dimodifikasi sesuai kebutuhan proyek.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Jawaban :
Autentikasi dan otorisasi merupakan dua yang konsep berbeda dalam sistem keamanan aplikasi web. Autentikasi adalah proses untuk memverifikasi identitas pengguna, yaitu memastikan bahwa username dan password yang dimasukkan benar-benar milik pengguna yang terdaftar. Sedangkan otorisasi adalah tahap setelah autentikasi, yaitu menentukan hak akses atau izin apa saja yang dimiliki pengguna tersebut. Contohnya, setelah seorang admin berhasil login (autentikasi), sistem akan memberi izin tambahan untuk mengakses dashboard admin (otorisasi). Django mengimplementasikan autentikasi melalui sistem login bawaan dengan form seperti AuthenticationForm dan fungsi authenticate(). Sementara itu, otorisasi diimplementasikan melalui sistem permission, group, dan decorator seperti @login_required atau @permission_required, yang memungkinkan developer mengatur akses pada view atau model tertentu. 

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Jawaban :
Session dan cookies sama-sama digunakan untuk menyimpan informasi state di aplikasi web yang sifatnya stateless, tetapi mekanismenya berbeda. Cookies menyimpan data langsung di browser pengguna dalam bentuk file kecil, sehingga server tidak perlu menyimpan banyak informasi. Kelebihan cookies adalah ringan bagi server dan dapat digunakan untuk kebutuhan sederhana seperti menyimpan preferensi tampilan. Kekurangannya adalah rentan terhadap serangan karena data berada di sisi klien. Sementara itu, session menyimpan data di server, sedangkan browser hanya menyimpan ID session untuk menghubungkannya. Kelebihan session adalah lebih aman karena data sensitif tidak langsung disimpan di browser, namun kekurangannya adalah dapat membebani server ketika jumlah pengguna semakin banyak.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Jawaban :
Penggunaan cookies secara default tidak sepenuhnya aman karena ada potensi risiko seperti pencurian data melalui serangan XSS (Cross-Site Scripting) maupun CSRF (Cross-Site Request Forgery). Cookies juga bisa disalahgunakan apabila berisi informasi sensitif tanpa enkripsi yang memadai. Oleh karena itu, dalam pengembangan web modern, cookies biasanya dibekali dengan konfigurasi tambahan agar lebih aman. Django menangani hal ini dengan menyediakan proteksi bawaan, misalnya dengan atribut HttpOnly yang mencegah cookies diakses melalui JavaScript, atribut Secure agar cookies hanya dikirim melalui koneksi HTTPS, serta penggunaan csrf_token untuk melindungi form dari serangan CSRF. Django termasuk framework yang memiliki sistem keamanan cookies cukup ketat secara default, namun pengembang tetap disarankan untuk memahami risikonya agar tidak salah konfigurasi.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban :
Saya mulai mengerjakan checklist pertama dengan menambahkan fungsi registrasi, login, dan logout. Untuk registrasi, saya menggunakan UserCreationForm dari Django yang sudah menyediakan validasi bawaan untuk username dan password. Form ini kemudian saya sambungkan ke sebuah view register yang berfungsi menyimpan data pengguna baru ketika form di-submit. Selanjutnya, saya membuat template register.html agar pengguna dapat melakukan registrasi melalui antarmuka web.

Langkah berikutnya adalah membuat fungsi login dengan memanfaatkan AuthenticationForm. Fungsi ini saya letakkan dalam view login_user, yang tidak hanya melakukan autentikasi data pengguna tetapi juga menyimpan informasi last_login ke dalam cookies menggunakan response.set_cookie. Data ini nantinya ditampilkan di halaman utama agar pengguna dapat melihat kapan terakhir kali mereka login. Setelah login berhasil, pengguna diarahkan kembali ke halaman utama aplikasi.

Untuk fungsi logout, saya menambahkan view logout_user yang memanfaatkan fungsi logout bawaan Django. Fungsi ini akan menghapus session pengguna, sehingga status login berakhir. 

Setelah itu, saya menyesuaikan halaman utama (main.html) agar menampilkan detail informasi pengguna yang sedang login. Informasi yang saya tampilkan meliputi username (request.user.username) dan data last_login yang diambil dari cookies. Saya juga menambahkan tombol filter seperti All Products dan My Products. Tombol ini membantu membedakan apakah produk yang ditampilkan adalah milik semua pengguna atau hanya produk milik akun yang sedang login.

Terakhir, saya melakukan pengujian dengan login menggunakan masing-masing akun. Saya menambahkan tiga produk untuk setiap akun dengan kategori berbeda (Sepatu, Bola, Jersey, dan Aksesoris). Hasilnya, di halaman All Products muncul seluruh data produk dari semua pengguna, sedangkan di halaman My Products hanya tampil produk yang sesuai dengan akun yang sedang login. Dengan cara ini, semua checklist terpenuhi mulai dari autentikasi, pembuatan dummy data, penghubungan model Product dengan User, hingga penampilan informasi login menggunakan cookies.

Referensi:
- Dokumentasi resmi Django
- Tutorial 3 PBP
- Website DigitalOcean – artikel tentang Understanding Sessions and Cookies in Django
- Website W3Schools - pembahasan tentang cookies dan session

=============== TUGAS 5 ===============
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Jawaban :
CSS memiliki aturan urutan prioritas yang disebut specificity. Urutan ini menentukan style mana yang “menang” jika ada konflik. Level paling rendah adalah selector elemen, misalnya div, p, atau h1, karena aturan ini biasanya berlaku umum. Selanjutnya ada class selector (misalnya .btn atau .container) yang lebih spesifik. Di atasnya lagi ada id selector seperti #navbar, yang sifatnya unik karena tiap halaman idealnya hanya punya satu id tertentu. Lebih tinggi dari semua itu adalah inline style, yaitu style yang langsung ditulis di atribut elemen HTML (misal, <p style="color:red">). Inline hampir selalu menang melawan selector lain. Namun, ada juga !important yang bisa memaksa satu aturan CSS untuk mengalahkan semua aturan lain meskipun specificity-nya lebih rendah.

Contoh, misal ada sebuah tombol dengan class .btn, id #submit, dan juga diberi inline style. Jika kita menulis .btn { color: blue; }, lalu menambahkan #submit { color: green; }, dan akhirnya menulis <button id="submit" class="btn" style="color: red;">Submit</button>, maka warna teks tombol akan menjadi merah karena inline style menang. Tapi jika di CSS ada aturan .btn { color: blue !important; }, maka warna biru akan tetap dipakai walaupun ada inline style.


2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Jawaban :
Responsive design adalah konsep agar tampilan website bisa otomatis menyesuaikan diri dengan ukuran layar pengguna. Hal ini sangat penting karena perangkat yang dipakai untuk membuka website sangat beragam, mulai dari laptop, tablet, hingga smartphone. Tanpa responsive design, tampilan website bisa kacau, misalnya teks terlalu kecil untuk dibaca di HP, gambar keluar dari layar, atau tombol sulit ditekan. Dengan responsive design, tata letak bisa berubah secara fleksibel agar tetap nyaman dipakai di semua perangkat.

Contohnya, website Instagram Web yang sudah menerapkan responsive design. Jika dibuka di laptop, tampilannya penuh dengan sidebar, feed, dan bagian explore. Tapi kalau dibuka di smartphone, layout-nya lebih ringkas, sidebar hilang, dan tombol-tombol dibuat lebih besar agar mudah ditekan dengan jari.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Jawaban :
Dalam CSS ada istilah box model, yaitu cara browser menggambarkan setiap elemen di halaman. Box model ini terdiri dari konten, padding, border, dan margin. Padding adalah ruang di dalam elemen, yaitu jarak antara konten dan border. Misalnya pada tombol, padding akan membuat teks di dalam tombol tidak mepet ke tepi, tapi punya jarak sehingga tombol lebih “lega”. Border adalah garis yang membungkus elemen, bisa diatur warnanya, ketebalannya, bahkan stylenya (solid, dashed, dotted). Sementara margin adalah jarak di luar elemen, yang memisahkan satu elemen dengan elemen lain di sekitarnya.

Contoh penggunaannya, jika kita membuat <button>Click</button> lalu menambahkan CSS padding: 10px; border: 2px solid black; margin: 20px;, maka teks tombol akan memiliki jarak 10px dari tepi tombol, tombol punya garis hitam setebal 2px, dan tombol tersebut akan berjarak 20px dari elemen lain di sekitarnya.

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Jawaban :
Flexbox dan Grid adalah dua metode layout modern dalam CSS yang membantu mengatur posisi elemen di halaman. Flexbox dirancang untuk layout satu dimensi, artinya lebih cocok ketika kita hanya ingin mengatur elemen dalam baris (row) atau kolom (column). Dengan flexbox, kita bisa mengatur apakah elemen-elemen rata kiri, kanan, tengah, atau bahkan memiliki jarak sama rata dengan justify-content: space-between. Kita juga bisa mengatur vertical alignment dengan align-items.

Berbeda dengan flexbox, Grid lebih cocok untuk layout dua dimensi, yaitu ketika kita ingin mengatur baris dan kolom sekaligus. Misalnya, kita bisa membuat halaman yang terdiri dari header di atas, sidebar di kiri, konten utama di tengah, dan footer di bawah hanya dengan beberapa baris kode CSS Grid. Dengan properti grid-template-columns dan grid-template-rows, kita bisa menentukan ukuran setiap bagian dengan sangat fleksibel.

Sebagai contoh nyata, e-commerce seperti Tokopedia atau Shopee biasanya menggunakan grid untuk menampilkan produk dalam bentuk kotak-kotak yang sejajar, tapi di dalam setiap kotak produknya bisa menggunakan flexbox untuk mengatur isi seperti gambar, nama produk, harga, dan tombol beli. Jadi keduanya sebenarnya saling melengkapi, grid untuk struktur besar, flexbox untuk detail kecil di dalam struktur tersebut.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Jawaban :
Langkah pertama yang saya lakukan adalah menambahkan Tailwind CSS sebagai framework utama styling. Hal ini dilakukan dengan menambahkan script CDN Tailwind pada file base.html di dalam folder templates. Selain itu, saya juga menambahkan tag <meta name="viewport"> agar halaman web bisa lebih responsif pada berbagai perangkat, terutama mobile. Dengan Tailwind, saya lebih mudah mengatur layout, warna, spacing, dan tampilan komponen tanpa harus menulis CSS manual terlalu banyak.

Setelah itu, saya mengerjakan bagian CRUD product, khususnya fungsi edit dan delete. Pada file views.py, saya membuat fungsi edit_product yang menerima parameter id produk. Fungsi ini menggunakan instance produk yang sudah ada untuk diisi ke dalam form sehingga pengguna dapat melakukan perubahan data. Jika form valid, perubahan langsung disimpan ke database.

Untuk delete product, saya menambahkan fungsi delete_product yang mengambil produk berdasarkan id lalu menghapusnya dari database. Kedua fungsi ini kemudian saya daftarkan di urls.py agar bisa diakses melalui tombol yang ada pada setiap card product maupun halaman detail. Dengan begitu, pengguna bisa lebih mudah mengelola produk langsung dari daftar produk maupun dari halaman detail.

Setelah fungsi CRUD selesai, saya membuat file navbar.html untuk menambahkan navigation bar yang konsisten di setiap halaman aplikasi. Navbar ini saya buat responsif menggunakan Tailwind. Pada tampilan desktop, navbar menampilkan menu utama secara penuh, sementara pada tampilan mobile saya menambahkan tombol hamburger untuk membuka menu. Warna dasar navbar saya gunakan police blue, dipadukan dengan teks dan tombol berwarna terang (marigold, putih, merah) agar kontras dan sesuai dengan tema olahraga. Navbar ini saya hubungkan ke semua halaman dengan {% include 'navbar.html' %}.

Selanjutnya, agar styling dan file tambahan bisa digunakan secara konsisten, saya mengatur konfigurasi static files di settings.py. Saya menambahkan middleware WhiteNoise agar file statis dapat disajikan dengan baik saat aplikasi dijalankan dalam mode produksi. Selain itu, saya juga memastikan bahwa folder /static dapat digunakan untuk menyimpan file CSS tambahan, gambar, dan asset lain. Pada file base.html, saya menautkan file global.css dari folder static agar bisa dipakai di seluruh template.

Bagian terakhir yang saya lakukan adalah melakukan styling pada halaman-halaman utama aplikasi. Saya mulai dari halaman login dan register dengan memberikan border, padding, dan highlight ketika input difokuskan. Kemudian pada halaman create product dan edit product, saya menambahkan layout form yang lebih rapi dengan tombol aksi yang dibedakan warnanya.

Untuk halaman product detail, saya menata ulang layout agar gambar produk berada di sebelah kiri, sedangkan informasi produk (nama, brand, harga, stok, tanggal dibuat, dan deskripsi) berada di sebelah kanan. Hal ini membuat tampilan lebih profesional dan mudah dibaca. Saya juga menambahkan informasi brand dan created at yang sebelumnya belum ditampilkan.

Terakhir, pada halaman daftar produk, saya menambahkan kondisi agar jika belum ada produk maka ditampilkan ilustrasi gambar no-product.png dengan pesan bahwa produk masih kosong. Jika produk sudah ada, setiap produk ditampilkan dalam bentuk card dengan desain grid. Pada setiap card terdapat tombol Edit dan Delete agar pengguna dapat langsung mengelola produk. Judul produk juga bisa diklik untuk menuju halaman detail produk.

Secara keseluruhan, saya mengikuti struktur besar dari tutorial, namun saya menyesuaikannya dengan tema aplikasi yang saya kerjakan. Dengan begitu, hasil akhir aplikasi saya tetap memenuhi checklist tugas, tetapi tetap memiliki gaya visual dan identitas sendiri yang berbeda dari contoh tutorial.

referensi:
- Tutorial 4 PBP
- EasyCoding.id – artikel Urutan Prioritas Selector CSS (Specificity): Panduan Lengkap untuk Memahami dan Menggunakan (https://www.easycoding.id/blog/urutan-prioritas-selector-css-specificity-panduan-lengkap-untuk-memahami-dan-menggunakan)
- W3Schools – Responsive Web Design (https://www.w3schools.com/html/html_responsive.asp)
- W3Schools – CSS Box Model (https://www.w3schools.com/css/css_boxmodel.asp)
- W3Schools – CSS Flexbox (https://www.w3schools.com/css/css3_flexbox.asp)
- CSS-Tricks – A Complete Guide to Flexbox (https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- Tailwind CSS v1 – Flexbox & Grid Components (https://v1.tailwindcss.com/components/flexbox-grids)