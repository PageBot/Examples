#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# -----------------------------------------------------------------------------
#
#     P A G E B O T  E X A M P L E S
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     httpshandler.py
#
#     HttpsHandler, imported by HttpsServer

import json
import tornado.web


class HttpsHandler(tornado.web.RequestHandler):

    def get(self, slug):
        print('get %s' % slug)
        html = self.get_html()
        self.write(html)

    def post(self, slug):
        print('post %s' % slug)
        data = json.loads(self.request.body.decode('utf-8'))
        print('Got JSON data:', data)
        self.write({ 'got' : 'your data' })

    def get_html(self):
        html = ''
        html += '<html><head><title>PageBot Server</title>'
        html += '<link rel="shortcut icon" href="http://localhost:8882/favicon.ico"/>'
        html += '</head><body>'
        html += '<h1>Hello world</h1>'
        html += '</body></html>'
        return html

    def data_received(self):
        pass
