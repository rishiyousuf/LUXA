# DETAILED INSTALLATION GUIDE

## System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python**: Version 3.8 or higher
- **pip**: Python package manager (usually comes with Python)
- **Git** (optional, for cloning the repository)

## Step-by-Step Installation

### 1. Prerequisites Check

**Windows:**
```bash
python --version
```

**macOS/Linux:**
```bash
python3 --version
```

Make sure you have Python 3.8 or higher installed.

### 2. Navigate to Project Directory

```bash
cd c:\Users\User\Desktop\web\luxury_watches
```

### 3. Create Virtual Environment

A virtual environment isolates your project dependencies from system Python.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt after activation.

### 4. Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask 2.3.3
- Flask-SQLAlchemy 3.0.5
- Werkzeug 2.3.7
- python-dotenv 1.0.0

### 6. Initialize Database

**Windows:**
```bash
python run.py init-db
python run.py seed-db
python run.py create-admin
```

**macOS/Linux:**
```bash
python run.py init-db
python run.py seed-db
python run.py create-admin
```

This will:
- Create the SQLite database
- Load sample luxury watch products
- Create an admin user account

### 7. Start the Development Server

```bash
python run.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
```

### 8. Access the Application

Open your web browser and visit:
```
http://localhost:5000
```

## First Steps After Installation

### 1. View the Application
- **Home Page**: http://localhost:5000/
- **Products**: http://localhost:5000/products/
- **About**: http://localhost:5000/about

### 2. Admin Panel
- **URL**: http://localhost:5000/admin/
- **Email**: admin@luxurywatches.com
- **Password**: admin123

### 3. Create a Test Account
- Go to http://localhost:5000/auth/signup
- Create a new account
- Browse products and add to cart

### 4. Test Checkout
- Add items to cart
- Complete checkout
- Verify order confirmation

## Environment Variables

The `.env` file contains configuration settings. Default values are provided, but you can customize:

```
FLASK_ENV=development      # Set to 'production' for live deployment
FLASK_DEBUG=1              # Set to 0 in production
SECRET_KEY=...             # Change this for production
```

## File Structure Explained

```
luxury_watches/
│
├── app/                           # Main application package
│   ├── __init__.py               # Flask app initialization
│   ├── models.py                 # Database models (User, Product, Order, etc.)
│   │
│   ├── routes/                   # Route handlers
│   │   ├── main.py              # Home, About, Contact pages
│   │   ├── products.py          # Product listing and details
│   │   ├── cart.py              # Shopping cart and checkout
│   │   ├── auth.py              # Login, signup, user profile
│   │   └── admin.py             # Admin dashboard and management
│   │
│   ├── templates/                # HTML templates
│   │   ├── base.html            # Base template (extends to all pages)
│   │   ├── home.html            # Home page
│   │   ├── products.html        # Products listing
│   │   ├── product_detail.html  # Single product page
│   │   ├── cart.html            # Shopping cart
│   │   ├── checkout.html        # Checkout page
│   │   ├── order_confirmation.html
│   │   ├── login.html           # Login page
│   │   ├── signup.html          # Registration page
│   │   ├── profile.html         # User profile/account
│   │   ├── about.html           # About page
│   │   ├── contact.html         # Contact page
│   │   └── admin/               # Admin templates
│   │       ├── dashboard.html
│   │       ├── products.html
│   │       ├── add_product.html
│   │       ├── edit_product.html
│   │       └── orders.html
│   │
│   └── static/                   # Static files
│       ├── css/
│       │   └── style.css        # Complete styling
│       ├── js/
│       │   └── main.js          # JavaScript functionality
│       └── images/              # Image directory
│
├── config.py                     # Flask configuration
├── run.py                        # Application entry point
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment template
├── README.md                     # Main documentation
├── INSTALL.md                    # This file
└── quickstart.py                 # Quick setup script
```

## Database Schema

The application uses SQLite with the following main tables:

### Users Table
- id, username, email, password_hash, first_name, last_name, created_at

### Products Table
- id, name, brand, price, description, category, image, movement, water_resistance, case_material

### Orders Table
- id, user_id, total_price, status, shipping_address, created_at

### Cart Table
- id, session_id, created_at

### Reviews Table
- id, product_id, author, rating, comment, created_at

### Wishlists Table
- id, user_id, product_id, created_at

## Common Issues & Solutions

### Issue: "python: command not found"
**Solution**: Python might be installed but not in PATH. Try `python3` instead.

### Issue: "pip install fails"
**Solution**: Upgrade pip first:
```bash
python -m pip install --upgrade pip
```

### Issue: Port 5000 already in use
**Solution**: Modify `run.py` to use a different port:
```python
app.run(debug=True, port=5001)
```

### Issue: Database errors after changes
**Solution**: Delete the database and reinitialize:
```bash
# Delete old database
rm app/luxury_watches.db

# Or on Windows
del app\luxury_watches.db

# Reinitialize
python run.py init-db
python run.py seed-db
python run.py create-admin
```

### Issue: Templates not loading
**Solution**: Ensure you're running from the correct directory and templates folder exists.

### Issue: CSS/JS not loading
**Solution**: Hard refresh browser (Ctrl+Shift+R) or clear browser cache.

## Development Tips

### Enable Debug Mode
Already enabled by default. For production, set:
```
FLASK_DEBUG=0
```

### Database Query Testing
```bash
python
>>> from app import create_app, db
>>> from app.models import Product
>>> app = create_app()
>>> with app.app_context():
...     products = Product.query.all()
...     for p in products:
...         print(p.name, p.price)
```

### View Database
You can use SQLite browser to view the database:
- Download: https://sqlitebrowser.org/
- Open: `app/luxury_watches.db`

## Deployment Preparation

### For Heroku:
1. Create `Procfile`:
```
web: python run.py
```

2. Create `runtime.txt`:
```
python-3.11.0
```

3. Deploy:
```bash
git push heroku main
```

### For AWS/DigitalOcean:
1. Use a production WSGI server (Gunicorn)
2. Set up PostgreSQL instead of SQLite
3. Configure environment variables
4. Set up SSL/HTTPS

### For Local Production Testing:
```bash
pip install gunicorn
gunicorn -w 4 "app:create_app()"
```

## Customization Checklist

- [ ] Change site name/logo in base.html
- [ ] Update brand colors in CSS variables
- [ ] Add your own product images
- [ ] Create admin account with new password
- [ ] Customize welcome email text
- [ ] Update contact information
- [ ] Modify footer content
- [ ] Add social media links
- [ ] Set up email service
- [ ] Configure payment gateway

## Next Steps

1. **Customize the site**: Edit templates and CSS
2. **Add your products**: Use admin panel
3. **Test thoroughly**: Try checkout flow
4. **Set up email**: For order confirmations
5. **Prepare for production**: Update config, add HTTPS
6. **Deploy**: Choose hosting platform

## Support & Help

- **Python Issues**: https://www.python.org/
- **Flask Documentation**: https://flask.palletsprojects.com/
- **SQLAlchemy Docs**: https://docs.sqlalchemy.org/
- **HTML/CSS/JS**: https://developer.mozilla.org/

## Quick Reference Commands

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Run application
python run.py

# Access database shell
python

# Stop server
Ctrl + C

# Deactivate virtual environment
deactivate
```

---

**Congratulations! You're ready to launch your luxury watch eCommerce store! 🎉**
