from datetime import datetime
from app.extensions import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    short_description = db.Column(db.Text, nullable=False)
    full_description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    technologies = db.Column(db.String(200), nullable=False)
    thumbnail = db.Column(db.String(100), default='default-project.jpg')
    project_status = db.Column(db.String(50), default='Selesai')
    demo_url = db.Column(db.String(200), nullable=True)
    repository_url = db.Column(db.String(200), nullable=True)
    is_featured = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    images = db.relationship('ProjectImage', backref='project', lazy=True, cascade='all, delete-orphan')

class ProjectImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    image_path = db.Column(db.String(100), nullable=False)
    alt_text = db.Column(db.String(100), nullable=True)
    sort_order = db.Column(db.Integer, default=0)

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(150), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    processing_status = db.Column(db.String(50), default='Baru')