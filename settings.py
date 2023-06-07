'''
Settings
'''

from helper import get_file_path

# Screen QR Reader interaction
SCREEN_QR_READER_POPUP_LINK = \
    'chrome-extension://ekoaehpknadfoaolagjfdefeopkhfhln/src/popup/popup.html'
SCREEN_QR_READER_SOURCE = get_file_path('extension_0_1_2_0.crx')

# Screen QR Reader download
GET_CRX_LINK = 'https://crx-downloader.com/'
SCREEN_QR_READER_WEBSTORE_LINK = \
    'https://chrome.google.com/webstore/detail/screen-qr-reader/ekoaehpknadfoaolagjfdefeopkhfhln'
# SCREEN_QR_READER_SOURCE_PATH = get_file_path('extension_0_1_2_0.crx')

# Launch zoom
ZOOM_LINK = 'https://zoom.us/j/4151086241?pwd=Nm5LWHYvUEhhUC9NTVg4V2lNRG5LQT09'

# PyAutoGUI
# continue with download
CONTINUE_IMAGE = get_file_path('continue_with_download.png', 'images')
# start video
START_IMAGE = get_file_path('start_video.png', 'images')
CONFERENCE_NAME = 'Zoom 회의'

# APScheduler timings
MINUTES = 7 # every 7 minutes
VIDEO_ON_HOUR = 13   # at hour 13
VIDEO_ON_MINUTE = 0  # at minute 0
ZOOM_ON_HOUR = 12    # at hour 12
ZOOM_ON_MINUTE = 55  # at minute 55

# misc
ZOOM_RESIZE_PARAMETERS = (0, 0, 1000, 800) # Reduce Zoom window size
