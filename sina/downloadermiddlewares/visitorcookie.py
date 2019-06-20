import requests
import re


class VisitorCookie(object):
    def process_request(self, request, spider):
        cookie = self.gen_cookie()
        request.cookies = cookie

    def gen_cookie(self):
        # 获取tid以及new_tid
        gen_visitor_url = 'https://passport.weibo.com/visitor/genvisitor?cb=gen_callback&' + \
                         'fp={"os":"1","browser":"Chrome70,0,3538,25",' + \
                         '"fonts":"undefined","screenInfo":"1920*1080*24",' + \
                         '"plugins":"Portable Document Format::internal-pdf-viewer' + \
                         '::Chromium PDF Plugin|::mhjfbmdgcfjbbpaeojofohoefgiehjai::' + \
                         'Chromium PDF Viewer|::gbkeegbaiigmenfmjfclcdgdpimamgkj::' + \
                         'Google文档、表格及幻灯片的Office编辑扩展程序|::internal-nacl-plugin::Native Client"}'
        res = requests.post(gen_visitor_url)
        text = res.text
        text = text.replace('"new_tid":true', '"new_tid":True')
        text = text.replace('"new_tid":false', '"new_tid":False')
        need = self.parse_reponse_text(text)
        params = {
            'a': 'incarnate',
            't': need['data']['tid'],
            'w': 3 if (need['data']['new_tid']) else 2,
            'c': need['data']['confidence'] if ('confidence' in need['data'].keys()) else 100,
            'cb': 'cross_domain',
            'from': 'weibo'
        }
        res = requests.get('https://passport.weibo.com/visitor/visitor', params)
        text = res.text
        text = text.replace('"sub":null', '"sub":\'\'')
        need = self.parse_reponse_text(text)
        if need['data']['sub'] == '':
            need['data']['sub'] = None
        return {'SUB': need['data']['sub'], 'SUBP': need['data']['subp']}

    def parse_reponse_text(self, text):
            data = re.findall(r"{.*?}}", text)
            return eval(data[0])
