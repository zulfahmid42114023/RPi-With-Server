import urllib2
import urllib

url = '' #your html in server

resp = urllib2.urlopen(url)
html = resp.read()
print html
