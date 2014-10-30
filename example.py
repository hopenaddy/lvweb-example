from twisted.internet import reactor
from twisted.web import server, resource
from twisted.python import log
from twisted.python.logfile import DailyLogFile
import sys
import argparse

parser = argparse.ArgumentParser(description='LVWEB-128 Example daemon')
parser.add_argument('-d', action='store_true', dest='debug', help='Write logs to stdout')
parser.add_argument('-l', action='store', dest='logfile', help='Write logfile ')
parser.add_argument('-p', action='store', dest='port', help='Port number', type=int)
args = parser.parse_args()

if args.debug:
    log.startLogging(sys.stdout)

if args.logfile:
    log.startLogging(DailyLogFile.fromFullPath(args.logfile))

class Hello(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return "Hello LVWEB-128!"

port = args.port or 8888
site = server.Site(Hello())
reactor.listenTCP(port, site)
reactor.run()
