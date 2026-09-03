import json
from wsgiref.simple_server import make_server

tasks = []
ID = 0

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
            
    elif verb == "POST":
        content_length = int(environ.get("CONTENT_LENGTH", 0))
        body = environ ["wsgi.input"].read(content_length)

        data = json.loads(body)
        global ID
        ID+= 1
        nuevatask = {
            "id": ID,
            "title": data.get("title", "Sin título"),
            "done": data.get("done", False)
        }
        tasks.append(nuevatask)
        status = "201 Created"
        response_body = json.dumps(nuevatask).encode("utf-8")
        headers = [("Content-Type", "application/json"),("Content-length", str(len(response_body)))]
        start_response(status, headers)
        return [response_body]
        
    elif verb == "DELETE":
        if len(path) == 3:
            index = path[2]
            index = int(index)
            encuentra = 0
            for i in range (len(tasks)):
                if(tasks[i]["id"] == index):
                    del(tasks[i])
                    encuentra = 1
                    break
            if encuentra == 1:
                status = "200 OK"
                start_response(status, headers)
                return [b""]
            else:
                status = "404 Not Found"
                start_response(status, headers)
                return [b"Not Found"]

    elif verb == "PATCH":
        if len(path) == 3:
            index = path[2]
            index = int(index)
            item_encon = None
            encuentra = 0
            for item in tasks:
                if item["id"] == index:
                    item_encon = item
                    encuentra = 1
                    break

            if encuentra == 1:
                content_length = int(environ.get("CONTENT_LENGTH", 0))
                body = environ ["wsgi.input"].read(content_length)

                data = json.loads(body)

                if "title" in data:
                    item_encon["title"] = data["title"]
                if "done" in data:
                    item_encon["done"] = data["done"]

                status = "200 OK"
                start_response(status, headers)
                return [json.dumps(item_encon).encode("utf-8")]
            else:
                status = "404 Not Found"
                start_response(status, headers)
                return [b"Not Found"]

    if len(path) >= 2 and path[1] == "tasks":
        status = "405 Method Not Allowed"
        start_response(status, headers)
        return[b""]
        
with make_server('', 9292, app) as httpd:
    print("Serving on port 9292...")
    httpd.serve_forever()
