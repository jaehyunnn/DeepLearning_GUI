### Requirements
    tensorflow >= 1.0.0
    python >= 3
    matplotlib >= 1.3.1
    scikit-image > 0.11.3
    
# Features

## 1. Model 

This TF-wrapper considers the layers in the neural network to be in the form of a Sequence. A quick way to define a network would be

        net = Sequential([Linear(input_dim=784,output_dim=1296, act ='relu', batch_size=FLAGS.batch_size),
                     Linear(1296, act ='relu'), 
                     Linear(1296, act ='relu'),
                     Linear(10, act ='relu'),
                     Softmax()])

        output = net.forward(input_data)
             
## 2. Train the network

This `net` can then be used to propogate and optimize using

        trainer = net.fit(output, ground_truth, loss='softmax_crossentropy', optimizer='adam', opt_params=[FLAGS.learning_rate])
