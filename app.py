from flash import Flash, render_template, request, jsonify

app=Flash(__name__)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)