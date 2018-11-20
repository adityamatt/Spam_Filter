from Utility import *
import sys
import matplotlib.pyplot as plt

#if len(sys.argv)<2:
#    print "Correct Syntax is python main.py <Choice>\nWhere Choice is \n1->Naive Bayes Classifiers\n2->K means Clustering"
#    sys.exit(0)


#Variables
train_data = "./nbctrain"
test_data  = "./nbctest"

#Training and test Information 
training_X,training_Y = get_data(train_data)
test_X,test_Y         = get_data(test_data)

#Training
spam_v,ham_v,num_spam,num_ham = get_vocab(train_data)

#Converting int to float for maintaining precision
num_spam = float(num_spam)
num_ham = float(num_ham)

#Counting Total mail
total_mail = num_spam + num_ham

#Probability of spam and ham
pr_spam = num_spam/total_mail
pr_ham  = num_ham /total_mail

#Printing Basic Results
m = float(len(spam_v))
p = 1/m

#Calculating Posteriour of words
pr_given_spam = pr_given_class_(spam_v,m,p)
pr_given_ham = pr_given_class_(ham_v,m,p)

#Printing the Results
print "Top 5 words indicating Spam with their posterior probability:"
top5(pr_given_spam)
print "Top 5 words indicating Ham with their  posterior probability:"
top5(pr_given_ham)

#Printint the Accuracy
print "Accuracy on Training is",accuracy(training_X,training_Y,pr_given_spam,pr_spam,pr_given_ham,pr_ham ,m,p,spam_v,ham_v)
print "Accuracy on   Test   is",accuracy(test_X,test_Y,pr_given_spam,pr_spam,pr_given_ham,pr_ham ,m,p,spam_v,ham_v)


#Experimenting on Values of M
if len(sys.argv)==1:
    sys.exit(0)
elif len(sys.argv)!=5:
    print "The correct Syntax \n\tpython main.py \n OR \n\t python main.py <start_m> <end_m> <step_size> <MP_IS_CONSTANT>"
    print "Where:\n\t <start_m> is the starting value of m\n\t<end_m> is the Ending value of m\n\t<step_size> is the skipping step of m"
    print "\t<MP_IS_CONSTANT> is a boolean Value TRUE or FALSE"
    sys.exit(0)

#Getting Command Line Inputs
start_m = int(sys.argv[1])
end_m   = int(sys.argv[2])
step    = int(sys.argv[3])

mp_value = str(sys.argv[4])

if mp_value!="TRUE" and mp_value!="FALSE":
    print "The correct Syntax \n\tpython main.py \n OR \n\t python main.py <start_m> <end_m> <step_size> <MP_IS_CONSTANT>"
    print "\t<MP_IS_CONSTANT> is a boolean Value TRUE or FALSE"
    sys.exit(0)

#Defining Variables
mod_vocab = float(len(spam_v))


m_list = list()
for i in range(start_m,end_m,step):
    m_list.append(i)

training_acc = list()
test_acc     = list()
print "M\t\tTraining_Accuracy\tTest_accuracy"
for m in m_list:
    #Probability Given Class
    m = float(m)
    if mp_value=="FALSE":
        p=1/mod_vocab
    else:
        p=1.0/m
    
    #Calculating the Posterior
    pr_given_spam = pr_given_class_(spam_v,m,p)
    pr_given_ham = pr_given_class_(ham_v,m,p)
    
    #Calculating the Accuracy
    train_acc1 = accuracy(training_X,training_Y,pr_given_spam,pr_spam,pr_given_ham,pr_ham ,m,p,spam_v,ham_v)
    test_acc1  = accuracy(test_X,test_Y,pr_given_spam,pr_spam,pr_given_ham,pr_ham ,m,p,spam_v,ham_v)
    
    #Printing the information
    print m,"\t\t", train_acc1,"\t\t\t",test_acc1
    
    training_acc.append(train_acc1)
    test_acc.append(test_acc1)
    
#Plotting the graph
plt.plot(m_list,training_acc,label="Training Accuracy",marker='X',color='red')
plt.plot(m_list,test_acc,label = "Test Accuracy",marker='X',color='green')
plt.xlabel("Value of M")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

