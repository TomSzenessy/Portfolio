function updateContent() {
    const lang = localStorage.getItem('selectedLang') || 'en';
    const langData = translations[lang];
    document.documentElement.setAttribute('lang', lang);

    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (langData && langData[key]) {
            if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
                element.placeholder = langData[key];
            } else if (element.hasAttribute('data-i18n-html')) {
                element.innerHTML = langData[key];
            } else {
                element.innerText = langData[key];
            }
        } else {
            console.warn(`Missing translation for key: ${key} in language: ${lang}`);
        }
    });

    // Update active state in lang selector buttons
    document.querySelectorAll('.lang-btn').forEach(btn => {
        const btnLang = btn.getAttribute('data-lang');
        if (btnLang === lang) {
            btn.classList.add('text-accent', 'underline', 'underline-offset-4');
            btn.classList.remove('text-text-muted');
        } else {
            btn.classList.remove('text-accent', 'underline', 'underline-offset-4');
            btn.classList.add('text-text-muted', 'hover:text-accent');
        }
    });
}

function setLanguage(lang) {
    localStorage.setItem('selectedLang', lang);
    updateContent();
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    updateContent();
});
