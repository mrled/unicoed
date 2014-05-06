#!/usr/bin/env python3

import json

# Manual installation requried for these
import cherrypy 

from unicoed import translate
    
class UCRoot:
    exposed = True

    def GET(self):
        return "Inside UCRoot.index()"

    def POST(self, inputtext, translatorname):
        return translate(inputtext, translatorname)

cherrypy.config.update({
    'server.socket_port' : 7979,
    #'server.socket_host' : '0.0.0.0',
})
cherrypy.tree.mount(
    UCRoot(), '/', 
    {'/':
        {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    }
)
cherrypy.server.start()
#cherrypy.server.block()

