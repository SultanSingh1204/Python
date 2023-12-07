def ConvertDectoBin():
    decimale1=input("Inserisci il numero decimale da Covertire")
    decimale=int(decimale1); 
    binario='';
    while(decimale>0):
       
        x = str(decimale%2) 
        binario = x + binario
        decimale=int(decimale/2)
       
    return binario;
def ConvertBintoDec(): 
   NumBin=input("Inserisci il numero binario da Convertire")
   i=0; 
   Decimale=0; 
   Bin=str(NumBin)
   Lunghezza=len(Bin)-1; 

   while Lunghezza!=-1: 
       Decimale=Decimale+ ((2**i)*(int(Bin[Lunghezza]))); 
       i+=1; 
       Lunghezza-=1;  
   return Decimale; 
       
def Operzaioni(): 
    Operazione= input("Vuoi convertire da Decimale a Binario? digita 0 altrimenti per convertire da Binario a decimale digita 1 ")
    if Operazione=="1": 
        print(ConvertDectoBin()); 
    else:
     print(ConvertBintoDec()); 



Operzaioni();
