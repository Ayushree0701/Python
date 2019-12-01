def search(string): 
      
    length = 0
       
    for word in string.split(): 
        if(len(word) > length): 
            length = len(word) 
      
    return length  
  
 
string =input("Enter the sentence:")
print(search(string))
 
