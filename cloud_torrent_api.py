import urllib.request
import http.cookiejar
import base64
import sys


class CloudTorrentApi(object):
    def __init__(self, cloud_torrent_api_url, user, password):
        self.cloud_torrent_api_url = cloud_torrent_api_url
        self.user = user
        self.password = password

        # install opener with cookiejar and auth header
        self.cookie = http.cookiejar.CookieJar()
        self.cookie_processor = urllib.request.HTTPCookieProcessor(self.cookie)
        self.opener = urllib.request.build_opener(self.cookie_processor)
        self.credentials = ("%s:%s" % (user, password))
        self.encode_credentials = base64.b64encode(self.credentials.encode())
        self.opener.addheaders = [
            ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0"),
            ("Authorization", "Basic %s" % self.encode_credentials.decode())
        ]
        urllib.request.install_opener(self.opener)

    def download(self, url):

        api = self.cloud_torrent_api_url + "/api/magnet"

        headers = {
            'accept': "application/json, text/plain, */*",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            'content-type': "application/json;charset=UTF-8",
            'accept-language': "zh-CN,zh;q=0.8,en;q=0.6",
        }

        url = url.encode("utf-8")
        request = urllib.request.Request(api, url, headers)
        responce = urllib.request.urlopen(request)
        data = responce.read().decode("utf-8")
       
        if data != "OK":
            print("Start download task failed.")
            sys.exit(1)
        else:
            print("Download started.")
