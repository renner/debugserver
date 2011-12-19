#!/usr/bin/python

import SimpleHTTPServer
import SocketServer
import cgi

# Listen port
PORT = 9999

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        print("--------------------")
        print(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        print("--------------------")
        print(self.headers)
        form = cgi.FieldStorage(fp=self.rfile, headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                    })
        print str(form)
        if form.list:
          for item in form.list:
            logging.error(item)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

## Start the server
handler = ServerHandler
httpd = SocketServer.TCPServer(("", PORT), handler)
print("Listening on port: " + str(PORT))
httpd.serve_forever()

