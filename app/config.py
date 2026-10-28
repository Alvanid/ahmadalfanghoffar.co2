import os
from dotenv import load_dotenv

load_dotenv()

# 1. Dapatkan path absolut ke folder root proyek (satu level di atas folder 'app')
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# 2. Tentukan path folder instance
INSTANCE_DIR = os.path.join(BASE_DIR, 'instance')

# 3. Path absolut ke file database
DB_PATH = os.path.join(INSTANCE_DIR, 'portfolio.db')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'super-secret-key-ganti-ini-12345')
    
    # PENTING: Gunakan path absolut dengan format URL SQLite yang aman untuk Windows
    # Mengganti backslash (\) menjadi forward slash (/) agar dikenali SQLAlchemy
    SAFE_DB_PATH = DB_PATH.replace('\\', '/')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{SAFE_DB_PATH}'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Rate Limiting
    RATELIMIT_DEFAULT = os.environ.get('RATELIMIT_DEFAULT', '200 per day, 50 per hour')
    RATELIMIT_STORAGE_URL = "memory://"

    # Email (Opsional)
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# Debug print untuk memastikan path sudah benar
print(f"✅ [DEBUG] Folder Instance: {INSTANCE_DIR}")
print(f"✅ [DEBUG] Database URI: {Config.SQLALCHEMY_DATABASE_URI}")