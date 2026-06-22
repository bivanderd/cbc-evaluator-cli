# 🩸 Basic Lab Triage (CBC Evaluator)

## 📌 Deskripsi
Program berbasis Command Line Interface (CLI) sederhana yang ditulis dengan Python untuk mengevaluasi parameter Darah Lengkap (Complete Blood Count / CBC). Program ini dirancang untuk mempercepat *screening* awal pasien berdasarkan nilai laboratorium standar.

## 🩺 Parameter Klinis yang Dievaluasi
Saat ini, program dapat menganalisis 3 parameter utama:
*   **Hemoglobin (Hb):** Deteksi dini Anemia atau Polisitemia.
*   **Leukosit (WBC):** Skrining tanda infeksi sistemik (Leukopenia untuk curiga virus/Dengue, Leukositosis untuk curiga bakteri/peradangan akut).
*   **Trombosit (Platelet):** Evaluasi fungsi pembekuan darah (risiko perdarahan pada Trombositopenia atau risiko trombosis pada Trombositosis).

## 🚀 Cara Penggunaan
Pastikan Python sudah terinstal di komputermu. Buka terminal dan jalankan perintah berikut:

```bash
python LabChecker.py
