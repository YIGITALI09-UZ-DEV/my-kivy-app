[app]
title = MyApp
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg,txt
version = 0.1
requirements = python3,kivy,pillow
orientation = portrait

# Android sozlamalari
android.api = 33
android.arch = armeabi-v7a
# android.ndk = 23b  # GitHub Actions default NDK ishlatadi

[buildozer]
log_level = 2