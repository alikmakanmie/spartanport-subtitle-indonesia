# Subtitle Indonesia untuk SpartanPort (God of War III Remastered)

Terjemahan penuh teks God of War III Remastered ke bahasa Indonesia,
sebagai mod untuk [SpartanPort](https://github.com/FelipePrado0/SpartanPort)
(port PC tidak resmi dari God of War III Remastered PS4).

## Cakupan (v4.1)

- **3.850 dari 4.016 entri** berbahasa Indonesia (dialog, subtitle
  cutscene, menu, tutorial, deskripsi, judul tempat).
- Sisa 166 entri tetap Inggris karena hanya nama tokoh/senjata
  (Hera, Blades of Exile), kode arena, placeholder internal, seruan
  tanpa padanan, atau nama tempat murni (Gaia, Tartarus).
- Dibangun dari terjemahan fan-made CUSA01623 + terjemahan penuh,
  dengan anggaran ukuran total **persis 0**: file hasil harus
  **456.432 byte** — loader SpartanPort menolak ukuran lain.

## File mod jadi (siap pakai)

`Subtitle-Indonesia.zip` adalah mod jadi v4.1 — letakkan langsung di
folder mods SpartanPort (lihat langkah 4–5 di bawah). File zip ini
berisi `R_LANG_EN.WAD` hasil terjemahan (file game yang sudah diubah),
jadi ini cara tercepat memakai mod.

Catatan hak cipta: file WAD asli adalah milik pemegang hak game.
Kalau kamu lebih memilih jalur bersih, jangan pakai zip — bangun
sendiri dari dump milikmu lewat `translations.json` + `build_mod.py`
di bawah (hasilnya byte-identik dengan zip ini).

## Cara membangun mod

1. Siapkan dump God of War III Remastered PS4 milikmu (CUSA01623
   01.02) dan SpartanPort.
2. Jalankan:
   `python3 build_mod.py <path ke R_LANG_EN.WAD aslimu> R_LANG_EN.WAD`
3. Buat folder mod `Subtitle Indonesia/` berisi:
   - `EXEC/WAD/PS4_LE/R_LANG_EN.WAD` (hasil langkah 2)
   - `mod.json` (dari repo ini)
   - atau zip ketiganya (root zip: `EXEC/`, `mod.json`) lalu letakkan
     zip di folder mods — launcher membongkarnya sendiri.
4. Letakkan di folder mods SpartanPort
   (`~/.local/share/spartanport/mods/` di Linux), pastikan **Load mods**
   ON dan mod tercentang di halaman Mods, lalu PLAY.
5. Di game: pilih bahasa **English + subtitle ON** (terjemahan
   menempati slot bahasa English).

## Mematikan mod

Uncheck mod di halaman Mods (atau hapus dari folder mods) — file
game aslimu tidak pernah diubah oleh mod ini (sistem overlay
SpartanPort).
