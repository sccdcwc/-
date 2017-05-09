class Replacement:
    def replaceSpace(self, iniString, length):
        # write code here
        for i in range(length):
            if(iniString[i]!=" "):
                iniString=iniString+iniString[i]
            else:
                iniString=iniString+"%20"
        return iniString[length:]
if __name__=="__main__":
    rep=Replacement()
    print(rep.replaceSpace("a v b d",7))