[app]

title = 车位导航
package.name = parkingnav
package.domain = com.parking

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

requirements = python3,kivy,pyjnius,android

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,BLUETOOTH_SCAN,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION

android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk = 31
android.build_tools_version = 31.0.0
android.skip_update = False
android.accept_sdk_license = True

android.archs = arm64-v8a,armeabi-v7a

android.allow_backup = True

android.wakelock = True

android.gradle_dependencies = 

android.add_src = 

android.manifest.intent_filters = 

services = 

p4a.branch = develop

p4a.bootstrap = sdl2

p4a.local_recipes = 

p4a.hook = 

p4a.port = 

log_level = 2

warn_on_root = 1


[buildozer]

log_level = 2

warn_on_root = 1
