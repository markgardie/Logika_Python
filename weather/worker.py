import json
from urllib.parse import urlencode

import constants
import requests
from PyQt6.QtCore import (
    QObject,
    QRunnable,
    pyqtSignal,
    pyqtSlot,
)