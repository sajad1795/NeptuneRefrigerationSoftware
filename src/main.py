import tkinter as tk
from tkinter import PhotoImage
import random

def setup_icons():
    # ایجاد پنجره اصلی نرم‌افزار
    root = tk.Tk()
    root.title("Neptune Refrigeration Software")

    # 1. تنظیم آیکون پنجره اصلی (آیکون 256x256 برای پنجره اصلی)
    root.iconbitmap("assets/icons/icon_256x256.ico")  # آیکون 256x256 برای پنجره اصلی

    # 2. تنظیم آیکون نوار وظیفه (آیکون 64x64 برای نوار وظیفه)
    root.iconphoto(True, tk.PhotoImage(file="assets/icons/icon_64x64.ico"))

    # 3. اضافه کردن دکمه‌ها با آیکون (آیکون 48x48 برای دکمه‌ها)
    button_icon = tk.PhotoImage(file="assets/icons/icon_48x48.png")  # آیکون 48x48 برای دکمه‌ها
    button = tk.Button(root, image=button_icon, command=lambda: print("Button clicked"))
    button.pack(pady=20)

    # 4. اضافه کردن دکمه‌هایی دیگر با آیکون‌های دیگر (آیکون 32x32 برای دکمه‌های کمکی)
    button2_icon = tk.PhotoImage(file="assets/icons/icon_32x32.png")
    button2 = tk.Button(root, image=button2_icon, command=lambda: print("Another button clicked"))
    button2.pack(pady=20)

    # 5. اضافه کردن دکمه‌هایی با آیکون 24x24 برای آیکون‌های کوچکتر
    button3_icon = tk.PhotoImage(file="assets/icons/icon_24x24.png")
    button3 = tk.Button(root, image=button3_icon, command=lambda: print("Yet another button clicked"))
    button3.pack(pady=20)

    # 6. استفاده از آیکون 16x16 برای نمایش در بخش‌های کوچکتر (مثلاً عنوان پنجره در تب‌ها)
    tab_icon = tk.PhotoImage(file="assets/icons/icon_16x16.png")
    # در اینجا فرض کرده‌ایم که از تَب‌ها یا پنجره‌های داخلی استفاده می‌کنیم
    tab_label = tk.Label(root, image=tab_icon, text="Tab Label", compound="left")
    tab_label.pack(pady=20)

    # اجرای برنامه
    root.mainloop()

class SplashScreen(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.title("Neptune Refrigeration Software")
        self.geometry("520x260")  # ابعاد پنجره اسپلش
        self.configure(bg='black')  # تنظیم پس‌زمینه
        self.images = [
            "assets/splash_image_1.png",
            "assets/splash_image_2.png",
            "assets/splash_image_3.png",
            "assets/splash_image_4.png",
            "assets/splash_image_5.png",
            "assets/splash_image_6.png",
            "assets/splash_image_7.png",
            "assets/splash_image_8.png",
            "assets/splash_image_9.png",
            "assets/splash_image_10.png",
            "assets/splash_image_11.png"
        ]
        random.shuffle(self.images)  # ترتیب رندوم تصاویر
        self.current_image = 0
        self.image_label = tk.Label(self)
        self.image_label.pack(fill="both", expand=True)

        self.show_next_image()

    def show_next_image(self):
        if self.current_image < len(self.images):
            image = PhotoImage(file=self.images[self.current_image])
            self.image_label.config(image=image)
            self.image_label.image = image
            self.current_image += 1
            
            # زمان نمایش تصویر اول 12 ثانیه و سایر تصاویر 10 ثانیه
            if self.current_image == 1:
                self.after(12000, self.show_next_image)  # 12 ثانیه برای تصویر اول
            else:
                self.after(10000, self.show_next_image)  # 10 ثانیه برای سایر تصاویر
        else:
            self.destroy()
            self.show_main_window()

    def show_main_window(self):
        # پس از تمام شدن اسپلش اسکرین، پنجره اصلی نرم‌افزار باز می‌شود
        main_window = tk.Tk()
        main_window.title("Neptune Refrigeration Software")
        main_window.geometry("1000x600")  # ابعاد پنجره نرم‌افزار
        label = tk.Label(main_window, text="Welcome to Neptune Refrigeration Software!", font=("Helvetica", 16))
        label.pack(pady=50)
        main_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # مخفی کردن پنجره اصلی تا نمایش اسپلش اسکرین
    splash = SplashScreen(root)
    splash.mainloop()
