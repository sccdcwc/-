class Zipper:
    def zipString(self, iniString):
        # write code here
        str1=""
        count=1
        for i in range(len(iniString)):
            if(i!=len(iniString)-1):
                if(iniString[i]==iniString[i+1]):
                    count+=1
                else:
                    str1=str1+iniString[i]+str(count)
                    count=1
            elif(iniString[i]!=iniString[i-1]):
                str1=str1+iniString[i]+"1"
            else:
                str1=str1+iniString[i]+str(count)
        if(len(str1)>=len(iniString)):
            return iniString
        else:
            return str1

if __name__=="__main__":
    zipper=Zipper()
    print(zipper.zipString("welcometonowcoderrrrr"))