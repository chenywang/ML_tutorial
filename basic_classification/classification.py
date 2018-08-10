# TensorFlow and tf.keras
# Helper libraries
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import numpy as np

from tools.images import show_image


if __name__ == '__main__':
    fashion_mnist = keras.datasets.fashion_mnist

    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

    print "train_images", train_images.shape
    print "train_labels", train_labels.shape

    print "test_images", test_images.shape
    print "test_labels", test_labels.shape
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    # inspect the first image
    show_image(train_images[0])

    train_images = train_images / 255.0

    test_images = test_images / 255.0

    # Display the first 25 images

    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid('off')
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[i]])
    plt.show()

    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation=tf.nn.relu),
        keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

    model.compile(optimizer=tf.train.AdamOptimizer(),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(train_images, train_labels, epochs=5)

    # Evaluate accuracy
    test_loss, test_acc = model.evaluate(test_images, test_labels)

    print 'Test accuracy:', test_acc

    # Make predictions

    predictions = model.predict(test_images)

    print predictions[0]

    print np.argmax(predictions[0])

    print test_labels[0]

    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid('off')
        plt.imshow(test_images[i], cmap=plt.cm.binary)
        predicted_label = np.argmax(predictions[i])
        true_label = test_labels[i]
        if predicted_label == true_label:
            color = 'green'
        else:
            color = 'red'
        plt.xlabel("{} ({})".format(class_names[predicted_label],
                                    class_names[true_label]),
                   color=color)
    plt.show()
    # predict one img
    img = test_images[0]
    print(img.shape)

    img = (np.expand_dims(img,0))
    predictions = model.predict(img)
    prediction = predictions[0]

    np.argmax(prediction)