import markdown

def insert_block(title,date,previewText):
    block = f"""                
    <div class="article">
        <a href="markdown_articles/{format(title)}/{format(title)}.html">{title}</a>
        <p>{date}</p>
        <p id="Preview">{previewText}</p>
    </div>
    """
    with open("../articles.html", 'r') as f:
        lines = f.readlines()
    with open("../articles.html", 'w') as f:
        for line in lines:
            f.write(line)
            if (line.strip() == "<!--LAST-->"):
                f.write(block)

def convert_md_to_html(title):
    markdown_text = ""
    with open(f"../markdown_articles/{title}/{title}.md", 'r') as f:
        lines = f.readlines()
        for line in lines:
            markdown_text += line + "\n"
    return markdown.markdown(markdown_text)

def format(title):
    return title.replace(" ", "")

def create_page(title):
    page_block = f"""
<!DOCTYPE html>

<html>
    <head>
        <link rel="stylesheet" type="text/css" href="../../styles.css">
        <link rel="icon" type="image/png" href="../../images/logo.png">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Share+Tech&display=swap" rel="stylesheet">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Audiowide&display=swap" rel="stylesheet">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Orbitron&display=swap" rel="stylesheet">
        <title>Eclipse_Cube - Articles</title>
    </head>

    <body>
        <div id="Top">
            <div id="Left">
                <div id="Date">Date: </div>
                <div id="IP">Your IP: </div>
                <div id="Location"></div>
            </div>
            <div id="ToggleMode" onclick="toggleMode()"></div>
        </div>
        <div id="Bottom">
        <div id="Navigator">
            <div id="LogoContainer">
                <div class="cube">
                    <div class="face front cubeface"><div class="circle"></div></div>
                    <div class="face back cubeface"><div class="circle"></div></div>
                    <div class="face left cubeface"><div class="circle"></div></div>
                    <div class="face right cubeface"><div class="circle"></div></div>
                    <div class="face top cubeface"><div class="circle"></div></div>
                    <div class="face bottom cubeface"><div class="circle"></div></div>
                </div>
                <h1 id="Title">Eclipse_Cube</h1>
            </div>
            <div id="LinkContainer">
                <a href="../../index.html"><p>Homepage</p></a>
                <a href="../../articles.html"><p>Articles</p></a>
                <a href="../..socials.html"><p>Socials</p></a>
            </div>
        </div>
        <div id="Content" class="articleContent">
            <!--LAST-->
        </div>
        </div>
        <script src="../../script.js"></script>
    </body>
</html>
"""
    title = format(title)
    with open(f"../markdown_articles/{title}/{title}.html", 'w') as f:
        f.write(page_block)
        f.close()
    with open(f"../markdown_articles/{title}/{title}.html", 'r') as f:
        lines = f.readlines()
    with open(f"../markdown_articles/{title}/{title}.html", "w") as f:
        for line in lines:
            f.write(line)
            if (line.strip() == "<!--LAST-->"):
                f.write(convert_md_to_html(title))

def main():
    title = input("Enter the title for the article: ")
    date = input("Enter the date: ")
    previewText = input("Enter the preview text: ")
    insert_block(title,date,previewText)
    create_page(title)

if __name__ == "__main__":
    main()