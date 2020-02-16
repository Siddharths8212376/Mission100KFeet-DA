# sending data to a server
import requests

API_ENDPOINT = 'http://pastebin.com/api/api_post.php'

API_KEY = '56c11331dce496e2ac91f09dc573e2e3'

data_file = open('raw_data.txt', mode='r', encoding='utf-8', errors='ignore')
data_ = data_file.read()
# print(data_)
data_post = {
    'api_dev_key':API_KEY,
    'api_option': 'paste',
    'api_paste_code': data_,
    'api_paste_format': 'text'
}

r = requests.post(url=API_ENDPOINT, data=data_post)

# extracting the response
pastebin_url = r.text
print("The pastebin URL is: %s" %pastebin_url)

# extracting back the text

# url = 'https://httpbin.org/post'

# files = {'file': open('raw_data.txt', mode='r', encoding='utf-8', errors='ignore')}

# r = requests.post(url, files=files)
# print(r.status_code)
# print(r.text)