from freebuf import freebuf
from weixin import weixin
from checkUrl import check
from zhihu import zhihu
from gpt import gpt2

from termcolor import colored
banner = colored('''[+]目前支持解析的链接如下:
[+]知乎专栏
[+]微信文章
[+]freebuf
''', 'green')
print(banner)
title = ''
con = ''
while True:
    url = input('[+]请输入文章链接: ')
    typ = check(url)
    if typ == '知乎专栏':
        title, con = zhihu(url)
    elif typ == '微信文章':
        title, con = weixin(url)
    elif typ == 'freebuf':
        title, con = freebuf(url)
    if len(f'Summarize an article titled "{title}" in detail, and list the important knowledge points, as follows:{con}') > 4096:
        print(colored('[+]内容超出负载!','red'))
    gpt_c = gpt2(f'Summarize an article titled "{title}" in detail, and list the important knowledge points, as follows:{con}').replace('\n\n','\n')
    print(colored(gpt_c, 'yellow'))
