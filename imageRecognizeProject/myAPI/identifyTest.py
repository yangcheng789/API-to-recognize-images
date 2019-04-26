# -*- coding: utf-8 -*-
import identifyImage as idi
if __name__ == "__main__":
    imagePath="../images/1.png"
    modelPath="../result/MNIST_Model/my_model_final"
    result=idi.identify(imagePath,modelPath)
    print(result)
