from flask import Flask, request, render_template
from keras.models import load_model
import time, cv2, os
import numpy as np
from PIL import Image

allow_ext = {'png', 'jpg', 'jpeg'}
app = Flask(__name__, template_folder='templates')
upload_folder = 'static'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024


@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/')
def index():
    return render_template('test.html')


@app.route('/predict', methods=['POST'])
def predict():
    chosen_model = request.form['select_model']
    model_dict = {
        'RPS Model': 'citra.h5',
        'LRSModel': 'citra.h5'
    }

    code = f'{model_dict[chosen_model]}'
    model = load_model(model_dict[chosen_model])
    model.compile()

    file = request.files['file']
    file.save(os.path.join('static', 'temp.jpg'))
    img = cv2.cvtColor(np.array(Image.open(file)), cv2.COLOR_BGR2RGB)
    img = np.expand_dims(cv2.resize(
        img, model.layers[0].input_shape[0][1:3]
        if not model.layers[0].input_shape[1:3]
        else model.layers[0].input_shape[1:3]
    ).astype('float32') / 255, axis=0)

    start = time.time()
    pred = model.predict(img)[0]
    labels = np.argmax(pred).astype(np.int32)
    print(labels)
    runtime = round(time.time()-start, 4)
    response_model = [round(item * 100, 2) for item in pred]
    return predict_result(chosen_model, runtime, response_model, 'temp.jpg', code)


def predict_result(model, run_time, predicted, img, code):
    if code == 'citra.h5':
        class_list = {'paper': 0, 'rock': 1, 'scissors': 2}
    else:
        class_list = {'Bandung food': 0, 'Jakarta food': 1, 'Malang food': 2, 'Semarang food': 3}
    index_predict = predicted.index(max(predicted))
    labels = list(class_list.keys())
    return render_template(
        r'result.html', labels=labels, probs=predicted,
        model=model, pred=index_predict, run_time=run_time, img=img
    )


if __name__ == '__main__':
    app.run(debug=True, port=2000)
