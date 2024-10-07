from flask import Flask, render_template
from flask_cors import CORS
from blueprints.ReadCSV import csv_blueprint
import config
from extensions import db
from flask_migrate import Migrate

# 初始化Flask应用
app = Flask(__name__)
CORS(app)

# register blueprints
app.register_blueprint(csv_blueprint)

# bind config
app.config.from_object(config)

# bind SQLAlchemy with app
db.init_app(app)

migrate = Migrate(app, db)

@app.route('/')
def upload_file():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)