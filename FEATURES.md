# Feature Guide & User Documentation

## For Customers

### 🛍️ Shopping Features

#### 1. Browsing Products
- **Home Page** (`/`): View featured luxury watches and brand information
- **Products Page** (`/products/`): Browse full collection with filtering options

#### 2. Product Filtering
- Filter by **Category**: Classic, Modern, Sports
- Filter by **Brand**: Chronos Luxe, Tempus Aurum, Futura Watch Co, Sportus Elite
- Filter by **Price Range**: Set min and max price
- **Pagination**: Navigate through products easily

#### 3. Product Details
Each product page includes:
- High-quality product images
- Detailed specifications (movement, water resistance, material)
- Price and availability
- Customer reviews and ratings
- Add to Cart button
- Add to Wishlist option

#### 4. Customer Reviews
- **View Reviews**: Read what other customers say
- **Leave Review**: Rate (1-5 stars) and write comments
- **Authentic Feedback**: See real customer experiences

### 🛒 Shopping Cart

#### Add to Cart
1. Go to product page
2. Select quantity (1-10)
3. Click "Add to Cart"
4. Confirmation message appears

#### Manage Cart
- **View Cart**: Click cart icon in navigation
- **Update Quantity**: Change amount for each item
- **Remove Items**: Delete products from cart
- **View Total**: See subtotal and shipping cost

### 💳 Checkout Process

#### Step 1: Review Cart
- See all items and prices
- Update quantities if needed
- See order total

#### Step 2: Enter Information
Required fields:
- First Name & Last Name
- Email Address
- Phone Number
- Shipping Address
- City & ZIP Code

#### Step 3: Payment Method
Choose from:
- Credit Card (Stripe integration ready)
- PayPal (integration ready)

#### Step 4: Order Confirmation
- Receive confirmation page
- Order number for tracking
- Expected delivery date
- Download invoice (optional feature)

### 👤 User Account

#### Create Account
1. Click "Sign Up" in navigation
2. Enter details:
   - First and Last Name
   - Email Address
   - Password (min 6 characters)
3. Account created automatically

#### Login
1. Click "Login" in navigation
2. Enter email and password
3. Access your profile

#### Profile Page Features
- **My Orders**: View all orders and status
- **Order History**: Track past purchases
- **My Wishlist**: View saved products
- **Account Settings**: View profile information
- **Order Tracking**: Monitor shipment status

### 💝 Wishlist

#### Add to Wishlist
1. Find a product you like
2. Click "Add to Wishlist ♡"
3. Must be logged in

#### View Wishlist
1. Go to Profile
2. Click "My Wishlist" tab
3. See all saved products
4. Quick view and add to cart options

### 📧 Contact & Support

#### Contact Form
- Fill out name, email, message
- Submit inquiry
- Receive confirmation
- Support team will respond

#### Find Us
- **Address**: 123 Luxury Lane, New York, NY 10001
- **Phone**: +1 (555) 123-4567
- **Email**: info@luxa.com
- **Hours**: Mon-Fri 10am-6pm EST, Sat 11am-4pm EST

#### Social Media
- Follow on Facebook, Instagram, Twitter, LinkedIn
- Latest updates and promotions

---

## For Administrators

### 🔐 Admin Access

#### Login to Admin Panel
1. Navigate to: `http://localhost:5000/admin/`
2. Login with credentials:
   - Email: admin@luxurywatches.com
   - Password: admin123

#### Change Password
⚠️ **IMPORTANT**: Change password immediately after first login!

### 📊 Dashboard

#### Dashboard Overview
- **Total Products**: Number of products in catalog
- **Total Users**: Active customer accounts
- **Total Orders**: All orders placed
- **Recent Orders**: Last 5 orders with status

### 📦 Product Management

#### View Products
1. Go to **Products** in admin menu
2. See all products in table format
3. Paginate through products

#### Add New Product
1. Click "Add New Product"
2. Fill in details:
   - **Product Name**: e.g., "Midnight Elegance"
   - **Brand**: e.g., "Chronos Luxe"
   - **Price**: e.g., "8500.00"
   - **Category**: Classic / Modern / Sports
   - **Description**: Product story and features
   - **Image URL**: Link to product image
   - **Movement**: Automatic / Mechanical / Quartz
   - **Water Resistance**: e.g., "100m"
   - **Case Material**: Gold / Silver / Titanium
3. Click "Add Product"

#### Edit Product
1. Click "Edit" on product row
2. Update any details
3. Click "Update Product"

#### Delete Product
1. Click "Delete" on product row
2. Confirm deletion
3. Product removed from catalog

