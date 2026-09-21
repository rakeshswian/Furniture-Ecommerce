# DecorNest — Furniture & Home Decor E-Commerce

DecorNest is a Flask-based Furniture & Home Decor E-Commerce web application developed as a college project. It provides a complete shopping flow from product browsing and cart management to checkout, order tracking, and an admin order dashboard.

## Features

- Furniture and home decor product catalog
- Product search and category filtering
- Add products to cart
- Increase/decrease product quantity
- Remove products from cart
- Automatic cart total calculation
- Checkout page
- Order placement with generated Order ID
- Customer order lookup through **My Orders**
- Order status display
- Order cancellation
- Admin dashboard for viewing orders
- Product-wise order details and subtotals
- SQLite database for storing orders
- Responsive web interface
- Cart data maintained in browser local storage

## Technologies Used

- **Python 3**
- **Flask**
- **SQLite**
- **HTML5**
- **CSS3**
- **JavaScript**
- **Browser LocalStorage**

## Project Structure

```text
Furniture_Ecommerce/
│
├── app.py
├── decor_nest.db
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── checkout.html
│   ├── my_orders.html
│   └── admin.html
│
└── static/
    ├── cart.js
    └── css/
        └── style.css
```

> The exact files in the `templates/` and `static/` folders may vary depending on the current version of the project.

## System Requirements

### Minimum Requirements

- Windows, Linux, macOS, or Android/Termux
- Python 3.9 or newer recommended
- Internet connection for installing Python packages
- Modern web browser such as Chrome, Edge, or Firefox

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Furniture_Ecommerce.git
cd Furniture_Ecommerce
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Check Python

```bash
python --version
```

On some systems you may need:

```bash
python3 --version
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `pip` does not work, try:

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Or on systems using `python3`:

```bash
python3 app.py
```

The application should start on:

```text
http://127.0.0.1:5000
```

Open that address in your browser.

## Windows CMD Setup

Open Command Prompt and run:

```cmd
cd Desktop\Furniture_Ecommerce
python --version
pip install -r requirements.txt
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

To stop the server:

```text
Ctrl + C
```

## Termux Setup

Install Python and Git:

```bash
pkg update
pkg install python git
```

Go to the project directory:

```bash
cd ~/Furniture_Ecommerce
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Then open the local address shown by Flask in a browser.

## Dependencies

The main Python dependency is Flask.

The `requirements.txt` file should contain:

```text
Flask
```

If the project is being deployed using Gunicorn, use:

```text
Flask
gunicorn
```

No external database server is required because the project uses SQLite.

## Database

DecorNest uses **SQLite** for storing order information.

The database file is:

```text
decor_nest.db
```

The database is created/initialized by the Flask application when required.

### Main Order Data

The application stores information such as:

- Customer name
- Email
- Address
- Order total
- Order date
- Order status

### Order Item Data

Individual order items contain information such as:

- Product name
- Price
- Quantity
- Related Order ID

The Order ID connects an order with its individual products.

## Application Flow

```text
Customer
   ↓
Browse Products
   ↓
Search / Filter Products
   ↓
Add to Cart
   ↓
Change Quantity
   ↓
Checkout
   ↓
Enter Customer Details
   ↓
Place Order
   ↓
Flask Backend
   ↓
SQLite Database
   ↓
Order ID Generated
   ↓
My Orders / Admin Dashboard
```

## Cart System

The shopping cart is handled using JavaScript.

Cart information is stored in the browser's **LocalStorage**, allowing the cart to remain available while navigating between pages.

The cart supports:

- Adding products
- Increasing quantity
- Decreasing quantity
- Removing products
- Calculating total price
- Displaying total number of items

## Order Management

When a customer places an order:

1. Customer details are submitted.
2. Flask receives the request.
3. Order information is stored in SQLite.
4. Individual products are stored as order items.
5. An Order ID is generated.
6. The customer can view the order through **My Orders**.
7. The admin can view the order from the admin dashboard.

## Order Cancellation

The cancellation feature changes the order status instead of deleting the order.

Example:

```text
Placed → Cancelled
```

This keeps the order record available in the database.

## Running the Project for a College Demo

Start the application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

Recommended demonstration sequence:

1. Open the DecorNest home page.
2. Show the product catalog.
3. Search or filter products.
4. Add a product to the cart.
5. Increase/decrease quantity.
6. Show the cart total.
7. Proceed to checkout.
8. Enter customer details.
9. Place an order.
10. Show the generated Order ID.
11. Open My Orders.
12. Show the order details and status.
13. Open the admin dashboard.
14. Show the order and its individual products.
15. Demonstrate order cancellation.

## API / Backend

The Flask backend handles:

- Page rendering
- Product-related requests
- Cart/order processing
- Checkout
- Order creation
- Order retrieval
- Order cancellation
- Database operations

The main backend file is:

```text
app.py
```

## Payment

If a payment gateway has not been integrated, payment functionality in this project should be treated as a demonstration/college-project feature rather than a real payment processing system.

Do not store real card numbers, passwords, or other sensitive payment information in this project.

## Security Notes

This project is intended primarily for learning and college demonstration.

For production use, additional security would be required, including:

- User authentication and authorization
- Password hashing
- CSRF protection
- Input validation
- Secure session handling
- Environment variables for secrets
- Production database
- HTTPS
- Proper payment gateway integration
- Production server configuration

## GitHub Upload

After making changes:

```bash
git add .
git commit -m "Update DecorNest project"
git push
```

For the first upload:

```bash
git init
git add .
git commit -m "Initial DecorNest project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Furniture_Ecommerce.git
git push -u origin main
```

## Important GitHub Note

The SQLite database file `decor_nest.db` can contain test order/customer information. For a public repository, use only dummy/test data and avoid uploading real personal information.

For a cleaner repository, you can add a `.gitignore` file containing:

```text
__pycache__/
*.pyc
.venv/
venv/
.env
```

If you intentionally want to preserve the demo database and its test orders, keep `decor_nest.db` in the repository.

## Future Improvements

Possible future improvements include:

- User registration and login
- Product details pages
- Product images stored through a proper media system
- Wishlist
- Product reviews and ratings
- Stock/inventory management
- Discount and coupon system
- Online payment gateway
- Order email notifications
- PostgreSQL/MySQL database
- Cloud deployment
- Admin authentication
- Product management from the admin dashboard

## Project Purpose

DecorNest was created as an academic project to demonstrate practical use of:

- Python programming
- Flask web development
- HTML/CSS/JavaScript
- SQLite database management
- CRUD-style order operations
- Frontend and backend integration
- E-commerce workflow design

## Author

**DecorNest — Furniture & Home Decor E-Commerce**

College Project
