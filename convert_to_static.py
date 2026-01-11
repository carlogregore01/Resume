import re

# Read the template file
with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Flask url_for with static paths
content = re.sub(r"{{\s*url_for\('static',\s*filename='([^']+)'\)\s*}}", r'./static/\1', content)

# Write to root directory
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Static index.html created successfully!')
