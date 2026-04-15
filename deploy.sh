#!/bin/bash
set -e

echo "🚀 Deploying scala.evolved to GitHub Pages..."

# Regenerate all detail pages
echo "📝 Regenerating detail pages..."
python3 generate-pages.py

# Add all changes
echo "📦 Adding changes to git..."
git add .

# Commit
echo "💾 Creating commit..."
git commit -m "Update: $(date '+%Y-%m-%d %H:%M')" || echo "No changes to commit"

# Push to main
echo "⬆️  Pushing to GitHub..."
git push origin main

echo ""
echo "✅ Done! Your site will be live at:"
echo "   https://scalaevolved.github.io/scala-evolved/"
echo ""
echo "⏱️  GitHub Pages may take 1-2 minutes to update."
