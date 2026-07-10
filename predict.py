import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Load the trained model
model = tf.keras.models.load_model("model/quality_model.keras")

# Class names
class_names = ["def_front", "ok_front"]


def predict_image(img_path):
    # Load and preprocess image
    img = image.load_img(img_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # Predict
    prediction = model.predict(img, verbose=0)

    # Confidence score
    confidence = float(prediction[0][0])

    # Determine label and confidence
    if confidence >= 0.5:
        label = class_names[1]      # Good Product
        score = confidence
    else:
        label = class_names[0]      # Defective Product
        score = 1 - confidence

    # Return actual confidence percentage
    return label, round(score * 100, 2)