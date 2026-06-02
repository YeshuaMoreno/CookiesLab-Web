/* CookiesLab – cart.js
   Maneja: carrito de pedido, generación de link WhatsApp,
   panel mobile (drawer), y filtro de categorías en el menú. */

(function () {
    'use strict';

    /* ── Estado ─────────────────────────────────────────── */
    const cart = new Map();

    /* ── Helpers ─────────────────────────────────────────── */
    function money(val) {
        return '$' + Number(val).toFixed(2);
    }

    function getTotal() {
        let t = 0;
        cart.forEach(function (item) { t += item.price * item.quantity; });
        return t;
    }

    function getCount() {
        let c = 0;
        cart.forEach(function (item) { c += item.quantity; });
        return c;
    }

    function buildWhatsAppUrl(name, delivery) {
        const number = (window.COOKIESLAB_WHATSAPP || '').trim();
        const biz = window.COOKIESLAB_NAME || 'CookiesLab';
        if (!number || cart.size === 0) return '#';

        const total = getTotal();
        const lines = [
            'Hola, quiero hacer un pedido en ' + biz + ' 🍪',
            '',
            'Productos:',
        ];
        cart.forEach(function (item) {
            lines.push('- ' + item.name + ' x' + item.quantity + ' — ' + money(item.price * item.quantity));
        });
        lines.push('', 'Total estimado: ' + money(total), '');
        lines.push('Nombre: ' + (name || ''));
        lines.push('Lugar / Hora de entrega: ' + (delivery || ''));
        lines.push('Método de pago: ');
        lines.push('Notas: ');

        return 'https://wa.me/' + number + '?text=' + encodeURIComponent(lines.join('\n'));
    }

    /* ── Render de items dentro de un contenedor ─────────── */
    function renderItems(container) {
        if (!container) return;
        container.innerHTML = '';
        if (cart.size === 0) {
            container.innerHTML = '<p class="text-sm text-amber-200/80">Aún no has agregado productos.</p>';
            return;
        }
        cart.forEach(function (item) {
            const row = document.createElement('div');
            row.className = 'flex items-center justify-between gap-3 rounded-2xl bg-white/10 p-3';
            row.innerHTML =
                '<div class="flex-1 min-w-0">' +
                    '<p class="font-bold text-sm leading-tight truncate">' + item.name + '</p>' +
                    '<p class="text-xs text-amber-300 mt-0.5">' + money(item.price) + ' c/u</p>' +
                '</div>' +
                '<div class="flex items-center gap-1.5 shrink-0">' +
                    '<button class="flex h-7 w-7 items-center justify-center rounded-full bg-white/20 font-black text-sm hover:bg-white/30 transition-colors" data-dec="' + item.id + '" aria-label="Quitar uno">−</button>' +
                    '<span class="w-5 text-center text-sm font-bold">' + item.quantity + '</span>' +
                    '<button class="flex h-7 w-7 items-center justify-center rounded-full bg-white/20 font-black text-sm hover:bg-white/30 transition-colors" data-inc="' + item.id + '" aria-label="Agregar uno">+</button>' +
                '</div>';
            container.appendChild(row);
        });
    }

    /* ── Referencia a elementos del DOM ──────────────────── */
    // Desktop
    const deskItems   = document.getElementById('cart-items');
    const deskTotal   = document.getElementById('cart-total');
    const deskWaBtn   = document.getElementById('whatsapp-order');
    const deskName    = document.getElementById('customer-name');
    const deskPlace   = document.getElementById('delivery-place');

    // Mobile bar
    const mobileBar       = document.getElementById('mobile-cart-bar');
    const mobileBarTotal  = document.getElementById('mobile-bar-total');
    const mobileBarCount  = document.getElementById('mobile-bar-count');
    const mobileToggle    = document.getElementById('mobile-cart-toggle');

    // Mobile drawer
    const mobileOverlay   = document.getElementById('mobile-cart-overlay');
    const mobileBackdrop  = document.getElementById('mobile-cart-backdrop');
    const mobileClose     = document.getElementById('mobile-cart-close');
    const mobileItems     = document.getElementById('mobile-cart-items');
    const mobileTotal     = document.getElementById('mobile-total');
    const mobileWaBtn     = document.getElementById('mobile-whatsapp-order');
    const mobileName      = document.getElementById('mobile-customer-name');
    const mobilePlace     = document.getElementById('mobile-delivery-place');

    /* ── Render global ───────────────────────────────────── */
    function render() {
        const total = getTotal();
        const count = getCount();
        const name  = (deskName && deskName.value) || (mobileName && mobileName.value) || '';
        const place = (deskPlace && deskPlace.value) || (mobilePlace && mobilePlace.value) || '';
        const url   = buildWhatsAppUrl(name, place);

        // ── Desktop sidebar ──
        renderItems(deskItems);
        if (deskTotal) deskTotal.textContent = money(total);
        if (deskWaBtn) {
            if (cart.size > 0 && (window.COOKIESLAB_WHATSAPP || '').trim()) {
                deskWaBtn.setAttribute('href', url);
                deskWaBtn.setAttribute('target', '_blank');
                deskWaBtn.setAttribute('rel', 'noopener');
                deskWaBtn.classList.remove('opacity-50', 'pointer-events-none', 'cursor-not-allowed');
            } else {
                deskWaBtn.setAttribute('href', '#');
                deskWaBtn.removeAttribute('target');
                deskWaBtn.classList.add('opacity-50', 'pointer-events-none', 'cursor-not-allowed');
            }
        }

        // ── Mobile bar ──
        if (mobileBarTotal) mobileBarTotal.textContent = money(total);
        if (mobileBarCount) {
            mobileBarCount.textContent = count;
            mobileBarCount.classList.toggle('hidden', count === 0);
        }

        // ── Mobile drawer ──
        renderItems(mobileItems);
        if (mobileTotal) mobileTotal.textContent = money(total);
        if (mobileWaBtn) {
            if (cart.size > 0 && (window.COOKIESLAB_WHATSAPP || '').trim()) {
                mobileWaBtn.setAttribute('href', url);
                mobileWaBtn.setAttribute('target', '_blank');
                mobileWaBtn.setAttribute('rel', 'noopener');
                mobileWaBtn.classList.remove('opacity-50', 'pointer-events-none', 'cursor-not-allowed');
            } else {
                mobileWaBtn.setAttribute('href', '#');
                mobileWaBtn.removeAttribute('target');
                mobileWaBtn.classList.add('opacity-50', 'pointer-events-none', 'cursor-not-allowed');
            }
        }
    }

    /* ── Mobile drawer abrir / cerrar ────────────────────── */
    function openDrawer() {
        if (!mobileOverlay) return;
        const drawer = mobileOverlay.querySelector('[data-drawer]');
        mobileOverlay.classList.remove('hidden');
        mobileOverlay.setAttribute('aria-hidden', 'false');
        if (drawer) drawer.classList.add('cart-drawer-enter');
        document.body.style.overflow = 'hidden';
    }

    function closeDrawer() {
        if (!mobileOverlay) return;
        mobileOverlay.classList.add('hidden');
        mobileOverlay.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
    }

    if (mobileToggle)   mobileToggle.addEventListener('click', openDrawer);
    if (mobileClose)    mobileClose.addEventListener('click', closeDrawer);
    if (mobileBackdrop) mobileBackdrop.addEventListener('click', closeDrawer);

    /* ── Sync inputs desktop ↔ mobile ────────────────────── */
    function syncInputs(src, dst) {
        if (src && dst) {
            src.addEventListener('input', function () { dst.value = src.value; render(); });
        }
    }
    syncInputs(deskName,  mobileName);
    syncInputs(mobileName, deskName);
    syncInputs(deskPlace,  mobilePlace);
    syncInputs(mobilePlace, deskPlace);

    if (deskName)  deskName.addEventListener('input', render);
    if (deskPlace) deskPlace.addEventListener('input', render);

    /* ── Botones "Agregar al pedido" ─────────────────────── */
    document.querySelectorAll('[data-add-product]').forEach(function (btn) {
        btn.addEventListener('click', function () {
            const id = btn.dataset.id;
            const existing = cart.get(id);
            if (existing) {
                existing.quantity += 1;
            } else {
                cart.set(id, {
                    id: id,
                    name: btn.dataset.name,
                    price: Number(btn.dataset.price),
                    quantity: 1,
                });
            }
            // Feedback visual al botón
            const original = btn.textContent;
            btn.textContent = '✓ Agregado';
            btn.disabled = true;
            setTimeout(function () {
                btn.textContent = original;
                btn.disabled = false;
            }, 900);
            render();
        });
    });

    /* ── Delegación de eventos +/- en items ─────────────── */
    document.addEventListener('click', function (e) {
        const inc = e.target.closest('[data-inc]');
        const dec = e.target.closest('[data-dec]');
        if (inc) {
            const item = cart.get(inc.dataset.inc);
            if (item) { item.quantity += 1; render(); }
        }
        if (dec) {
            const item = cart.get(dec.dataset.dec);
            if (item) {
                item.quantity -= 1;
                if (item.quantity <= 0) cart.delete(dec.dataset.dec);
                render();
            }
        }
    });

    /* ── Filtro de categorías (solo menú) ────────────────── */
    const catPills = document.querySelectorAll('[data-filter]');
    const prodCards = document.querySelectorAll('[data-category]');

    catPills.forEach(function (pill) {
        pill.addEventListener('click', function () {
            catPills.forEach(function (p) { p.classList.remove('active'); });
            pill.classList.add('active');
            const filter = pill.dataset.filter;
            prodCards.forEach(function (card) {
                card.style.display = (filter === 'all' || card.dataset.category === filter) ? '' : 'none';
            });
        });
    });

    /* ── Render inicial ──────────────────────────────────── */
    render();
})();
