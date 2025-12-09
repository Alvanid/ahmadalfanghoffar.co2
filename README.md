
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profil - Ahmad Alfan Ghoffar</title>
    <meta name="description" content="Profil Ahmad Alfan Ghoffar - Mahasiswa Teknologi Informasi semester 7 di ITB Ahmad Dahlan Lamongan">

    <!-- Tambahkan tag meta untuk aksesibilitas -->
    <meta name="author" content="Ahmad Alfan Ghoffar">
    <meta name="keywords" content="profil, mahasiswa, teknologi informasi, ITB Ahmad Dahlan Lamongan">
    
    <!-- Tambahkan link ke font yang lebih mudah dibaca -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Tambahkan icon untuk Favicon -->
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>👨‍💻</text></svg>">

    <style>
        /* ================================
           RESET & ROOT VARIABLES
        ================================= */
        :root {
            --primary-color: #4f46e5;
            --primary-light: #6366f1;
            --primary-dark: #3730a3;
            --accent-color: #8b5cf6;
            --secondary-color: #ec4899;
            --text-primary: #f8fafc;
            --text-secondary: #cbd5e1;
            --text-muted: #94a3b8;
            --bg-primary: #0f172a;
            --bg-secondary: #1e293b;
            --bg-tertiary: #334155;
            --surface: rgba(30, 41, 59, 0.8);
            --surface-light: rgba(51, 65, 85, 0.6);
            --border-color: rgba(148, 163, 184, 0.1);
            --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.1);
            --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.15);
            --shadow-lg: 0 16px 40px rgba(0, 0, 0, 0.2);
            --shadow-xl: 0 24px 60px rgba(0, 0, 0, 0.25);
            --gradient-primary: linear-gradient(135deg, var(--primary-color), var(--primary-light));
            --gradient-accent: linear-gradient(135deg, var(--accent-color), var(--secondary-color));
            --focus-outline: 2px solid var(--accent-color);
            --focus-offset: 2px;
        }

        /* Tambahkan style untuk skip navigation link */
        .skip-link {
            position: absolute;
            top: -40px;
            left: 0;
            background: var(--primary-color);
            color: white;
            padding: 8px;
            z-index: 100;
            transition: top 0.3s;
        }

        .skip-link:focus {
            top: 0;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.6;
            overflow-x: hidden;
            scroll-behavior: smooth;
        }

        /* Background Pattern */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                radial-gradient(circle at 25% 25%, rgba(79, 70, 229, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 75% 75%, rgba(139, 92, 246, 0.1) 0%, transparent 50%);
            z-index: -1;
            pointer-events: none;
        }

        /* Typography */
        h1, h2, h3 {
            font-weight: 700;
            line-height: 1.2;
        }

        p {
            color: var(--text-secondary);
            margin-bottom: 1rem;
        }

        a {
            color: var(--primary-light);
            text-decoration: none;
            transition: color 0.3s ease;
        }

        a:hover {
            color: var(--accent-color);
        }

        /* Tambahkan style untuk focus indicators yang lebih jelas */
        a:focus,
        button:focus,
        input:focus,
        textarea:focus,
        select:focus {
            outline: var(--focus-outline);
            outline-offset: var(--focus-offset);
        }

        /* Loading Screen */
        .loader-wrapper {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: var(--bg-primary);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            transition: opacity 0.5s ease;
        }

        .loader {
            width: 60px;
            height: 60px;
            border: 3px solid var(--border-color);
            border-top-color: var(--primary-color);
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        /* Container */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        /* Navigation */
        header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border-color);
            z-index: 1000;
            transition: all 0.3s ease;
        }

        header.scrolled {
            background: rgba(15, 23, 42, 0.98);
            box-shadow: var(--shadow-md);
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.5rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 800;
            background: var(--gradient-primary);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
            list-style: none;
        }

        .nav-links a {
            color: var(--text-secondary);
            font-weight: 500;
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            transition: all 0.3s ease;
            position: relative;
        }

        .nav-links a:hover {
            color: var(--text-primary);
            background: var(--surface-light);
        }

        .nav-links a.active {
            color: var(--primary-color);
            background: rgba(79, 70, 229, 0.1);
        }

        /* Hero Section */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 6rem 2rem 4rem;
            text-align: center;
            position: relative;
            background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
        }

        .hero-content {
            max-width: 800px;
            position: relative;
            z-index: 2;
        }

        .profile-container {
            margin-bottom: 3rem;
            position: relative;
            display: inline-block;
        }

        .profile-sphere {
            width: 220px;
            height: 220px;
            border-radius: 50%;
            background: var(--gradient-primary);
            padding: 4px;
            position: relative;
            animation: float 6s ease-in-out infinite;
            box-shadow: 0 0 40px rgba(79, 70, 229, 0.4);
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }

        .profile-img {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid var(--bg-primary);
        }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            background: var(--gradient-primary);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: fadeInUp 0.8s ease;
        }

        .hero-subtitle {
            font-size: 1.125rem;
            color: var(--text-secondary);
            margin-bottom: 2rem;
            animation: fadeInUp 0.8s ease 0.2s both;
        }

        .hero-description {
            font-size: 1.125rem;
            color: var(--text-muted);
            margin-bottom: 3rem;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            animation: fadeInUp 0.8s ease 0.4s both;
        }

        .hero-buttons {
            display: flex;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
            animation: fadeInUp 0.8s ease 0.6s both;
        }

        .btn-primary {
            display: inline-block;
            padding: 1rem 2.5rem;
            background: var(--gradient-primary);
            color: white;
            font-weight: 600;
            border-radius: 2rem;
            text-decoration: none;
            transition: all 0.3s ease;
            box-shadow: var(--shadow-md);
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }
        
        .btn-secondary {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 1rem 2.5rem;
            background: transparent;
            color: var(--primary-light);
            font-weight: 600;
            border-radius: 2rem;
            text-decoration: none;
            border: 2px solid var(--primary-light);
            transition: all 0.3s ease;
        }

        .btn-secondary:hover {
            background: var(--primary-light);
            color: white;
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }

        /* Download Icon */
        .download-icon {
            width: 18px;
            height: 18px;
            fill: currentColor;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Section Styles */
        section {
            padding: 6rem 0;
            position: relative;
        }

        .section-title {
            font-size: 2.5rem;
            margin-bottom: 3rem;
            text-align: center;
            background: var(--gradient-primary);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        /* Card Component */
        .card {
            background: var(--surface);
            backdrop-filter: blur(20px);
            border: 1px solid var(--border-color);
            border-radius: 1.5rem;
            padding: 3rem;
            box-shadow: var(--shadow-md);
            transition: all 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-xl);
            border-color: rgba(79, 70, 229, 0.3);
        }

        /* Info Grid */
        .info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .info-item {
            background: var(--surface-light);
            padding: 1.5rem;
            border-radius: 1rem;
            border-left: 4px solid var(--primary-color);
            transition: all 0.3s ease;
            display: flex;
            align-items: flex-start;
            gap: 1rem;
        }

        .info-item:hover {
            transform: translateX(5px);
            background: var(--surface);
            box-shadow: var(--shadow-sm);
        }

        .info-item .icon {
            width: 24px;
            height: 24px;
            flex-shrink: 0;
            margin-top: 2px;
        }

        .info-item-content {
            flex-grow: 1;
        }

        .info-item strong {
            color: var(--text-primary);
            display: block;
            margin-bottom: 0.5rem;
        }

        /* Timeline */
        .timeline {
            position: relative;
            padding-left: 3rem;
            margin: 3rem 0;
        }

        .timeline::before {
            content: '';
            position: absolute;
            left: 1rem;
            top: 0;
            bottom: 0;
            width: 2px;
            background: var(--gradient-primary);
        }

        .timeline-item {
            position: relative;
            margin-bottom: 2.5rem;
            animation: fadeInUp 0.8s ease both;
        }

        .timeline-item::before {
            content: '';
            position: absolute;
            left: -2.5rem;
            top: 0.5rem;
            width: 1rem;
            height: 1rem;
            border-radius: 50%;
            background: var(--primary-color);
            border: 3px solid var(--bg-primary);
            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.2);
        }

        .timeline-date {
            display: inline-block;
            padding: 0.25rem 1rem;
            background: rgba(79, 70, 229, 0.1);
            color: var(--primary-light);
            border-radius: 1rem;
            font-size: 0.875rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
        }

        .timeline-title {
            font-size: 1.25rem;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 0.5rem;
        }

        .timeline-subtitle {
            color: var(--accent-color);
            font-weight: 500;
            margin-bottom: 0.75rem;
        }

        .timeline-description {
            color: var(--text-muted);
            line-height: 1.7;
        }

        /* Parallax Sections */
        .parallax {
            background-attachment: fixed;
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }

        .parallax::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(15, 23, 42, 0.8);
            z-index: 1;
        }

        .parallax-content {
            position: relative;
            z-index: 2;
            max-width: 800px;
            padding: 0 2rem;
        }

        .parallax h2 {
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            color: white;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        }

        .parallax p {
            font-size: 1.25rem;
            color: rgba(255, 255, 255, 0.9);
            margin-bottom: 0;
        }

        /* Social Links */
        .social-links {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            flex-wrap: wrap;
        }

        .social-link {
            display: inline-flex;
            align-items: center;
            gap: 0.75rem;
            padding: 1rem 2rem;
            background: var(--surface-light);
            color: var(--text-primary);
            border-radius: 1rem;
            text-decoration: none;
            font-weight: 500;
            transition: all 0.3s ease;
            border: 1px solid var(--border-color);
        }

        .social-link:hover {
            background: var(--gradient-primary);
            color: white;
            transform: translateY(-3px);
            box-shadow: var(--shadow-md);
        }

        .social-link .icon {
            width: 24px;
            height: 24px;
            fill: currentColor;
        }

        /* Footer */
        footer {
            background: var(--bg-secondary);
            border-top: 1px solid var(--border-color);
            padding: 3rem 0;
            text-align: center;
        }

        footer p {
            color: var(--text-muted);
            margin: 0;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }

            .hero h1 {
                font-size: 2rem;
            }

            .hero-subtitle {
                font-size: 1rem;
            }

            .section-title {
                font-size: 2rem;
            }

            .parallax h2 {
                font-size: 2rem;
            }

            .card {
                padding: 2rem;
            }

            .timeline {
                padding-left: 2rem;
            }

            .timeline::before {
                left: 0.5rem;
            }

            .timeline-item::before {
                left: -1.5rem;
            }

            .info-grid {
                grid-template-columns: 1fr;
            }
        }

        /* Scroll Reveal */
        .reveal {
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.8s ease;
        }

        .reveal.active {
            opacity: 1;
            transform: translateY(0);
        }

        /* Notification Toast */
        .toast {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: var(--surface);
            border: 1px solid var(--border-color);
            border-left: 4px solid var(--primary-color);
            border-radius: 0.5rem;
            padding: 1rem 1.5rem;
            box-shadow: var(--shadow-lg);
            display: flex;
            align-items: center;
            gap: 1rem;
            transform: translateX(400px);
            transition: transform 0.3s ease;
            z-index: 1000;
        }

        .toast.show {
            transform: translateX(0);
        }

        .toast-icon {
            width: 24px;
            height: 24px;
            fill: var(--primary-color);
        }

        .toast-message {
            color: var(--text-primary);
            font-weight: 500;
        }

        /* Tambahkan style untuk mode kontras tinggi */
        @media (prefers-contrast: high) {
            :root {
                --primary-color: #0000ff;
                --primary-light: #4d4dff;
                --primary-dark: #000080;
                --accent-color: #9933ff;
                --secondary-color: #ff00ff;
                --text-primary: #ffffff;
                --text-secondary: #e0e0e0;
                --text-muted: #b0b0b0;
                --bg-primary: #000000;
                --bg-secondary: #1a1a1a;
                --bg-tertiary: #333333;
                --surface: rgba(26, 26, 26, 0.9);
                --surface-light: rgba(51, 51, 51, 0.8);
                --border-color: #ffffff;
            }
        }

        /* Tambahkan style untuk mode gerak berkurang */
        @media (prefers-reduced-motion: reduce) {
            * {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        }
    </style>
</head>

<body>
    <!-- Skip Navigation Link -->
    <a href="#main-content" class="skip-link">Langsung ke konten utama</a>

    <!-- Loading Screen -->
    <div class="loader-wrapper" role="status" aria-label="Memuat konten">
        <div class="loader"></div>
    </div>

    <!-- Navigation -->
    <header id="header" role="banner">
        <nav role="navigation" aria-label="Navigasi utama">
            <div class="logo">Ahmad Alfan Ghoffar</div>
            <ul class="nav-links">
                <li><a href="#about" class="nav-link">Tentang</a></li>
                <li><a href="#motivation" class="nav-link">Motivasi</a></li>
                <li><a href="#contact" class="nav-link">Kontak</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero" id="main-content" role="main">
        <div class="hero-content">
            <div class="profile-container">
                <div class="profile-sphere">
                    <img src="https://z-cdn-media.chatglm.cn/files/b006107e-2989-42c4-9a80-9bb3a0b69979.jpg?auth_key=1865260309-1ed5a895e4f5405fa1efe56080913f6b-0-44e064aad0e6baa0f58a229c8ced7659" alt="Foto profil Ahmad Alfan Ghoffar" class="profile-img">
                </div>
            </div>
            <h1>Ahmad Alfan Ghoffar</h1>
            <!-- Removed hero-tagline and hero-skills sections -->
            <p class="hero-subtitle">Mahasiswa Teknologi Informasi | Semester 7</p>
            <p class="hero-description">
                Saya adalah mahasiswa yang berdedikasi dan siap belajar teknologi baru. 
                Siap berkontribusi melalui pengalaman kerja nyata dalam dunia IT.
            </p>
           <div class="hero-buttons">
    <a href="#contact" class="btn-primary" aria-label="Hubungi Ahmad Alfan Ghoffar">Hubungi Saya</a>
    
    <!-- Tombol Unduh CV -->
    <a href="dokumen/CV Ahmad Alfan Ghoffar ITB Ahmad Dahlan Lamongan.pdf" 
       download="CV Ahmad Alfan Ghoffar ITB Ahmad Dahlan Lamongan.pdf" 
       class="btn-secondary" 
       id="download-cv" 
       aria-label="Unduh CV Ahmad Alfan Ghoffar ITB Ahmad Dahlan Lamongan">
        <svg class="download-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/>
        </svg>
        Unduh CV
    </a>
</div>

<!-- Opsional: Tambahkan notifikasi jika unduhan berhasil dimulai -->
<script>
    document.getElementById('download-cv').addEventListener('click', function(e) {
        // Anda bisa menambahkan notifikasi sederhana di sini jika mau
        // Contoh: console.log('CV sedang diunduh...');
        // Atau tampilkan alert:
        // alert('Terima kasih! CV Anda sedang diunduh.');
    });
</script>

<script>
    document.getElementById('download-cv').addEventListener('click', function(e) {
        // Pastikan file ada sebelum mencoba mengunduh
        const fileUrl = this.getAttribute('href');
        
        // Coba untuk memeriksa apakah file ada (metode ini mungkin tidak bekerja di semua browser karena CORS)
        fetch(fileUrl, { method: 'HEAD' })
            .then(response => {
                if (!response.ok) {
                    // Jika file tidak ditemukan, tampilkan pesan
                    e.preventDefault();
                    alert('Maaf, CV sedang tidak tersedia. Silakan hubungi langsung untuk mendapatkan CV.');
                    return false;
                }
                // Jika file ada, biarkan unduhan berlanjut
            })
            .catch(error => {
                // Jika terjadi error (misalnya CORS), biarkan unduhan berlanjut
                console.log('Tidak dapat memverifikasi file, melanjutkan unduhan...');
            });
    });
</script>
                </a>
            </div>
        </div>
    </section>

    <!-- Parallax Section 1 -->
    <section class="parallax" style="background-image: url('https://picsum.photos/seed/portfolio1/1920/1080.jpg');" aria-label="Gambar latar belakang profil">
        <div class="parallax-content reveal">
            <h2>Selamat Datang di Profil Saya</h2>
            <p>Halaman profil modern dengan desain yang bersih dan profesional</p>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="container" aria-labelledby="about-heading">
        <div class="card reveal">
            <div style="text-align: center; margin-bottom: 2rem;">
                <img src="https://z-cdn-media.chatglm.cn/files/b006107e-2989-42c4-9a80-9bb3a0b69979.jpg?auth_key=1865260309-1ed5a895e4f5405fa1efe56080913f6b-0-44e064aad0e6baa0f58a229c8ced7659" alt="Foto Ahmad Alfan Ghoffar" style="width: 120px; height: 120px; border-radius: 50%; object-fit: cover; border: 4px solid var(--primary-color);">
            </div>
            <h2 class="section-title" id="about-heading">Profil Lengkap</h2>

            <!-- Personal Information -->
            <div class="info-grid">
                <div class="info-item">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                        <circle cx="12" cy="7" r="4"></circle>
                    </svg>
                    <div class="info-item-content">
                        <strong>Nama Lengkap</strong>
                        Ahmad Alfan Ghoffar
                    </div>
                </div>
                <div class="info-item">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M22 10v6M2 10l10-5 10 5-10 5z"></path>
                        <path d="M6 12v5c3 3 9 3 12 0v-5"></path>
                    </svg>
                    <div class="info-item-content">
                        <strong>NIM</strong>
                        2202010052
                    </div>
                </div>
                <div class="info-item">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                        <polyline points="22,6 12,13 2,6"></polyline>
                    </svg>
                    <div class="info-item-content">
                        <strong>Email</strong>
                        <a href="mailto:alfanghofar81@gmail.com">alfanghofar81@gmail.com</a>
                    </div>
                </div>
                <div class="info-item">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                    </svg>
                    <div class="info-item-content">
                        <strong>WhatsApp</strong>
                        <a href="https://wa.me/6285748730209" target="_blank" rel="noopener noreferrer">+62 857-4873-0209</a>
                    </div>
                </div>
                <div class="info-item">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="16" y1="2" x2="16" y2="6"></line>
                        <line x1="8" y1="2" x2="8" y2="6"></line>
                        <line x1="3" y1="10" x2="21" y2="10"></line>
                    </svg>
                    <div class="info-item-content">
                        <strong>Tempat, Tanggal Lahir</strong>
                        Lamongan, 29 Maret 2001
                    </div>
                </div>
            </div>

            <!-- Education Timeline -->
            <h3 style="margin-bottom: 2rem; color: var(--text-primary);">Riwayat Pendidikan</h3>
            <div class="timeline" role="list">
                <div class="timeline-item" role="listitem">
                    <span class="timeline-date">2022 - Sekarang</span>
                    <h3 class="timeline-title">ITB Ahmad Dahlan Lamongan</h3>
                    <p class="timeline-subtitle">S1 Teknologi Informasi</p>
                    <p class="timeline-description">
                        Fokus pada pengembangan web, database, dan pengembangan sistem informasi. 
                        
                    </p>
                </div>

                <div class="timeline-item" role="listitem">
                    <span class="timeline-date">2020 - 2022</span>
                    <h3 class="timeline-title">SMA Al-Kautsar Sekaran</h3>
                    <p class="timeline-subtitle">IPS</p>
                    <p class="timeline-description">
                        Mendalami ilmu pengetahuan sosial dengan fokus pada sejarah dan mendalami teknologi informasi.
                    </p>
                </div>

                <div class="timeline-item" role="listitem">
                    <span class="timeline-date">2016 - 2020</span>
                    <h3 class="timeline-title">Pondok Langitan Tuban</h3>
                    <p class="timeline-subtitle">Pendidikan Islam dan Mendalami kitab kuning</p>
                    <p class="timeline-description">
                        Mendalami ilmu agama Islam dengan tata kerama yang lebih.
                    </p>
                </div>

                <div class="timeline-item" role="listitem">
                    <span class="timeline-date">2013 - 2016</span>
                    <h3 class="timeline-title">SMP Negeri 1 Sekaran</h3>
                    <p class="timeline-subtitle">Pendidikan Menengah Pertama</p>
                    <p class="timeline-description">
                        Mempelajari dasar-dasar ilmu pengetahuan dan teknologi.
                    </p>
                </div>

                <div class="timeline-item" role="listitem">
                    <span class="timeline-date">2007 - 2013</span>
                    <h3 class="timeline-title">SD Negeri Kudikan</h3>
                    <p class="timeline-subtitle">Pendidikan Dasar</p>
                    <p class="timeline-description">
                        Mendapatkan fondasi pendidikan dasar yang kuat.
                    </p>
                </div>
            </div>

            <!-- Relevant Courses -->
            <h3 style="margin: 3rem 0 2rem; color: var(--text-primary);">Mata Kuliah Relevan</h3>
            <div class="info-grid">
                <div class="info-item">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <polyline points="16 18 22 12 16 6"></polyline>
                        <polyline points="8 6 2 12 8 18"></polyline>
                    </svg>
                    <div class="info-item-content">
                        <strong>Pemrograman Web</strong>
                        HTML, CSS, JavaScript, PHP
                    </div>
                </div>
                <div class="info-item">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <ellipse cx="12" cy="5" rx="9" ry="3"></ellipse>
                        <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path>
                        <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path>
                    </svg>
                    <div class="info-item-content">
                        <strong>Database</strong>
                        MySQL, SQL Server
                    </div>
                </div>
                <div class="info-item">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
                        <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
                    </svg>
                    <div class="info-item-content">
                        <strong>Jaringan Komputer</strong>
                        TCP/IP, Routing, Switching
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Motivation Section -->
    <section id="motivation" class="container" aria-labelledby="motivation-heading">
        <div class="card reveal">
            <h2 class="section-title" id="motivation-heading">Motivasi Magang</h2>
            <p style="font-size: 1.125rem; margin-bottom: 2rem; color: var(--text-secondary);">
                Fokus utama saya adalah mengembangkan diri dan siap mempelajari sistem kerja di perusahaan Anda.
            </p>
            <div class="info-grid">
                <div class="info-item">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"></path>
                        <polyline points="14,2 14,8 20,8"></polyline>
                        <line x1="16" y1="13" x2="8" y2="13"></line>
                        <line x1="16" y1="17" x2="8" y2="17"></line>
                        <polyline points="10,9 9,9 8,9"></polyline>
                    </svg>
                    <div class="info-item-content">
                        <strong>Semangat Belajar</strong>
                        Cepat adaptasi tools baru
                    </div>
                </div>
                <div class="info-item">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                        <circle cx="9" cy="7" r="4"></circle>
                        <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                        <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                    </svg>
                    <div class="info-item-content">
                        <strong>Kolaborasi</strong>
                        Cepat beradaptasi dalam lingkungan baru 
                    </div>
                </div>
                <div class="info-item">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                        <line x1="8" y1="21" x2="16" y2="21"></line>
                        <line x1="12" y1="17" x2="12" y2="21"></line>
                    </svg>
                    <div class="info-item-content">
                        <strong>Dasar IT</strong>
                        Siap bantu dokumentasi & support
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Parallax Section 2 -->
    <section class="parallax" style="background-image: url('https://picsum.photos/seed/portfolio2/1920/1080.jpg');" aria-label="Gambar latar belakang motivasi">
        <div class="parallax-content reveal">
            <h2>Motivasi Membawa Saya Maju</h2>
            <p>Dengan semangat belajar, saya berusaha menjadi lebih baik setiap hari</p>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="container" aria-labelledby="contact-heading">
        <div class="card reveal">
            <h2 class="section-title" id="contact-heading">Mari Terhubung</h2>
            <div class="social-links">
                <a href="https://wa.me/6285748730209" target="_blank" rel="noopener noreferrer" class="social-link" aria-label="Hubungi Ahmad Alfan Ghoffar melalui WhatsApp">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.149-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 2.16 3.912c2.861 2.498 5.979 2.248 7.166 1.364.198-.149.874-.874.874-1.685 0-.198-.075-.423-.324-.673zM12.043 20.534h-.006a9.96 9.96 0 01-5.342-1.557l-.383-.226-3.968 1.042 1.06-3.873-.25-.396A9.928 9.928 0 012.043 12c0-5.523 4.496-10.02 10.02-10.02 2.679 0 5.194 1.043 7.085 2.934A9.937 9.937 0 0122.063 12c0 5.523-4.496 10.02-10.02 10.02z"/>
                    </svg>
                    WhatsApp
                </a>
                <a href="https://www.instagram.com/alvn.id_?igsh=MWdkcDl4MjBqcXptcQ==" target="_blank" rel="noopener noreferrer" class="social-link" aria-label="Kunjungi profil Instagram Ahmad Alfan Ghoffar">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zM5.838 12a6.162 6.162 0 1112.324 0 6.162 6.162 0 01-12.324 0zM12 16a4 4 0 110-8 4 4 0 010 8zm4.965-10.405a1.44 1.44 0 112.881.001 1.44 1.44 0 01-2.881-.001z"/>
                    </svg>
                    Instagram
                </a>
                <a href="https://www.tiktok.com/@alvnn.id_?_r=1&_t=ZS-924ktGtazrj" target="_blank" rel="noopener noreferrer" class="social-link" aria-label="Kunjungi profil TikTok Ahmad Alfan Ghoffar">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.12 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/>
                    </svg>
                    TikTok
                </a>
                <a href="mailto:alfanghofar81@gmail.com" target="_blank" rel="noopener noreferrer" class="social-link" aria-label="Kirim email ke Ahmad Alfan Ghoffar">
                    <svg class="icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                        <polyline points="22,6 12,13 2,6"></polyline>
                    </svg>
                    Email
                </a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer role="contentinfo">
        <p>© 2025 Ahmad Alfan Ghoffar — Dibuat dengan Semangat Belajar</p>
    </footer>

    <!-- Notification Toast -->
    <div class="toast" id="download-toast" role="status" aria-live="polite">
        <svg class="toast-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
        </svg>
        <span class="toast-message">CV sedang diunduh...</span>
    </div>

    <script>
        // Loader
        window.addEventListener('load', function() {
            setTimeout(function() {
                const loader = document.querySelector('.loader-wrapper');
                loader.style.opacity = '0';
                setTimeout(() => {
                    loader.style.display = 'none';
                }, 500);
            }, 1000);
        });

        // Header scroll effect
        window.addEventListener('scroll', function() {
            const header = document.getElementById('header');
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });

        // Active navigation link
        const sections = document.querySelectorAll('section');
        const navLinks = document.querySelectorAll('.nav-link');

        window.addEventListener('scroll', () => {
            let current = '';
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.clientHeight;
                if (scrollY >= (sectionTop - 200)) {
                    current = section.getAttribute('id');
                }
            });

            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href').slice(1) === current) {
                    link.classList.add('active');
                }
            });
        });

        // Scroll reveal animation
        const reveals = document.querySelectorAll('.reveal');

        function revealOnScroll() {
            reveals.forEach(element => {
                const windowHeight = window.innerHeight;
                const elementTop = element.getBoundingClientRect().top;
                const elementVisible = 150;

                if (elementTop < windowHeight - elementVisible) {
                    element.classList.add('active');
                }
            });
        }

        window.addEventListener('scroll', revealOnScroll);
        revealOnScroll(); // Initial check

        // Smooth scrolling for navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                // Prevent default for anchor links, but not for others like 'mailto' or external links
                if (this.getAttribute('href').startsWith('#')) {
                    e.preventDefault();
                    const target = document.querySelector(this.getAttribute('href'));
                    if (target) {
                        target.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                }
            });
        });

        // Add animation delays to timeline items
        const timelineItems = document.querySelectorAll('.timeline-item');
        timelineItems.forEach((item, index) => {
            item.style.animationDelay = `${index * 0.1}s`;
        });

        // Fungsi untuk menampilkan notifikasi saat CV diunduh
        const downloadBtn = document.getElementById('download-cv');
        const toast = document.getElementById('download-toast');

        downloadBtn.addEventListener('click', function(e) {
            // Tampilkan notifikasi
            toast.classList.add('show');
            
            // Sembunyikan notifikasi setelah 3 detik
            setTimeout(() => {
                toast.classList.remove('show');
            }, 3000);
        });

        // Tambahkan fitur aksesibilitas keyboard
        document.addEventListener('keydown', function(e) {
            // Tekan Tab untuk navigasi keyboard
            if (e.key === 'Tab') {
                document.body.classList.add('keyboard-nav');
            }
        });

        document.addEventListener('mousedown', function() {
            document.body.classList.remove('keyboard-nav');
        });

        // Tambahkan deteksi preferensi pengguna
        const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
        const prefersHighContrast = window.matchMedia('(prefers-contrast: high)');

        // Terapkan pengaturan berdasarkan preferensi pengguna
        if (prefersReducedMotion.matches) {
            document.body.classList.add('reduced-motion');
        }

        if (prefersHighContrast.matches) {
            document.body.classList.add('high-contrast');
        }

        // Perbarui pengaturan jika preferensi berubah
        prefersReducedMotion.addEventListener('change', (e) => {
            if (e.matches) {
                document.body.classList.add('reduced-motion');
            } else {
                document.body.classList.remove('reduced-motion');
            }
        });

        prefersHighContrast.addEventListener('change', (e) => {
            if (e.matches) {
                document.body.classList.add('high-contrast');
            } else {
                document.body.classList.remove('high-contrast');
            }
        });
    </script>
</body>
</html>
