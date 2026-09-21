let cart = JSON.parse(localStorage.getItem('cart')) || [];

function updateCartUI() {
    const badge = document.getElementById('cart-badge');
    const drawer = document.getElementById('cart-items');
    const totalEl = document.getElementById('cart-total');

    const totalCount = cart.reduce((sum, item) => sum + item.qty, 0);
    badge.innerText = `Cart (${totalCount})`;

    if (!drawer) return;
    drawer.innerHTML = '';
    let totalSum = 0;

    cart.forEach(item => {
        totalSum += item.price * item.qty;
        drawer.innerHTML += `
            <div class="drawer-item">
                <div>
                    <strong>${item.name}</strong>
                    <p>$${item.price} × ${item.qty}</p>
                </div>
                <button class="remove-btn" onclick="removeFromCart(${item.id})">✕</button>
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
        cart.push({ id, name, price, qty: 1 });
    }
    updateCartUI();
    toggleDrawer(true);
}

function removeFromCart(id) {
    cart = cart.filter(item => item.id !== id);
    updateCartUI();
}

function toggleDrawer(open) {
    const drawer = document.getElementById('cart-drawer');
    drawer.classList.toggle('active', open);
}

document.addEventListener('DOMContentLoaded', updateCartUI);

