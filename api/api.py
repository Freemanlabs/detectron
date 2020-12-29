import crochet

crochet.setup()


import os
from flask import (
    Flask,
    request,
    json,
    redirect,
    url_for,
    abort,
    send_from_directory,
    session,
)
from flask_cors import CORS
from werkzeug.utils import secure_filename
from process_file import get_text
from get_urls import urls
from scraper import ScraperSpider
from scrapy.crawler import CrawlerRunner
from scrapy import signals
from scrapy.signalmanager import dispatcher
from plagiarism_checker import check_plagiarism
from dotenv import load_dotenv
import time

load_dotenv()

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = [".txt", ".docx"]

app = Flask(__name__)
CORS(app)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["ALLOWED_EXTENSIONS"] = ALLOWED_EXTENSIONS

app.secret_key = os.getenv("SECRET_KEY")

crawl_runner = CrawlerRunner()


@app.route("/api", methods=["POST"])
def report():
    request_data = request.get_json()
    text = request_data["text"]

    url_list = urls(text)

    scrape_with_crochet(url_list)

    time.sleep(60)

    percentage = check_plagiarism(
        "json/search_result.json", session.get("filename", "")
    )

    print("Done.")
    print("percentage", percentage)

    return {"percentage_of_similarity": percentage}


@crochet.run_in_reactor
def scrape_with_crochet(url_list):
    # dispatcher.connect(_crawler_result, signal=signals.item_scraped)

    crawl_runner.crawl(ScraperSpider, urls=url_list)
    # return eventual


@app.route("/api/upload", methods=["POST"])
def upload_file():
    uploaded_file = request.files["file"]

    if uploaded_file:
        filename = secure_filename(uploaded_file.filename)
        file_ext = os.path.splitext(filename)[1]

        if file_ext not in app.config["ALLOWED_EXTENSIONS"]:
            return "400"

        uploaded_file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        text = get_text(f"{UPLOAD_FOLDER}/{filename}")

        session["filename"] = f"{UPLOAD_FOLDER}/{os.path.splitext(filename)[0]}.txt"

    return {"text": text}
