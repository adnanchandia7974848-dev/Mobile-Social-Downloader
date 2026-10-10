[app]

# (str) Title of your application
title = A Social Downloader

# (str) Package name
package.name = asocialdownloader

# (str) Package domain (needed for android/ios packaging)
package.domain = org.asocial.downloader

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,yt-dlp,requests,plyer,pillow,urllib3,certifi,idna,charset_normalizer

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (bool) If true, then skip try to update the Android sdk apps
android.skip_update = False

# (bool) If true, then automatically accept SDK licenses
android.accept_sdk_license = True

# (list) List of Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
