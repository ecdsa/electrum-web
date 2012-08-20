import urllib, zipfile, os
p="http://electrum-desktop.com/files/"
n="e4a"
nz=n+".zip"
urllib.urlretrieve(p,nz)
zipfile.ZipFile(nz).extractall()
os.rename(n,'scripts/'+n)
