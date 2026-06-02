(function () {
    const buttons = document.querySelectorAll('[data-add-product]');
    const itemsBox = document.getElementById('cart-items');
    const totalBox = document.getElementById('cart-total');
    const whatsappBtn = document.getElementById('whatsapp-order');
    const customerName = document.getElementById('customer-name');
    const deliveryPlace = document.getElementById('delivery-place');
    const cart = new Map();

    function money(value) {
        return '$' + Number(value).toFixed(2);
    }

    function render() {
        if (!itemsBox || !totalBox || !whatsappBtn) return;
        itemsBox.innerHTML = '';
        let total = 0;

        if (cart.size === 0) {
            itemsBox.innerHTML = '<p class="text-amber-100">Aún no has agregado productos.</p>';
        } else {
            cart.forEach((item) => {
                total += item.price * item.quantity;
                const row = document.createElement('div');
                row.className = 'flex items-center justify-between gap-3 rounded-2xl bg-white/10 p-3';
                row.innerHTML = `
                    <div>
                        <p class="font-bold">${item.name}</p>
                        <p class="text-sm text-amber-100">${money(item.price)} x ${item.quantity}</p>
                    </div>
                    <div class="flex items-center gap-2">
                        <button class="rounded-full bg-white/20 px-3 py-1 font-black" data-dec="${item.id}">-</button>
                        <button class="rounded-full bg-white/20 px-3 py-1 font-black" data-inc="${item.id}">+</button>
                    </div>
                `;
                itemsBox.appendChild(row);
            });
        }

        totalBox.textContent = money(total);
        buildWhatsAppLink(total);
    }

    function buildWhatsAppLink(total) {
        const number = window.COOKIESLAB_WHATSAPP || '';
        const businessName = window.COOKIESLAB_NAME || 'CookiesLab';
        if (!number || cart.size === 0) {
            whatsappBtn.setAttribute('href', '#');
            return;
        }

        const lines = [];
        lines.push(`Hola, quiero hacer un pedido en ${businessName} 🍪`);
        lines.push('');
        lines.push('Productos:');
        cart.forEach((item) => {
            lines.push(`- ${item.name} x${item.quantity} - ${money(item.price * item.quantity)}`);
        });
        lines.push('');
        lines.push(`Total estimado: ${money(total)}`);
        lines.push('');
        lines.push(`Nombre: ${customerName ? customerName.value : ''}`);
        lines.push(`Lugar/Hora de entrega: ${deliveryPlace ? deliveryPlace.value : ''}`);
        lines.push('Método de pago:');
        lines.push('Notas:');

        whatsappBtn.setAttribute('href', `https://wa.me/${number}?text=${encodeURIComponent(lines.join('\n'))}`);
        whatsappBtn.setAttribute('target', '_blank');
        whatsappBtn.setAttribute('rel', 'noopener');
    }

    buttons.forEach((button) => {
        button.addEventListener('click', () => {
            const id = button.dataset.id;
            const existing = cart.get(id);
            if (existing) {
                existing.quantity += 1;
            } else {
                cart.set(id, {
                    id,
                    name: button.dataset.name,
                    price: Number(button.dataset.price),
                    quantity: 1,
                });
            }
            render();
        });
    });

    document.addEventListener('click', (event) => {
        const inc = event.target.closest('[data-inc]');
        const dec = event.target.closest('[data-dec]');
        if (inc) {
            const item = cart.get(inc.dataset.inc);
            if (item) item.quantity += 1;
            render();
        }
        if (dec) {
            const item = cart.get(dec.dataset.dec);
            if (item) {
                item.quantity -= 1;
                if (item.quantity <= 0) cart.delete(dec.dataset.dec);
            }
            render();
        }
    });

    if (customerName) customerName.addEventListener('input', () => render());
    if (deliveryPlace) deliveryPlace.addEventListener('input', () => render());
})();
