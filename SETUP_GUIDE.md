# 详细安装和构建指南

本指南提供完整的环境配置和 APK 构建步骤。

## 目录

1. [环境准备](#环境准备)
2. [安装依赖](#安装依赖)
3. [构建 APK](#构建-apk)
4. [问题排查](#问题排查)
5. [高级配置](#高级配置)

## 环境准备

### 推荐系统

- **Ubuntu 22.04 LTS**（推荐）
- Ubuntu 20.04 LTS
- Debian 11+
- 其他 Linux 发行版（可能需要调整依赖包名）

### 硬件要求

- CPU: 4核心以上
- 内存: 8GB+
- 磁盘: 至少 20GB 可用空间
- 网络: 稳定的互联网连接

## 安装依赖

### 步骤 1: 更新系统

```bash
sudo apt-get update
sudo apt-get upgrade -y
```

### 步骤 2: 安装 Java JDK

```bash
# 安装 OpenJDK 17
sudo apt-get install -y openjdk-17-jdk

# 验证安装
java -version
javac -version

# 设置 JAVA_HOME
echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### 步骤 3: 安装 Python 和开发工具

```bash
# 安装 Python 3 和 pip
sudo apt-get install -y python3 python3-pip python3-dev

# 安装构建工具
sudo apt-get install -y \
    git \
    zip \
    unzip \
    autoconf \
    libtool \
    pkg-config \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libtinfo5 \
    cmake \
    libffi-dev \
    libssl-dev \
    build-essential \
    ccache \
    libsqlite3-dev \
    libreadline-dev \
    libbz2-dev \
    libgdbm-dev \
    libgdbm-compat-dev \
    liblzma-dev

# 验证安装
python3 --version
pip3 --version
```

### 步骤 4: 安装 Buildozer 和 Cython

```bash
# 升级 pip
pip3 install --user --upgrade pip

# 安装 Buildozer 和 Cython
pip3 install --user --upgrade buildozer
pip3 install --user cython==0.29.33

# 添加用户 bin 目录到 PATH
echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

# 验证安装
buildozer --version
```

### 步骤 5: 配置 Android SDK（自动）

Buildozer 会在首次构建时自动下载 Android SDK 和 NDK，无需手动配置。

## 构建 APK

### 快速构建（调试版）

```bash
# 1. 进入项目目录
cd /path/to/parking-nav-app

# 2. 赋予脚本执行权限
chmod +x build.sh

# 3. 运行构建脚本
./build.sh
```

### 首次构建说明

首次构建会：
1. 下载 Android SDK (约 500MB)
2. 下载 Android NDK (约 1GB)
3. 下载 Python-for-Android
4. 编译所有依赖库

**预计时间**：30-60 分钟（取决于网络速度和机器性能）

### 构建过程监控

```bash
# 使用详细日志
buildozer -v android debug

# 查看构建目录
ls -lh .buildozer/

# 监控磁盘使用
df -h
```

### 构建输出

成功构建后，APK 文件位于：
```
bin/parkingnav-1.0.0-arm64-v8a-debug.apk
bin/parkingnav-1.0.0-armeabi-v7a-debug.apk
```

## 问题排查

### 问题 1: Buildozer 未找到

**错误信息**：
```
buildozer: command not found
```

**解决方案**：
```bash
# 检查 PATH
echo $PATH

# 添加到 PATH
export PATH=$HOME/.local/bin:$PATH

# 或重新安装
pip3 install --user --upgrade --force-reinstall buildozer
```

### 问题 2: 磁盘空间不足

**错误信息**：
```
No space left on device
```

**解决方案**：
```bash
# 检查磁盘空间
df -h

# 清理 Buildozer 缓存
rm -rf ~/.buildozer
rm -rf .buildozer

# 清理 pip 缓存
pip3 cache purge
```

### 问题 3: SDK 下载失败

**错误信息**：
```
Failed to download Android SDK
```

**解决方案**：
```bash
# 手动指定镜像（如果在中国）
export ANDROID_SDK_HOME=$HOME/.buildozer/android/platform/android-sdk

# 或使用代理
export https_proxy=http://your-proxy:port
```

### 问题 4: NDK 版本不匹配

**错误信息**：
```
NDK version mismatch
```

**解决方案**：
编辑 `buildozer.spec`：
```ini
android.ndk = 25b
```

然后清理并重新构建：
```bash
buildozer android clean
buildozer android debug
```

### 问题 5: Cython 编译错误

**错误信息**：
```
Cython compilation failed
```

**解决方案**：
```bash
# 使用特定版本的 Cython
pip3 install --user cython==0.29.33

# 清理并重试
buildozer android clean
buildozer android debug
```

## 高级配置

### 自定义应用图标

1. 准备图标文件（512x512 PNG）
2. 保存为 `assets/icon.png`
3. 编辑 `buildozer.spec`：
```ini
icon.filename = %(source.dir)s/assets/icon.png
```

### 自定义启动画面

1. 准备启动画面（1280x720 PNG）
2. 保存为 `assets/presplash.png`
3. 编辑 `buildozer.spec`：
```ini
presplash.filename = %(source.dir)s/assets/presplash.png
```

### 添加额外的权限

编辑 `buildozer.spec`：
```ini
android.permissions = INTERNET,BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,BLUETOOTH_SCAN,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,CAMERA
```

### 修改应用版本

编辑 `buildozer.spec`：
```ini
version = 1.1.0
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py
```

### 优化 APK 大小

编辑 `buildozer.spec`：
```ini
# 仅构建 ARM64（现代设备）
android.archs = arm64-v8a

# 排除不需要的文件
source.exclude_patterns = test,tests,*.pyc,__pycache__
```

### 启用混淆

编辑 `buildozer.spec`：
```ini
android.enable_proguard = True
```

## 使用 GitHub Actions 自动构建

创建 `.github/workflows/build.yml`：

```yaml
name: Build Android APK

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y openjdk-17-jdk
        pip install buildozer cython==0.29.33
    
    - name: Build APK
      run: |
        buildozer android debug
    
    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: parking-nav-apk
        path: bin/*.apk
```

## Docker 构建（隔离环境）

创建 `Dockerfile`：

```dockerfile
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    openjdk-17-jdk \
    git \
    zip \
    unzip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install buildozer cython==0.29.33

WORKDIR /app

CMD ["buildozer", "android", "debug"]
```

使用 Docker 构建：
```bash
docker build -t parking-nav-builder .
docker run -v $(pwd):/app parking-nav-builder
```

## 测试 APK

### 在模拟器中测试

```bash
# 启动 Android 模拟器
emulator -avd Pixel_4_API_31

# 安装 APK
adb install bin/parkingnav-*.apk

# 查看日志
adb logcat | grep python
```

### 在真机上测试

```bash
# 连接设备并启用 USB 调试
adb devices

# 安装 APK
adb install bin/parkingnav-*.apk

# 启动应用
adb shell am start -n com.parking.parkingnav/.MainActivity

# 查看日志
adb logcat -s python
```

## 性能优化

### 减少构建时间

```bash
# 使用 ccache
export USE_CCACHE=1
export CCACHE_DIR=$HOME/.ccache

# 并行编译
export MAKEFLAGS="-j$(nproc)"
```

### 缓存依赖

构建完成后，`.buildozer` 目录包含所有下载的依赖。保留此目录可以加速后续构建。

## 发布到 Google Play

1. 构建发布版 APK
2. 使用密钥签名
3. 创建 Google Play 开发者账号
4. 上传 APK
5. 填写应用信息和截图
6. 提交审核

详细步骤请参考 [Google Play Console 文档](https://support.google.com/googleplay/android-developer)。

---

**提示**：遇到问题时，使用 `-v` 参数查看详细日志，大多数问题都能从日志中找到线索。
