class Avtomabil:
    def __init__(self,model,yil,narx):
        self .model=model
        self.yil=yil
        self.narx=narx
    def get_malumot(self):
        return f"{self.model}  {self.yil}   {self.narx}" 
a=Avtomabil("cobalt",2022,"20000$")   
print(a.get_malumot())
 
       
