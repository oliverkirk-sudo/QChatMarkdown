# QChatAIPaint

适用于[QChatGPT]()的markdown文本转图像插件,参考了[nonebot-plugin-htmlrender](https://github.com/kexue-z/nonebot-plugin-htmlrender)的代码

## 1、前置工作

- 下载本插件`!plugin get https://github.com/oliverkirk-sudo/QChatMarkdown.git`

## 2、配置

- 修改配置文件
```python
class Config:
    def __init__(self):
        self.open: bool = True
        self.width: int = 500  # 图片宽度
        self.type: str = "png"  # 图片类型，["jpeg", "png"]
        self.quality: int = 100  # 图片质量 0-100 当为png时无效
        self.scale: float = 2  # 缩放比例,类型为float,值越大越清晰
        self.htmlrender_browser: Optional[str] = "chromium" # 默认浏览器可选chromium,firefox
        self.htmlrender_download_host: Optional[str] = None # 配置源下载地址
        self.htmlrender_proxy_host: Optional[str] = None # 代理设置
```
- 安装依赖

### UBUNTU
```sh
apt update && apt install -y locales locales-all fonts-noto libnss3-dev libxss1 libasound2 libxrandr2 libatk1.0-0 libgtk-3-0 libgbm-dev libxshmfence1
```

- 然后设置 ENV local

```sh
LANG zh_CN.UTF-8
LANGUAGE zh_CN.UTF-8
LC_ALL zh_CN.UTF-8
```

### CentOS

```sh
dnf install -y alsa-lib at-spi2-atk at-spi2-core atk cairo cups-libs dbus-libs expat flac-libs gdk-pixbuf2 glib2 glibc gtk3 libX11 libXcomposite libXdamage libXext libXfixes libXrandr libXtst libcanberra-gtk3 libdrm libgcc libstdc++ libxcb libxkbcommon libxshmfence libxslt mesa-libgbm nspr nss nss-util pango policycoreutils policycoreutils-python-utils zlib cairo-gobject centos-indexhtml dbus-glib fontconfig freetype gtk2 libXcursor libXi libXrender libXt liberation-fonts-common liberation-sans-fonts libffi mozilla-filesystem p11-kit-trust pipewire-libs harfbuzz-icu libglvnd-glx libglvnd-egl libnotify opus woff2 gstreamer1-plugins-base gstreamer1-plugins-bad-free openjpeg2 libwebp enchant libsecret hyphen libglvnd-gles
```

## 3、支持

- 使用 `GitHub-light` 样式
- 支持绝大部分 md 语法
- 代码高亮
- latex 数学公式
  - 使用 `$$...$$` 来输入独立公式
  - 使用 `$...$` 来输入行内公式

## 4、接口

- 提供了md转图片，html转图片，文本转图片，模板转图片这几个接口供其他插件使用
```python
from plugins.QChatMarkdown import *

def text_to_pic():
    """多行文本转图片
    
    Args:
        text (str): 纯文本, 可多行
        css_path (str, optional): css文件
        width (int, optional): 图片宽度，默认为 500
        type (Literal["jpeg", "png"]): 图片类型, 默认 png
        quality (int, optional): 图片质量 0-100 当为`png`时无效
        device_scale_factor: 缩放比例,类型为float,值越大越清晰(真正想让图片清晰更优先请调整此选项)
    
    Returns:
        bytes: 图片, 可直接发送
    """
def html_to_pic():
    """html转图片

    Args:
        html (str): html文本
        wait (int, optional): 等待时间. Defaults to 0.
        template_path (str, optional): 模板路径 如 "file:///path/to/template/"
        type (Literal["jpeg", "png"]): 图片类型, 默认 png
        quality (int, optional): 图片质量 0-100 当为`png`时无效
        device_scale_factor: 缩放比例,类型为float,值越大越清晰(真正想让图片清晰更优先请调整此选项)
        **kwargs: 传入 page 的参数
    
    Returns:
        bytes: 图片, 可直接发送
    """

def md_to_pic():
    """markdown 转 图片
    
    Args:
        md (str, optional): markdown 格式文本
        md_path (str, optional): markdown 文件路径
        css_path (str,  optional): css文件路径. Defaults to None.
        width (int, optional): 图片宽度，默认为 500
        type (Literal["jpeg", "png"]): 图片类型, 默认 png
        quality (int, optional): 图片质量 0-100 当为`png`时无效
        device_scale_factor: 缩放比例,类型为float,值越大越清晰(真正想让图片清晰更优先请调整此选项)
    
    Returns:
        bytes: 图片, 可直接发送
    """
def template_to_pic():
    """使用jinja2模板引擎通过html生成图片

    Args:
        template_path (str): 模板路径
        template_name (str): 模板名
        templates (dict): 模板内参数 如: {"name": "abc"}
        pages (dict): 网页参数 Defaults to
            {"base_url": f"file://{getcwd()}", "viewport": {"width": 500, "height": 10}}
        wait (int, optional): 网页载入等待时间. Defaults to 0.
        type (Literal["jpeg", "png"]): 图片类型, 默认 png
        quality (int, optional): 图片质量 0-100 当为`png`时无效
        device_scale_factor: 缩放比例,类型为float,值越大越清晰(真正想让图片清晰更优先请调整此选项)
    Returns:
        bytes: 图片 可直接发送
    """
```
