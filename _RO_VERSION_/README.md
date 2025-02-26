Script de Conversie Imagini - Descriere & Ghid de Instalare Prezentare Generală Acest script permite conversia imaginilor între diferite formate, inclusiv PNG, JPG, DDS și TGA. Scriptul scanează un folder de intrare, procesează imaginile și le salvează într-un folder de ieșire, generând în același timp un log cu rezultatele conversiei. De asemenea, oferă interacțiune cu utilizatorul pentru selecția formatelor.

Funcționalități ✅ Conversie între formatele PNG, JPG, DDS, TGA și WEBP ✅ Utilizează texconv.exe pentru conversia DDS ✅ Generează log-uri pentru fiecare conversie ✅ Permite selectarea interactivă a formatelor ✅ Creează automat folderul necesar pentru ieșire

Instalare și Configurare Pasul 1: Instalează Dependențele Necesare Asigură-te că ai instalat Python 3 pe sistemul tău. De asemenea, ai nevoie de anumite biblioteci Python.

Instalare module necesare Rulează următoarea comandă în terminal sau în linia de comandă:

pip install pillow imageio numpy

Pasul 2: Descarcă texconv.exe (Necesar pentru conversia DDS) Dacă intenționezi să convertești imagini în format DDS, trebuie să descarci și să plasezi texconv.exe în același director cu scriptul.

Descarcă texconv.exe aici: https://github.com/Microsoft/DirectXTex/releases

După descărcare, copiază texconv.exe în același folder unde ai scriptul conv.py.

Instrucțiuni de Utilizare Pasul 1: Pregătește Fișierele Creează un folder numit input în directorul scriptului. Plasează imaginile pe care vrei să le convertești în acest folder. Pasul 2: Rulează Scriptul Rulează scriptul utilizând comanda:

python conv.py

Pasul 3: Selectează Formatele La rulare, scriptul te va întreba:

Formatul fișierelor de intrare. Formatul dorit pentru conversie. Introdu numărul corespunzător formatului dorit.

Pasul 4: Verifică Fișierele Convertite Imaginile convertite vor fi salvate în folderul output. Log-ul conversiei va fi salvat în log.txt.

Depanare (Troubleshooting) Erori Comune & Soluții ❌ Eroare: texconv.exe nu a fost găsit ✔ Soluție: Asigură-te că texconv.exe este plasat în folderul scriptului.

❌ Eroare: [X] Folderul 'input' nu există! ✔ Soluție: Creează un folder numit input și adaugă imaginile.

❌ Eroare: [X] Nu s-au găsit fișiere cu extensia .xxx în 'input' ✔ Soluție: Verifică dacă ai plasat imaginile în folderul input și dacă ai ales formatul corect.

Note Suplimentare Evită modificarea secțiunilor marcate cu "DON'T TOUCH IF YOU DON'T KNOW WHAT ARE YOU DOING". Scriptul suportă conversia între formatele .PNG, .JPG, .TGA și .DDS. Procesul de conversie utilizează Pillow pentru majoritatea formatelor și texconv.exe pentru DDS. 🚀 Acum ești pregătit să începi conversia imaginilor! 🚀
