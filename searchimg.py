from pickle import TRUE
from bing_image_urls import bing_image_urls

url = bing_image_urls("Samsung orj şervİs ekranı A310 BEYAZ", limit=1,verify_status_only=TRUE)[0]

print(url)
