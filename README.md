# NeuronNetwork
## Formulation and Schematics
The Neuron Network consists of two inputs x<sub>1</sub> and x<sub>2</sub> (input layer) which pass into neurons h<sub>1</sub> (hidden layer) and h<sub>2</sub> (output layer).
The outputs produced by h<sub>1</sub> and h<sub>2</sub> act as the inputs for neuron o<sub>1</sub>, which then produces a final output,
as shown in the Figure below:<br/>
![network](https://victorzhou.com/27cf280166d7159c0465a58c68f99b39/network3.svg)

To predict the single output value g(x) in terms of multiple inputs x = {x<sub>1</sub>, x<sub>2</sub>,...x<sub>n</sub>}, I use Kolmogorov Theorem (1957) along with the sigmoid activation function, denoted as f. Hence g(x) can be expressed as:<br/>
                                         <p align="center"> g(x) = f(<span>&Sigma;</span><sub>i</sub> x<sub>i</sub>w<sub>i</sub>) </p>

