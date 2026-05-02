# LUXA - QUICK REFERENCE GUIDE

## 🚀 30-Second Quick Start

```bash
cd c:\Users\User\Desktop\web\luxury_watches
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py init-db
python run.py seed-db
python run.py create-admin
python run.py
```

Then open: **http://localhost:5000**

---

## 🔐 Default Login Credentials

| Role | Email | Password |
|------|-------|----------|
| Admin | admin@luxurywatches.com | admin123 |
| Test Customer | (create via signup) | (your choice) |

⚠️ **Change admin password immediately!**

---

## 📍 Key URLs

| Purpose | URL |
|---------|-----|
| Home | http://localhost:5000/ |
| Products | http://localhost:5000/products/ |
| Sign Up | http://localhost:5000/auth/signup |
| Login | http://localhost:5000/auth/login |
| Admin | http://localhost:5000/admin/ |
| About | http://localhost:5000/about |
| Contact | http://localhost:5000/contact |

---

## 📁 Important Files to Customize

| File | Purpose | Action |
|------|---------|--------|
| `app/templates/base.html` | Site header/footer | Update logo, company name |
| `app/static/css/style.css` | Colors & styling | Modify color variables |
| `config.py` | Settings | Change SECRET_KEY |
| `.env` | Environment vars | Set FLASK_ENV, SECRET_KEY |
| `README.md` | Documentation | Update project info |

---

## 🎨 Customization Tips

### Change Brand Colors
Edit `app/static/css/style.css` (line 7-15):
```css
:root {
    --primary-color: #000000;     /* Change to YOUR primary color */
    --secondary-color: #d4af37;   /* Change to YOUR accent color */
    --light-color: #ffffff;
    /* ... */
}
```

### Update Site Name
1. `app/templates/base.html` - Change "LUXA" to your name
2. `config.py` - Update site title in environment
3. README.md - Update documentation

### Add Your Products
1. Login to admin: http://localhost:5000/admin/
2. Go to Products → Add New Product
3. Fill in details and submit
4. Product appears in catalog

---

## 🛠️ Common Commands

```bash
# Activate environment
venv\Scripts\activate

# Install new package
pip install package_name

# Run application
python run.py

# Reset database
rm app/luxury_watches.db
python run.py init-db
python run.py seed-db

# Deactivate environment
deactivate

# Stop server
Ctrl + C
```

---

## 📱 Features at a Glance

| Feature | Status | Location |
|---------|--------|----------|
| Home Page | ✅ Complete | `/` |
| Product Grid | ✅ Complete | `/products/` |
| Product Filters | ✅ Complete | `/products/` |
| Shopping Cart | ✅ Complete | `/cart/` |
| Checkout | ✅ Complete | `/cart/checkout` |
| User Auth | ✅ Complete | `/auth/` |
| Wishlist | ✅ Complete | `/auth/profile` |
| Reviews | ✅ Complete | `/products/<id>` |
| Admin Panel | ✅ Complete | `/admin/` |
| Responsive Design | ✅ Complete | All pages |
| Animations | ✅ Complete | Throughout |

---

## 🚨 Troubleshooting

### Port Already in Use
Edit `run.py` and change:
```python
app.run(debug=True, port=5001)  # Use 5001 instead
```

### Database Errors
```bash
# Reset database
rm app/luxury_watches.db
python run.py init-db
python run.py seed-db
python run.py create-admin
```

### Templates Not Loading
- Ensure `app/templates/` folder exists
- Check folder permissions
- Restart Flask server

### CSS/JS Not Showing
- Hard refresh: `Ctrl + Shift + R`
- Check browser console for errors
- Verify files exist in `app/static/`

---

## 📚 Documentation Files

1. **README.md** - Project overview (start here!)
2. **INSTALL.md** - Step-by-step installation
3. **FEATURES.md** - Feature guide & user manual
4. **PROJECT_SUMMARY.md** - Technical overview
5. **QUICKREF.md** - This file

---

## 🔄 File Organization

```
Your Project
├── Configuration: config.py, .env, requirements.txt
├── Backend: run.py, app/models.py, app/routes/
├── Frontend: app/templates/, app/static/
├── Database: app/luxury_watches.db (created after init)
└── Documentation: README.md, INSTALL.md, etc.
```

---

## 💡 Pro Tips

1. **Use environment variables** for sensitive data
2. **Enable debug mode** only during development
3. **Regular backups** of database and files
4. **Test thoroughly** before deploying
5. **Keep dependencies updated** for security
6. **Monitor error logs** for issues
7. **Use version control** (Git) for changes

---

## 🎯 Typical Workflow

### Day 1: Setup & Testing
```
1. Extract/clone project
2. Create virtual environment
3. Install dependencies
4. Initialize database
5. Start server
6. Visit http://localhost:5000
7. Test home page
8. Try admin login
```

### Day 2: Customization
```
1. Update site name and logo
2. Change color scheme
3. Customize content
4. Add your product images
5. Test all features
6. Verify responsive design
```

### Day 3: Data Entry
```
1. Login to admin
2. Add your products
3. Set prices and specs
4. Upload images
5. Create categories
6. Add descriptions
```

### Day 4+: Testing & Launch
```
1. Test checkout flow
2. Test user registration
3. Test admin functions
4. Verify all links work
5. Test on mobile
6. Deploy to server
```

---

## 📧 Configuration for Email (Optional)

To enable email notifications, update `.env`:
```
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-specific-password
```

Then implement in `app/routes/cart.py` and `app/routes/auth.py`

---

## 💳 Payment Integration (Optional)

### Stripe Integration Ready
1. Sign up at https://stripe.com
2. Get API keys
3. Add to `.env`:
   ```
   STRIPE_PUBLIC_KEY=pk_test_...
   STRIPE_SECRET_KEY=sk_test_...
   ```
4. Install: `pip install stripe`
5. Update checkout template and route

### PayPal Integration Ready
Similar process - update checkout form and route

---

## 🌍 Deployment (When Ready)

### Option 1: Heroku (Easiest)
```bash
heroku login
heroku create your-app-name
git push heroku main
```

### Option 2: PythonAnywhere
1. Upload files
2. Configure Python version
3. Set WSGI file
4. Visit your-username.pythonanywhere.com

### Option 3: DigitalOcean
1. Create droplet
2. SSH in
3. Clone repository
4. Setup environment
5. Run with Gunicorn

---

## 📞 Getting Help

- **Python Issues**: Check https://www.python.org/
- **Flask Help**: Visit https://flask.palletsprojects.com/
- **CSS/JS**: See https://developer.mozilla.org/
- **Installation**: Read INSTALL.md

---

## ✅ Pre-Launch Checklist

- [ ] All products added
- [ ] Admin password changed
- [ ] Site colors customized
- [ ] Logo/branding updated
- [ ] Checkout tested end-to-end
- [ ] Mobile version tested
- [ ] All links working
- [ ] Reviews working
- [ ] Wishlist working
- [ ] Admin functions verified

---

**Happy selling! 🎉 Your luxury watch store is ready to launch!**

**Questions?** Check README.md or INSTALL.md for more details.
