from flask import Flask, render_template
from OpenSSL import SSL
context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
context.use_privatekey_file('ssl/certificate.key')
context.use_certificate_file('ssl/certificate_ca.crt')

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000, ssl_context=context)