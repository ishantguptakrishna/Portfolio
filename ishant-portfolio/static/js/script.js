// ---------- Mobile tab menu ----------
const menuToggle = document.querySelector('.menu-toggle');
const tabs = document.querySelector('.tabs');
if (menuToggle && tabs) {
  menuToggle.addEventListener('click', () => tabs.classList.toggle('open'));
}

// ---------- Scroll reveal ----------
const revealEls = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('in');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.12 });
  revealEls.forEach(el => io.observe(el));
} else {
  revealEls.forEach(el => el.classList.add('in'));
}

// ---------- Hero terminal typing effect ----------
function typeLine(el, text, speed = 22) {
  return new Promise(resolve => {
    let i = 0;
    el.textContent = '';
    el.classList.add('typed');
    const timer = setInterval(() => {
      el.textContent += text.charAt(i);
      i++;
      if (i >= text.length) {
        clearInterval(timer);
        el.classList.remove('typed');
        resolve();
      }
    }, speed);
  });
}

async function runTerminal() {
  const target = document.getElementById('typed-name');
  if (!target) return;
  const phrases = ['Ishant Kumar Gupta', 'B.Tech CSE @ PIET, Jaipur', 'Aspiring ML / Python Developer'];
  let idx = 0;
  while (true) {
    await typeLine(target, phrases[idx], 35);
    await new Promise(r => setTimeout(r, 1400));
    // erase
    const full = phrases[idx];
    for (let l = full.length; l >= 0; l--) {
      target.textContent = full.slice(0, l);
      await new Promise(r => setTimeout(r, 18));
    }
    idx = (idx + 1) % phrases.length;
  }
}
runTerminal();

// ---------- Generic modal / lightbox for cert & internship images ----------
function buildModal() {
  const overlay = document.createElement('div');
  overlay.className = 'modal-overlay';
  overlay.innerHTML = `
    <div class="modal-box">
      <div class="modal-bar">
        <span id="modal-title">certificate.png</span>
        <button class="modal-close" aria-label="Close">&times;</button>
      </div>
      <img id="modal-img" src="" alt="Certificate preview" />
    </div>`;
  document.body.appendChild(overlay);

  const close = () => overlay.classList.remove('show');
  overlay.querySelector('.modal-close').addEventListener('click', close);
  overlay.addEventListener('click', (e) => { if (e.target === overlay) close(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });

  return {
    open(src, title) {
      overlay.querySelector('#modal-img').src = src;
      overlay.querySelector('#modal-title').textContent = title || 'certificate.png';
      overlay.classList.add('show');
    }
  };
}

const modal = buildModal();
document.querySelectorAll('[data-modal-img]').forEach(trigger => {
  trigger.addEventListener('click', () => {
    modal.open(trigger.getAttribute('data-modal-img'), trigger.getAttribute('data-modal-title'));
  });
});

// ---------- Accordion-style expand for cert buttons (mobile-friendly quick preview) ----------
document.querySelectorAll('.cert-btn').forEach(btn => {
  btn.setAttribute('type', 'button');
});
