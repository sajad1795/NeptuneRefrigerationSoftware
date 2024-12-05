import tkinter as tk

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

if __name__ == "__main__":
    setup_icons()
