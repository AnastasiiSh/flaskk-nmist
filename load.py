from keras.models import model_from_json
import tensorflow as tf


def init():
    #json_file = open('/usr/local/bin/python-getting-started/deploy_mnist_flask/model/model.json','r')
    json_file = open('model.json','r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
   #load weights into new model
    #loaded_model.load_weights("/usr/local/bin/python-getting-started/deploy_mnist_flask/model/model.h5")
    loaded_model.load_weights("model.h5")
    print("Loaded Model from disk")
    #compile and evaluate loaded model
    loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    graph = tf.get_default_graph()
    
    return loaded_model,graph