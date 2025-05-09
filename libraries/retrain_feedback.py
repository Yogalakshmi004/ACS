

import numpy as np
import tensorflow as tf
import os

# Assuming feedback_data is saved during runtime
feedback_data_path = 'storage/feedback_data.npz'

def load_feedback_data():
    if not os.path.exists(feedback_data_path):
        print("[INFO] No feedback data available yet.")
        return None, None
    data = np.load(feedback_data_path)
    return data['X'], data['y']

def retrain_model(model_path='saved_model', save_path='saved_model'):
    # Load feedback
    X_feedback, y_feedback = load_feedback_data()

    if X_feedback is None or len(X_feedback) == 0:
        print("[INFO] No feedback samples to retrain on.")
        return

    # Load model
    model = tf.keras.models.load_model(model_path)

    # Retrain
    print(f"[INFO] Retraining model on {len(X_feedback)} feedback samples...")
    model.fit(X_feedback, y_feedback, epochs=5, batch_size=8)

    # Save updated model
    model.save(save_path)
    print(f"[SUCCESS] Model retrained and saved to {save_path}")

if _name_ == "_main_":
    retrain_model()