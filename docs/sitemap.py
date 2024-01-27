# i want you to make a sitemap for me in programmatic way that too manually like all html files in all subdirectories and their sub-folders of this directory should be made into a sitemap.xml file
import os

# Define the directory you want to start from
rootDir = '.'

sitemap = open("sitemap.xml", "w")
sitemap.write('<?xml version="1.0" encoding="UTF-8"?>\n')
sitemap.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

# index.html 

sitemap.write('<url>\n')
sitemap.write('<loc>https://testing.collegehive.in</loc>\n')
sitemap.write('</url>\n')


site_url = 'https://testing.collegehive.in/docs/'

for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        if fname.endswith('.html'):
            sitemap.write('<url>\n')
            link = os.path.join(dirName, fname)
            # it is generating a link like this https://testing.collegehive.in/docs.\2nd_sem\site\home.html
            # but i want it to be https://testing.collegehive.in/docs/2nd_sem/site/home.html
            # so i want you to remove the .\ from the link
            # if link.startswith(".\"):
            link = link[2:]
            sitemap.write('<loc>' + site_url + link + '</loc>\n')
            sitemap.write('</url>\n')

sitemap.write('</urlset>')
sitemap.close()

