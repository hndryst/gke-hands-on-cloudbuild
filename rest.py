from flask import Flask, Response
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type=str, help="No task defined", required=True)

tasks = {}


def abort_if_not_exists(task_id):
    if task_id not in tasks:
        # abort(404, "Not Found", message="Video id is not valid...")
        abort(404, message="Task id is not valid...")


def abort_if_exists(task_id):
    if task_id in tasks:
        abort(409, message="Task already exists with that ID...")


class Task(Resource):
    def get(self, task_id):
        abort_if_not_exists(task_id)
        return tasks[task_id]

    def post(self, task_id):
        abort_if_exists(task_id)
        args = task_post_args.parse_args()
        tasks[task_id] = args
        # return args.name
        return tasks[task_id], 201

    def delete(self, task_id):
        abort_if_not_exists(task_id)
        del tasks[task_id]
        return "", 204


class Health(Resource):
    def get(self):
        # return "", 200
        return Response(status=200)


api.add_resource(Task, "/task/<int:task_id>")
api.add_resource(Health, "/healthz", "/readyz")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
