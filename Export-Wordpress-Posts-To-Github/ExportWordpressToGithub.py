# 📝 WordPress to GitHub Export
import os
import re
import requests
import urllib3
from datetime import datetime
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# Simple tool to export WordPress posts into categorized Markdown files for GitHub.

def sanitize_filename(title):
    return re.sub(r'[^\w\s-]', '', title).strip().lower().replace(' ', '-')

def download_image(image_url, category_dir, post_title, site_url, image_counter):
    try:
        # Handle relative URLs
        if image_url.startswith('//'):
            image_url = 'https:' + image_url
        elif image_url.startswith('/'):
            image_url = site_url + image_url
        elif not image_url.startswith(('http://', 'https://')):
            image_url = site_url + '/' + image_url

        # Create images directory inside category
        images_dir = os.path.join(category_dir, 'images')
        if not os.path.exists(images_dir):
            os.makedirs(images_dir)
        
        # Get image filename from URL
        image_name = os.path.basename(urlparse(image_url).path)
        # Sanitize image name
        image_name = re.sub(r'[^\w\-._]', '', image_name)
        # Save image with post title prefix to avoid conflicts
        image_name = f"{sanitize_filename(post_title)}-{image_name}"
        
        image_path = os.path.join(images_dir, image_name)
        
        # Download image
        response = requests.get(image_url, verify=False)
        if response.status_code == 200:
            with open(image_path, 'wb') as f:
                f.write(response.content)
            image_counter[0] += 1  # Increment image counter
            # Return relative path for markdown
            return f'images/{image_name}'
    except Exception as e:
        print(f"Error downloading image {image_url}: {e}")
    return None

def process_content(content, category_dir, post_title, site_url, image_counter):
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find all images
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            # Download image and get new path
            new_path = download_image(src, category_dir, post_title, site_url, image_counter)
            if new_path:
                # Update image source in content
                content = content.replace(src, new_path)
    
    return content

def create_markdown_content(post_data):
    content = f"# {post_data['title']}\n\n"
    content += f"Date: {post_data['date']}\n\n"
    content += f"Categories: {', '.join(post_data['categories'])}\n\n"
    content += "---\n\n"
    content += post_data['content']
    return content

def get_posts(site_url, per_page=100, page=1):
    url = f"{site_url}/wp-json/wp/v2/posts"
    params = {
        'per_page': per_page,
        'page': page,
        'status': 'publish',
        '_embed': 'true'
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive'
    }
    
    session = requests.Session()
    session.verify = False
    urllib3.disable_warnings()
    
    response = session.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        total_pages = int(response.headers.get('X-WP-TotalPages', 1))
        return response.json(), total_pages
    elif response.status_code == 400:
        return None, 0
    else:
        print(f"Error: HTTP {response.status_code} - {response.text}")
        return None, 0

def file_exists_check(filepath):
    if os.path.exists(filepath):
        response = input(f"File {filepath} already exists. Do you want to overwrite? (y/n): ")
        return response.lower() == 'y'
    return True

def main():
    site_url = "https://solucoesms.com.br"
    
    output_dir = "github_solutions"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    page = 1
    total_posts = 0
    unique_posts = set()  # Track unique posts
    image_counter = [0]  # Use list to allow modification in nested functions
    
    # Add before the main loop
    overwrite_all = None

    while True:
        try:
            posts, total_pages = get_posts(site_url, page=page)
            if not posts:
                break

            for post in posts:
                # Extract categories
                categories = []
                if '_embedded' in post and 'wp:term' in post['_embedded']:
                    for terms in post['_embedded']['wp:term']:
                        for term in terms:
                            if term['taxonomy'] == 'category':
                                categories.append(term['name'])

                if not categories:
                    categories = ['uncategorized']

                post_data = {
                    'title': post['title']['rendered'],
                    'content': post['content']['rendered'],
                    'date': datetime.fromisoformat(post['date']).strftime('%Y-%m-%d %H:%M:%S'),
                    'categories': categories
                }

                # Create category directories and save files
                for category in categories:
                    category_dir = os.path.join(output_dir, sanitize_filename(category))
                    if not os.path.exists(category_dir):
                        os.makedirs(category_dir)

                    filename = f"{sanitize_filename(post_data['title'])}.md"
                    filepath = os.path.join(category_dir, filename)

                    # Check if file exists and handle overwrite
                    if overwrite_all is None and os.path.exists(filepath):
                        response = input("Files already exist. Do you want to: \n"
                                      "1. Ask for each file\n"
                                      "2. Overwrite all\n"
                                      "3. Skip all existing\n"
                                      "Choose (1/2/3): ")
                        if response == '2':
                            overwrite_all = True
                        elif response == '3':
                            overwrite_all = False

                    should_write = True
                    if overwrite_all is not None:
                        should_write = overwrite_all
                    elif os.path.exists(filepath):
                        should_write = file_exists_check(filepath)

                    if should_write:
                        # Process content to download images and update references
                        processed_content = process_content(post_data['content'], category_dir, post_data['title'], site_url, image_counter)
                        post_data['content'] = processed_content

                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(create_markdown_content(post_data))
                        print(f"Processed post: {post_data['title']}")
                        unique_posts.add(post_data['title'])  # Add to unique posts set
                    else:
                        print(f"Skipped existing post: {post_data['title']}")

                    total_posts += 1

            print(f"Processed page {page}/{total_pages} - Total posts: {total_posts}")
            
            if page >= total_pages:
                break
                
            page += 1
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching posts: {e}")
            break

    print(f"Export completed successfully!")
    print(f"Total unique posts exported: {len(unique_posts)}")
    print(f"Total images downloaded: {image_counter[0]}")

if __name__ == "__main__":
    main()
