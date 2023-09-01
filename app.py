from flask import Flask, request, render_template
from entropy import calculate_entropy
from gain import information_gain
from sum_to_n import sum_of_numbers

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/entropy', methods=['GET', 'POST'])
def entropy():
    if request.method == 'POST':
        pos = int(request.form['positive'])
        neg = int(request.form['negative'])
        result = calculate_entropy(pos, neg)
        return f"Entropy: {result}"
    return render_template('entropy.html')


@app.route('/gain', methods=['GET', 'POST'])
def gain():
    if request.method == 'POST':
        subsets = []
        for i in range(5):  # As max subsets is 5
            pos_key = f"pos_{i}"
            neg_key = f"neg_{i}"
            if pos_key in request.form and neg_key in request.form:
                pos = int(request.form[pos_key])
                neg = int(request.form[neg_key])
                subsets.append((pos, neg))

        # Compute original entropy from provided original set:
        original_pos = int(request.form["original_pos"])
        original_neg = int(request.form["original_neg"])
        original_entropy = calculate_entropy(original_pos, original_neg)

        result = information_gain(original_entropy, subsets)
        return f"Information Gain: {result:.4f}"

    return render_template('gain.html')


@app.route('/sum_to_n', methods=['GET', 'POST'])
def sum_to_n():
    if request.method == 'POST':
        n = int(request.form['n'])
        result = sum_of_numbers(n)
        return f"Sum up to {n}: {result}"
    return render_template('sum_to_n.html')


if __name__ == '__main__':
    app.run(debug=True)
