
import matplotlib.pyplot as plt

def plot_accuracy(history):
    plt.plot(history.history['accuracy'], label='Train Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.title('Model Training Accuracy')
    plt.legend()
    plt.show()

def plot_uncertainty(std_preds):
    plt.hist(std_preds, bins=50)
    plt.title('Uncertainty Distribution')
    plt.xlabel('Standard Deviation')
    plt.ylabel('Frequency')
    plt.show()
