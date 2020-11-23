# -*- coding: utf-8 -*-

from google_images_download import google_images_download
import glob
import os

config = {
    "Records": [
        {
            "keywords": "日本　一軒家",
            "no_numbering": True,
            "limit": 100,
            "output_directory": "images",
            "image_directory": "building",
            "chromedriver": "/usr/local/bin/chromedriver",

        }
    ]
}

response = google_images_download.googleimagesdownload()
for rc in config["Records"]:
    response.download(rc)

gifImgs = glob.glob("images" + os.sep + "*" + os.sep + "*.gif")
print(f"removing gif files: {len(gifImgs)} files")
_ = [os.remove(f) for f in gifImgs]
