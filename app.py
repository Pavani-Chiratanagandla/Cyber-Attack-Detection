from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')  

@app.route('/predict', methods=['POST'])
def predict():
    bytes_per_sec = float(request.form['Flow_Bytes_per_second'])
    packets_per_sec = float(request.form['Flow_Packets_per_second'])
    fwd_packets = float(request.form['Fwd_Packets_per_second'])
    ack_flags = float(request.form['ACK_Flag_Count'])
    if bytes_per_sec > 1000 or ack_flags > 10:
        result = "Cyber Attack"
        bg_image = url_for('static', filename='images/result1.webp')
    else:
        result = "NOT Cyber Attack"
        bg_image = url_for('static', filename='images/result2.jpg')

    return render_template('result.html', result=result, bg_image=bg_image)

if __name__ == '__main__':
    app.run(debug=True)
