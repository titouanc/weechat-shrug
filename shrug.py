# Copyright 2016 Colleen Murphy
# Apache 2.0
# Source: https://github.com/cmurphy/weechat-shrug
#
import weechat

SHRUG = u"\u00af\_(\u30c4)_/\u00af"

weechat.register("shrug", "krinkle", "0.0.1", "Apache-2.0", "Shrug", "", "")

def shrug(data, buffer, args):
    text = (' '.join([args, SHRUG])) if args else SHRUG
    weechat.command(buffer, text.encode('utf-8'))
    return weechat.WEECHAT_RC_OK

hook = weechat.hook_command("shrug", "Shrug", "", "", "", "shrug", weechat.current_buffer())
