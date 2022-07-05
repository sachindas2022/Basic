#First I'm Added Parent Class...
class Father(object):
    def BB(BBB, SN, V, P):
        BBB.SN = SN
        BBB.V = V
        BBB.P = P

    def Dis(BBB):
        print("Last Name :", BBB.SN)
        print("Your Village Name:", BBB.V)
        print("Your Plot No :", BBB.P)

#Here I'm Starting Child Class...
class Child(Father):
    def CHI(AAA, SNA, VP, PA):
        AAA.SNA = SNA
        AAA.VP=VP
        AAA.PA=PA
    def prin(AAA):
        print("Your Name :",AAA.SNA)
        print("Your Current Location :",AAA.PA)
        print("Your From :",AAA.VP)
        print("Your Father Name :",AAA.SN)
        print("Your Father Village Name:", AAA.V)
        print("Your Father Plot No :", AAA.P)
Father().BB(SN=input("Enter Your Father Name :"),P=input("Enter Your Plot "),V=input("Enter Your Village Name :"))
Father().Dis()
Child().CHI(NA=input("Enter Your Name :"),PA=input("Enter Your Current Location :"),VP=input("Enter Your State Name :"))
Child().prin()
Father().BB("PRADEEP","A","B")
Child().CHI("SATYA","C","D")
Child().prin()
