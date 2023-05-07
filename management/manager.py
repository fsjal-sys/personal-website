import os, markdown

def get_block(title, date, preview):
    return f'''
                <div class="article">
                    <h1 class="article-title">{title}</h1>
                    <i class="article-date">{date}</i>
                    <p class="article-preview-text">{preview}</p>
                    <a href="../src/articles/{to_camel_case(title)}.html" class="read-more-link">>>Read More</a>
                </div>
    '''

def get_article_block():
    return f'''
<!DOCTYPE html>

<html>
    <head>
        <title>2kPILOT - HOME</title>
        <link rel="stylesheet" type="text/css" href="../styles.css">
        <script>

        </script>
    </head>
    
    <body>

        <div id="Banner">
            <h1>2kPILOT</h1>
            <img id="bit" src="../images/bit.png"/>
        </div>

        <div id="Navigator">
            <a href="../index.html"><h2>HOME</h2></a>
            <a href="../articles.html"><h2>ARTICLES</h2></a>
            <a href="../contact.html"><h2>CONTACT</h2></a>
        </div>

        <div class="content">
            <div class="article-Content-Wrapper">
                <!--LAST-->
            </div>
        </div>

        <div id="Footer">
            <p>2kPILOT 2023</p>
        </div>

    </body>
</html>
    '''

def insert_new_article(filepath, block):
    with open(filepath, 'r') as file:
        content = file.read()

    last_tag = "<!--LAST-->"
    new_content = content.replace(last_tag, last_tag + block)

    with open(filepath, 'w') as file:
        file.write(new_content)

def create_html_file(title, content):
    title = to_camel_case(title)

    file_path = f"../src/articles/{title}.html"
    with open(file_path, 'w') as file:
        file.write(content)

    return file_path

def insert_html_block(html_file, html_block):
    with open(html_file, 'r') as f:
        content = f.read()

    content = content.replace("<!--LAST-->", html_block + "<!--LAST-->")

    with open(html_file, 'w') as f:
        f.write(content)

def markdown_to_html(markdown_article_title):
    markdown_path = os.path.abspath(f"../markdown_articles/{markdown_article_title}.md")
    with open(markdown_path) as file:
        content = file.read()

    html_content = markdown.markdown(content)

    return html_content

def to_camel_case(s):
    words = s.split()
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

if __name__ == "__main__":
    title = input("Enter article title: ")
    date = input("Enter article date: ")
    preview = input("Enter article preview: ")

    block = get_block(title, date, preview)
    file_path = os.path.join(os.getcwd(), "../src/articles.html")
    insert_new_article(file_path, block)

    article_block = get_article_block()
    file_path = create_html_file(title, article_block)

    markdown_article_title = input("Enter the title of the markdown file (excluding .md): ")
    html_content = markdown_to_html(markdown_article_title)

    insert_html_block(file_path, html_content)
