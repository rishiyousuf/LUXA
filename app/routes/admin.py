from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Product, User, Order

bp = Blueprint('admin', __name__, url_prefix='/admin')

def admin_required(f):
    """Decorator to check if user is admin"""
    from functools import wraps
    from flask import session
    
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # For simplicity, we'll use a simple admin check
        # In production, implement proper role-based access control
        admin_emails = ['admin@luxurywatches.com']
        user_email = session.get('user_email')
        
        if not user_email or user_email not in admin_emails:
            return redirect(url_for('main.home'))
        
        return f(*args, **kwargs)
    
    return decorated_function

@bp.route('/')
@admin_required
def dashboard():
    """Admin dashboard"""
    total_products = Product.query.count()
    total_users = User.query.count()
    total_orders = Order.query.count()
    recent_orders = Order.query.order_by(Order.created_at.desc()).limit(5).all()
    
    return render_template('admin/dashboard.html',
                         total_products=total_products,
                         total_users=total_users,
                         total_orders=total_orders,
                         recent_orders=recent_orders)

@bp.route('/products')
@admin_required
def manage_products():
    """Manage products"""
    page = request.args.get('page', 1, type=int)
    products = Product.query.paginate(page=page, per_page=10)
    
    return render_template('admin/products.html', products=products)

@bp.route('/products/add', methods=['GET', 'POST'])
@admin_required
def add_product():
    """Add new product"""
    if request.method == 'POST':
        product = Product(
            name=request.form.get('name'),
            brand=request.form.get('brand'),
            price=request.form.get('price', type=float),
            description=request.form.get('description'),
            category=request.form.get('category'),
            image=request.form.get('image'),
            movement=request.form.get('movement'),
            water_resistance=request.form.get('water_resistance'),
            case_material=request.form.get('case_material')
        )
        
        db.session.add(product)
        db.session.commit()
        
        return redirect(url_for('admin.manage_products'))
    
    return render_template('admin/add_product.html')

@bp.route('/products/edit/<int:product_id>', methods=['GET', 'POST'])
@admin_required
def edit_product(product_id):
    """Edit product"""
    product = Product.query.get_or_404(product_id)
    
    if request.method == 'POST':
        product.name = request.form.get('name')
        product.brand = request.form.get('brand')
        product.price = request.form.get('price', type=float)
        product.description = request.form.get('description')
        product.category = request.form.get('category')
        product.image = request.form.get('image')
        product.movement = request.form.get('movement')
        product.water_resistance = request.form.get('water_resistance')
        product.case_material = request.form.get('case_material')
        
        db.session.commit()
        
        return redirect(url_for('admin.manage_products'))
    
    return render_template('admin/edit_product.html', product=product)

@bp.route('/products/delete/<int:product_id>')
@admin_required
def delete_product(product_id):
    """Delete product"""
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    
    return redirect(url_for('admin.manage_products'))

@bp.route('/orders')
@admin_required
def manage_orders():
    """Manage orders"""
    page = request.args.get('page', 1, type=int)
    orders = Order.query.order_by(Order.created_at.desc()).paginate(page=page, per_page=10)
    
    return render_template('admin/orders.html', orders=orders)

@bp.route('/orders/<int:order_id>/update-status', methods=['POST'])
@admin_required
def update_order_status(order_id):
    """Update order status"""
    order = Order.query.get_or_404(order_id)
    status = request.form.get('status')
    
    order.status = status
    db.session.commit()
    
    return redirect(url_for('admin.manage_orders'))
