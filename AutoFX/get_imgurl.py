import random
import re
def search_images(md_file):
    with open(md_file, 'r', encoding='utf-8') as file:
        md_content = file.read()

    # Regular expression to find image URLs in Markdown with ![]() syntax
    markdown_pattern = re.compile('!\[.*?\]\((.*?)\)')

    # Regular expression to find image URLs in Markdown with <img> tag
    img_pattern = re.compile('<img.*?src=["\'](.*?)["\']', re.IGNORECASE)

    # Find all image URLs in the Markdown content
    markdown_urls = re.findall(markdown_pattern, md_content)
    img_urls = re.findall(img_pattern, md_content)

    # Combine the two lists of image URLs
    all_image_urls = markdown_urls + img_urls

    # Check if there are any images
    if not all_image_urls:
        print("No images found in the Markdown file.")
        return None

    # Select a random image URL
    random_image_url = random.choice(all_image_urls)

    return random_image_url
md_file = r'D:\MyBlog\source\_posts\Paper\Awesome-Talking-Head-Synthesis.md'
print(search_images(md_file))