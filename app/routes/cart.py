from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from app import db
from app.models import Cart, CartItem, Product, Order, OrderItem, User
from datetime import datetime
import uuid

bp = Blueprint('cart', __name__, url_prefix='/cart')

def get_or_create_cart():
    """Get or create shopping cart for current session"""
    session_id = session.get('session_id')
    if not session_id:
        session_id = str(uuid.uuid4())
        session['session_id'] = session_id
    
    cart = Cart.query.filter_by(session_id=session_id).first()
    if not cart:
        cart = Cart(session_id=session_id)
        db.session.add(cart)
        db.session.commit()
    
    return cart

@bp.route('/')
def view_cart():
    """View shopping cart"""
    cart = get_or_create_cart()
    total_price = sum(item.product.price * item.quantity for item in cart.items)
    
    return render_template('cart.html', cart=cart, total_price=total_price)

@bp.route('/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    """Add product to cart"""
    product = Product.query.get_or_404(product_id)
    quantity = request.form.get('quantity', 1, type=int)
    
    cart = get_or_create_cart()
    
    # Check if product already in cart
    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
    
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)
        db.session.add(cart_item)
    
    db.session.commit()
    
    return redirect(request.referrer or url_for('cart.view_cart'))

@bp.route('/update/<int:item_id>', methods=['POST'])
def update_cart_item(item_id):
    """Update cart item quantity"""
    cart_item = CartItem.query.get_or_404(item_id)
    quantity = request.form.get('quantity', 1, type=int)
    
    if quantity <= 0:
        db.session.delete(cart_item)
    else:
        cart_item.quantity = quantity
    
    db.session.commit()
    
    return redirect(url_for('cart.view_cart'))

@bp.route('/remove/<int:item_id>')
def remove_from_cart(item_id):
    """Remove item from cart"""
    cart_item = CartItem.query.get_or_404(item_id)
    db.session.delete(cart_item)
    db.session.commit()
    
    return redirect(url_for('cart.view_cart'))

@bp.route('/checkout', methods=['GET', 'POST'])
def checkout():
    """Checkout page"""
    if request.method == 'POST':
        cart = get_or_create_cart()
        
        if not cart.items:
            return redirect(url_for('cart.view_cart'))
        
        # Get form data
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        address = request.form.get('address')
        city = request.form.get('city')
        zip_code = request.form.get('zip')
        phone = request.form.get('phone')
        
        # Create or get user
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(
                username=email,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            db.session.add(user)
            db.session.commit()
        
        # Calculate total
        total_price = sum(item.product.price * item.quantity for item in cart.items)
        
        # Create order
        shipping_address = f"{address}, {city} {zip_code}"
        order = Order(
            user_id=user.id,
            total_price=total_price,
            shipping_address=shipping_address,
            status='confirmed'
        )
        db.session.add(order)
        db.session.commit()
        
        # Create order items
        for item in cart.items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.product.price,
                product_name=item.product.name
            )
            db.session.add(order_item)
        
        # Clear cart
        for item in cart.items:
            db.session.delete(item)
        
        db.session.commit()
        
        session['order_id'] = order.id
        return redirect(url_for('cart.order_confirmation', order_id=order.id))
    
    cart = get_or_create_cart()
    total_price = sum(item.product.price * item.quantity for item in cart.items)
    
    return render_template('checkout.html', cart=cart, total_price=total_price)

@bp.route('/order-confirmation/<int:order_id>')
def order_confirmation(order_id):
    """Order confirmation page"""
    order = Order.query.get_or_404(order_id)
    return render_template('order_confirmation.html', order=order)
