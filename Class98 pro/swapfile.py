def Swapfile():
    file_name=input("Enter sample txt: ")
    file=open(file_name,'r')
    for line in file:
        words=line.split()
        Number_of_words=Number_of_words+len(words) 
    print("Numberof_words: ",Numberof_words)
    print(words)    
Swapfile()    