### 📋 Order Management

#### View Orders
1. Go to **Orders** in admin menu
2. See all customer orders
3. View order details:
   - Order ID
   - Customer name
   - Total amount
   - Current status
   - Order date

#### Update Order Status
Status workflow:
- **Pending**: Order received, awaiting processing
- **Confirmed**: Payment confirmed, preparing shipment
- **Shipped**: Package sent to customer
- **Delivered**: Order received by customer

To update:
1. Click status dropdown
2. Select new status
3. Status updates immediately

#### View Order Details
- Customer information
- Shipping address
- Order items and quantities
- Order total
- Order history/timeline

### 👥 Dashboard Statistics

#### Key Metrics
- **Active Customers**: Total registered users
- **Total Revenue**: Sum of all orders
- **Average Order Value**: Revenue / orders
- **Pending Orders**: Awaiting shipment
- **Recent Activity**: Latest actions

#### Reports (Future Feature)
- Sales by month/year
- Best selling products
- Customer demographics
- Popular categories

### 🔧 System Management

#### Database Management
```bash
# Backup database
cp app/luxury_watches.db app/luxury_watches.db.backup

# Reset database (⚠️ Careful - deletes all data!)
rm app/luxury_watches.db
python run.py init-db
python run.py seed-db
```

#### Logs & Monitoring
- Check terminal output for errors
- Review admin actions in database
- Monitor application performance

---

## Common Tasks

### 🛒 Customer: Placing an Order

```
1. Browse Products → 2. Add to Cart → 3. View Cart → 4. Checkout
  ↓                   ↓                ↓              ↓
View items        Select qty      Review total   Enter info
See details       Update cart    See items       Choose payment
Add to wishlist                  Remove items    Place order
                                                ↓
                            5. Order Confirmation
                                ↓
                            See confirmation #
                            Track order status
```

### 👨‍💼 Admin: Daily Operations

```
1. Check Dashboard
   ├─ View recent orders
   ├─ Monitor stats
   └─ Identify issues

2. Process Orders
   ├─ Review pending orders
   ├─ Verify payment
   ├─ Update status to "Confirmed"
   └─ Prepare shipment

3. Manage Inventory
   ├─ Check product stock
   ├─ Add new products
   ├─ Update descriptions
   └─ Remove discontinued items

4. Customer Service
   ├─ Review inquiries
   ├─ Respond to questions
   └─ Process returns/refunds
```

### 📧 Email Notifications (When Configured)

**Automatic emails sent to:**
- Order confirmation
- Shipping notification
- Delivery confirmation
- Customer support responses

---

## Best Practices

### For Customers
✓ Use strong passwords (mix of letters, numbers, symbols)
✓ Save order confirmation emails
✓ Update profile with correct address
✓ Leave reviews for products you purchased
✓ Check FAQ before contacting support

### For Administrators
✓ Change default admin password immediately
✓ Keep product descriptions accurate
✓ Update inventory regularly
✓ Monitor orders closely
✓ Respond to inquiries quickly
✓ Regular database backups
✓ Update product images professionally
✓ Track customer feedback

---

## Troubleshooting

### Issue: Can't login to admin
**Solution**: 
- Verify email: admin@luxurywatches.com
- Check password (default: admin123)
- Ensure database initialized
- Check browser console for errors

### Issue: Product images not showing
**Solution**:
- Verify image URL is correct
- Image must be publicly accessible
- Try HTTPS URLs for better compatibility
- Use JPEG or PNG format

### Issue: Cart not persisting
**Solution**:
- Enable cookies in browser
- Clear browser cache
- Try different browser
- Check browser console for errors

### Issue: Orders not processing
**Solution**:
- Check all required fields filled
- Verify phone number format
- Ensure address is complete
- Try alternate browser

---

## Privacy & Security

### Your Data
- Passwords are encrypted with industry-standard hashing
- Personal information stored securely
- Payment info processed through secure gateways
- No sharing of data with third parties
- Regular security updates

### Best Practices
- Never share your password
- Log out when using public computers
- Use unique passwords
- Keep contact information updated
- Report suspicious activity

---

## Getting Help

### Self-Service
1. Check FAQ and guides
2. Search product reviews
3. Browse Help Center
4. View video tutorials

### Contact Support
1. **Email**: info@luxa.com
2. **Phone**: +1 (555) 123-4567
3. **Chat**: Live chat (future feature)
4. **Contact Form**: Use form on Contact page

### Response Times
- Email: 24-48 hours
- Phone: Business hours
- Chat: Real-time (when available)

---

**Happy shopping! For any questions, don't hesitate to contact us. 📞**
