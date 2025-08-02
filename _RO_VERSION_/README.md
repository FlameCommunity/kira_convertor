Script de Conversie Imagini - Descriere & Ghid de Instalare Prezentare Generală Acest script permite conversia imaginilor între diferite formate, inclusiv PNG, JPG, DDS, TGA, WEBP, ICO și BMP. Scriptul scanează un folder de intrare, procesează imaginile și le salvează într-un folder de ieșire, generând în același timp un log cu rezultatele conversiei. De asemenea, oferă interacțiune cu utilizatorul pentru selecția formatelor.

Funcționalități ✅ Conversie între formatele PNG, JPG, DDS, TGA, WEBP, ICO and BMP ✅ Utilizează texconv.exe pentru conversia DDS ✅ Generează log-uri pentru fiecare conversie ✅ Permite selectarea interactivă a formatelor ✅ Creează automat folderul necesar pentru ieșire

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

Acest script Python a fost actualizat pentru a suporta conversia imaginilor în și din formatul ICO, pe lângă formatele deja existente: PNG, JPG, DDS, TGA, WEBP, ICO și BMP.

Funcționalități principale:
📂 Conversie automată a tuturor fișierelor dintr-un folder specificat.
🎨 Suport pentru formatele PNG, JPG, DDS, TGA, WEBP, ICO și BMP.
📝 Logare automată a tuturor conversiilor și erorilor într-un fișier log.txt.
🔄 Procesare rapidă și interfață prietenoasă cu mesaje colorate în terminal.
⚡ Conversia fișierelor WEBP la alte formate și viceversa, cu setare implicită de calitate 90 pentru WebP.
Acum poți converti imagini cu ușurință între multiple formate, inclusiv WEBP, folosind acest script simplu și eficient. 🚀

------------------------------------------------------------------------------------------------------------------------------------------------
[UPDATE]
Fișierul syserr.txt
– Înregistrează toate erorile întâmpinate în timpul conversiei (calea fișierului sursă → destinație și mesajul de eroare).
– Este golit automat la începutul fiecărei rulări.

Mesaj final („EndTask”)
– Afișează numărul total de imagini procesate și procentajul de conversii reușite, ex: 25/25 (100%).
– Dacă una sau mai multe conversii eșuează, listează în syserr.txt detaliile erorilor și în log.txt mesajele complete de eroare.

Fișierul log.txt
– Păstrează un jurnal detaliat pentru fiecare fișier procesat: timestamp, stare ([OK] sau [X]), cale sursă și destinație, plus mesajele de eroare când apare excepție.

Ștergerea automată a syserr.txt
– La fiecare pornire a scriptului, syserr.txt este golit pentru a începe cu un jurnal curat al erorilor curente.

Output colorat în consolă
– Mesaje de stare afișate cu culori diferite (albastru pentru procesare, verde pentru succes, roșu pentru erori, galben pentru anunțuri).

Conversie DDS, TGA și BMP
– Suport direct pentru export în formatele TGA (folosind imageio), DDS (prin texconv.exe) și BMP (prin PIL), pe lângă PNG, JPG, WEBP și ICO.

Selecție interactivă a formatelor
– Meniuri în consolă pentru alegerea formatului de intrare și ieșire prin taste numerice.

Calcul și afișare a duratei totale
– Cronometrează întreg procesul și afișează timpul scurs în secunde la final.

Listă automată a fișierelor de intrare
– Scanează folderul input pentru toate imaginile cu extensia aleasă și procesează batch-ul fără intervenție manuală.
------------------------------------------------------------------------------------------------------------------------------------------------
