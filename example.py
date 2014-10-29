from twisted.internet import reactor
from twisted.web import server, resource


class Hello(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return "Hello LVWEB-128!"


site = server.Site(Hello())
reactor.listenTCP(8888, site)
reactor.run()
