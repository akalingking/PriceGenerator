'''
https://opensource.org/licenses/MIT

License: The MIT License (MIT)

Copyright (c) 2016 Ariel Kalingking akalingking@gmail.com

Permission is hereby granted, free of charge, to any person 
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, 
merge, publish, distribute, sublicense, and/or sell copies of 
the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
'''
from ws4py.websocket import WebSocket
from wsgiref.simple_server import make_server
from ws4py.server.wsgirefserver import WSGIServer, WebSocketWSGIRequestHandler
from ws4py.server.wsgiutils import WebSocketWSGIApplication
import threading

subscribers = []

class Connection(WebSocket):
    global subscribers
    
    def received_message(self, message):
        print ("ConnectionWebSocket::receive_message '%s'" % message)
        #test so that we see from the server
        self.send(message.data, message.is_binary)
        
    def opened(self):
        WebSocket.opened(self)
        print("Connection.opened '%s'" % self._local_address[0])
        subscribers.append(self)
        
    def closed(self, code, reason):
        print("Connection.closed '%s'" % self._local_address[0])
        WebSocket.closed(self, code, reason)
        subscribers.remove(self)
        
    def send(self, payload, binary=False):
        WebSocket.send(self, payload, binary)
        
        
class Handler(WebSocketWSGIRequestHandler):
    def __init__(self,request, client_address, server):
        WebSocketWSGIRequestHandler.__init__(self,request,client_address,server)
        
        
class Server(WSGIServer):
    def __init__(self,server_address,RequestHandlerClass,bind_and_activate=True):
        WSGIServer.__init__(self,server_address,RequestHandlerClass,bind_and_activate)
    
        
class WsServer(object):
    def __init__(self, server, port):
        self.server_ = make_server(
            server, 
            port, 
            server_class=Server,
            handler_class=Handler,
            app=WebSocketWSGIApplication(handler_cls=Connection))
     
    def run_thread_(self):
        print ("WsServer.run_thread_ start")
        
        try:
            self.server_.serve_forever()
        except Exception as e:
            print ("WsServer.run_thread_ exception='%s") % e
        
        print ("WsServer.run_thread_ stop")            
        
    def start(self):
        self.server_.initialize_websockets_manager()
        self.thread_ = threading.Thread(target=self.run_thread_)
        self.thread_.start()
        
    def stop(self):
        self.server_.shutdown()
        
    def wait(self):
        self.thread_.join()
        
    def send(self, payload, binary=False):
        global subscribers
        for subscriber in subscribers:
            subscriber.send(payload, binary)
