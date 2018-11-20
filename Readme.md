# Naive Bayes Classifier:

    To simply run the code for normal m,Enter
       ``` python main.py ```
       
        output is the top 5 words of spam and ham and accuracy on training and test
        
        
    To run the code for varying m Enter
    
        python main.py <start_m> <end_m> <step_size> <MP_IS_CONSTANT>
        Where
        <start_m> is the starting value of m
        <end_m> is the Ending value of m
        <step_size> is the skipping step of m
        <MP_IS_CONSTANT> is a boolean Value TRUE or FALSE
        
        <MP_IS_CONSTANT> if is TRUE, would vary p for each M such that MxP always remains = 1 if false, it takes p = 1/|VOCAB|
        e.g run:
            python main.py 1,2000,50 FALSE
            python main.py 1,2000,50 TRUE
        
        The output would be a graph along with normal output of python main.py

