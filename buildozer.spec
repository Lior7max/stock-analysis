[app]
title = מעקב מניות
package.name = stocktracker
package.domain = org.stocktracker
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

requirements = python3,kivy,requests,urllib3,charset-normalizer,idna,certifi

orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.arch = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1