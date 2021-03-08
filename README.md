# Webscraper
FE 595 Assignment 2

For this assignment you will be using your knowledge of HTML and the requests library to create a web scraper using Python. Create a new git repository for this submission. Do not reuse the git repository you used for assignment 1.

Your script should make a GET requests to `http://18.206.38.144:8000/random_company` to scrape 50 company names and purposes. You should save this this information to the file system of your computer, but you should NOT commit it to your git repository. Share this file with the other members of your group.

Important things to remember about this assignment: 
1. HTML is just text and you can treat it that way if you want. However there are a number of HTML libraries available in Python such as Beautiful Soup. It is not required, but you might find that library useful.
2. Only scrape the data you need. Don't clutter your data.
3. Writes to the file system are slow in comparison to writes to RAM. Find a way to only open and write to a file once.
4. The way you store your data is up to you, but make sure you can retrieve it later.
