def que_list():
    question_list = [
        "How many continents are there?",             
        "What is the capital of India?",            
        "NG mei kaun se course padhaya jaata hai?"
    ]
    return question_list
que = que_list()
####opetion function
def opt_list():
    option_list = [
        ["Four", "Nine", "Seven", "Eight"],
        ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
        ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
    ]
    return option_list
ope = opt_list()
####answer function
def answer_list():    
    ans_list=[3, 4, 1]
    return ans_list
answer=answer_list()
#### lifeline function
def lifeline():
    option_list1=[["Nine","Seven"],["Delhi","Chennai"],["Software Engineering","Counseling"]]
    return option_list1
life=lifeline()
####lifeline option list
def answer_list1():
    ans_list =[2,1,1]
    return ans_list
answer1=answer_list1()         
sum=0
i=0
index=1
count=1                                                              
#lifecount=0
while i<len(que):
    print("#",index,que[i])
    j=0
    index1=1
    while j<len(ope[i]):
        print(index1,ope[i][j])
        index1=index1+1
        j=j+1
    if count<=1:
        lifeline2=input("enter any answer or use lifeline")
        if lifeline2=="yes":
            k=0
            index3=1
            while k<len(life[i]):
                print(index3,life[i][k])
                index3=index3+1
                k=k+1
            num=int(input("enter your answer"))
            if num==answer1[i]:
                sum=sum+20000
                print("right answer")
                print("you win this",sum)                    
            else:
                print("your answer is wrong")
                print("Game over",sum)
                break
            count=count+1
        else:
                # print("you can't use life line again")             
            num=int(input("enter your answer"))
            if num==answer[i]:
                sum=sum+20000
                print("right answer")
                print("you win  this",sum)                        
            else:
                print("your answer is wrong")
                print("game over",sum)
                break        
    else:
        num=int(input("enter your answer"))
        if num==answer[i]:
            sum=sum+20000
            print("right answer")
            print("you win this",sum)
        else:
            print("your answer is wrong")
            print("Game over",sum)
            break
    index=index+1        
    i=i+1