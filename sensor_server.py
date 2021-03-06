"""
Simple socket server for testing
default port 1313, use -p to change
"""

import SocketServer
import json
import sys, getopt
import csv


def get_args(argv):
    """ get sys args """
    port = 1313
    opts, args = getopt.getopt(argv[1:], "p:", ["port="])
    for opt, arg in opts:
        if opt in ('-p', '--port'):
            port = arg
    return port


class MyTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True


class MyTCPServerHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:
            data = json.loads(self.request.recv(1024).strip())
            print data
            # save data to file
            for key, val in data['temp data'].iteritems():
                fname = data['unit_id'] + key +'.csv'
                with open(fname, 'ab') as outfile:
                    writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow([data['datetime'], val])
            # send some 'ok' back
            self.request.sendall(json.dumps({'return':'ok'}))
        except Exception, e:
            print "Exception while receiving message: ", e


def main(argv):
    """ set up the server """
    port = get_args(argv)
    ip_addr = '0.0.0.0'
    server = MyTCPServer((ip_addr, 1313), MyTCPServerHandler)
    print "Server established. listening on address: ", ip_addr, " port: ", port 
    server.serve_forever()

if __name__ == '__main__':
    main(sys.argv)
