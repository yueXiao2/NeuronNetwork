# NeuronNetwork
## Formulation and Schematics
The Neuron Network consists of two inputs x<sub>1</sub> and x<sub>2</sub> (input layer) which pass into neurons h<sub>1</sub> and h<sub>2</sub> (hidden layer).
The outputs produced by h<sub>1</sub> and h<sub>2</sub> act as the inputs for neuron o<sub>1</sub> (output layer), which then produces a final output,
as shown in the Figure below:<br/>
![network](https://victorzhou.com/27cf280166d7159c0465a58c68f99b39/network3.svg)

To predict the single output value g(x) in terms of multiple inputs x = {x<sub>1</sub>, x<sub>2</sub>,...x<sub>n</sub>}, I use Kolmogorov Theorem (1957) along with the sigmoid activation function, denoted as f. Hence g(x) can be expressed as:<br/>
                                         <p align="center"> g(x) = f(<span>&Sigma;</span><sub>i</sub> x<sub>i</sub>w<sub>i</sub>)   (1)</p><br/>
where w<sub>i</sub> are the weighting factors of each input to a specific neuron.
Because this model has multiple neural layers, I first calculate the outputs produced by h<sub>1</sub> and h<sub>2</sub> using Equation (1), denoted y<sub>1</sub> and y<sub>2</sub>:<br/>
<p align="center"> y<sub>1</sub>(x) = f(x<sub>1</sub>w<sub>1</sub> + x<sub>2</sub>w<sub>2</sub>)   (2) </p><br/>
<p align="center"> y<sub>2</sub>(x) = f(x<sub>1</sub>w<sub>3</sub> + x<sub>2</sub>w<sub>4</sub>)   (3) </p><br/>
Then these outputs are used as inputs for neuron o<sub>1</sub>, denoted as o:<br/>
<p align="center"> o(x) = f(y<sub>1</sub>w<sub>5</sub> + y<sub>2</sub>w<sub>6</sub>)   (4) </p><br/>

