from twisted.internet import reactor
from twisted.web import server, resource
from twisted.python import log
import sys

class Hello(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return "Hello LVWEB-128!"

log.startLogging(sys.stdout)

site = server.Site(Hello())
reactor.listenTCP(8888, site)
reactor.run()
