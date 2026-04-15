#!/usr/bin/env python3
import json
import os
from pathlib import Path
import html

# Load snippets
with open('data/snippets.json', 'r') as f:
    snippets = json.load(f)

def escape_html(text):
    return html.escape(text) if text else ""

def get_category_display(category):
    display_names = {
        'enums': 'Enums & ADTs',
        'contextual': 'Contextual Abstractions',
        'types': 'Type System',
        'syntax': 'Syntax',
        'collections': 'Collections',
        'errors': 'Error Handling',
        'metaprogramming': 'Metaprogramming',
        'interop': 'Interop',
        'concurrency': 'Concurrency'
    }
    return display_names.get(category, category.title())

def get_difficulty_display(difficulty):
    return difficulty.title()

def generate_page(snippet, prev_snippet, next_snippet):
    category = snippet['category']
    slug = snippet['slug']

    # Navigation arrows
    nav_arrows = ""
    if prev_snippet:
        nav_arrows += f'<a href="/scala-evolved/{prev_snippet["category"]}/{prev_snippet["slug"]}.html" class="nav-arrow prev" title="{escape_html(prev_snippet["title"])}">←</a>'
    if next_snippet:
        nav_arrows += f'<a href="/scala-evolved/{next_snippet["category"]}/{next_snippet["slug"]}.html" class="nav-arrow next" title="{escape_html(next_snippet["title"])}">→</a>'

    # Base prefix for assets
    base_prefix = "/scala-evolved/"

    html_content = f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escape_html(snippet['title'])} | scala.evolved</title>
  <meta name="description" content="{escape_html(snippet['summary'])}">
  <meta name="robots" content="index, follow">

  <link rel="stylesheet" href="{base_prefix}styles.css">
  <script>
    (function(){{var t=localStorage.getItem('theme')||(window.matchMedia('(prefers-color-scheme: light)').matches?'light':'dark');document.documentElement.setAttribute('data-theme',t);}})();
  </script>

  <link rel="icon" href="{base_prefix}favicon.ico" sizes="any">
  <link rel="icon" href="{base_prefix}favicon-192.png" type="image/png" sizes="192x192">
  <link rel="apple-touch-icon" href="{base_prefix}apple-touch-icon.png">
  <link rel="manifest" href="{base_prefix}manifest.json">
  <meta name="theme-color" content="#dc322f">

  <meta property="og:title" content="{escape_html(snippet['title'])} | scala.evolved">
  <meta property="og:description" content="{escape_html(snippet['summary'])}">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="scala.evolved">
