from flask import Flask, jsonify, request
from scraper.yp_usa_scraper import scrape_all_pages_yp_usa
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/scrape/yp-usa', methods=["GET"])
def get():
    return "GET"
@app.route('/scrape/yp-usa', methods=["POST"])
def scrape_yp_usa():

    base_url = request.get_json()["base_url"]
    all_data = scrape_all_pages_yp_usa(base_url)
    return jsonify(all_data), 200 
    

if __name__ == '__main__':
    app.run(debug=True)
