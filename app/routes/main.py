from flask import Blueprint, render_template, session, request, redirect, url_for
from app import db
from app.models import Product, Review

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    """Home page with featured products"""
    featured_products = Product.query.limit(6).all()
    return render_template('home.html', featured_products=featured_products)

@bp.route('/about')
def about():
    """About us page"""
    return render_template('about.html')

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # In production, send email here
        # For now, just store in session
        session['contact_submitted'] = True
        return redirect(url_for('main.contact'))
    
    submitted = session.pop('contact_submitted', False)
    return render_template('contact.html', submitted=submitted)
