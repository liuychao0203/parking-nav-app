#!/bin/bash
# Android APK 打包脚本

set -e

echo "======================================"
echo "  车位导航 APP - Android APK 打包  "
echo "======================================"
echo ""

if ! command -v buildozer &> /dev/null; then
    echo "错误: 未安装 Buildozer"
    echo "请运行以下命令安装:"
    echo "  sudo apt-get update"
    echo "  sudo apt-get install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev"
    echo "  pip3 install --user --upgrade buildozer cython==0.29.33"
    exit 1
fi

echo "1. 清理旧的构建文件..."
buildozer android clean || true

echo ""
echo "2. 开始构建 APK (调试版本)..."
buildozer -v android debug

echo ""
echo "3. 构建完成！"
echo ""

shopt -s nullglob
APK_FILES=(bin/*.apk)
if [ ${#APK_FILES[@]} -gt 0 ]; then
    APK_FILE=$(ls -t bin/*.apk 2>/dev/null | head -1)
    echo "APK 文件位置: $APK_FILE"
    echo "文件大小: $(du -h "$APK_FILE" | cut -f1)"
    echo ""
    echo "安装说明:"
    echo "1. 将 APK 文件传输到 Android 设备"
    echo "2. 在设备上启用'允许安装未知来源应用'"
    echo "3. 点击 APK 文件进行安装"
else
    echo "警告: 未找到生成的 APK 文件"
    echo "请检查构建日志中的错误信息"
fi

echo ""
echo "======================================"
