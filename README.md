# Tom Szenessy Portfolio - Astro Version

This is the high-performance, modular version of my portfolio, migrated from a monolithic HTML structure to [Astro](https://astro.build/).

## 🚀 Features

- **Static Branding & i18n:** Full support for English, German, and Spanish with static routing for SEO and speed.
- **Optimized Assets:** Automatic image optimization (WebP/compression) via `astro:assets`.
- **Modern Styling:** Built with Tailwind CSS 4 and custom Bricolage Grotesque/Fraunces typography.
- **Interactive Elements:** Smooth reveal animations, a custom particle background system, and a playful "Peeking Tom" scroll-triggered avatar.
- **Zero JS by Default:** Ships minimal JavaScript, only where interactivity is required.

## 🛠️ Project Structure

```text
.
├── src/
│   ├── assets/           # Original high-res images and certificates
│   ├── components/       # Modular Astro components (Hero, Projects, etc.)
│   ├── i18n/             # Localization logic and translation strings
│   ├── layouts/          # Base HTML structure
│   ├── pages/            # Multi-language static routes
│   └── styles/           # Global Tailwind and custom CSS
├── public/               # Static assets served as-is
├── legacy/               # Backup of the original monolithic files
└── astro.config.mjs      # Astro configuration
```

## 🏗️ Getting Started

### Prerequisites
- Node.js (v18+)
- npm

### Development
```bash
npm install
npm run dev
```
Open `http://localhost:4321` in your browser.

### Build & Deploy
```bash
npm run build
```
The production-ready site will be generated in the `dist/` directory.

## 📈 Performance Improvements
- **PageSpeed Score:** Significant boost by removing Tailwind CDN and using build-time compilation.
- **FCP (First Contentful Paint):** Dramatically reduced through static generation and optimized media.

---
Made with ♥ by Tom Szenessy
