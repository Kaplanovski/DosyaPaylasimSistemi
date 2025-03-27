# 📁 Dosya Paylaşım Sistemi

## Proje Hakkında
Dosya Paylaşım Sistemi (DPS), kullanıcıların dosyalarını güvenli bir şekilde yüklemelerini, bu dosyalara erişmelerini ve görüntülemelerini sağlayan bir **Flask web uygulamasıdır**. Kullanıcıların erişim yetkilendirmesi, 🆔 öğrenci numarası doğrulaması yoluyla gerçekleştirilir. Uygulama ayrıca 📂 dosya listeleme ve 📥 dosya indirme gibi işlevleri barındırır. Güvenlik önlemleri 🛡️ ve kullanıcı dostu bir tasarıma odaklanılarak oluşturulmuştur.

---

## ✨ Özellikler
- **🔒 Güvenlik**: Kullanıcı doğrulama ile yalnızca yetkilendirilmiş kişilerin erişimini sağlar.
- **📤 Dosya Yükleme**: Kullanıcıların dosyalarını kolay ve güvenli bir şekilde sisteme yüklemesine olanak tanır.
- **🗂️ Dosya Listeleme ve İndirme**: Yüklenen dosyalar listelenir ve kullanıcılar tarafından indirilebilir.

---

## 🛠️ Teknik Detaylar
- **🌐 Framework**: Flask, Python tabanlı bir web geliştirme framework'ü.
- **💾 Veritabanı**: MySQL, kullanıcı doğrulama ve veri saklama işlemleri için kullanılır.
- **🔑 Oturum Yönetimi**: Flask'in `session` özelliği, kullanıcıların oturumlarını güvenli bir şekilde yönetir.
- **📂 Dosya İşlemleri**: Dosyalar sistemde bir `uploads` klasöründe saklanır.

---

## 🔧 İşlevlerin Ayrıntıları

### 🆔 Kullanıcı Doğrulama
Sisteme giriş yapmak isteyen kullanıcılar, öğrenci numaralarını girerek doğrulama sürecinden geçer. Numara şu özelliklere sahip olmalıdır:
1. **11 haneli** olmalı.
2. **Yalnızca rakamlardan oluşmalı**.

Girilen öğrenci numarası, MySQL veritabanındaki `izinli_ogrenciler` tablosunda kontrol edilir. Eğer numara bu tabloda kayıtlı değilse kullanıcı giriş yapamaz.

---

### 📤 Dosya Yükleme
Kullanıcılar, dosya yükleme işlemine izin veren bir form aracılığıyla dosyalarını sisteme yükler. Yükleme sırasında:
- Dosyanın varlığı kontrol edilir.
- Dosya adı boş bırakılmışsa kullanıcıya bir hata mesajı gösterilir.
- Dosyalar, sistemde **`uploads`** klasörüne kaydedilir.

---

### 📥 Dosya Listeleme ve İndirme
Ana sayfada, yüklenen tüm dosyalar listelenir. Kullanıcılar bu dosyalara erişim sağlayabilir ve gerektiğinde indirebilir. Sistem, her bir dosya için güvenli bir erişim sağlar ve dosya önbelleklemesini otomatik olarak yönetir.

 🚀✨📄

## 🔧 Teknik Detaylar
- **🌐 Framework**: Flask, Python tabanlı bir web geliştirme framework'ü olarak kullanılmıştır.
- **💾 Veritabanı**: MySQL, kullanıcı doğrulama ve veri saklama işlemlerini destekler.
- **🔑 Oturum Yönetimi**: Flask'in `session` özelliği, giriş yapmış kullanıcıların oturumlarını takip eder.
- **📂 Dosya İşlemleri**: Python'un `os` modülü, dosya ve klasörlerin yönetimi için kullanılmıştır.
- **📤 Dosya Yükleme**: Yüklenen dosyalar `uploads` adlı bir klasörde saklanır ve gerektiğinde sunulur.

---

## 🛠️ Gereksinimler
1. **🖥️ İşletim Sistemi**: Windows, macOS veya Linux
2. **🐍 Python Sürümü**: Python 3.x
3. **📦 Gerekli Kütüphaneler**:
   - Flask:
     ```bash
     pip install flask
     ```
   - MySQL Connector:
     ```bash
     pip install mysql-connector-python
     ```
4. **💽 Veritabanı Sunucusu**:
   - XAMPP ya da MySQL Server
5. **🌍 Tarayıcı**: Güncel bir tarayıcı (Google Chrome, Firefox, vb.)

# 📸 Proje Ekran Görüntüleri 📸

Aşağıda projenin ekran görüntülerini bulabilirsiniz. Solda ve sağda yer alan görüntüler ekranın çalışma şeklini temsil ediyor.

| Giriş Ekranı 🏞️           | Dosya Paylaşım Ekranı 🏞️ |
|---------------------------|---------------------------|
| ![screen](./screen.png)   | ![screen2](./screen2.png) |
