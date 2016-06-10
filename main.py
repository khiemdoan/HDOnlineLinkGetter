import requests
import re
import json


def get_link_video(link):
    r = requests.get(link)
    r.close()

    # lay cooie
    cookie = re.search(r'__cfduid=[\w]+', r.headers['Set-Cookie'], re.M | re.I).group()

    # lay fid
    fid = re.search(r'PlayFilm.*\d+', r.text, re.M | re.I).group()
    fid = re.search(r'\d+', fid, re.M | re.I).group()

    # lay token
    token = re.search(r'\w{96}.*\d{10}', r.text, re.M | re.I).group()
    token = token.replace('|', '-')

    headers = dict()
    headers['Accept'] = 'application/json, text/javascript, */*; q=0.01'
    headers['Accept-Encoding'] = 'gzip, deflate, sdch'
    headers['Accept-Language'] = 'en-US,en;q=0.8,vi;q=0.6'
    headers['Cache-Control'] = 'max-age=0'
    headers['Connection'] = 'keep-alive'
    headers['Cookie'] = cookie +'; PHPSESSID=j3gpim2rp04baa1hsttbbh8t77; alertMobile=Fri Jun 10 2016 14:45:11 GMT+0700 (ICT); gsScrollPos=0; _gat_HDViet=1; UWatch={"12433":{"ep":"102208","add":1465547236}}; _gat=1; _ga=GA1.2.9111453.1465544711; jwplayer.captionconfig={"back":false,"fontSize":20,"fontFamily":"Arial","fontOpacity":100,"color":"#FFFFFF","backgroundColor":"#000","backgroundOpacity":50,"edgeStyle":"uniform","windowColor":"#FFF","windowOpacity":0,"delayTime":0,"textShadow":"#080808","captionSecondPos":"below"}'
    headers['Host'] = 'hdonline.vn'
    headers['Referer'] = link
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'

    xmlplay_url = 'http://hdonline.vn/frontend/episode/xmlplay?ep=1&fid=' + fid + '&token=' + token + '&format=json'
    r = requests.get(xmlplay_url, headers=headers)
    r.close()

    data = json.loads(r.text)
    return data['level'][0]['file']


if __name__ == "__main__":
    link = input('Enter url: ')
    link = link.strip()
    print(get_link_video(link))
