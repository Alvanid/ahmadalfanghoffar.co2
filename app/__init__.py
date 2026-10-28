import os
from flask import Flask, render_template
from app.config import Config
from app.extensions import db, csrf, limiter

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inisialisasi ekstensi
    db.init_app(app)
    csrf.init_app(app)
    limiter.init_app(app)

    # Registrasi Blueprint
    from app.main.routes import main_bp
    from app.projects.routes import projects_bp
    from app.contact.routes import contact_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(projects_bp, url_prefix='/projects')
    app.register_blueprint(contact_bp, url_prefix='/contact')

    # Error Handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('500.html'), 500

    # Buat database dan seed data jika belum ada
    with app.app_context():
        db.create_all()
        seed_data()

    return app

def seed_data():
    from app.models import Project
    if Project.query.count() == 0:
        projects = [
            Project(
                title="Aplikasi Prediksi Harga Saham LQ45",
                slug="prediksi-saham-lq45",
                short_description="Perancangan aplikasi prediksi harga saham LQ45 menggunakan Neural Network berbasis Backpropagation sebagai tugas akhir S1.",
                full_description="Proyek ini merupakan tugas akhir S1 yang berfokus pada implementasi Machine Learning untuk memprediksi tren harga saham. Menggunakan arsitektur Neural Network dengan algoritma Backpropagation, aplikasi ini memproses data historis untuk memberikan estimasi pergerakan harga. Dibangun dengan Python dan Flask, dilengkapi visualisasi data untuk memudahkan interpretasi hasil prediksi.",
                category="Machine Learning / Data Analysis",
                technologies="Python, Flask, SQLite, Scikit-learn, Matplotlib",
                project_status="Proyek Akademik",
                is_featured=True
            ),
            Project(
                title="Sistem Data Wilayah Administrasi Indonesia",
                slug="sistem-data-wilayah-indonesia",
                short_description="Perancangan sistem pengelolaan data wilayah administrasi Indonesia menggunakan PHP dan MySQL.",
                full_description="Sistem informasi berbasis web yang dirancang untuk mengelola dan memetakan data wilayah administrasi di Indonesia. Memungkinkan pengguna untuk melihat hierarki wilayah dari tingkat provinsi hingga desa. Dibangun dengan fokus pada struktur database yang efisien dan antarmuka yang mudah digunakan oleh administrator.",
                category="Web Development",
                technologies="PHP, MySQL, HTML, CSS, JavaScript",
                project_status="Selesai",
                is_featured=True
            ),
            Project(
                title="Portfolio Graphic Design",
                slug="portfolio-graphic-design",
                short_description="Galeri untuk menampilkan karya desain grafis yang benar-benar dimiliki pemilik website.",
                full_description="Koleksi kurasi karya desain visual yang mencakup pembuatan logo, poster, dan materi promosi digital. Setiap karya ditampilkan dengan resolusi tinggi dan deskripsi konsep di balik pembuatannya. Menunjukkan kemampuan dalam pengolahan desain visual dan pemahaman prinsip-prinsip desain grafis.",
                category="Graphic Design",
                technologies="Adobe Illustrator, Adobe Photoshop, Figma",
                project_status="Dalam Pengembangan",
                is_featured=True
            )
        ]
        db.session.bulk_save_objects(projects)
        db.session.commit()