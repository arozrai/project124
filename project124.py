from flask import Flask, jsonify, request

App = Flask(__name__)
Task = [
    {
        "id":1,
        "name":"john",
        "contact":"35283618",
        "done":False
    },
    {
        "id":2,
        "name":"alex",
        "contact":"74823744",
        "done":False
    }
]
@App.route("/AddData",methods = ["POST"])

# def Hello_World():
#     return "Hello World"

def AddTask():
    if not request.json:
        return jsonify(
            {
                "status":"error",
                "message":"please provide data"
            },
            400
        )
    task = {
        "id":Task[-1]["id"]+1,
        "name":request.json["title"],
        "contact":request.json.get("description"),
        "done":False
    }
    Task.append(task)
    return jsonify(
        {
            "status":"success",
            "message":"task added successfully"
        }
    )

@App.route("/get-data")

def GetTask():
    return jsonify(
        {
            "data":Task
        }
    )
    
if (__name__=="__main__"):
    App.run(debug=True)