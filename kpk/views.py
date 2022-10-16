from django.shortcuts import render

# Create your views here.
def kpk(request):
    judul = ["Tunjukanlah bahwa setiap kelipatan persekutuan dari dua bilangan bulat positif mesti terbagi oleh kelipatan persekutuan terkecilnya.", "Jika c|a dan d|b dengan (c,d) = 1, apakah [a, b] = cd?"]
    gambaranumum = "Di Sekolah Dasar dan Sekolah Menengah Pertama, kita telah mempelajari kelipatan persekutuan terkecil (KPK) dari dua bilangan bulat atau lebih. Misalnya, kelipatan bulat positif dari 3 adalah 3, 6, 9, 12, 15, 18,.... Kelipatan bulat positif dari 4 adalah 4, 8, 12, 16, 20, 24, 28,..... Maka kelipatan persekutuan dari 3 dan 4 adalah 12, 24, 36, 48, .... Selanjutnya istilah kelipatan bulat positif hanya dikatakan lebih singkat menjadi kelipatan saja. Selanjutnya secara umum pengertian kelipatan persekutuan dari dua bilangan bulat dinyatakan dalam definisi berikut ini."

    konteks = {
        'jdl': judul,
        'gbrumum': gambaranumum,
    }
    return render(request, 'kpk.html', konteks)