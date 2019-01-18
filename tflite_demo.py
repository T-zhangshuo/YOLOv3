import time

import cv2
import os
import numpy as np

from tensorflow.contrib.lite.python import interpreter as interpreter_wrapper

from definitions import ROOT_DIR
from predict import preprocess_image
from predict import predict, handle_predictions

def load_labels(filename):
  my_labels = []
  input_file = open(filename, 'r')
  for l in input_file:
    my_labels.append(l.strip())
  return my_labels

model_path = os.path.join(ROOT_DIR, 'model', 'yolov3.tflite')

labels=load_labels('data/coco.names')
interpreter = interpreter_wrapper.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print("输入数据\n",input_details)
print("输出数据\n",output_details)

orig = cv2.imread('data/dog-cycle-car.png')

height = input_details[0]['shape'][1]
width = input_details[0]['shape'][2]

image, image_data = preprocess_image(orig, (height, width))

start = time.time()
interpreter.set_tensor(input_details[0]['index'], image_data)
interpreter.invoke()
end = time.time()

output_data=interpreter.get_tensor(output_details[0]['index'])
results = np.squeeze(output_data)
top_k = results.argsort()[-5:][::-1]
print(len(top_k[0]),"\n")
print("Inference time: {:.2f}s".format((end - start)))
