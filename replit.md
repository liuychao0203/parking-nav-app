# 车位导航 Android APP 打包项目

## 项目概述

这是一个基于 Kivy 框架的车位导航 Android 应用打包项目。应用通过蓝牙连接控制车位导航系统，支持车位号输入和设备管理。

## 项目状态

- **创建日期**: 2025-11-03
- **当前版本**: 1.0.0
- **打包状态**: 配置完成，等待在 Linux 环境中构建

## 技术栈

- **框架**: Kivy 2.3.0
- **构建工具**: Buildozer
- **蓝牙接口**: PyJNIus (Android Java 桥接)
- **目标平台**: Android 5.0+ (API 21+)
- **支持架构**: ARM64-v8a, ARMv7

## 项目结构

```
.
├── main.py                 # 主应用代码
├── buildozer.spec          # Buildozer 配置文件
├── requirements.txt        # Python 依赖
├── build.sh               # 调试版构建脚本
├── build_release.sh       # 发布版构建脚本
├── verify.py              # 代码验证脚本
├── README.md              # 使用说明
├── SETUP_GUIDE.md         # 详细安装指南
└── assets/                # 资源文件
    └── icon.png           # 应用图标
```

## 核心功能

1. **车位号解析**: 支持 A11-D33 格式的车位号输入
2. **蓝牙设备扫描**: 自动扫描已配对的蓝牙设备
3. **设备连接管理**: 一键连接和断开蓝牙设备
4. **导航指令发送**: 将车位坐标通过蓝牙发送到导航系统
5. **实时状态反馈**: 显示连接状态和操作结果

## 开发说明

### 在 Replit 环境中

由于 Android APK 构建需要完整的 Android SDK/NDK 环境，**无法在 Replit 中直接构建 APK**。

Replit 环境仅用于：
- ✅ 代码编辑和语法验证
- ✅ 项目配置管理
- ✅ 文档编写

### LSP 警告说明

您可能会看到以下导入错误，这些是**正常的**：
- `Import "kivy.*" could not be resolved`
- `Import "jnius" could not be resolved`
- `Import "android.permissions" could not be resolved`

这些库仅在 Android 构建环境中可用，不影响项目的正确性。验证脚本已确认代码语法正确。

### 构建 APK

要构建实际的 APK 文件，请：

1. **在 Ubuntu/Linux 环境中**：
   ```bash
   ./build.sh
   ```

2. **使用 Docker**：
   ```bash
   docker run -v $(pwd):/app ubuntu:22.04 bash -c "apt-get update && apt-get install -y python3-pip openjdk-17-jdk && pip3 install buildozer cython==0.29.33 && cd /app && buildozer android debug"
   ```

3. **使用 GitHub Actions**：
   - 将项目推送到 GitHub
   - 配置 GitHub Actions 自动构建（参见 SETUP_GUIDE.md）

## 权限配置

应用已配置以下 Android 权限：
- `BLUETOOTH` - 蓝牙基础功能
- `BLUETOOTH_ADMIN` - 蓝牙管理
- `BLUETOOTH_CONNECT` - 蓝牙连接（Android 12+）
- `BLUETOOTH_SCAN` - 蓝牙扫描（Android 12+）
- `ACCESS_FINE_LOCATION` - 精确位置（蓝牙扫描需要）
- `ACCESS_COARSE_LOCATION` - 粗略位置

## 用户偏好

- **语言**: 中文
- **目标**: 打包成可安装的 Android APK
- **部署方式**: 本地安装（不发布到应用商店）

## 下一步操作

1. 下载项目文件到本地 Linux 环境
2. 按照 SETUP_GUIDE.md 安装依赖
3. 运行 `./build.sh` 构建 APK
4. 将生成的 APK 安装到 Android 设备

## 维护日志

### 2025-11-03
- ✅ 创建项目结构
- ✅ 配置 Buildozer 打包配置
- ✅ 添加蓝牙权限和 Android 12+ 兼容性
- ✅ 创建自动化构建脚本
- ✅ 编写完整的使用文档
- ✅ 添加代码验证工作流

## 常见问题

**Q: 为什么在 Replit 中看到导入错误？**
A: Kivy 和 Android 库仅在构建环境中可用，这些错误不影响最终的 APK 构建。

**Q: 如何在手机上测试？**
A: 在 Linux 环境中构建 APK 后，通过 USB 或文件传输安装到 Android 设备。

**Q: 构建需要多长时间？**
A: 首次构建约 30-60 分钟（下载 SDK/NDK），后续构建约 5-10 分钟。

**Q: 可以在 Windows 上构建吗？**
A: 建议使用 Linux，或在 Windows 上使用 WSL2 或 Docker。
