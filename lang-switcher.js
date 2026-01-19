function updateContent() {
    const lang = localStorage.getItem('selectedLang') || 'en';
    const langData = translations[lang];

    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (langData[key]) {
            if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
                element.placeholder = langData[key];
            } else if (element.hasAttribute('data-i18n-html')) {
                element.innerHTML = langData[key];
            } else {
                element.innerText = langData[key];
            }
        }
    });

    // Update active state in lang selector
    document.querySelectorAll('.lang-link').forEach(link => {
        link.classList.toggle('active', link.getAttribute('onclick').includes(lang));
    });

    // Specific update for funny quote on home page
    const quoteElement = document.querySelector('.parallax-quote blockquote');
    const citeElement = document.querySelector('.parallax-quote cite');
    if (quoteElement && langData.parallax_quote) {
        quoteElement.innerText = langData.parallax_quote;
    }
    if (citeElement && langData.parallax_cite) {
        citeElement.innerText = langData.parallax_cite;
    }
}

function setLanguage(lang) {
    localStorage.setItem('selectedLang', lang);
    updateContent();
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    updateContent();
});
