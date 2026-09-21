let cart = JSON.parse(localStorage.getItem('cart')) || [];

function updateCartUI() {
    const badge = document.getElementById('cart-badge');
    const drawer = document.getElementById('cart-items');
    const totalEl = document.getElementById('cart-total');

    const totalCount = cart.reduce((sum, item) => sum + item.qty, 0);

    if (badge) {
        badge.innerText = `Cart (${totalCount})`;
    }

    if (!drawer) return;

    drawer.innerHTML = '';
    let totalSum = 0;

    cart.forEach(item => {
        totalSum += item.price * item.qty;

        drawer.innerHTML += `
            <div class="drawer-item">

                <div>
                    <strong>${item.name}</strong>
                    <p>$${item.price.toFixed(2)} × ${item.qty}</p>

                    <div style="display:flex;align-items:center;gap:8px;margin-top:8px;">
                        <button
                            onclick="changeQuantity(${item.id}, -1)"
                            style="padding:4px 10px;"
                        >−</button>

                        <strong>${item.qty}</strong>

                        <button
                            onclick="changeQuantity(${item.id}, 1)"
                            style="padding:4px 10px;"
                        >+</button>
                    </div>
                </div>

                <button
                    class="remove-btn"
                    onclick="removeFromCart(${item.id})"
                >
                    ✕
                </button>

            </div>
        `;
    });

    totalEl.innerText = `$${totalSum.toFixed(2)}`;

    localStorage.setItem('cart', JSON.stringify(cart));
}

function addToCart(id, name, price) {

    const existing = cart.find(item => item.id === id);

    if (existing) {
        existing.qty += 1;
    } else {
        cart.push({
            id: id,
            name: name,
            price: Number(price),
            qty: 1
        });
    }

    updateCartUI();
    toggleDrawer(true);
}

function changeQuantity(id, change) {

    const item = cart.find(item => item.id === id);

    if (!item) return;

    item.qty += change;

    if (item.qty <= 0) {
        cart = cart.filter(item => item.id !== id);
    }

    updateCartUI();
}

function removeFromCart(id) {

    cart = cart.filter(item => item.id !== id);

    updateCartUI();
}

function toggleDrawer(open) {

    const drawer = document.getElementById('cart-drawer');

    if (!drawer) return;

    drawer.classList.toggle('active', open);
}

document.addEventListener('DOMContentLoaded', updateCartUI);
