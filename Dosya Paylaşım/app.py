from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory, flash
import mysql.connector
import os

# Flask uygulamasını başlatıyoruz
app = Flask(__name__)

# Gizli anahtar oturumlar için
app.secret_key = "supersecretkey"

# Veritabanı bağlantısı
db = mysql.connector.connect(
    host="localhost",         # XAMPP kullanıyorsanız genelde 'localhost'
    user="root",              # Varsayılan kullanıcı adı
    password="",              # Varsayılan şifre genelde boş bırakılır
    database="ngrok_proje"    # Oluşturduğunuz veritabanı adı
)
cursor = db.cursor()

# Yükleme yapılacak klasörü belirliyoruz
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Yüklenen dosyaların önbelleğe alınmasını devre dışı bırakıyoruz
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Giriş sayfası (Giriş yapılmadan index'e gidilmemeli)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        student_id = request.form['student_id']
        
        # Öğrenci numarasının 11 haneli olup olmadığını kontrol ediyoruz
        if len(student_id) != 11:
            flash("Öğrenci numarası 11 haneli olmalıdır!", "error")
            return redirect(url_for('login'))
        
        # Öğrenci numarasının sadece rakam olduğuna emin olalım
        if not student_id.isdigit():
            flash("Öğrenci numarası sadece rakamlardan oluşmalıdır!", "error")
            return redirect(url_for('login'))
        
        # Veritabanında öğrenci numarasını kontrol et
        query = "SELECT * FROM izinli_ogrenciler WHERE ogrenci_no = %s"
        cursor.execute(query, (student_id,))
        result = cursor.fetchone()
        
        if result:  # Eğer öğrenci numarası veritabanında varsa
            session['logged_in'] = True
            return redirect(url_for('index'))  # Giriş başarılı ise index sayfasına yönlendir
        else:
            flash("Geçersiz öğrenci numarası! Geri dönüp tekrar deneyin.", "error")
            return redirect(url_for('login'))

    return render_template('giris.html')  # GET isteği için giriş sayfası

# Ana sayfa
@app.route('/')
def index():
    if not session.get('logged_in'):  # Eğer giriş yapılmamışsa login sayfasına yönlendir
        return redirect(url_for('login'))  
    
    # Yüklenen dosyaların listesini alıyoruz
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)  # Ana sayfa (index.html)

# Dosya yükleme işlemi
@app.route('/upload', methods=['POST'])
def upload_file():
    if not session.get('logged_in'):  # Giriş kontrolü
        return redirect(url_for('login'))
    
    # Dosya var mı kontrolü
    if 'file' not in request.files:
        return 'No file part', 400  # Dosya yoksa hata döndürülür

    file = request.files['file']

    # Dosya seçilmediyse hata döndürülür
    if file.filename == '':
        return 'No selected file', 400

    # Yükleme klasörü yoksa oluşturuyoruz
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Dosya kaydediliyor
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    # Yükleme işlemi tamamlandıktan sonra ana sayfaya yönlendiriyoruz
    return redirect(url_for('index'))

# Yüklenen dosyayı sunmak için
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    if not session.get('logged_in'):  # Giriş kontrolü
        return redirect(url_for('login'))
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Flask uygulamasını çalıştırma
if __name__ == '__main__':
    app.run(debug=True)
