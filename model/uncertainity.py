python
import numpy as np

def predict_with_uncertainty(f_model, X, n_iter=100):
    preds = np.array([f_model(X, training=True).numpy() for _ in range(n_iter)])
    mean_preds = preds.mean(axis=0)
    std_preds = preds.std(axis=0)
    return mean_preds, std_preds
