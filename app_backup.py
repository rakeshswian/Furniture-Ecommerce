from flask import Flask, render_template

app = Flask(__name__)

# Sample furniture catalog
PRODUCTS = [
    {
        "id": 1,
        "name": "Nordic Lounge Chair",
        "category": "Seating",
        "price": 189.99,
        "image": "https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?w=500&q=80"
    },
    {
        "id": 2,
        "name": "Minimalist Ceramic Vase",
        "category": "Decor",
        "price": 34.50,
        "image": "https://images.unsplash.com/photo-1578749556568-bc2c40e68b61?w=500&q=80"
    },
    {
        "id": 3,
        "name": "Oak Bedside Table",
        "category": "Storage",
        "price": 120.00,
        "image": "https://images.unsplash.com/photo-1532372320572-cda25653a26d?w=500&q=80"
    },
    {
        "id": 4,
        "name": "Warm Brass Desk Lamp",
        "category": "Lighting",
        "price": 58.00,
        "image": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=500&q=80"
    }
]

@app.route("/")
def home():
    return render_template("index.html", products=PRODUCTS)

if __name__ == "__main__":
    app.run(debug=True)

