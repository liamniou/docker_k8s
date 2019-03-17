import os
import yaml
from flask import Flask


app = Flask(__name__)


@app.route('/')
def return_status():
    return "APP STATUS: RUNNING"


@app.route('/version')
def return_version():
    config = load_yaml("config.yaml")
    return "APP VERSION: {}".format(config['version'])


def load_yaml(file_name):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name), 'r') as file:
        return yaml.load(file)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
