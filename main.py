#3 Neurons using for loops

#input to neuron layer
inputs = [2.0, 4.0, 1.6, 2.8]

#weights associated to different input for each neuron in the layer
weights = [
    [0.2, 0.12, 0.4, -0.5],
    [1, -0.35, -0.21, 0.6],
    [-0.2, 0.31, 0.22, 0.33]
]

#bias for each neuron
biases = [2, 1, 1.2]

#this will contain the output form each of the neurons
layerOutput = []

for neuronWeights, neuronBias in zip(weights, biases):
    neuronOutput = 0

    for nWeight, nInput in zip(neuronWeights, inputs):
        neuronOutput += (nWeight*nInput)

    neuronOutput += neuronBias

    layerOutput.append(neuronOutput)

print(layerOutput)