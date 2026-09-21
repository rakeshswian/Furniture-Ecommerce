from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Nordic Lounge Chair", "category": "Seating", "price": 189.99, "image": "https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?w=500&q=80"},
    {"id": 2, "name": "Modern Sofa", "category": "Seating", "price": 499.99, "image": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=500&q=80"},
    {"id": 3, "name": "Dining Chair", "category": "Seating", "price": 129.99, "image": "https://images.unsplash.com/photo-1503602642458-232111445657?w=500&q=80"},
    {"id": 4, "name": "Office Chair", "category": "Seating", "price": 159.99, "image": "https://images.unsplash.com/photo-1580480055273-228ff5388ef8?w=500&q=80"},
    {"id": 5, "name": "King Size Bed", "category": "Storage", "price": 699.99, "image": "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=500&q=80"},
    {"id": 6, "name": "Oak Bedside Table", "category": "Storage", "price": 120.00, "image": "https://images.unsplash.com/photo-1532372576444-dda954194ad0?w=500&q=80"},
    {"id": 7, "name": "Modern Wardrobe", "category": "Storage", "price": 549.99, "image": "https://images.unsplash.com/photo-1558997519-83ea9252edf8?w=500&q=80"},
    {"id": 8, "name": "Wooden Bookshelf", "category": "Storage", "price": 249.99, "image": "https://images.unsplash.com/photo-1594620302200-9a762244a156?w=500&q=80"},
    {"id": 9, "name": "Minimalist Ceramic Vase", "category": "Decor", "price": 34.50, "image": "https://images.unsplash.com/photo-1578749556568-bc2c40e68b61?w=500&q=80"},
    {"id": 10, "name": "Decorative Wall Mirror", "category": "Decor", "price": 149.99, "image": "https://images.unsplash.com/photo-1618220179428-22790b461013?w=500&q=80"},
    {"id": 11, "name": "Wall Painting", "category": "Decor", "price": 79.99, "image": "https://images.unsplash.com/photo-1577083288073-40892c0860a4?w=500&q=80"},
    {"id": 12, "name": "Modern Wall Clock", "category": "Decor", "price": 45.99, "image": "https://images.unsplash.com/photo-1563861826100-9cb868fdbe1c?w=500&q=80"},
    {"id": 13, "name": "Decorative Flower Pot", "category": "Decor", "price": 29.99, "image": "https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=500&q=80"},
    {"id": 14, "name": "Modern Wall Paper", "category": "Decor", "price": 89.99, "image": "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=500&q=80"},
    {"id": 15, "name": "Warm Brass Desk Lamp", "category": "Lighting", "price": 58.00, "image": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=500&q=80"},
    {"id": 16, "name": "Modern Ceiling Light", "category": "Lighting", "price": 99.99, "image": "https://images.unsplash.com/photo-1524484485831-a92ffc0de03f?w=500&q=80"},
    {"id": 17, "name": "Modern Floor Lamp", "category": "Lighting", "price": 139.99, "image": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=500&q=80"},
    {"id": 18, "name": "Decorative Table Lamp", "category": "Lighting", "price": 64.99, "image": "https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?w=500&q=80"},
    {"id": 19, "name": "Ceiling Fan", "category": "Lighting", "price": 179.99, "image": "https://images.unsplash.com/photo-1558008258-3256797b43f3?w=500&q=80"},
    {"id": 20, "name": "Glass Set", "category": "Decor", "price": 24.99, "image": "https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?w=500&q=80"},
    {"id": 21, "name": "Spoon Set", "category": "Decor", "price": 19.99, "image": "https://images.unsplash.com/photo-1584346133934-a3afd2a33c4c?w=500&q=80"},
    {"id": 22, "name": "Coffee Mug Set", "category": "Decor", "price": 32.99, "image": "https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?w=500&q=80"},
    {"id": 23, "name": "Dinner Plate Set", "category": "Decor", "price": 49.99, "image": "https://images.unsplash.com/photo-1603199506016-b9a594b593c0?w=500&q=80"},
    {"id": 24, "name": "Washing Machine", "category": "Storage", "price": 599.99, "image": "https://images.unsplash.com/photo-1626806787461-102c1bfaaea1?w=500&q=80"},
    {"id": 25, "name": "Electric Kettle", "category": "Lighting", "price": 39.99, "image": "https://images.unsplash.com/photo-1594213114663-d94db9b171e4?w=500&q=80"}
]

def init_db():
    conn = sqlite3.connect("decor_nest.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            email TEXT,
            address TEXT,
            total REAL,
            order_date TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER,
            product_name TEXT,
            price REAL,
            quantity INTEGER
        )
    """)

    # Add status column to existing database without deleting old orders
    try:
        cur.execute(
            "ALTER TABLE orders ADD COLUMN status TEXT DEFAULT 'Placed'"
        )
    except sqlite3.OperationalError:
        pass

    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html", products=PRODUCTS)

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/api/products")
def products():
    return jsonify(PRODUCTS)

@app.route("/api/order", methods=["POST"])
def create_order():
    data = request.get_json()

    customer_name = data.get("customer_name", "")
    email = data.get("email", "")
    address = data.get("address", "")
    items = data.get("items", [])
    total = float(data.get("total", 0))

    if not customer_name or not email or not address or not items:
        return jsonify({
            "success": False,
            "message": "Please fill all details."
        }), 400

    conn = sqlite3.connect("decor_nest.db")
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO orders
        (customer_name, email, address, total, order_date, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        customer_name,
        email,
        address,
        total,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Placed"
    ))

    order_id = cur.lastrowid

    for item in items:
        cur.execute("""
            INSERT INTO order_items
            (order_id, product_name, price, quantity)
            VALUES (?, ?, ?, ?)
        """, (
            order_id,
            item.get("name"),
            float(item.get("price", 0)),
            int(item.get("qty", 1))
        ))

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "order_id": order_id,
        "message": "Order placed successfully!"
    })

@app.route("/api/order/<int:order_id>/cancel", methods=["POST"])
def cancel_order(order_id):

    conn = sqlite3.connect("decor_nest.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT status FROM orders WHERE id = ?",
        (order_id,)
    )

    order = cur.fetchone()

    if not order:
        conn.close()
        return jsonify({
            "success": False,
            "message": "Order not found."
        }), 404

    if order[0] == "Cancelled":
        conn.close()
        return jsonify({
            "success": False,
            "message": "Order is already cancelled."
        }), 400

    cur.execute(
        "UPDATE orders SET status = 'Cancelled' WHERE id = ?",
        (order_id,)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "message": "Order cancelled successfully."
    })


@app.route("/my-orders")
def my_orders():
    return render_template("my_orders.html")

@app.route("/api/my-orders", methods=["POST"])
def get_my_orders():
    data = request.get_json()

    email = data.get("email", "").strip()
    order_id = data.get("order_id", "").strip()

    if not email or not order_id:
        return jsonify({
            "success": False,
            "message": "Please enter Order ID and Email."
        }), 400

    conn = sqlite3.connect("decor_nest.db")
    conn.row_factory = sqlite3.Row

    order = conn.execute(
        "SELECT * FROM orders WHERE id = ? AND email = ?",
        (order_id, email)
    ).fetchone()

    if not order:
        conn.close()
        return jsonify({
            "success": False,
            "message": "Order not found. Please check Order ID and Email."
        }), 404

    items = conn.execute(
        "SELECT * FROM order_items WHERE order_id = ?",
        (order_id,)
    ).fetchall()

    conn.close()

    return jsonify({
        "success": True,
        "order": dict(order),
        "items": [dict(item) for item in items]
    })

@app.route("/admin")
def admin():

    conn = sqlite3.connect("decor_nest.db")
    conn.row_factory = sqlite3.Row

    orders = conn.execute(
        "SELECT * FROM orders ORDER BY id DESC"
    ).fetchall()

    order_items = {}

    for order in orders:
        items = conn.execute(
            "SELECT * FROM order_items WHERE order_id = ?",
            (order["id"],)
        ).fetchall()

        order_items[order["id"]] = items

    conn.close()

    return render_template(
        "admin.html",
        orders=orders,
        order_items=order_items
    )

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
