def check(url):
    if 'zhuanlan.zhihu.com/p' in url:
        return '知乎专栏'
    elif 'mp.weixin.qq.com/s' in url:
        return '微信文章'
    elif 'www.freebuf.com/articles' in url:
        return 'freebuf'