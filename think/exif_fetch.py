from urllib.request import urlopen
from urllib.parse import urlsplit
from os.path import basename
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS


def find_images(url):
    print('[+] Finding images on %s' % url)
    url_content = urlopen(url).read()
    soup = BeautifulSoup(url_content)
    return soup.findAll('img')


def download_image(img_tag):
    try:
        print('[+] Downloading image...')
        img_src = img_tag['src']
        img_content = urlopen(img_src).read()
        img_fn = basename(urlsplit(img_src)[2])
        img_f = open(img_fn, 'wb')
        img_f.write(img_content)
        img_f.close()
        return img_fn
    except Exception as e:
        return ''


def test_for_exif(img_fn):
    try:
        exif_data = {}
        img_f = Image.open(img_fn)
        info = img_f._getexif()
        if info:
            for (tag, val) in info.items():
                decoded = TAGS.get(tag, tag)
                exif_data[decoded] = value
            exif_gps = exif_data['GPSInfo']
            if exif_gps:
                print('[*] %s contains GPS MetaData' % img_fn)
    except Exception as e:
        pass




url = 'http://www.flickr.com/photos/dvids/4999001925/sizes/o'

img_tags = find_images(url)
for img_tag in img_tags:
    img_fn = download_image(img_tag)
    test_for_exif(img_fn)
