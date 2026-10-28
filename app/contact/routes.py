from flask import Blueprint, render_template, flash, redirect, url_for, current_app
from app.extensions import limiter
from app.contact.forms import ContactForm
from app.models import ContactMessage
from app.extensions import db

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/send', methods=['GET', 'POST'])
@limiter.limit("5 per minute") # Rate limiting untuk mencegah spam
def send_message():
    form = ContactForm()
    if form.validate_on_submit():
        new_message = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(new_message)
        db.session.commit()
        
        # Di sini bisa ditambahkan logika pengiriman email nyata menggunakan Flask-Mail
        # Untuk saat ini, kita simpan ke database dan beri notifikasi sukses
        
        flash('Pesan Anda berhasil dikirim! Saya akan membalas secepatnya.', 'success')
        return redirect(url_for('main.index') + '#contact')
    
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error pada {getattr(form, field).label.text}: {error}", 'danger')

    return redirect(url_for('main.index') + '#contact')