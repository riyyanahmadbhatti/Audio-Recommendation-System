from flask import Flask, render_template, request, send_from_directory
import csv

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fma_large2/<path:filename>')
def download_file(filename):
    return send_from_directory('static/fma_large2', filename)

@app.route('/display_similar', methods=['POST'])
def display_similar():
    selected_file = request.form['audioFile']
    similar_files = find_similar_files(selected_file)
    return similar_files

def find_similar_files(selected_file):
    similar_files = ""
    with open('static/similaraudio.csv/part-00000-e413de01-6577-4569-b914-026bfa77d106-c000.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == selected_file:
                similar_files = row[1]
                break
    return similar_files

if __name__ == '__main__':
    app.run(debug=True)
