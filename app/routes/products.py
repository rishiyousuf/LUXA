from flask import Blueprint, render_template, request, jsonify
from app.models import Product, Review
from sqlalchemy import and_

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/')
def products_list():
    """Products listing page with filters"""
    # Get filter parameters
    page = request.args.get('page', 1, type=int)
    category = request.args.get('category', None)
    brand = request.args.get('brand', None)
    min_price = request.args.get('min_price', 0, type=float)
    max_price = request.args.get('max_price', 999999, type=float)
    
    # Build query
    query = Product.query
    
    if category:
        query = query.filter_by(category=category)
    if brand:
        query = query.filter_by(brand=brand)
    
    query = query.filter(and_(Product.price >= min_price, Product.price <= max_price))
    
    # Pagination
    per_page = 12
    products = query.paginate(page=page, per_page=per_page)
    
    # Get unique brands and categories for filters
    brands = [b[0] for b in db.session.query(Product.brand).distinct()]
    categories = [c[0] for c in db.session.query(Product.category).distinct()]
    
    return render_template('products.html', 
                         products=products,
                         brands=brands,
                         categories=categories,
                         current_brand=brand,
                         current_category=category)

@bp.route('/<int:product_id>')
def product_detail(product_id):
    """Product detail page"""
    product = Product.query.get_or_404(product_id)
    reviews = Review.query.filter_by(product_id=product_id).all()
    avg_rating = sum([r.rating for r in reviews]) / len(reviews) if reviews else 0
    
    return render_template('product_detail.html', 
                         product=product,
                         reviews=reviews,
                         avg_rating=avg_rating)

@bp.route('/<int:product_id>/reviews', methods=['POST'])
def add_review(product_id):
    """Add review to product"""
    product = Product.query.get_or_404(product_id)
    
    author = request.form.get('author')
    rating = request.form.get('rating', type=int)
    comment = request.form.get('comment')
    
    review = Review(product_id=product_id, author=author, rating=rating, comment=comment)
    db.session.add(review)
    db.session.commit()
    
    return redirect(f'/products/{product_id}')

from app import db
