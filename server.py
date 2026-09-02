import json
from wsgiref.simple_server import make_server

tasks = [{"id": 1, "titulo": "prueba", "estado": False}]

def app(environ, start_response):
    verb = environ.get("REQUEST_METHOD")
    path = environ.get("PATH_INFO")
    headers = [("Content-Type", "application/json")]
    path = path.split('/')

    if verb == "GET":
        if len(path) == 3:
            index = path[2]
            index = int(index)
            item_encon = None
            for item in tasks:
                if item["id"] == index:
                    item_encon = item
                    break
                if item_encon != None:
                    status = "200 OK"
                    start_response(status, headers)
                    return [json.dumps(item_encon).encode("utf-8")]
            else:
                status = "404 Not Found"
                start_response(status, headers)
                return [b"Not Found"]
            
        elif len(path) == 2:
            status == "200 OK"
            start_response(status, headers)
            return [json.dumps(tasks).encode("utf-8")]

with make_server('', 9292, app) as httpd:
    print("Serving on port 9292...")
    httpd.serve_forever()