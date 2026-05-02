from flask import Blueprint, render_template, request, redirect, url_for, session
from app import db
from app.models import User, Wishlist, Product
from werkzeug.security import check_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['user_email'] = user.email
            return redirect(url_for('main.home'))
        else:
            error = 'Invalid email or password'
            return render_template('login.html', error=error)
    
    return render_template('login.html')

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """User registration"""
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            error = 'Passwords do not match'
            return render_template('signup.html', error=error)
        
        if User.query.filter_by(email=email).first():
            error = 'Email already registered'
            return render_template('signup.html', error=error)
        
        username = email.split('@')[0]
        user = User(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        session['user_id'] = user.id
        session['username'] = user.username
        session['user_email'] = user.email
        
        return redirect(url_for('main.home'))
    
    return render_template('signup.html')

@bp.route('/logout')
def logout():
    """User logout"""
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('user_email', None)
    return redirect(url_for('main.home'))

@bp.route('/profile')
def profile():
    """User profile"""
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    
    user = User.query.get(user_id)
    wishlists = Wishlist.query.filter_by(user_id=user_id).all()
    
    return render_template('profile.html', user=user, wishlists=wishlists)

@bp.route('/wishlist/add/<int:product_id>')
def add_to_wishlist(product_id):
    """Add product to wishlist"""
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    
    product = Product.query.get_or_404(product_id)
    
    # Check if already in wishlist
    existing = Wishlist.query.filter_by(user_id=user_id, product_id=product_id).first()
    if not existing:
        wishlist = Wishlist(user_id=user_id, product_id=product_id)
        db.session.add(wishlist)
        db.session.commit()
    
    return redirect(request.referrer or url_for('products.products_list'))

@bp.route('/wishlist/remove/<int:wishlist_id>')
def remove_from_wishlist(wishlist_id):
    """Remove product from wishlist"""
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    
    wishlist = Wishlist.query.get_or_404(wishlist_id)
    
    if wishlist.user_id == user_id:
        db.session.delete(wishlist)
        db.session.commit()
    
    return redirect(request.referrer or url_for('auth.profile'))
