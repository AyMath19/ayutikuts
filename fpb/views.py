from django.shortcuts import render

# Create your views here.
def fpb(request):
    judul = ["Apabila (a, b) = d, buktikan bahwa d|(ax + by) untuk setiap bilangan-bilangan bulat x dan y.", "Buktikan bahwa ((a,b), b) = (a, b)", "jika (a, b) = 1 dan c|a, buktikan bahwa (c, b) = 1"]
    gambaranumum = "Karena 1 adalah pembagi (faktor) dari setiap bilangan bulat, maka 1 adalah faktor persekutuan dari dua bilangan bulat sembarang a dan b. Jadi himpunan faktor persekutuan dari a dan b tidak pemah kosong."

    konteks = {
        'jdl': judul,
        'gbrumum': gambaranumum,
    }  
    return render(request,'fpb.html', konteks)