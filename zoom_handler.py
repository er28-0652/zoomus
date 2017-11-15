import logging
import json

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request


class ZoomLogHandler(logging.Handler):
    def __init__(self, webhook_url, token):
        logging.Handler.__init__(self)
        self.webhook_url = webhook_url
        self.token = token
        self.formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] [%(module)s]')

    def _make_content(self, record):
        return {
            'title': self.format(record),
            'summary': record.msg['summary'],
            'body': record.msg['body']
        }

    def emit(self, record):
        try:
            req = Request(self.webhook_url)
            req.add_header('Content-Type', 'application/json')
            req.add_header('X-Zoom-Token', self.token)

            content = self._make_content(record)
            urlopen(req, json.dumps(content).encode('utf-8'))
        except:
            self.handleError(record)
