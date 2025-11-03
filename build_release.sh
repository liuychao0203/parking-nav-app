#!/bin/bash
# Android APK 发布版本打包脚本

set -e

echo "======================================"
echo "  车位导航 APP - 发布版 APK 打包  "
echo "======================================"
echo ""

if ! command -v buildozer &> /dev/null; then
    echo "错误: 未安装 Buildozer"
    exit 1
fi

if [ ! -f "parking-release-key.keystore" ]; then
    echo "生成密钥库..."
    keytool -genkey -v -keystore parking-release-key.keystore -alias parking -keyalg RSA -keysize 2048 -validity 10000
    echo ""
fi

echo "1. 清理旧的构建文件..."
buildozer android clean || true

echo ""
echo "2. 开始构建发布版 APK..."
buildozer -v android release

echo ""
echo "3. 签名 APK..."
APK_UNSIGNED=$(ls -t bin/*-release-unsigned.apk | head -1)
APK_SIGNED="${APK_UNSIGNED%-unsigned.apk}-signed.apk"

jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore parking-release-key.keystore "$APK_UNSIGNED" parking

zipalign -v 4 "$APK_UNSIGNED" "$APK_SIGNED"

echo ""
echo "4. 构建完成！"
echo "发布版 APK: $APK_SIGNED"
echo "文件大小: $(du -h "$APK_SIGNED" | cut -f1)"
echo ""
echo "======================================"
