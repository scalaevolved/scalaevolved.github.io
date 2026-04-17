# scala.evolved

**Scala has evolved. Your code can too.**

🔗 **[scalaevolved.github.io](https://scalaevolved.github.io)**

A collection of side-by-side code comparisons showing old Scala 2 patterns next to their clean, modern Scala 3 replacements.

🔗 **Live site:** (coming soon)

## What is this?

Every snippet shows two panels:

- **✕ Scala 2** — the traditional way (Scala 2.13)
- **✓ Scala 3** — the clean, modern replacement (Scala 3.x)

Each comparison includes an explanation of *why* the modern approach is better and which Scala version introduced it.

## Categories

| Category | Examples |
|---|---|
| **Enums & ADTs** | Enums for algebraic data types, cleaner ADT syntax |
| **Contextual Abstractions** | Given instances, using clauses, extension methods |
| **Type System** | Union types, intersection types, opaque types, match types |
| **Syntax** | Top-level definitions, optional braces, indentation syntax |
| **Metaprogramming** | Inline methods, macros, quotes and splices |
| **Collections** | Improved APIs and syntax |

## How to use

### Local development

Simply open `index.html` in your browser, or serve with any static server:

```bash
# Python 3
python3 -m http.server 8000

# PHP
php -S localhost:8000

# Node.js
npx http-server

# Or just open directly
open index.html  # macOS
xdg-open index.html  # Linux
```

Then navigate to `http://localhost:8000`

### Deploy to GitHub Pages

1. Push this repository to GitHub
2. Go to Settings → Pages
3. Set Source to "Deploy from a branch"
4. Select branch `main` and folder `/` (root)
5. Save and wait for deployment

## Architecture

This project is built with:

- **Plain HTML, CSS, and JavaScript** — no build step, no frameworks
- **JSON data** — examples stored in `data/snippets.json`
- **CSS Variables** — dark/light themes
- **Frontend-only** — fully static, works anywhere

The structure is inspired by [java.evolved](https://javaevolved.github.io), which uses a similar approach but with a build pipeline.

## Features

- 🌓 **Dark/light theme** toggle
- 🔍 **Search** functionality (⌘K / Ctrl+K)
- 🏷️ **Filter** by category
- 📱 **Responsive** design
- 🚀 **Zero dependencies** — no npm, no build
- ⚡ **Fast** — pure static HTML

## Contributing

Contributions are welcome! To add a new pattern:

1. Edit `data/snippets.json`
2. Add a new object with this structure:

```json
{
  "id": 11,
  "slug": "your-pattern-slug",
  "title": "Pattern Title",
  "category": "category-name",
  "difficulty": "beginner|intermediate|advanced",
  "scalaVersion": "3.0",
  "oldLabel": "Scala 2",
  "modernLabel": "Scala 3",
  "oldCode": "// Old Scala 2 code",
  "modernCode": "// New Scala 3 code",
  "summary": "One-line description",
  "explanation": "Detailed explanation"
}
```

3. Test locally
4. Submit a pull request

## Tech Stack

- Plain HTML5, CSS3, JavaScript ES6+
- CSS Grid and Flexbox for layout
- CSS Variables for theming
- Local Storage for preferences
- Fetch API for data loading

## Inspiration

This project is inspired by [java.evolved](https://javaevolved.github.io) by [Bruno Borges](https://github.com/brunoborges).

## License

MIT License - see [LICENSE](LICENSE) for details.

## Resources

- [Scala 3 Book](https://docs.scala-lang.org/scala3/book/introduction.html)
- [Scala 3 Migration Guide](https://docs.scala-lang.org/scala3/guides/migration/compatibility-intro.html)
- [Scala 3 Reference](https://docs.scala-lang.org/scala3/reference/)
- [New in Scala 3](https://docs.scala-lang.org/scala3/new-in-scala3.html)

## Credits

- Design and frontend structure inspired by [java.evolved](https://javaevolved.github.io)
- Solarized-inspired color scheme
- Icons from embedded SVG
