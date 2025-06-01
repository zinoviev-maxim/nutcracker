from flask import Flask, render_template
import ssl

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile='ssl/certificate_ca.crt', keyfile='ssl/certificate.key')
    app.run(host="0.0.0.0", debug=True, port=5000, ssl_context=context)