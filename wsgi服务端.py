from wsgiref.simple_server import make_server

# def app(environ,start_response):
#     status = '200,ok'
#     headers = [('Content-Type','text/html;charset=utf-8')]
#     start_response(status,headers)
#     html = '<h1>hello,world</h1>'.encode('utf-8')
#     return [html]
#
# ip = '192.168.1.107'
# port = 9999
# server = make_server(ip,port, app)
# server.serve_forever()
#


# from wsgiref.simple_server import make_server
# #
# #
# # def application(environ,start_response):
# #     status = '200 ok'
# #     headers = [('Content-Type', 'text.html;charset=utf-8')]
# #     start_response(status,headers)
# #     html = '<h1>hello,world</h1>'.encode('utf-8')
# #     return [html]
# #
# #
# # ip = '127.0.0.1'
# # port = 9999
# # server = make_server(ip,port,application)
# # server.serve_forever()


# from webob import Response,Request
# from webob.dec import wsgify
# from wsgiref.simple_server import make_server
#
#
# class App:
#     # wsgify装饰器装饰的函数应该具有一个参数，这个参数是webob.Request类型，是对字典environ的对象化后的实例
#     @wsgify
#     def __call__(self, request:Request):
#         return '<h1>hello,world!!!!!</h1>'
#
#
# if __name__ == '__main__':
#     ip = '127.0.0.1'
#     port = 9999
#     server = make_server(ip,port,App())
#     try:
#         server.serve_forever()
#     except KeyboardInterrupt:
#         server.shutdown()
#         server.server_close()


from webob import Request,Response
from webob.dec import wsgify
from wsgiref.simple_server import make_server
from webob.exc import HTTPNotFound
import re


class Router:
    ROUTETABLE = []

    @classmethod
    def route(cls,pattern,*methods):
        def wrapper(handler):
            cls.ROUTETABLE.append(
                (tuple(map(lambda x:x.upper(),methods)),
                 re.compile(pattern),handler))
            return handler
        return wrapper

    @classmethod
    def get(cls,pattern):
        return cls.route(pattern,'get')

    @classmethod
    def post(cls,pattern):
        return cls.route(pattern,'post')

    @classmethod
    def head(cls,pattern):
        return cls.route(pattern,'head')


@Router.get(r'^/$')
@Router.route(r'^/(p<id>\d+)$')
def indexhandler(request):
    return '<h1>hello</h1>'


@Router.get('^/python$')
def pythonhandler(request):
    res = Response()
    res.charset='utf-8'
    res.body = '<h1>hello,python</h1>'.encode()
    return res


class App:
    _Router = Router
    @wsgify
    def __call__(self,request:Request):
        for methods,pattern,handler in self._Router.ROUTETABLE:
            if not methods or request.method.upper() in methods:
                matcher = pattern.match(request.path)
                if matcher:
                    request.groups = matcher.groups()
                    request.groupdict = matcher.groupdict()
                    return handler
        raise HTTPNotFound('<h1>notfound</h1>')


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 9999
    server = make_server(ip,port,App())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shotdown()
        server.server_close()












