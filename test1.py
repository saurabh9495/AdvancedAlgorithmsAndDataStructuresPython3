strSample='abc/defgh$ij'
 
#convert string into list
listSample=list(strSample)
 
i=0
j=len(listSample)-1

low = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
upper = 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'


while i<j:
    if not listSample[i].isalpha():
        i+=1
    elif not listSample[j].isalpha():
        j-=1
    else:
        #swap the element in the list 
        #if both elements are alphabets
        listSample[i], listSample[j]=listSample[j], listSample[i]
        i+=1
        j-=1

#convert list into string 
#by concatinating each element in the list
strOut=''.join(listSample)
print(strOut)