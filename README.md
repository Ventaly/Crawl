# Playwright 自动化任务解决方案

## 项目简介

本项目使用 [Playwright](https://playwright.dev/) 结合 Python，旨在自动化处理特定网站的登录、导航、数据筛选以及滑块验证码的处理等任务。项目主要面向需要批量处理用户简历、沟通候选人等场景。

---

## 功能描述

1. **自动登录**：通过用户名和密码自动登录指定网站，并支持滑块验证码处理。
2. **页面导航**：
   - 自动跳转到推荐、沟通、申请等页面。
   - 自动执行筛选和筛选条件的选择。
3. **自动化操作**：
   - 批量点击按钮（如 "立即沟通"）。
   - 下载简历文件并保存至本地。
   - 处理候选人的简历申请和沟通请求。
4. **滑块验证码处理**：通过 `Slider_Captcha` 模块集成验证码破解逻辑。
5. **日志与错误处理**：实时打印任务状态，并记录错误信息。

---

## 依赖

在运行此项目之前，请确保已安装以下依赖项：

- **Python 3.7+**
- **Playwright**：用于浏览器自动化。
- **BeautifulSoup**：用于 HTML 内容解析。
- **Requests**：用于 HTTP 请求处理。
- **OpenCV 和 NumPy**：用于滑块验证码的图像处理。
- **Pillow**：用于图像处理和转换。

### 安装依赖

运行以下命令以安装所有必要的依赖项：

```bash
pip install playwright requests beautifulsoup4 opencv-python-headless numpy pillow
```
# 项目文件说明

## main.py
项目的主入口，包含自动化任务的核心逻辑。

## Slider_Captcha.py
滑块验证码处理模块。

## GetImage.py
用于处理图片的工具模块。

## README.md
项目说明文档（即本文件）。

# 使用方法

## 克隆项目

```bash
git clone https://github.com/your-repository-url 
cd your-repository-folder
```
配置登录信息：
在 main.py 中修改以下代码，替换为实际的用户名和密码：

```bash
await page.fill('input#username', 'YourUsername')
await page.fill('input#password', 'YourPassword')
````
运行脚本：
执行以下命令启动任务：

```bash
python main.py
```
#### 查看结果：
脚本执行过程中会输出日志信息，显示任务进度。下载的简历会存储在本地指定的 E:\Email-Attachments 文件夹。

## 注意事项
### 网站适配性：
脚本目前仅适用于特定网站，请确保目标页面的结构未发生重大变化。如果页面布局或 HTML 元素发生变化，需要调整选择器。

### 滑块验证码：
如果滑块验证码频繁失败，可尝试调整 Slider_Captcha.py 模块中的图像处理逻辑。

### 文件路径：
确保本地文件夹 E:\Email-Attachments 存在且具有写入权限。

### 反爬机制：
若运行过程中频繁遇到验证码或其他反爬机制，可适当降低操作速度（增加 asyncio.sleep 时间）。

## 贡献
欢迎提交 Issue 或 Pull Request 来改进本项目。

## 许可证
本项目基于 MIT License 开源。
