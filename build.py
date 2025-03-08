import os

# Read the header and footer content
header = open('includes/header.html').read()
footer = open('includes/footer.html').read()

# Ensure the docs directory exists
if not os.path.exists('docs'):
    os.makedirs('docs')

# Process each page
for page in os.listdir('pages'):
    if page.endswith('.html'):
        # Read the page content
        content = open(os.path.join('pages', page)).read()
        # Extract the parts before and after the <body> content
        head_start = content.find('<body>')
        head_end = content.find('</body>')
        if head_start != -1 and head_end != -1:
            head_part = content[:head_start + 6]  # Include <body>
            body_content = content[head_start + 6:head_end]
            foot_part = content[head_end:]  # Include </body>
            # Combine with header and footer
            full_page = head_part + '\n' + header + '\n' + body_content + '\n' + footer + '\n' + foot_part
            # Write to the docs directory
            with open(os.path.join('docs', page), 'w') as f:
                f.write(full_page)