from flask import Flask
import database

import routes



app = Flask(__name__)

app.register_blueprint(routes.monitor_routes)

if __name__ == '__main__':
    app.run(host="0.0.0.0")