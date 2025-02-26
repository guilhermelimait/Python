# 📝 WordPress to GitHub Export

Simple tool to export WordPress posts into categorized Markdown files for GitHub.

## 🚀 Quick Start

1. Install Python requirements:
```bash
pip install requests beautifulsoup4
```

2. Update your WordPress URL in the script:
```python
site_url = "https://your-wordpress-site.com"
```

3. Run the export:
```bash
python exportwordpressposts.py
```

## 📂 Output Format

Posts are organized by categories with their images:
```
github_solutions/
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

- Exports all published posts from WordPress
- Downloads and organizes images locally
- Updates image references in markdown files
- Handles duplicate posts across categories
- Provides file overwrite options
- Shows export statistics (posts and images)

## ⚠️ Troubleshooting

- SSL errors are automatically handled with certificate verification disabled
- For existing files, you can:
  1. Ask for each file
  2. Overwrite all
  3. Skip all existing

## 📊 Statistics

After export, the script shows:
- Total unique posts exported
- Total images downloaded
- Processing progress per page

## 📜 License

MIT License
