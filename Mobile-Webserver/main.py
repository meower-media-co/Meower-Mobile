from flask import Flask, make_response, render_template
app = Flask(__name__, static_url_path='')

cljs_vers = "1"
update_statuses = {
  "0.4.3": "current",
  "0.5.2": "currnet"
}

@app.route("/")
def index():
  return "Landing page coming soon!"

@app.route("/update_status/<vers>")
def update_status(vers):
  if not vers in update_statuses:
    return "obsolete"
  else:
    return update_statuses[vers]

@app.route("/cljs_vers")
def cljs_status():
  return cljs_vers

@app.route("/cljs_download")
def cljs_download():
    resp = make_response(render_template('mobile.html'))
    return resp

if __name__ == "__main__":
  app.run("0.0.0.0", 35755)
