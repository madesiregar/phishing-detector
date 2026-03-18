# Phishing Detector

Tool berbasis web untuk menganalisis URL dan isi email dalam mendeteksi indikator phishing. Dibangun menggunakan Python dan Flask.

---

## Apa itu Phishing?

Phishing adalah teknik serangan siber di mana penyerang menyamar sebagai pihak terpercaya seperti bank, platform e-commerce, atau layanan email untuk mengelabui korban agar menyerahkan informasi sensitif seperti password, nomor kartu kredit, atau data pribadi lainnya.

Serangan ini sudah ada selama puluhan tahun dan masih menjadi salah satu metode paling efektif karena menyasar perilaku manusia, bukan hanya celah teknis pada sistem.

**Di mana phishing paling sering terjadi?**

Email adalah jalur yang paling umum digunakan. Penyerang mengirim pesan berisi notifikasi palsu seperti tagihan, penangguhan akun, atau permintaan reset password dengan satu tujuan yaitu membuat korban mengklik sebuah link.

Link itulah senjatanya. Sebuah domain seperti `paypa1-secure.tk` terlihat sah pada pandangan pertama, terutama di layar ponsel di mana URL lengkapnya sering tersembunyi. Email phishing dan URL phishing hampir selalu bekerja bersama, dan itulah yang dirancang untuk dideteksi oleh tool ini.

---

## Kenapa Tool Ini Dibuat

Kebanyakan orang tidak bisa membedakan URL phishing dari yang asli hanya dengan melihatnya sekilas. Teknik yang digunakan penyerang seperti typosquatting, TLD mencurigakan, subdomain berlapis, dan karakter yang di-encode memang dirancang untuk tidak mencolok.

Tool ini dibuat untuk membuat analisis tersebut menjadi cepat, sistematis, dan bisa dijelaskan. Alih-alih mengandalkan intuisi, tool ini memecah setiap indikator mencurigakan yang ditemukan dalam URL atau isi email dan memberikan skor risiko berdasarkan seberapa berbahaya indikator tersebut.

Tujuannya bukan sekadar mengatakan aman atau phishing, tapi menunjukkan alasannya.

---

## Alur Kerja Tool

Pengguna memasukkan URL atau isi email melalui antarmuka web.

Input tersebut kemudian melewati beberapa lapisan analisis yang berjalan bersamaan.

Untuk URL, tool akan memeriksa apakah domain meniru brand terkenal seperti paypa1, g00gle, atau amaz0n. Selain itu juga memeriksa apakah TLD yang digunakan termasuk yang sering disalahgunakan seperti .tk, .ml, .ga, dan .cf. Tool juga mendeteksi penggunaan IP address langsung sebagai pengganti nama domain, kedalaman subdomain yang tidak wajar, panjang URL yang berlebihan, keberadaan kata kunci sensitif seperti verify dan suspended, serta pola redirect tersembunyi dalam struktur URL.

Untuk isi email, tool akan mendeteksi bahasa yang bersifat mendesak seperti "act immediately" atau "account will be deleted", sapaan generik seperti "Dear Customer" yang tidak menyebut nama penerima, jumlah link yang tidak wajar dalam satu email, serta ketidakcocokan antara teks link yang ditampilkan dengan URL tujuan sebenarnya.

Setiap indikator membawa bobot skor masing-masing. Semua skor dijumlahkan dan hasilnya masuk ke salah satu dari tiga verdict berikut.

| Skor          | Verdict    |
|---------------|------------|
| 0 sampai 24   | SAFE       |
| 25 sampai 59  | SUSPICIOUS |
| 60 sampai 100 | PHISHING   |

Antarmuka menampilkan verdict, total skor risiko, dan rincian setiap indikator yang terdeteksi sehingga hasilnya selalu bisa dijelaskan, bukan sekadar label.

---

## Tech Stack

- Backend menggunakan Python dan Flask
- Analisis menggunakan tldextract, regex, dan heuristic rules
- Frontend menggunakan HTML, CSS, dan JavaScript

---

## Cara Menjalankan
git clone https://github.com/madesiregar/phishing-detector.git
cd phishing-detector
pip install -r requirements.txt
python app.py
```

Buka `http://localhost:5000` di browser.

---

## Roadmap

- [x] URL heuristic analysis
- [x] Email body analysis
- [x] Risk scoring engine
- [x] Web interface
- [ ] Integrasi VirusTotal API
- [ ] WHOIS domain age lookup
- [ ] Machine learning model dengan dataset PhishTank
- [ ] Chrome extension
- [ ] Batch URL scanning

---

## Author

Made Siregar
GitHub: [@madesiregar](https://github.com/madesiregar)

---

Dibuat untuk project personal di bidang cybersecurity. Jangan digunakan untuk tujuan yang merugikan pihak lain. 