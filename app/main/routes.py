import os
from flask import Blueprint, render_template, current_app, send_file, flash, redirect, url_for, Response
from app.models import Project
from app.contact.forms import ContactForm

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Halaman utama portofolio."""
    projects = Project.query.filter_by(is_featured=True).order_by(Project.created_at.desc()).all()
    form = ContactForm()
    return render_template('index.html', projects=projects, form=form)


@main_bp.route('/download-cv')
def download_cv():
    """Endpoint untuk mengunduh file CV PDF."""
    filename_pdf = 'Ahmad_Alfan_Ghofar_CV.pdf'
    filepath = os.path.join(current_app.root_path, 'static', 'files', filename_pdf)

    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True, download_name=filename_pdf)
    else:
        flash('Dokumen CV PDF sedang disiapkan dan belum tersedia untuk diunduh.', 'warning')
        return redirect(url_for('main.index') + '#contact')


@main_bp.route('/robots.txt')
def robots():
    """File robots.txt untuk SEO."""
    return Response(render_template('robots.txt'), mimetype='text/plain')


@main_bp.route('/sitemap.xml')
def sitemap():
    """File sitemap.xml untuk SEO."""
    projects = Project.query.all()
    xml = render_template('sitemap.xml', projects=projects)
    return Response(xml, mimetype='application/xml')