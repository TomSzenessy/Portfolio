const DEFAULT_LANG = 'en';
const STORAGE_KEY = 'selectedLang';
let memoryLang = DEFAULT_LANG;

function getStoredLang() {
    try {
        return localStorage.getItem(STORAGE_KEY) || memoryLang || DEFAULT_LANG;
    } catch (err) {
        return memoryLang || DEFAULT_LANG;
    }
}

function setStoredLang(lang) {
    memoryLang = lang;
    try {
        localStorage.setItem(STORAGE_KEY, lang);
    } catch (err) {
        // Ignore storage errors (private mode, disabled storage, etc.)
    }
}

function updateContent() {
    const requestedLang = getStoredLang();
    const lang = translations[requestedLang] ? requestedLang : DEFAULT_LANG;
    const langData = translations[lang] || {};
    const fallbackData = translations[DEFAULT_LANG] || {};
    document.documentElement.setAttribute('lang', lang);

    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        const value = langData[key] ?? fallbackData[key];
        if (value) {
            if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
                element.placeholder = value;
            } else if (element.hasAttribute('data-i18n-html')) {
                element.innerHTML = value;
            } else {
                element.innerText = value;
            }
        } else {
            console.warn(`Missing translation for key: ${key} in language: ${lang}`);
        }
    });

    document.querySelectorAll('.lang-btn').forEach(btn => {
        const btnLang = btn.getAttribute('data-lang');
        const isActive = btnLang === lang;
        btn.classList.toggle('is-active', isActive);
        btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
    });
}

function setLanguage(lang) {
    setStoredLang(lang);
    updateContent();
}

document.addEventListener('DOMContentLoaded', () => {
    updateContent();
});

window.setLanguage = setLanguage;
