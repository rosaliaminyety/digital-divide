from flask import Flask, redirect, url_for, render_template, request
from digitaldivide import read_markets, Market
app = Flask (__name__)
app.config['SERVER_NAME'] = "localhost:5000"


@app.route("/", methods=["GET", "POST"])
def digital_divide():
    if "zip_entry" in request.args:
        zip_code=request.args["zip_entry"]
        markets = read_markets("digitaldivide.txt")
        markets_for_zipcode = markets[zip_code]
    else:
        zip_code=None
        markets_for_zipcode = []
    return render_template("index.html", zip=zip_code, markets=markets_for_zipcode)
        
    """
    if request.method == "POST":
        req = request.form
        zipcode=req["zipcode"]
        print(zipcode)
        return redirect(request.url)
        
    return render_template("index.html")
    """
    
if __name__ == "__main__":
    app.run()
    
    #putting  app.run(host="0.0.0.0") apparently lets you access the link from 
    #any other computer in netfwork? https://www.codegrepper.com/code-examples/python/how+to+access+flask+app+from+another+computer
    