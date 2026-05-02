# LUXA - Luxury Watches eCommerce Platform

A premium, modern eCommerce website for luxury watches built with Flask (Python) and responsive HTML/CSS/JavaScript.

## Features

### 🛍️ Core Features
- **Home Page**: Hero section with featured products and brand story
- **Products Page**: Grid layout with filters (price, brand, category)
- **Product Details**: Full product information, images, reviews, and add to cart
- **Shopping Cart**: Add/remove items, quantity adjustment, totals
- **Checkout**: Multi-step checkout with shipping information
- **Order Confirmation**: Order summary and status tracking
- **User Authentication**: Sign up, login, and profile management
- **Wishlist**: Save favorite products for later

### 🎨 Design Features
- **Luxury Theme**: Black, gold, and white color scheme
- **Responsive Design**: Mobile, tablet, and desktop optimized
- **Smooth Animations**: Fade-in effects, hover interactions, transitions
- **Modern Typography**: Clean, elegant fonts
- **Premium Styling**: Subtle shadows, proper spacing, high-quality layouts

### ⚙️ Admin Features
- **Admin Dashboard**: View stats and recent orders
- **Product Management**: Add, edit, and delete products
- **Order Management**: View and update order status
- **Admin Panel**: Secure admin area

### 🔒 Security Features
- **User Authentication**: Secure password hashing
- **Session Management**: Secure session handling
- **Form Validation**: Client-side and server-side validation
- **CSRF Protection Ready**: Flask structure supports CSRF tokens

## Tech Stack

### Backend
- **Framework**: Flask 2.3.3
- **Database**: SQLite (easily upgradeable to MySQL/PostgreSQL)
- **ORM**: SQLAlchemy
- **Security**: Werkzeug (password hashing)

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with flexbox and grid
- **JavaScript**: Vanilla JS for interactions and animations
- **Responsive**: Mobile-first approach

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone/Download Project
```bash
cd c:\Users\User\Desktop\web\luxury_watches
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Initialize Database
```bash
python run.py db init
python run.py seed-db  # Load sample products
python run.py create-admin  # Create admin user
```

### Step 5: Run the Application
```bash
python run.py
```

The application will be available at: **http://localhost:5000**

## Usage

### For Customers
1. Visit the home page
2. Browse products or use filters
3. View product details and reviews
4. Add items to cart
5. Proceed to checkout
6. Create account or continue as guest
7. Receive order confirmation

### For Admin
1. Navigate to `http://localhost:5000/admin/`
2. Login with admin credentials (admin@luxurywatches.com / admin123)
3. Manage products and orders from the dashboard

## Default Admin Credentials
- **Email**: admin@luxurywatches.com
- **Password**: admin123

⚠️ **Important**: Change these credentials in production!

## Project Structure

```
luxury_watches/
├── app/
│   ├── models.py           # Database models
│   ├── __init__.py         # Flask app initialization
│   ├── routes/
│   │   ├── main.py         # Home, about, contact pages
│   │   ├── products.py     # Products and details
│   │   ├── cart.py         # Shopping cart and checkout
│   │   ├── auth.py         # Authentication and profile
│   │   └── admin.py        # Admin dashboard
│   ├── templates/          # HTML templates
│   ├── static/
│   │   ├── css/style.css   # Main stylesheet
│   │   ├── js/main.js      # JavaScript
│   │   └── images/         # Images directory
├── config.py               # Configuration settings
├── run.py                  # Application entry point
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Customization

### Change Brand Name
1. Edit templates: Search for "LUXA" and replace with your brand
2. Update logo in `base.html`

### Change Colors
Edit CSS variables in `app/static/css/style.css`:
```css
:root {
    --primary-color: #000000;    /* Change to your primary color */
    --secondary-color: #d4af37;  /* Change to your accent color */
}
```

### Add More Products
Run the Django shell or directly add to database:
```bash
python run.py shell
>>> from app.models import Product
>>> from app import db
>>> p = Product(name="...", price=..., ...)
>>> db.session.add(p)
>>> db.session.commit()
```

## Advanced Features to Add

### Bonus Features (Ready for Implementation)
1. **Payment Integration**
   - Stripe integration
   - PayPal integration
   - Order payment confirmation

2. **Email Notifications**
   - Order confirmations
   - Shipping updates
   - Password reset emails

3. **Search Functionality**
   - Full-text product search
   - Search suggestions

4. **Analytics**
   - Page views
   - Popular products
   - Sales reports

5. **Email Marketing**
   - Newsletter signup
   - Promotional emails

6. **Advanced Admin**
   - User management
   - Sales reports and analytics
   - Inventory management

## Common Tasks

### Reset Database
```bash
# Delete old database
rm app/luxury_watches.db

# Reinitialize
python run.py db init
python run.py seed-db
python run.py create-admin
```

### Add New Routes
Create a new file in `app/routes/` and register in `app/__init__.py`

### Modify Database Schema
1. Update models in `app/models.py`
2. Delete database and reinitialize

## Deployment

### Production Checklist
- [ ] Change SECRET_KEY in config.py
- [ ] Set DEBUG = False
- [ ] Use environment variables for sensitive data
- [ ] Set up proper database (MySQL/PostgreSQL)
- [ ] Configure email service for notifications
- [ ] Set up SSL/HTTPS
- [ ] Add payment gateway
- [ ] Configure backup strategy
- [ ] Set up error logging
- [ ] Deploy to hosting service (Heroku, AWS, etc.)

## Troubleshooting

### Database Issues
```bash
# Reset everything
rm app/luxury_watches.db
python run.py db init
python run.py seed-db
```

### Port Already in Use
```bash
# Run on different port
python run.py --port 5001
```

### Missing Dependencies
```bash
pip install --upgrade -r requirements.txt
```

## Performance Optimization

- Images are optimized for web
- CSS is minified for production
- JavaScript is optimized
- Database queries are efficient
- Caching can be added with Flask-Caching

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## License

This project is open source and available under the MIT License.

## Support & Documentation

For issues or questions:
1. Check the troubleshooting section
2. Review the code comments
3. Consult Flask documentation: https://flask.palletsprojects.com/
4. SQLAlchemy docs: https://docs.sqlalchemy.org/

## Future Enhancements

- [ ] Progressive Web App (PWA)
- [ ] Mobile app (React Native)
- [ ] Advanced analytics dashboard
- [ ] AI-based product recommendations
- [ ] Live chat support
- [ ] Social media integration
- [ ] AR product preview

---

**Built with ❤️ for luxury watch enthusiasts**
