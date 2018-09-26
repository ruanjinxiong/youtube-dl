# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor

class ZingMp3IE(InfoExtractor):
    _VALID_URL = r'https?://mp3\.zing\.vn/(?:bai-hat|album|playlist|video-clip)/[^/]+/(?P<id>\w+)\.html'
    _TESTS = [{
        'url': 'http://mp3.zing.vn/bai-hat/Xa-Mai-Xa-Bao-Thy/ZWZB9WAB.html',
        'md5': 'ead7ae13693b3205cbc89536a077daed',
        'info_dict': {
            'id': 'ZWZB9WAB',
            'title': 'Xa Mãi Xa',
            'ext': 'mp3',
            'thumbnail': r're:^https?://.*\.jpg$',
        },
    }, {
        'url': 'http://mp3.zing.vn/video-clip/Let-It-Go-Frozen-OST-Sungha-Jung/ZW6BAEA0.html',
        'md5': '870295a9cd8045c0e15663565902618d',
        'info_dict': {
            'id': 'ZW6BAEA0',
            'title': 'Let It Go (Frozen OST)',
            'ext': 'mp4',
        },
    }, {
        'url': 'http://mp3.zing.vn/album/Lau-Dai-Tinh-Ai-Bang-Kieu-Minh-Tuyet/ZWZBWDAF.html',
        'info_dict': {
            '_type': 'playlist',
            'id': 'ZWZBWDAF',
            'title': 'Lâu Đài Tình Ái - Bằng Kiều,Minh Tuyết | Album 320 lossless',
        },
        'playlist_count': 10,
        'skip': 'removed at the request of the owner',
    }, {
        'url': 'http://mp3.zing.vn/playlist/Duong-Hong-Loan-apollobee/IWCAACCB.html',
        'only_matching': True,
    }]
    IE_NAME = 'zingmp3'
    IE_DESC = 'mp3.zing.vn'

    def _real_extract(self, url):
        page_id = self._match_id(url)

        webpage = self._download_webpage(url, page_id)

        player_json_url = self._search_regex([
            r'data-xml="([^"]+)',
            r'&amp;xmlURL=([^&]+)&'
        ], webpage, 'player xml url')

        player_json_url = "https://mp3.zing.vn/xhr" + player_json_url

        playlist_title = None
        page_type = self._search_regex(r'type=([^/-]+)&', player_json_url, 'page type')

        player_json = self._download_json(player_json_url, page_id, 'Downloading Player JSON')
        items = player_json['data']
        source = items.get('source')
        print(source.get('128'))
        return {
            'id': page_id,
            'title': (items.get('name') or item.get('title')).strip(),
            'url': source.get('128'),
            'ext': 'mp3',
            'thumbnail': items.get('thumbnail'),
            'artist': items.get('artist'),
        }






