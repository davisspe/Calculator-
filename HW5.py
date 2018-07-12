#HW5

import math  
import pdb

class Calculator:
    class stack:
        class node:        ### stack design for our calculator
        # push the position of every ( and pop when ) is found.
        # This way parentheses are matched
        # ---  code the rest of the class ---
        #   It's very similar to the queue in EX9_15
        #
            def __init__(self, val, nextNode):
                self.value=val
                self.nextNode=nextNode
    
        def __init__(self):
            self.top=None
            self.size=0
        def __len__(self):
            return self.size
        def push(self, val):
            #It adds a new node including val at the top pointer
            newStack=self.node(val,None)
            if self.size==0:
                self.top=newStack
                self.size=1
            else:
                newStack.nextNode=self.top
                self.top=newStack
                self.size+=1
        def pop(self):
            #It returns the value at the top pointer, then delete the node
            popped=self.top.value
            self.top=self.top.nextNode
            self.size-=1
            return popped
    #----- until here ----#
        
    def exeOpr(self,num1, opr, num2):
        #This is a simple utility function skipping type check
        if opr=="+":
            return num1+num2
        elif opr=="-":
            return num1-num2
        elif opr=="*":
            return num1*num2
        elif opr=="/":
            return num1/num2
        elif opr=="^":
            return num1**num2
        else:
            return None

    def findNextOpr(self,s):
        if len(s)<=0 or not isinstance(s,str):
            print("type mimatch error: findNextOpr")
            return "type mimatch error: findNextOpr"
    
        for i in range(len(s)):
            if (s[i]=="+" or s[i]=="-" or s[i]=="*" or s[i]=="/" or s[i]=="^"):
                return i
        return -1
    #--- function code ends -----#
    def isNumber(self,s):
        #s must be a non-empty string
        #returns True if it's convertible to float, else False
        if len(s)==0 or not isinstance(s, str):
            print("type mismatch error: isNumber")
            return "type mismatch error: isNumber"
        #--- function code starts ---#
        l=["0","1","2","3","4","5","6","7","8","9"]
        dotCount=0
        if s[0]==".":
            dotCount+=1
        elif(s[0] not in l and s[0]!="-"):
            return False
        for i in range(1,len(s)):
            if s[i]==".":
                dotCount+=1
                if dotCount>1:
                    return False
            elif s[i] not in l:
                return False
        return True 
        #--- function code ends ---#
 
 
    
    def isVariable(self, s):
        ## It returns True if s is a string
        #   that can be a variable, 
        #   i.e. after striping it consists of only
        #    alphabet letters and 0-9,
        #    and the first char must be a letter
        if isinstance(s,str):
            if s[:6]=="return":
                return False
            if s[0].isalpha():
                return True
            else:
                return False
        else:
            return False
    
    ### modify getNextNumber into this
    def getNextItem(self, expr, pos):
        #expr is a given arithmetic formula in string
        #pos = start position in expr
        #1st returned value = the next number or a variable(None if N/A)
        #   -- So the change is to recognize a variable
        #2nd returned value = the next operator (None if N/A)
        #3rd retruned value = the next operator position (None if N/A)
        if len(expr)==0 or not isinstance(expr, str) or pos<0 or pos>=len(expr) or not isinstance(pos, int):
            print("type mismatch error: getNextNumber")
            return None, None, "type mismatch error: getNextNumber"
    #--- function code starts ---#
        else:
            nb=False
            vb=False
            end=self.findNextOpr(expr[pos:len(expr)])
            neg=False
            if end==0 and expr[pos+end]=="-":
                end=self.findNextOpr(expr[pos+1:len(expr)])
                pos+=1
                neg=True
            if end!=-1:
                end+=len(expr[0:pos]) 
                n1=-1
                for z in range(pos,end):
                    if self.isNumber(expr[z]) and not vb:
                        nb=True
                        n1=z
                        for k in range(z,end):
                            if not self.isNumber(expr[k]):
                                n2=k
                                break
                            else:
                                n2=end
                        break
                    elif self.isVariable(expr[z]) and not nb:
                        vb=True
                        n1=z
                        for k in range(z,end):
                            if not self.isVariable(expr[k]) and not self.isNumber(expr[k]):
                                n2=k
                                break
                            else:
                                n2=end
                        break
                if (n1!=-1) and nb:
                    if neg:
                        num=float(expr[n1:n2])
                        num*=-1
                    else:
                        num=float(expr[n1:n2])
                elif (n1!=-1) and vb:
                    if neg:
                        num=self.varDic[expr[n1:n2]]
                        num*=-1
                    else:
                        if expr[n1:n2] in self.varDic:
                            num=self.varDic[expr[n1:n2]]
                        else:
                            num=None
                else:
                    num=None
                return num, expr[end],end
            else:
                if not self.isVariable(expr[pos:len(expr)]):
                    if neg:
                        num=float(expr[pos:len(expr)])
                        num*=-1
                    else:
                        num=float(expr[pos:len(expr)])
                else:
                    if neg:
                        num=self.varDic[expr[pos:len(expr)]]
                        num*=-1
                    else:
                        num=self.varDic[expr[pos:len(expr)]]
            return num,None,None
 
  
    #--- function code ends ---#
    def __init__(self):
        self.lines = []
        #e.g. if expr = " a = 2+3*(1+3 / 2) ; b = 4*(a+3)  ",
        #   self.lines = [["a", "2+3*(1+3 / 2)"], ["b", "4*(a+3)"]]
        self.varDic = {}
        # The variable dictionary
        #   whose keys are all the currently detected variables
        #   whose values (as a dictionary) are
        #               the values of the variables
        # You can add other class instance variables here too
        self.funcDic={}
        self.setFunct()
    def setFunct(self):
        # The function refers to self.functDef,
        #  and set self.functDic to be
         self.funcDic={'sqrt': 'x: math.sqrt(x)', 'exp': 'x: math.exp(x)', 'sin': 'x: math.sin(x)',
           'cos': 'x: math.cos(x)', 'tan': 'x: math.cos(x)', 'ln': 'x: math.log(x)',
           'lg': 'x: math.log(x) / math.log(2)', 'round': 'x, d: round(x, d)'}

    def getLines(self, expr):
         #expr : input to calc
         #the function sets self.lines
             lines=expr.split(";")
             for part in range(len(lines)):
                 lines[part]=lines[part].split('=')
             self.lines=lines
        
 
    def _calc(self,expr):
        #expr: nonempty string that is an arithmetic expression
        #the fuction returns the calculated result
        if len(expr)<=0 or not isinstance(expr,str):
            print("argument error: line A in eval_expr")        #Line A
            return "argument error: line A in eval_expr"
        #Hold two modes: "addition" and "multiplication"
        #Initializtion: get the first number
        newNumber, newOpr, oprPos = self.getNextItem(expr, 0)
        if newNumber is None:
            print("input formula error: line B in eval_expr")   #Line B
            return "input formula error: line B in eval_expr" 
        elif newOpr is None:
            return newNumber
        elif newOpr=="+" or newOpr=="-":
            mode="add"
            addResult=newNumber     #value so far in the addition mode
            mulResult=None          #value so far in the mulplication mode
            powResult=None
        elif newOpr=="*" or newOpr=="/":
            mode="mul"
            addResult=0
            mulResult=newNumber
            powResult=None
        elif newOpr=="^":
            mode="pow"
            addResult=0
            mulResult=0
            powResult= newNumber
        pos=oprPos+1                #the new current position
        opr=newOpr                  #the new current operator
        #start the calculation. Use the above functions effectively.
        aws=newNumber
        tempOp=""
        while True:
            #--- code outer while loop ---#
            if len(expr[pos:])==0 and addResult==None:
                break
            else:
                newNumber, newOpr, oprPos = self.getNextItem(expr, pos)
            if newNumber is None:
                print("input formula error: line B in eval_expr")   #Line B
                return "input formula error: line B in eval_expr"
            #start calc
            #power
            if mode=="pow":
                aws=self.exeOpr(aws,opr,newNumber)
            #multiply if no power next 
            elif mode=="mul" and newOpr!="^":
                aws=self.exeOpr(aws,opr,newNumber)
            #multiply with power break
            #fix
            elif mode=="mul" and newOpr=="^":
                holdaws=aws
                holdopr=opr
                aws=newNumber
                pos=oprPos+1
                opr=newOpr
                mode="pow"
                newNumber, newOpr, oprPos = self.getNextItem(expr, pos)
                if newNumber is None:
                    print("input formula error: line B in eval_expr")   #Line B
                    return "input formula error: line B in eval_expr"
                aws=self.exeOpr(aws,opr,newNumber)
                aws=self.exeOpr(holdaws,holdopr,aws)
            #add if next is not multiply or power
            elif newOpr!='*' and newOpr!='/' and newOpr!='^':
                if mulResult!=None:
                    aws=self.exeOpr(aws,opr,newNumber)
                else:
                    aws=self.exeOpr(aws,opr,newNumber)
                addResult==0
            #add if multiply are after it.
            else:
                holdaws=aws
                holdopr=opr
                aws=newNumber
                pos=oprPos+1
                opr=newOpr
                if opr=="*" or opr=="/":
                    mode="mul"
                elif opr=="^":
                    mode="pow"
                
                while True:
                    #start of inner While loop
                    newNumber, newOpr, oprPos = self.getNextItem(expr, pos)
                    if newNumber is None:
                        print("input formula error: line B in eval_expr")   #Line B
                        return "input formula error: line B in eval_expr"
                    if mode=="pow":
                        aws=self.exeOpr(aws,opr,newNumber)
                    elif mode=="mul":
                        if newOpr!="^":
                            aws=self.exeOpr(aws,opr,newNumber)
                        else:
                            holdaws1=aws
                            holdopr1=opr
                            aws=newNumber
                            pos=oprPos+1
                            opr=newOpr
                            mode="pow"
                            newNumber, newOpr, oprPos = self.getNextItem(expr, pos)
                            if newNumber is None:
                                print("input formula error: line B in eval_expr")   #Line B
                                return "input formula error: line B in eval_expr"
                            aws=self.exeOpr(aws,opr,newNumber)
                            aws=self.exeOpr(holdaws1,holdopr1,aws)                               
                    if newOpr is None:
                        break
                    elif newOpr=="+" or newOpr=="-":
                        mode="add"
                        addResult=newNumber     
                        mulResult=None
                        powResult=None
                        break
                    elif newOpr=="*" or newOpr=="/":
                        mode="mul"
                        addResult=0
                        mulResult=newNumber
                        powResult=None
                    elif newOpr=="^":
                        mode="pow"
                        addResult=0
                        mulResult=0
                        powResult= newNumber
                    if newNumber is None and addResult==None:
                        break
                    pos=oprPos+1                
                    opr=newOpr
                    #end of inner while loop
                aws=self.exeOpr(holdaws,holdopr,aws)
            #end of calc
            #Reset for next caculation
            if newOpr is None:
                break
            elif newOpr=="+" or newOpr=="-":
                mode="add"
                addResult=newNumber     
                mulResult=None          
                powResult=None
            elif newOpr=="*" or newOpr=="/":
                mode="mul"
                addResult=0
                mulResult=newNumber
                powResult=None
            elif newOpr=="^":
                mode="pow"
                addResult=0
                mulResult=0
                powResult= newNumber
            if newNumber is None and addResult==None:
                break
            pos=oprPos+1                #the new current position
            opr=newOpr                  #the new current operator
            #end of outer while loop 
        return aws
            #--- end of function ---#
    def funcCalc(self,expr):
        #Find all functions and return caculated values of the functions
        for eq in self.funcDic:
            par=expr.find(eq)
            if par!=-1:
                par+=len(eq)+1
                if(expr[par-1]!="("):
                    expr=expr[:par-1]+expr[par:]
                counter=par
                inner=0
                while True:
                    if(expr[counter]=="("):
                       inner+=1
                    elif(expr[counter]==")" and inner==0):
                        x=self._calcHW3(expr[par:counter])
                        y=eval("lambda "+self.funcDic[eq])
                        incert=y(x)
                        start=par-len(eq)-1
                        expr=expr[:start]+str(incert)+expr[counter+1:]
                        break
                    elif(expr[counter]==")"):
                        inner-=1
                    counter+=1
                    
            
        modCheck=expr.find("mod")
        if modCheck!=-1:
                modLoc=modCheck+3+1
                if(expr[modCheck-1]!="("):
                    expr=expr[:modCheck-1]+expr[modCheck:]
                counter=modLoc
                inner=0
                while True:
                    if(expr[counter]=="("):
                       inner+=1
                    elif(expr[counter]==")" and inner==0):
                        comma=expr.find(",",modCheck)
                        x=self._calcHW3(expr[modLoc:comma])
                        d=self._calcHW3(expr[comma:counter])
                        y=eval("lambda "+"x,d: x%d")
                        incert=y(x,d)
                        start=modLoc-3-2
                        expr=expr[:start]+str(incert)+expr[counter+1:]
                        break
                    elif(expr[counter]==")"):
                        inner-=1
                    counter+=1
        #find paren 
        return expr;
    def _calcHW3(self,expr):
        expr=self.funcCalc(expr)
        c=0
        while True:
            if c>=len(expr):
                break
            if expr[c] is " ":
                expr=expr[:c]+expr[c+1:]
            else:
                c+=1
        left=0
        right=0
        s=Calculator.stack()
        findPar=0
        for x in expr:
            if x=="(":
                left+=1
            elif x==")":
                right+=1
        if right!=left:
            return "Error: Invalid Parentheses"
        while True:
            if findPar>=len(expr):
                break
            if expr[findPar]=="(":
                s.push(findPar)
            elif expr[findPar]==")" and s.size!=0:
                left=s.pop()
                z=self._calc(expr[(left+1):findPar])
                if isinstance(z,str):
                    return z
                else:
                    if(left==0):
                        expr=expr[:left]+str(z)+expr[findPar+1:]
                        findPar=left-1
                    else:    
                        expr=expr[:left]+str(z)+expr[findPar+1:]
                        findPar=left-1
            findPar+=1
        return self._calc(expr)
    ### THe main function
    def calc(self, expr):
        ## First split expr into the lines.
        ## Further modify so that self.lines is correctly set.
        ## Then execute self.lines from the top one by one
        ##       calling _calcHW3
        ## Find the value of the RHS...
        ret=expr.find("return")
        if ret==-1:
            print("Error: no return statment")
            return "Error: No Return statement"
        else:
            ret+=6
        self.getLines(expr)
        for x in self.lines:
            y=x[0]
            c=0
            while True:
                if c>=len(y):
                    break
                if y[c] is " ":
                   y=y[:c]+y[c+1:]
                else:
                    c+=1
            if self.isVariable(y):
                z=x[1]
                w=self._calcHW3(z)
                if(isinstance(w,str)):
                    print(w)
                    return w
                self.varDic[y]=w
        y=self._calcHW3(expr[ret:])
        self.varDic["__return__"]=y
        return y
    ##### Make sure everything is on self.
    ##### Calling fucntions will not work inside the class without self.
    #end of calculator

## To debug
c = Calculator()
#s=""
#s= " a1 =3  ;  bb = 1 ; c54 = a1 + bb ; new = 34; return 3 "
#s = "  a1 = (4.2 + 5)/ 3  ;  bb = a1 * 2 + 1 ; c54 = a1 + bb ;return c54*5 + a1"
#s = "  a = (4.2 + 5)/ 3  ;b = 1 + 2*3; c = 4*a + 5 ; return c"
#s  = " a = 2 ; pi = 3.141596; return pi* a^2"
s="pi = 3.1415926 ; x = sin(2*pi/3) + 3* cos( pi / 4);  return x"
#*******
#s=" a1 = 3 ; b2  =  cos(a1) ; c = sqrt (a1+b2) ; return c / lg(10)"
#s=" y1 = 2*sin ( lg ( 2 - 1/3)) + 2 ; return y1"
#s = "  x = 20 ;  y = 3 ;  return mod(x - 2*y, y+1) "
#s=" return arctan(3.1415926)   "
print(s)
print(c.calc(s))
