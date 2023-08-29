import base64

from mirai import Image

from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost
from plugins.QChatMarkdown.config.config import Config


def send_msg(kwargs, msg):
    host: pkg.plugin.host.PluginHost = kwargs['host']
    host.send_person_message(kwargs['launcher_id'], msg) if kwargs[
                                                                'launcher_type'] == 'person' else host.send_group_message(
        kwargs['launcher_id'], msg)


config = Config()


# 注册插件
@register(name="QChatMarkdown", description="将内容以Markdown图片形式输出", version="1.0", author="oliverkirk-sudo")
class QChatMarkdownPlugin(Plugin):

    # 插件加载时触发
    # plugin_host (pkg.plugin.host.PluginHost) 提供了与主程序交互的一些方法，详细请查看其源码
    def __init__(self, plugin_host: PluginHost):
        pass

    @on(NormalMessageResponded)
    def process_message(self, event: EventContext, **kwargs):
        if config.open:
            from plugins.QChatMarkdown import md_to_pic
            b64_img = base64.b64encode(md_to_pic(md=kwargs["response_text"], width=config.width, type=config.type, quality=config.quality if config.type == 'jpg' else None, device_scale_factor=config.scale)).decode()
            event.add_return("reply", [Image(base64=b64_img)])
            event.prevent_default()
            event.prevent_postorder()
            pass

    # 当收到个人消息时触发
    @on(PersonNormalMessageReceived)
    @on(GroupNormalMessageReceived)
    def normal_message_received(self, event: EventContext, **kwargs):
        pass

    @on(PersonCommandSent)
    @on(GroupCommandSent)
    def command_message_received(self, event: EventContext, **kwargs):
        pass

    # 插件卸载时触发
    def __del__(self):
        pass
