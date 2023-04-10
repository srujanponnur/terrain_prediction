# Takes the model and evalutes against data in TestData

import os
from os import path

test_path = "./TestData"
target_path = "./output"

def evaluate_model(model):

    files = sorted(os.listdir(test_path))

    for i in range(0, len(files), 4):
        x_time, x, y_time, y = files[i: i + 4]

    


evaluate_model()