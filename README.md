# zoomus
scripts for zoom.us

# Usage
use as zoon client
```python
from zoom_client import ZoomClient

ZOOM_URL = 'YOUR_OWN_WEBHOOK_URL'
ZOOM_TOKEN = 'YOUR_TOKEN_FOR_ZOOM'

zoom = ZoomClient(ZOOM_URL, ZOOM_TOKEN)
# just send message as body
zoo.send_msgm('hello zoom')
# add title and summary
zoom.send_msg('hello zoom', title='title', summary='summary)
# add send botton
zoom.send_msg('hello zoom', action='send')
```

use as log handler
```python
import logging
from zoom_handler import ZoomLogHandler

ZOOM_URL = 'YOUR_OWN_WEBHOOK_URL'
ZOOM_TOKEN = 'YOUR_TOKEN_FOR_ZOOM'

zoom_handler = ZoomLogHandler(ZOOM_URL, ZOOM_TOKEN)
logger = logging.getLogger(__name__)
logger.addHandler(zoom_handler)
logger.setLevel(logging.INFO)

logger.info(('summary', 'body'))
```
