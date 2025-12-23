# 📝 WordPress to GitHub Export

Simple tool to export WordPress posts into categorized Markdown files for GitHub.

## 🚀 Quick Start

1. Install Python requirements:
```bash
pip install requests beautifulsoup4
```

2. Run the export:
```bash
python exportwordpressposts.py
```

3. Follow the prompts to:
   - Enter WordPress site URL
   - Select time period for export:
     - Last 24 hours
     - Last 7 days
     - Last 30 days
     - Everything
   - Choose file overwrite options

## 🌐 Compatible Sites

The tool works with WordPress sites that have a public API enabled, such as:
- https://techcrunch.com
- https://wordpress.org/news
- https://wptavern.com
- https://make.wordpress.org

## 📂 Output Format

Posts are organized by site domain and categories:
```
website-domain/
├── category1/
│   ├── images/
│   │   ├── post-title-1-image1.jpg
│   │   └── post-title-1-image2.png
│   └── post-title-1.md
└── category2/
    ├── images/
    │   └── post-title-2-image1.jpg
    └── post-title-2.md
```

Each file contains:
```markdown
# Post Title
Date: YYYY-MM-DD HH:MM:SS
Categories: Category1, Category2
---
Content here with updated image links...
```

## 🔄 Features

- Interactive WordPress site URL input
- Customizable time period for post export
- Downloads and organizes images locally
- Updates image references in markdown files
- Handles duplicate posts across categories
- Provides file overwrite options
- Shows export statistics (posts and images)
- Site-specific folder organization

## ⚠️ Troubleshooting

- SSL errors are automatically handled
- For existing files, you can:
  1. Ask for each file
  2. Overwrite all
  3. Skip all existing
- Some WordPress sites may require authentication and won't work with this tool

## 📊 Statistics

After export, the script shows:
- Total unique posts exported
- Total images downloaded
- Processing progress per page

## 📜 License

MIT License

---

**Part of the [Python Projects Collection](../README.md)**
