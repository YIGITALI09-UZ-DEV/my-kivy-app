[app]
title = MyApp
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg,txt
version = 0.1
requirements = python3,kivy,pillow,cython
orientation = portrait

# Android sozlamalari
android.api = 33
android.archs = armeabi-v7a  # eski android.arch o‘rniga
[buildozer]
log_level = 2