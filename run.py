#!/usr/bin/env python
import os
from dotenv import load_dotenv
from app import create_app, db
from app.models import User, Product, Review

# Load environment variables
load_dotenv()

# Create Flask app
app = create_app(os.getenv('FLASK_ENV', 'development'))

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Product': Product}

@app.cli.command()
def init_db():
    """Initialize the database."""
    db.create_all()
    print('Database initialized.')

@app.cli.command()
def seed_db():
    """Seed the database with sample products."""
    # Clear existing products
    Product.query.delete()
    
    # Sample products
    products = [
        Product(
            name='Midnight Elegance',
            brand='Chronos Luxe',
            price=8500.00,
            category='Classic',
            description='A stunning timepiece with an impeccable black dial and gold accents.',
            image='https://images.unsplash.com/photo-1523170335684-f042070fe1c7?w=500&h=500&fit=crop',
            movement='Automatic',
            water_resistance='100m',
            case_material='Titanium'
        ),
        Product(
            name='Royal Crown',
            brand='Tempus Aurum',
            price=12500.00,
            category='Classic',
            description='Exquisite craftsmanship with a luxurious gold case and leather strap.',
            image='https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=500&h=500&fit=crop',
            movement='Mechanical',
            water_resistance='50m',
            case_material='Gold'
        ),
        Product(
            name='Modern Ascent',
            brand='Futura Watch Co',
            price=6800.00,
            category='Modern',
            description='Contemporary design meets Swiss precision in this stunning modern watch.',
            image='https://images.unsplash.com/photo-1501593346292-83386f59f3dd?w=500&h=500&fit=crop',
            movement='Quartz',
            water_resistance='200m',
            case_material='Silver'
        ),
        Product(
            name='Athletic Pro',
            brand='Sportus Elite',
            price=5200.00,
            category='Sports',
            description='High-performance sports watch designed for extreme conditions.',
            image='https://images.unsplash.com/photo-1592417817098-24ac0f513d77?w=500&h=500&fit=crop',
            movement='Automatic',
            water_resistance='500m',
            case_material='Titanium'
        ),
        Product(
            name='Celestial Wonder',
            brand='Cosmos Watches',
            price=9800.00,
            category='Modern',
            description='Inspired by the cosmos with starry night details and precision engineering.',
            image='https://images.unsplash.com/photo-1516992654410-c47ce1b90d3a?w=500&h=500&fit=crop',
            movement='Automatic',
            water_resistance='300m',
            case_material='Gold'
        ),
        Product(
            name='Heritage Classic',
            brand='Tempus Aurum',
            price=7500.00,
            category='Classic',
            description='A tribute to classic watchmaking with modern reliability.',
            image='https://images.unsplash.com/photo-1517421292736-97dcc56a96d1?w=500&h=500&fit=crop',
            movement='Mechanical',
            water_resistance='100m',
            case_material='Silver'
        ),
        Product(
            name='Urban Navigator',
            brand='Futura Watch Co',
            price=5800.00,
            category='Modern',
            description='Perfect companion for the modern urbanite. Sleek, sophisticated, reliable.',
            image='https://images.unsplash.com/photo-1523293182086-7651a899d37f?w=500&h=500&fit=crop',
            movement='Automatic',
            water_resistance='150m',
            case_material='Titanium'
        ),
        Product(
            name='Ocean Master',
            brand='Sportus Elite',
            price=4500.00,
            category='Sports',
            description='Built for underwater adventures with uncompromising durability.',
            image='https://images.unsplash.com/photo-1509941943669-30a3be3d402c?w=500&h=500&fit=crop',
            movement='Automatic',
            water_resistance='1000m',
            case_material='Titanium'
        ),
    ]
    
    for product in products:
        db.session.add(product)
    
    db.session.commit()
    print(f'Seeded database with {len(products)} products.')

@app.cli.command()
def create_admin():
    """Create admin user."""
    admin = User.query.filter_by(email='admin@luxurywatches.com').first()
    
    if admin:
        print('Admin user already exists.')
        return
    
    admin = User(
        username='admin',
        email='admin@luxurywatches.com',
        first_name='Admin',
        last_name='User'
    )
    admin.set_password('admin123')
    
    db.session.add(admin)
    db.session.commit()
    
    print('Admin user created: admin@luxurywatches.com / admin123')

if __name__ == '__main__':
    app.run(debug=True)
