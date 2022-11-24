import pyqrcode

s="https://www.instagram.com/python.times/"

url = pyqrcode.create(s)

url.svg("your qrcode.svg",scale=8)