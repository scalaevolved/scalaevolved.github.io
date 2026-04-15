# Quick Start Guide

## View the site locally

### Option 1: Python (easiest)
```bash
python3 -m http.server 8000
```
Then open: http://localhost:8000

### Option 2: PHP
```bash
php -S localhost:8000
```
Then open: http://localhost:8000

### Option 3: Node.js
```bash
npx http-server -p 8000
```
Then open: http://localhost:8000

### Option 4: Direct (limited features)
```bash
open index.html  # macOS
xdg-open index.html  # Linux  
start index.html  # Windows
```
⚠️ Note: Some features (like data loading) may not work without a server due to CORS.

## Add new examples

1. Edit `data/snippets.json`
2. Add your pattern following the existing structure
3. Refresh the page

## Customize

- **Colors**: Edit CSS variables in `styles.css` (:root section)
- **Branding**: Update `index.html` and `manifest.json`
- **Content**: Modify `data/snippets.json`

## Deploy to GitHub Pages

1. Create a new GitHub repository
2. Push this code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/scala-evolved.git
   git push -u origin main
   ```
3. Go to repository Settings → Pages
4. Set Source to "Deploy from a branch"
5. Select `main` branch and `/` (root) folder
6. Save

Your site will be live at: `https://yourusername.github.io/scala-evolved`

## Troubleshooting

**Problem**: Examples don't load  
**Solution**: Make sure you're running a local server (not opening file:// directly)

**Problem**: Search doesn't work  
**Solution**: Check browser console for errors, ensure `data/snippets.json` is valid JSON

**Problem**: Styles look broken  
**Solution**: Verify `styles.css` and `assets/fonts/` exist
