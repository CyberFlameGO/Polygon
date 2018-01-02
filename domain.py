from urllib.parse import urlparse

def g_d_n(u):
    try:
        result = g_s_d_n(u).split('.')
        return result[-2] + '.' + result[-1]
    except:
        return ''

def g_s_d_n(u):
    try:
        return urlparse(u).netloc
    except:
        return ''