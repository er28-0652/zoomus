import json
from datetime import datetime

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request



class ZoomClient:
    def __init__(self, webhook_url, token):
        self.req = Request(webhook_url)
        self.req.add_header('Content-Type', 'application/json')
        self.req.add_header('X-Zoom-Token', token)
        
    def send_msg(self, body, title=None, summary=None, action=None):
        title = title or datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        summary = summary or ""
        content = make_content(title, summary, body, action)
        conn = urlopen(self.req, json.dumps(content).encode('utf-8'))
        return conn.getcode()

    @staticmethod
    def make_content(title, summary, body, action=None):
            content =  {
                'title': '<p><label>{}</label></p>'.format(title),
                'summary': '<p><label>{}</label></p>'.format(summary),
                'body': '<p><label style="color: black;">{}</label></p>'.format(body)
            }
            if action is not None:
                content['actions'] = {
                    'send': "<p><button onclick=\"sendMsg('1', {})\">send</button></p>",
                    'copy': "<p><button onclick=\"copyMsg('1', {})\">copy</button></p>"
                }.get(action).format(body)
            return content
