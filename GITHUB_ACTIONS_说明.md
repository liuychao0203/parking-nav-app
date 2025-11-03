# GitHub Actions 自动构建 APK 说明

## 🚀 快速开始

### 步骤 1：创建 GitHub 仓库

1. 登录 [GitHub](https://github.com)
2. 点击右上角的 "+" → "New repository"
3. 填写仓库名称（例如：parking-nav-app）
4. 选择 Public（公开）或 Private（私有）
5. 点击 "Create repository"

### 步骤 2：上传代码到 GitHub

在当前项目目录打开 PowerShell 或 CMD，运行以下命令：

```bash
# 初始化 Git 仓库（如果还没有）
git init

# 添加所有文件
git add .

# 提交代码
git commit -m "Initial commit - 车位导航 APP"

# 关联远程仓库（替换为你的 GitHub 仓库地址）
git remote add origin https://github.com/你的用户名/parking-nav-app.git

# 推送代码
git push -u origin main
```

**注意**：将 `你的用户名` 和 `parking-nav-app` 替换为实际的值。

如果遇到分支名称问题，可能需要运行：
```bash
git branch -M main
```

### 步骤 3：触发自动构建

代码推送到 GitHub 后，构建会自动开始！你可以：

1. 访问你的 GitHub 仓库
2. 点击顶部的 "Actions" 标签
3. 查看构建进度

**首次构建大约需要 30-60 分钟**（因为需要下载 Android SDK 和 NDK）。后续构建会快很多（约 5-15 分钟）。

### 步骤 4：下载构建好的 APK

#### 方法 A：从 Actions Artifacts 下载

1. 在 "Actions" 页面，点击最新的成功构建
2. 向下滚动到 "Artifacts" 部分
3. 点击 "parkingnav-apk" 下载 ZIP 文件
4. 解压后得到 APK 文件

#### 方法 B：从 Releases 下载（推荐）

1. 访问你的仓库主页
2. 点击右侧的 "Releases"
3. 找到最新的版本
4. 在 "Assets" 下方直接下载 APK 文件

## 🔧 手动触发构建

如果你想在不推送代码的情况下重新构建：

1. 访问 GitHub 仓库的 "Actions" 页面
2. 点击左侧的 "构建 Android APK"
3. 点击右侧的 "Run workflow" 按钮
4. 选择分支（通常是 main）
5. 点击 "Run workflow"

## 📱 安装 APK 到手机

### USB 安装（推荐）

```bash
# 连接手机并启用 USB 调试
adb install 下载的APK文件名.apk
```

### 手动安装

1. 将 APK 文件传输到手机（通过 USB、微信、邮件等）
2. 在手机上打开"设置" → "安全"
3. 启用"允许安装未知来源应用"
4. 使用文件管理器找到 APK 文件
5. 点击安装

## ⚡ 加速后续构建

GitHub Actions 已经配置了缓存，所以：
- **首次构建**：30-60 分钟
- **后续构建**：5-15 分钟（使用缓存）

## 🔍 故障排查

### 构建失败

1. 进入 "Actions" 页面
2. 点击失败的构建
3. 查看详细日志找出错误原因

常见问题：
- **磁盘空间不足**：GitHub Actions 提供足够的空间，不会出现此问题
- **依赖下载失败**：重新运行工作流（点击 "Re-run jobs"）
- **权限问题**：确保仓库设置中启用了 Actions

### 找不到 APK

确保构建成功完成（显示绿色的 ✓ 标记）。如果构建失败，APK 不会生成。

## 🎯 下一步

- 修改代码后，只需推送到 GitHub，APK 会自动重新构建
- 每次构建都会创建一个新的 Release，方便版本管理
- 可以在手机上卸载旧版本，安装新版本

## 💡 提示

- 构建完全免费（GitHub 提供免费的 Actions 额度）
- 每次推送代码都会触发自动构建
- 可以在 `.github/workflows/build-apk.yml` 中自定义构建流程
- Release 中的 APK 文件会保存 30 天（可在配置中修改）

---

**需要帮助？** 查看构建日志或联系开发者。

