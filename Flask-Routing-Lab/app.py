from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)
app.config['SECRET-KEY']="ko394d"

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/proudct')
def product_page():
    return render_template("product.html")

@app.route('/cart')
def cart_page():
    return render_template("cart.html")



if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
