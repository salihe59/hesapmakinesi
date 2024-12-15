import tkinter as tk
from tkinter import messagebox

# Hesaplama işlevini tanımla
def hesapla():
    try:
        sayi1 = float(entry1.get())
        sayi2 = float(entry2.get())
        islem = secim.get()

        if islem == "Toplama":
            sonuc = sayi1 + sayi2
        elif islem == "Çıkarma":
            sonuc = sayi1 - sayi2
        elif islem == "Çarpma":
            sonuc = sayi1 * sayi2
        elif islem == "Bölme":
            if sayi2 == 0:
                messagebox.showerror("Hata", "Sıfıra bölme hatası!")
                return
            sonuc = sayi1 / sayi2
        elif islem == "Güç Alma":
            sonuc = sayi1 ** sayi2
        elif islem == "Karekök":
            if sayi1 < 0:
                messagebox.showerror("Hata", "Negatif sayının karekökü alınamaz!")
                return
            sonuc = sayi1 ** 0.5
        elif islem == "Mod":
            if sayi2 == 0:
                messagebox.showerror("Hata", "Mod işlemi için ikinci sayı sıfır olamaz!")
                return
            sonuc = sayi1 % sayi2
        else:
            messagebox.showerror("Hata", "Geçersiz işlem!")
            return

        # Sonucu ekranda göster
        label_sonuc.config(text=f"Sonuç: {sonuc}")

    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Hesap Makinesi")

# Pencereyi boyutlandır
root.geometry("400x400")

# Birinci sayı için etiket ve giriş alanı
label1 = tk.Label(root, text="Birinci Sayıyı Girin:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

# İkinci sayı için etiket ve giriş alanı
label2 = tk.Label(root, text="İkinci Sayıyı Girin:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

# İşlem seçimi için seçenekler
secim = tk.StringVar(root)
secim.set("Toplama")  # Varsayılan işlem

operation_menu = tk.OptionMenu(root, secim, "Toplama", "Çıkarma", "Çarpma", "Bölme", "Güç Alma", "Karekök", "Mod")
operation_menu.pack()

# Hesapla butonu
buton_hesapla = tk.Button(root, text="Hesapla", command=hesapla)
buton_hesapla.pack()

# Sonuç etiketi
label_sonuc = tk.Label(root, text="Sonuç: ")
label_sonuc.pack()

# Pencereyi çalıştır
root.mainloop()
