from django.shortcuts import render

# Create your views here.
def relasi(request):
    prodi = "Buktikan bahwa jika a|b, maka a|mb untuk setiap bilangan bulat m."
    gambaranumum = "Semesta pembicaraan dalam Teori Bilangan adalah himpunan semua bilangan bulat. Bilangan-bilangan bulat dinyatakan dengan huruf-huruf latin kecil a, b, c,.., m, n,,,, dan sebagainya yang dapat bernilai positif, negatif atau nol. Namun banyak pembahasan dalam Teori Bilangan yang semesta pembicaraannya terbatas pada himpunan semua bilangan asli."

    konteks = {
        'prodi': prodi,
        'gbrumum': gambaranumum,
    }
    return render(request, 'relasi.html', konteks)