from numpy import *


def sigmoid(x):
    """
    The formula of sigmoid function

    :param x: The value of x to map to the sigmoid function
    :return: The value of f(x) on the sigmoid curve
    """
    return 1 / (1 + exp(-x))


def sigmoid_derivative(x):
    """
    The formula of the sigmoid gradient function

    :param x: The value of x to map to the function
    :return: The value of f'(x) on the sigmoid curve derivative
    """
    fx = sigmoid(x)
    return fx * (1 - fx)


def mse_loss(desireOutput, predictOutput):
    """
    Computes the Mean Squared Loss (MSE) given a prediction and a desired outcome

    :param desireOutput: The desired value of output
    :param predictOutput: The predicted value of output
    :return: The Mean Squared Loss MSE
    """
    return ((desireOutput - predictOutput)**2).mean()


class NeuralNet(object):
    """
    This class trains a two-input neuron network, x1 and x2.
    Both of these two inputs would be passed onto the two neurons h1 and h2.
    The outputs of the neurons will be the input of the final neuron o1,
    which produces the final output.
    """
    def __init__(self):
        """
        Constructor

        """
        # Generate random numbers
        random.seed(1)

        # Assign random weights of each neuron to an array
        self.h1_weights = array([random.random(), random.random()])
        self.h2_weights = array([random.random(), random.random()])
        self.o1_weights = array([random.random(), random.random()])

    def train(self, inputs, outputs, training_iterations):
        """
        supervised training of the neuron network given a training sample sets
        :param inputs [x1, x2]: inputs for neurons h1 and h2 of the training set
        :param outputs o1: output from neuron o1 of the training set
        :param training_iterations: The number of iterations that the training undergoes
        """

        # The learning rate constant.
        eta = 0.01

        for iteration in range(training_iterations):
            k = 0

            # Adjust weight with refinement from each pair of input in the training set
            while k < len(inputs):

                # The input and output of the current training set
                x = inputs[k]
                y_true = outputs[k]

                # Expected output of each neuron with the current weights
                predict_output = self.learn(x)
                h1 = predict_output[0]
                h2 = predict_output[1]
                o1 = predict_output[2]

                y_pred = o1

                # dot product of each neuron given inputs from training set
                sum_h1 = dot(x, self.h1_weights)
                sum_h2 = dot(x, self.h2_weights)
                sum_o1 = dot(x, self.o1_weights)

                # ---------Calculate the derivatives------------#
                dL_dy = -2*(y_true - y_pred)
                dy_dh1 = (self.o1_weights[0] * sigmoid_derivative(sum_o1))
                dy_dh2 = (self.o1_weights[1] * sigmoid_derivative(sum_o1))

                # Neuron h1
                dh1_dw = x * sigmoid_derivative(sum_h1)

                # Neuron h2
                dh2_dw = x * sigmoid_derivative(sum_h2)

                # Neuron o1
                h_array = array([h1, h2])
                dy_dw = h_array * sigmoid_derivative(sum_o1)

                # --------------- Update the weight -------------#
                # Neuron h1
                dL_dw = eta * dL_dy * dy_dh1 * dh1_dw
                self.h1_weights = subtract(self.h1_weights, dL_dw)

                # Neuron h2
                self.h2_weights = subtract(self.h2_weights, eta * dL_dy * dy_dh2 * dh2_dw)

                # Neuron o1
                self.o1_weights = subtract(self.o1_weights, eta * dL_dy * dy_dw)

                k += 1

    def learn(self, inputs):
        """
        Predict the outputs from each neuron with current weights
        :param inputs: inputs from x1 and x2
        :return: output of neurons in a list
        """
        h1 = sigmoid(dot(inputs, self.h1_weights))
        h2 = sigmoid(dot(inputs, self.h2_weights))
        o1_inputs = array([h1, h2]).T
        o1 = sigmoid(dot(o1_inputs, self.o1_weights))

        return [h1, h2, o1]


if __name__ == "__main__":
    # Initialize
    neural_network = NeuralNet()

    # The training set.
    inputs = array([[-2, -1], [25, 6], [17, 4], [-15, -6]])
    outputs = array([1, 0, 0, 1], dtype=float64).T

    # Train the neural network
    neural_network.train(inputs, outputs, 10000)

    # Test the neural network with a test example.
    print(int(round(neural_network.learn(array([-10, -10]))[2])))
