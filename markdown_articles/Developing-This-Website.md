# Developing this website
_May 6, 2023_

Recently I've been writing a lot of notes out in Markdown. This eventually led me to want to start posting my notes onto a website. Most people would probably do this using Jekyll or Hugo, which are pretty solid options. I decided to develop my own simple website from scratch. It would definitely be a lot easier to just use a static site generator, but I just felt like creating this, so I created this :)

I was thinking of using something like ReactJS but just decided to go with vanilla HTML, CSS, and JavaScript. Maybe one day I'll make my own large webapp using a big framework, or maybe I'll just procastinate on that forever. 

This website uses a custom CMS (Content Management System) written in Python. Actually I kind of feel like calling it a CMS is kind of pretentious, it's literally just a single Python script. But it works, it adds content to the website pretty fast, which is cool.

I'll post some notes on here soon, I mainly wrote this article just to test out how the article is going to look.

## How the site works:
So basically, the site has three main directories: The root directory which contains all of the base files (index.html, contact.html, styles.css, etc).
Within this root directory, there's four sub-directories: articles, markdown_articles, images, and management. 

The management directory contains the CMS script, appropriately named manager.py. The markdown_articles directory is to contain all of my Markdown articles and the articles directory is where the respective HTML files for the articles are to be stored. I use the command-line a lot, so in order to push an article to my website, I made it so I just have to open the terminal in the management directory and run a command:

```
user@host management % python3 manager.py
Enter the name of the article: This is an Article Title\n
Enter the date: May 6, 2023
Enter the preview text: This article is about . . .
Enter the name of the Markdown file: This-Article.md
```

And then the python script automaticlly goes in and adds the appropratiate HTML elements in the appropriate file. Then it automatically creates a new HTML file. Finally it reads the Markdown file, converts that into HTML, and then updates the newly created file to contain the new HTML.

It's pretty amateurish I will admit... but it's simple, and it works :)))