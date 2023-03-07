from flask import Flask, render_template
from routes import home, about, projects, brainmap

app = Flask(__name__)

app.register_blueprint(home.bp)
app.register_blueprint(about.bp)
app.register_blueprint(projects.bp)
app.register_blueprint(brainmap.bp)

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
