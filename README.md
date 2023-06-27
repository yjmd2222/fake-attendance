[![Total clone count](https://img.shields.io/badge/dynamic/json?color=green&label=Total%20clones&query=count&url=https://raw.githubusercontent.com/yjmd2222/fake-attendance/stats/clones.json&logo=github)](https://github.com/yjmd2222/fake-attendance)[![Unique clone count](https://img.shields.io/badge/dynamic/json?color=blue&label=Unique&query=uniques&url=https://raw.githubusercontent.com/yjmd2222/fake-attendance/stats/clones.json&logo=github)](https://github.com/yjmd2222/fake-attendance)[![Today's clone count](https://img.shields.io/badge/dynamic/json?color=purple&label=Today%27s%20clones&query=clones[0][%27count%27]&url=https://raw.githubusercontent.com/yjmd2222/fake-attendance/stats/clones.json&logo=github)](https://github.com/yjmd2222/fake-attendance)

[![Total view count](https://img.shields.io/badge/dynamic/json?color=yellow&label=Total%20views&query=count&url=https://raw.githubusercontent.com/yjmd2222/fake-attendance/stats/views.json&logo=github)](https://github.com/yjmd2222/fake-attendance)[![Unique view count](https://img.shields.io/badge/dynamic/json?color=indigo&label=Unique&query=uniques&url=https://raw.githubusercontent.com/yjmd2222/fake-attendance/stats/views.json&logo=github)](https://github.com/yjmd2222/fake-attendance)[![Today's clone count](https://img.shields.io/badge/dynamic/json?color=orange&label=Today%27s%20views&query=views[0][%27count%27]&url=https://raw.githubusercontent.com/yjmd2222/fake-attendance/stats/views.json&logo=github)](https://github.com/yjmd2222/fake-attendance)

# Fake attendance script for you-know-what
For educational purposes only

## Requirements
Windows 10 or higher. If you want to use it as is, Windows 11 with default settings in Korean.

Run below in a Python 3 environment, 3.11.3 recommended.

`pip install -r requirements.txt`

Install the Chrome extension [Screen QR Reader](https://chrome.google.com/webstore/detail/screen-qr-reader/ekoaehpknadfoaolagjfdefeopkhfhln).

Fill out the template [info-template.py](fake_attendance/info-template.py) with your login, email information, and the zoom link without the `#success`. Rename the file to `info.py`

Note: If the module fails to download the Chrome extension source, you can try downloading it manually. Put it in the root of the repository. See [this](https://crx-downloader.com/how-it-works).

## Run
Run `python -m fake_attendance` for download, launch Zoom, and check_in. Read [How it works and why](#how-it-works-and-why) for explanation.

For testing QR scan scheduler, you can run `python test_scheduler.py YOUR-ARGUMENT-HERE` with `YOUR-ARGUMENT-HERE` as either:
- A text file that contains a 24-hour format time sets such as [test_times.txt](test_times.txt)
- A json-like format such as `'[{"hour": int, "minute": int},...]'`
- Leaving it blank to run scheduler at default times: See [settings.py](fake_attendance/settings.py)
- For a single test to fire right now, run `python -m fake_attendance.fake_check_in`.

## How it works and why
Last updated 2023-06-21

This module automates all check-ins for you-know-what: launch and quit Zoom at corresponding times and read the QR code in Zoom to complete the check-in form.
This check is done throughout the day. See [settings.py](fake_attendance/settings.py) for the actual timings.

So why this? My online class used to require I sit at the desk on Zoom from 9 AM to 6 PM (lunch time from 12 to 1 is excluded) with camera on the entire time.
This is ridiculous, and everyone must be thinking of putting on a fake recording of themself in the background. But the admins are going to send a QR image for us to check in every hour or two
which is on another level of shit. So I made a little script that scans the QR image on the Zoom meeting. They said they would give 10 minutes to check in,
so the script checks multiple times around the check-in time.

But then they changed the rules to allow turning off the Zoom camera, so this part is removed. You can look at the archived code in [turn_on_video.py](archive/turn_on_video.py)

The other day I learned Selenium and its RPA and APIs, so this is a little project of what I learned. The admins must be happy.

This is all a joke :) Interpreting what I mean with 'this' is up to you, as in the whole script or the whole situation.

## Credits
- You-know-what admins and the overseers and their disrespect for privacy that gave me the idea for this project
- tkobayashi0111 for [Screen QR Reader](https://chrome.google.com/webstore/detail/screen-qr-reader/ekoaehpknadfoaolagjfdefeopkhfhln)
- Yay me for starting and maintaining this project

## License
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This work is licensed under the Apache 2.0 License.
