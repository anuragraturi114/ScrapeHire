from flask import Flask, render_template, request, send_file
from scraper import LinkedInJobsScraper
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        location = request.form.get('location')

        scraper = LinkedInJobsScraper()
        jobs = scraper.scrape_jobs(keywords=title, location=location, max_jobs=50)
        filename = scraper.save_results(jobs)

        return render_template('index.html', download_link=filename)

    return render_template('index.html')

@app.route('/download')
def download_csv():
    file_path = "linkedin_jobs.csv"
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True)