</head>
<body data-page="single">
  <nav>
    <div class="nav-inner">
      <a href="/scala-evolved/" class="logo">scala.<span>evolved</span></a>
      <div class="nav-right">
        <a href="https://github.com/yourusername/scala-evolved" target="_blank" rel="noopener" class="github-link" aria-label="View on GitHub">
          <svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
            <circle cx="10" cy="10" r="9" fill="none" stroke="currentColor" stroke-width="1.5"/>
            <path d="M10 3C6.13 3 3 6.13 3 10c0 3.09 2 5.71 4.77 6.63.35.06.48-.15.48-.33v-1.16c-1.95.42-2.36-1.07-2.36-1.07-.32-.81-.78-1.03-.78-1.03-.64-.43.05-.42.05-.42.7.05 1.07.72 1.07.72.63 1.08 1.65.77 2.05.59.06-.46.24-.77.44-.95-1.57-.18-3.22-.78-3.22-3.48 0-.77.27-1.4.72-1.89-.07-.18-.31-.9.07-1.87 0 0 .59-.19 1.93.72.56-.16 1.16-.24 1.76-.24s1.2.08 1.76.24c1.34-.91 1.93-.72 1.93-.72.38.97.14 1.69.07 1.87.45.49.72 1.12.72 1.89 0 2.71-1.65 3.3-3.23 3.47.25.22.48.65.48 1.31v1.94c0 .19.13.4.48.33C15 15.71 17 13.09 17 10c0-3.87-3.13-7-7-7z"/>
          </svg>
        </a>
        <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">☀️</button>
        <a href="/scala-evolved/" class="back-link">← All Patterns</a>
        <div class="nav-arrows">
          {nav_arrows}
        </div>
      </div>
    </div>
  </nav>

  <article class="article">
    <div class="breadcrumb">
      <a href="/scala-evolved/">Home</a>
      <span class="sep">/</span>
      <a href="/scala-evolved/#{category}">{get_category_display(category)}</a>
      <span class="sep">/</span>
      <span>{escape_html(snippet['title'])}</span>
    </div>

    <div class="tip-header">
      <div class="tip-meta">
        <span class="badge {category}">{get_category_display(category)}</span>
        <span class="badge {snippet['difficulty']}">{get_difficulty_display(snippet['difficulty'])}</span>
      </div>
      <h1>{escape_html(snippet['title'])}</h1>
      <p>{escape_html(snippet['summary'])}</p>
    </div>

    <section class="compare-section">
      <div class="section-label">Code Comparison</div>
      <div class="compare-container">
        <div class="compare-panel old-panel">
          <div class="compare-panel-header">
            <span class="compare-tag old">✕ {escape_html(snippet['oldLabel'])}</span>
            <button class="copy-btn" data-code-old>Copy</button>
          </div>
          <div class="compare-code">
            <pre class="code-text">{escape_html(snippet['oldCode'])}</pre>
          </div>
        </div>
        <div class="compare-panel modern-panel">
          <div class="compare-panel-header">
            <span class="compare-tag modern">✓ {escape_html(snippet['modernLabel'])}</span>
            <button class="copy-btn" data-code-modern>Copy</button>
          </div>
          <div class="compare-code">
            <pre class="code-text">{escape_html(snippet['modernCode'])}</pre>
          </div>
        </div>
      </div>
    </section>

    <div class="info-grid">
      <div class="info-card">
        <div class="info-label">Old Approach</div>
        <div class="info-value red">{escape_html(snippet['oldLabel'])}</div>
      </div>
      <div class="info-card">
        <div class="info-label">Modern Approach</div>
        <div class="info-value green">{escape_html(snippet['modernLabel'])}</div>
      </div>
      <div class="info-card">
        <div class="info-label">Since Scala</div>
        <div class="info-value accent">{escape_html(snippet['scalaVersion'])}</div>
      </div>
      <div class="info-card">
        <div class="info-label">Difficulty</div>
        <div class="info-value blue">{get_difficulty_display(snippet['difficulty'])}</div>
      </div>
    </div>

    <section class="explanation">
      <div class="section-label">How It Works</div>
      <p>{escape_html(snippet['explanation'])}</p>
    </section>

    <section class="docs-section">
      <div class="section-label">Related Resources</div>
      <div class="docs-links">
        <a href="https://docs.scala-lang.org/scala3/" target="_blank" rel="noopener" class="doc-link">
          Scala 3 Documentation →
        </a>
        <a href="https://docs.scala-lang.org/scala3/guides/migration/compatibility-intro.html" target="_blank" rel="noopener" class="doc-link">
          Migration Guide →
        </a>
      </div>
    </section>
  </article>

  <footer>
    <p><a href="/scala-evolved/">scala.evolved</a> — Scala has evolved. Your code can too.</p>
    <p>Made with ❤️ for the Scala community</p>
    <p>Inspired by <a href="https://javaevolved.github.io" target="_blank" rel="noopener">java.evolved</a></p>
    <p><a href="https://github.com/scalaevolved/scala-evolved" target="_blank" rel="noopener">View on GitHub</a></p>
  </footer>

  <script src="/scala-evolved/app.js"></script>
  <script>
    // Copy button functionality
    document.querySelectorAll('.copy-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        const pre = btn.closest('.compare-panel').querySelector('.code-text');
        navigator.clipboard.writeText(pre.textContent).then(() => {{
          btn.textContent = 'Copied!';
          setTimeout(() => btn.textContent = 'Copy', 2000);
        }});
      }});
    }});
  </script>
</body>
</html>"""

    return html_content

# Create category directories
categories = set(s['category'] for s in snippets)
for category in categories:
    Path(category).mkdir(exist_ok=True)

# Generate all pages
for i, snippet in enumerate(snippets):
    prev_snippet = snippets[i-1] if i > 0 else None
    next_snippet = snippets[i+1] if i < len(snippets)-1 else None

    html_content = generate_page(snippet, prev_snippet, next_snippet)

    # Write file
    filepath = Path(snippet['category']) / f"{snippet['slug']}.html"
    with open(filepath, 'w') as f:
        f.write(html_content)

    print(f"✅ Generated: {filepath}")

print(f"\n🎉 Generated {len(snippets)} pages in {len(categories)} categories!")
