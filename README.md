
## Developing / adding content
https://docs.getpelican.com/en/latest/quickstart.htmlhttps://docs.getpelican.com/en/latest/content.html
https://docs.getpelican.com/en/latest/content.html

(requires installing pelican)
```
python -m pip install "pelican[markdown]" # install pelican
# clone the repository
pelican content # generate website
pelican --listen # start server locally
```

## Publishing to GitHub
https://docs.getpelican.com/en/3.5.0/tips.html

(requires installing pelican and ghp-import, through pip)
```
pelican content -o output -s pelicanconf.py
ghp-import output
git push origin gh-pages
```