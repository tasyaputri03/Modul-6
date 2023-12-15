# Modul-6
Project praktikum modul 6 ini menggunakan MobileNetV2 sebagai model pretrained yang diambil menggunakan pustaka resNet. Instalasi python version >= 3.9.12 dengan https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe

environment - path : 3.9.12 
Vscode : pip install flask . pip install tensorflow . pip install pillow . pip install opencv-2 pip list python. 
Setelah itu install semua requirements pip install -r requirements Lalu jalankan flask python app.py

Web Image dapat diakses dengan url http://127.0.0.1:2000

Dataset Project ini menggunakan dataset rock, paper, scissors dengan jumlah data sebanyak 2520 file. Load image menggunakan image_dataset_from_directory dari pustaka resNet dengan pembagian train validation dan test validation dengan seed 123. Dataset menggunakan label categorical sehingga label dalam bentuk one hot encoding. Image size menggunakan (224, 244) dan batch size menggunakan 128.

#Local Development

Tampilan Awal


Tampilan Result
