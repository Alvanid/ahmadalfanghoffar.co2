from flask import Blueprint, render_template, abort
from app.models import Project

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/')
def list_projects():
    projects = Project.query.filter_by(is_featured=True).order_by(Project.created_at.desc()).all()
    return render_template('index.html', projects=projects) # Dikembalikan ke index untuk single page feel, atau buat halaman terpisah

@projects_bp.route('/<slug>')
def project_detail(slug):
    project = Project.query.filter_by(slug=slug).first_or_404()
    return render_template('project_detail.html', project=project)