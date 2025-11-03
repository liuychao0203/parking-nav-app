# 车位导航 Android APP

一个基于 Kivy 框架的车位导航 Android 应用，通过蓝牙连接控制车位导航系统。

## 功能特性

- 🚗 车位号输入和解析（支持 A11-D33 格式）
- 📡 蓝牙设备扫描和连接
- 📤 导航指令发送
- 📱 Android 原生蓝牙支持
- 🎨 简洁直观的用户界面

## 系统要求

### 开发环境
- Ubuntu 20.04+ 或其他 Linux 发行版
- Python 3.8+
- Java JDK 17+
- Android SDK & NDK
- 至少 20GB 可用磁盘空间

### 运行环境
- Android 5.0 (API 21) 或更高版本
- 蓝牙功能
- 位置权限（蓝牙扫描需要）

## 安装依赖

### 1. 安装系统依赖

```bash
sudo apt-get update
sudo apt-get install -y git zip unzip openjdk-17-jdk python3-pip \
    autoconf libtool pkg-config zlib1g-dev libncurses5-dev \
    libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
```

### 2. 安装 Python 依赖

```bash
pip3 install --user --upgrade buildozer cython==0.29.33
```

### 3. 验证安装

```bash
buildozer --version
python3 --version
java -version
```

## 构建 APK

### 调试版本（快速测试）

```bash
chmod +x build.sh
./build.sh
```

调试版 APK 将生成在 `bin/` 目录下，文件名类似：`parkingnav-1.0.0-arm64-v8a-debug.apk`

### 发布版本（正式发布）

```bash
chmod +x build_release.sh
./build_release.sh
```

首次运行会提示创建密钥库，请记住设置的密码。

## 手动构建步骤

如果自动脚本失败，可以手动执行：

```bash
# 初始化项目（仅第一次）
buildozer init

# 清理旧构建
buildozer android clean

# 构建调试版
buildozer -v android debug

# 或构建发布版
buildozer -v android release
```

## 安装到 Android 设备

### 方法一：USB 连接

```bash
# 启用 USB 调试后连接设备
adb install bin/parkingnav-*.apk
```

### 方法二：手动安装

1. 将 APK 文件传输到 Android 设备
2. 在设备上打开"设置" → "安全"
3. 启用"允许安装未知来源应用"
4. 使用文件管理器找到 APK 文件并点击安装

## 使用说明

### 1. 启动应用

在 Android 设备上打开"车位导航"应用。

### 2. 扫描蓝牙设备

- 点击"扫描设备"按钮
- 应用会列出已配对的蓝牙设备
- 首次使用需要先在系统设置中配对蓝牙设备

### 3. 连接设备

- 从列表中选择目标设备（点击设备名称）
- 点击"连接设备"按钮
- 等待状态栏显示"连接成功"

### 4. 发送导航指令

- 在输入框中输入车位号（如：A11、B23、C12）
- 点击"发送导航"按钮
- 应用会将坐标发送到蓝牙设备

### 车位号格式

- 格式：字母 + 两位数字
- 字母范围：A-D
- 数字范围：00-39
- 示例：A11、B23、C12、D03

## 权限说明

应用需要以下权限：

- **蓝牙**：用于连接蓝牙设备
- **位置**：Android 要求蓝牙扫描必须有位置权限
- **互联网**：用于未来的在线功能（可选）

## 项目结构

```
.
├── main.py                 # 主应用代码
├── buildozer.spec          # Buildozer 配置文件
├── requirements.txt        # Python 依赖
├── build.sh               # 调试版构建脚本
├── build_release.sh       # 发布版构建脚本
├── README.md              # 本文档
├── SETUP_GUIDE.md         # 详细安装指南
└── assets/                # 资源文件
    └── icon.png           # 应用图标
```

## 常见问题

### 构建失败

**问题**：`buildozer android debug` 失败

**解决方案**：
1. 确保所有依赖都已安装
2. 检查磁盘空间（至少需要 20GB）
3. 删除 `.buildozer` 目录后重试
4. 使用 `-v` 参数查看详细日志

### 蓝牙连接失败

**问题**：无法连接蓝牙设备

**解决方案**：
1. 确保设备已在系统设置中配对
2. 检查设备是否支持 SPP 协议
3. 重启应用和蓝牙
4. 查看应用日志了解错误信息

### 权限被拒绝

**问题**：应用无法访问蓝牙或位置

**解决方案**：
1. 打开系统设置 → 应用 → 车位导航
2. 手动授予所有权限
3. 重启应用

## 技术栈

- **框架**：Kivy 2.3.0
- **构建工具**：Buildozer
- **蓝牙接口**：PyJNIus (Android Java 桥接)
- **目标平台**：Android 5.0+

## 开发说明

### 修改应用代码

编辑 `main.py` 文件后，重新运行构建脚本即可。

### 修改应用配置

编辑 `buildozer.spec` 文件可以修改：
- 应用名称和版本
- 权限配置
- 图标和启动画面
- API 级别等

### 调试应用

```bash
# 查看应用日志
adb logcat | grep python

# 或使用 buildozer
buildozer android logcat
```

## 更新日志

### v1.0.0 (2025-11-03)
- ✨ 初始版本发布
- 🚀 基本蓝牙功能
- 📱 车位导航指令发送

## 许可证

本项目仅供学习和个人使用。

## 联系方式

如有问题或建议，请通过以下方式联系：
- 提交 Issue
- 发送邮件

---

**注意**：首次构建可能需要下载大量依赖（约 2-3GB），请确保网络连接稳定。
