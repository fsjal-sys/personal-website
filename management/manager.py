import os

def get_article_block(title, date, preview):
    return f'''
                <div class="article">
                    <h1 class="article-title">{title}</h1>
                    <i class="article-date">{date}</i>
                    <p class="article-preview-text">{preview}</p>
                    <a href="#" class="read-more-link">>>Read More</a>
                </div>
'''

def insert_new_article(filepath, block):
    with open(filepath, 'r') as file:
        content = file.read()

    last_tag = "<!--LAST-->"
    new_content = content.replace(last_tag, last_tag + block)

    with open(filepath, 'w') as file:
        file.write(new_content)

if __name__ == "__main__":
    title = input("Enter article title: ")
    date = input("Enter article date: ")
    preview = input("Enter article preview: ")

    block = get_article_block(title, date, preview)
    file_path = os.path.join(os.getcwd(), "../src/articles.html")
    insert_new_article(file_path, block)
