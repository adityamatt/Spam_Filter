import math

def get_vocab(input_file_name):
    content = open(input_file_name).read().splitlines()
    for i in range(len(content)):
        content[i]=content[i].split(" ")
    spam_output = dict()
    ham_output  = dict()
    spam = 0
    ham = 0
    for i in range(len(content)):
        mail_type = str(content[i][1])
        content[i]=content[i][2:]
        if mail_type == "ham":
            ham = ham + 1
            for j in range(0,len(content[i]),2):
                word = str(content[i][j])
                freq = int(content[i][j+1])
                if word not in ham_output:
                    ham_output[word] = freq
                else:
                    ham_output[word] = ham_output[word] + freq
                if word not in spam_output:
                    spam_output[word] = int(0)
                    
        else:
            spam = spam +1
            for j in range(0,len(content[i]),2):
                word = str(content[i][j])
                freq = int(content[i][j+1])
                if word not in ham_output:
                    spam_output[word] = freq
                else:
                    spam_output[word] = spam_output[word] + freq
                if word not in spam_output:
                    ham_output[word] = int(0)
                    

    return spam_output,ham_output,spam,ham
    
def top5(class_vocab):
    i=0
    for key, value in sorted(class_vocab.iteritems(), key=lambda (k,v): (v,k),reverse=True):
        if i<5:
            print "%s:\t\t %s" % (key, value)
            i=i+1
        else:
            break
            
            
def get_data(input_file_name):
    content = open(input_file_name).read().splitlines()
    for i in range(len(content)):
        content[i]=content[i].split(" ")
    output_X = list()
    output_Y = list()
    for i in range(len(content)):
        mail_type = str(content[i][1])
        content[i]=content[i][2:]
        words = dict()
        for j in range(0,len(content[i]),2):
            words[str(content[i][j])]=int(content[i][j+1])
        output_X.append(words)
        output_Y.append(mail_type)
    return output_X,output_Y
        

def pr_given_class_(vocab,m,p):
    output = dict()
    total = sum(vocab[k] for k in vocab)
    for k in vocab:
        output[k] = float(vocab[k]+m*p)/(m+total)
    return output

def probability_class(pr_given_class,pr_class,Xi,m,p,class_vocab,sum_freq):
    output = 0;
    for k in Xi:
        if k in pr_given_class:
            pr = pr_given_class[k]
        else:
            pr = float(m*p)/(m+sum_freq)
            
        output = output +math.log10(pr)
#        output = output +math.log10(pr)+math.log10(Xi[k])
    output= output + math.log10(pr_class)
    return output

def predict_class(Xi ,pr_given_spam ,pr_spam ,pr_given_ham ,pr_ham ,m ,p ,vocab_spam ,vocab_ham):
    sum_freq_spam = sum(vocab_spam[k] for k in vocab_spam)
    sum_freq_ham  = sum(vocab_ham[k] for k in vocab_ham)
    a = probability_class(pr_given_spam,pr_spam,Xi,m,p,vocab_spam,sum_freq_spam)
    b =probability_class(pr_given_ham,pr_ham,Xi,m,p,vocab_ham,sum_freq_ham)
    if a>b:
        return "spam"
    else:
        return "ham"
        
def accuracy(X ,Y ,pr_given_spam ,pr_spam ,pr_given_ham ,pr_ham ,m ,p, vocab_spam,vocab_ham):
    correct = 0
    for i in range(len(X)):
        if Y[i]==predict_class(X[i],pr_given_spam,pr_spam,pr_given_ham,pr_ham, m ,p, vocab_spam, vocab_ham):
            correct = correct + 1
    correct = float(correct)
    return correct/len(X)
