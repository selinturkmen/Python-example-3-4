

def capitalizer(sentences, punctuations, names):
  
    names  = [elem.lower() for elem in names]
 
    for a in sentences and names:
        b = a.capitalize()
        sentences = sentences.replace(a, b)

    sentences = list(sentences)
    sentences[0]= sentences[0].upper()
   
    for i in range(len(sentences)):
       if sentences[i] in punctuations:
           if i+2 in range(len(sentences)):
               sentences[i+2] = sentences[i+2].upper()
    sentences = '' .join(sentences)
    return sentences
    


def main():
 
    sentences = "hello, my name is joe. what is your name? my name is john."
    punctuations = ['.', '!', '?']
    names = ["John", "James", "Alice", "Bob", "Joe"]
    print(capitalizer(sentences, punctuations, names))
    

    
################################################################ 

if __name__ == '__main__':
    main()
