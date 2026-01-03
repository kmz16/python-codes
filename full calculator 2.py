import time
print(" is 4 #.#.#.#.# worng ")
time.sleep(1.5)
print("welcome calucalator ")
t=input("how go calcularor?(y/n) ")
if t == "y":

    b =input("how go 1.#.# , 2.#.#.# 3 #.#.#.# 4 #.#.#.#.# ")
    if b == "1":
        c =float(input("first one "))
        d =float(input("secord two "))
        e =input(" +,-,?,*, how to go? ")
        if e == "+":
            c += d
            print(f"answer {c}")
        if e == "-":
            c -= d
            print(f"answer {c}")
        if e == "*":
            c *= d
            print(f"answer {c}")
        if e == "/":
            c /= d
            print(f"answer {c}")
        else:
            print("please enter agin ")   
    if b == "2":
        c =float(input("frist one "))
        b =float(input("secord two "))
        e =input(" +,-,?,*, how to go? ")
        if e == "+":
            d=(c+b)
            print(f"answer {d}")
            f=input("enter agin? (y/n) ")
            if f == "y":
                g=(input("how to go? +,-,/,* "))
                if g == "+":
                    u=float(input("thrid three "))
                    h=(d+u)
                    print(f"answer {h}")
                
                if g == "-":
                    u=float(input("thrid three "))
                    h=(d-u)
                    print(f"answer {h}")

                if g == "*":
                    u=float(input("thrid three "))
                    h=(d*u)
                    print(f"answer {h}")

                if g == "/":
                    u=float(input("thrid three "))
                    h=(d/u)
                    print(f"answer {h}")
                else:
                    print("please enter agin")
            if f == "n":
                print(f"thanks")
            else:
                print("please enter agin")
            
                     #########################          
        if e == "-":
            d=(c-b)
            print(f"answer {d}")
            f=input("enter agin? (y/n) ")
            if f == "y":
                g=(input("how to go? +,-,/,* "))
                if g == "+":
                    u=float(input("thrid three "))
                    h=(d+u)
                    print(f"answer {h}")
                
                if g == "-":
                    u=float(input("thrid three "))
                    h=(d-u)
                    print(f"answer {h}")

                if g == "*":
                    u=float(input("thrid three "))
                    h=(d*u)
                    print(f"answer {h}")

                if g == "/":
                    u=float(input("thrid three "))
                    h=(d/u)
                    print(f"answer {h}")
                else:
                    print("please enter agin ")
                
            if f == "n":
                print(f"thanks")
            else:
                print("please enter agin")    
                
                
                    ##############
        if e == "*":
            d=(c*b)
            print(f"answer {d}")
            f=input("enter agin? (y/n) ")
            if f == "y":
                g=(input("how to go? +,-,/,*"))
                if g == "+":
                    u=float(input("thrid three "))
                    h=(d+u)
                    print(f"answer {h}")
                
                if g == "-":
                    u=float(input("thrid three "))
                    h=(d-u)
                    print(f"answer {h}")

                if g == "*":
                    u=float(input("thrid three "))
                    h=(d*u)
                    print(f"answer {h}")

                if g == "/":
                    u=float(input("thrid three "))
                    h=(d/u)
                    print(f"answer {h}")
                else:
                    print("please enter agin")
            
            if f == "n":
                print(f"thanks")
            else:
                print("please enter agin")
            
            
                    ###
        if e == "/":
            d=(c/b)
            print(f"answer {d}")
            f=input("enter agin? (y/n) ")
            if f == "y":
                g=(input("how to go? +,-,/,* "))
                if g == "+":
                    u=float(input("thrid three "))
                    h=(d+u)
                    print(f"answer {h}")
                
                if g == "-":
                    u=float(input("thrid three "))
                    h=(d-u)
                    print(f"answer {h}")

                if g == "*":
                    u=float(input("thrid three "))
                    h=(d*u)
                    print(f"answer {h}")

                if g == "/":
                    u=float(input("thrid three "))
                    h=(d/u)
                    print(f"answer {h}")
                else:
                    print("please enter agin")
        
            if f == "n":
                print(f"thanks")
            else:
                print("please enter agin")
        
        else:
            print("please enter agin")
    if b == "3":
        c=float(input("first one "))
        b=float(input("secord two "))
        e=input("how to go? +,-,/,* ")
        if e == "+":
            f=(c+b)
            print(f"answer {f}")
            g=input("enter agin?(y/n) ")
            if g == "y":
                h=input("how to go? +,-,/,* ")
                if h == "+":
                    j=float(input("thrid three "))
                    k=(j+f)
                    print(f"answer {k}")
                    m=input("enter agin?(y/n) ")
                    if m == "y":
                        u=input("how to go? +,-,/,* ")
                        if u == "+":
                            l=float(input("fourth "))
                            p=(k+l)
                            print(f"answer {p}")
                        
                        if u == "-":
                            l=float(input("fourth "))
                            p=(k-l)
                            print(f"answer {p}")
                        
                        if u == "*":
                            l=float(input("fourth "))
                            p=(k*l)
                            print(f"answer {p}")
                        
                        if u == "/":
                            l=float(input("fourth "))
                            p=(k/l)
                            print(f"answer {p}")
                        
                        else:
                            print("enter agin")

                    if m == "n":
                        print("thanks")

                    else:
                        print("enter agin")
                     ####################    
                if h == "-":
                    j=float(input("thrid three "))
                    k=(j-f)
                    print(f"answer {k}")
                    m=input("enter agin?(y/n)")
                    if m == "y":
                        u=input("how to go? +,-,/,*")
                        if u == "+":
                            l=float(input("fourth "))
                            p=(k+l)
                            print(f"answer {p}")
                        
                        if u == "-":
                            l=float(input("fourth "))
                            p=(k-l)
                            print(f"answer {p}")
                        
                        if u == "*":
                            l=float(input("fourth "))
                            p=(k*l)
                            print(f"answer {p}")
                        
                        if u == "/":
                            l=float(input("fourth "))
                            p=(k/l)
                            print(f"answer {p}")
                    
                    if m == "n":
                        print("thanks")

                    else:
                        print("enter agin")
                        ############
                
                if h == "*":
                    j=float(input("thrid three "))
                    k=(j*f)
                    print(f"answer {k}")
                    m=input("enter agin?(y/n) ")
                    if m == "y":
                        u=input("how to go? +,-,/,* ")
                        if u == "+":
                            l=float(input("fourth "))
                            p=(k+l)
                            print(f"answer {p}")
                        
                        if u == "-":
                            l=float(input("fourth "))
                            p=(k-l)
                            print(f"answer {p}")
                        
                        if u == "*":
                            l=float(input("fourth "))
                            p=(k*l)
                            print(f"answer {p} ")
                        
                        if u == "/":
                            l=float(input("fourth "))
                            p=(k/l)
                            print(f"answer {p}")
                    
                    if m == "n":
                        print("thanks")

                    else:
                        print("enter agin") 
                        ##############

                if h == "/":
                    j=float(input("thrid three "))
                    k=(j/f)
                    print(f"answer {k}")
                    m=input("enter agin?(y/n) ")
                    if m == "y":
                        u=input("how to go? +,-,/,* ")
                        if u == "+":
                            l=float(input("fourth "))
                            p=(k+l)
                            print(f"answer {p}")
                        
                        if u == "-":
                            l=float(input("fourth "))
                            p=(k-l)
                            print(f"answer {p}")
                        
                        if u == "*":
                            l=float(input("fourth "))
                            p=(k*l)
                            print(f"answer {p}")
                        
                        if u == "/":
                            l=float(input("fourth "))
                            p=(k/l)
                            print(f"answer {p}")
                        else:
                            print("enter agin")

                    if m == "n":
                        print("thanks")

                    else:
                        print("enter agin")                     
                    
                else:
                    print("enter agin")    
            
            if g == "n":
                print("thanks")
            
            else:
                ("enter agin")
                      ##################
        if e == "-":
            f=(c-b)
            print(f"answer {f}")
            g=input("enter agin?(y/n) ")
            if g == "y":
                h=input("how to go? +,-,/,* ")
                if h == "+":
                    j=float(input("thrid three "))
                    k=(j+f)
                    print(f"answer {k}")
                    m=input("enter agin?(y/n) ")
                    if m == "y":
                        u=input("how to go? +,-,/,* ")
                        if u == "+":
                            l=float(input("fourth "))
                            p=(k+l)
                            print(f"answer {p}")
                        
                        if u == "-":
                            l=float(input("fourth "))
                            p=(k-l)
                            print(f"answer {p}")
                        
                        if u == "*":
                            l=float(input("fourth "))
                            p=(k*l)
                            print(f"answer {p}")
                        
                        if u == "/":
                            l=float(input("fourth "))
                            p=(k/l)
                            print(f"answer {p}")
                        else:
                            print("enter agin")

                         
                    if m == "n":
                        print("thanks")

                    else:
                        print("enter agin")
                     ####################    
                if h == "-":
                    j=float(input("thrid three "))
                    k=(j-f)
                    print(f"answer {k}")
                    m=input("enter agin?(y/n) ")
                    if m == "y":
                        u=input("how to go? +,-,/,* ")
                        if u == "+":
                            l=float(input("fourth "))
                            p=(k+l)
                            print(f"answer {p}")
                        
                        if u == "-":
                            l=float(input("fourth "))
                            p=(k-l)
                            print(f"answer {p}")
                        
                        if u == "*":
                            l=float(input("fourth "))
                            p=(k*l)
                            print(f"answer {p}")
                        
                        if u == "/":
                            l=float(input("fourth "))
                            p=(k/l)
                            print(f"answer {p}")
                        
                        else:
                            print("enter agin")
                    if m == "n":
                        print("thanks")

                    else:
                        print("enter agin")
                        ############
                
                if h == "*":
                    j=float(input("thrid three "))
                    k=(j*f)
                    print(f"answer {k}")
                    m=input("enter agin?(y/n) ")
                    if m == "y":
                        u=input("how to go? +,-,/,* ")
                        if u == "+":
                            l=float(input("fourth "))
                            p=(k+l)
                            print(f"answer {p}")
                        
                        if u == "-":
                            l=float(input("fourth "))
                            p=(k-l)
                            print(f"answer {p}")
                        
                        if u == "*":
                            l=float(input("fourth "))
                            p=(k*l)
                            print(f"answer {p}")
                        
                        if u == "/":
                            l=float(input("fourth "))
                            p=(k/l)
                            print(f"answer {p}")
                        else:
                            print("enter agin")

                    if m == "n":
                        print("thanks")

                    else:
                        print("enter agin") 
                        ##############

                if h == "/":
                    j=float(input("thrid three "))
                    k=(j/f)
                    print(f"answer {k}")
                    m=input("enter agin?(y/n) ")
                    if m == "y":
                        u=input("how to go? +,-,/,* ")
                        if u == "+":
                            l=float(input("fourth "))
                            p=(k+l)
                            print(f"answer {p}")
                        
                        if u == "-":
                            l=float(input("fourth "))
                            p=(k-l)
                            print(f"answer {p}")
                        
                        if u == "*":
                            l=float(input("fourth "))
                            p=(k*l)
                            print(f"answer {p}")
                        
                        if u == "/":
                            l=float(input("fourth "))
                            p=(k/l)
                            print(f"answer {p}")
                        
                        else:
                            print("enter agin")

                
                    if m == "n":
                        print("thanks")

                    else:
                        print("enter agin")            
                else:
                    print("enter agin")



            if g == "n":
                print("thanks")

            else:
                print("enter agin")            
        if e == "*":
            f=(c*b)
            print(f"answer {f}")
            g=input("enter agin?(y/n) ")
            if g == "y":
                h=input("how to go? +,-,/,* ")
                if h == "+":
                    j=float(input("thrid three "))
                    k=(j+f)
                    print(f"answer {k}")
                    m=input("enter agin?(y/n) ")
                    if m == "y":
                        u=input("how to go? +,-,/,* ")
                        if u == "+":
                            l=float(input("fourth "))
                            p=(k+l)
                            print(f"answer {p}")
                        
                        if u == "-":
                            l=float(input("fourth "))
                            p=(k-l)
                            print(f"answer {p}")
                        
                        if u == "*":
                            l=float(input("fourth "))
                            p=(k*l)
                            print(f"answer {p}")
                        
                        if u == "/":
                            l=float(input("fourth "))
                            p=(k/l)
                            print(f"answer {p}")
                        else:
                            ("enter agin")
                        
                    if m == "n":
                        print("thanks")

                    else:
                        print("enter agin")
                     ####################    
                if h == "-":
                    j=float(input("thrid three "))
                    k=(j-f)
                    print(f"answer {k}")
                    m=input("enter agin?(y/n) ")
                    if m == "y":
                        u=input("how to go? +,-,/,* ")
                        if u == "+":
                            l=float(input("fourth "))
                            p=(k+l)
                            print(f"answer {p}")
                        
                        if u == "-":
                            l=float(input("fourth "))
                            p=(k-l)
                            print(f"answer {p}")
                        
                        if u == "*":
                            l=float(input("fourth "))
                            p=(k*l)
                            print(f"answer {p}")
                        
                        if u == "/":
                            l=float(input("fourth "))
                            p=(k/l)
                            print(f"answer {p}")
                        else:
                            print("enter agin")

                    if m == "n":
                        print("thanks")

                    else:
                        print("enter agin")
                        ############
                
                if h == "*":
                    j=float(input("thrid three "))
                    k=(j*f)
                    print(f"answer {k}")
                    m=input("enter agin?(y/n) ")
                    if m == "y":
                        u=input("how to go? +,-,/,* ")
                        if u == "+":
                            l=float(input("fourth "))
                            p=(k+l)
                            print(f"answer {p}")
                        
                        if u == "-":
                            l=float(input("fourth "))
                            p=(k-l)
                            print(f"answer {p}")
                        
                        if u == "*":
                            l=float(input("fourth "))
                            p=(k*l)
                            print(f"answer {p}")
                        
                        if u == "/":
                            l=float(input("fourth "))
                            p=(k/l)
                            print(f"answer {p}")
                        else:
                            ("enter agin")


                    if m == "n":
                        print("thanks")

                    else:
                        print("enter agin") 
                        ##############

                if h == "/":
                    j=float(input("thrid three "))
                    k=(j/f)
                    print(f"answer {k}")
                    m=input("enter agin?(y/n) ")
                    if m == "y":
                        u=input("how to go? +,-,/,* ")
                        if u == "+":
                            l=float(input("fourth "))
                            p=(k+l)
                            print(f"answer {p}")
                        
                        if u == "-":
                            l=float(input("fourth "))
                            p=(k-l)
                            print(f"answer {p}")
                        
                        if u == "*":
                            l=float(input("fourth "))
                            p=(k*l)
                            print(f"answer {p}")
                        
                        if u == "/":
                            l=float(input("fourth "))
                            p=(k/l)
                            print(f"answer {p}")
                        else:
                            ("enter agin")                     

                    if m == "n":
                        print("thanks")

                    else:
                        print("enter agin")
                else:
                    print("enter agin")        
        if e == "/":

            f=(c/b)
            print(f"answer {f}")
            g=input("enter agin?(y/n) ")
            if g == "y":
                h=input("how to go? +,-,/,* ")
                if h == "+":
                    j=float(input("thrid three "))
                    k=(j+f)
                    print(f"answer {k}")
                    m=input("enter agin?(y/n) ")
                    if m == "y":
                        u=input("how to go? +,-,/,* ")
                        if u == "+":
                            l=float(input("fourth "))
                            p=(k+l)
                            print(f"answer {p}")
                        
                        if u == "-":
                            l=float(input("fourth "))
                            p=(k-l)
                            print(f"answer {p}")
                        
                        if u == "*":
                            l=float(input("fourth "))
                            p=(k*l)
                            print(f"answer {p}")
                        
                        if u == "/":
                            l=float(input("fourth "))
                            p=(k/l)
                            print(f"answer {p}")
                        else:
                            print("enter agin")

                    if m == "n":
                        print("thanks")

                    else:
                        print("enter agin")
                     ####################    

                if h == "-":
                    j=float(input("thrid three "))
                    k=(j-f)
                    print(f"answer {k}")
                    m=input("enter agin?(y/n) ")
                    if m == "y":
                        u=input("how to go? +,-,/,* ")
                        if u == "+":
                            l=float(input("fourth "))
                            p=(k+l)
                            print(f"answer {p}")
                        
                        if u == "-":
                            l=float(input("fourth "))
                            p=(k-l)
                            print(f"answer {p}")
                        
                        if u == "*":
                            l=float(input("fourth "))
                            p=(k*l)
                            print(f"answer {p}")
                        
                        if u == "/":
                            l=float(input("fourth "))
                            p=(k/l)
                            print(f"answer {p}")
                        else:
                            print("enter agin")

                    if m == "n":
                        print("thanks")

                    else:
                        print("enter agin")
                        ############
                
                if h == "*":
                    j=float(input("thrid three "))
                    k=(j*f)
                    print(f"answer {k}")
                    m=input("enter agin?(y/n) ")
                    if m == "y":
                        u=input("how to go? +,-,/,* ")
                        if u == "+":
                            l=float(input("fourth "))
                            p=(k+l)
                            print(f"answer {p}")
                        
                        if u == "-":
                            l=float(input("fourth "))
                            p=(k-l)
                            print(f"answer {p}")
                        
                        if u == "*":
                            l=float(input("fourth "))
                            p=(k*l)
                            print(f"answer {p}")
                        
                        if u == "/":
                            l=float(input("fourth "))
                            p=(k/l)
                            print(f"answer {p}")
                        else:
                            print("enter agin")

                    if m == "n":
                        print("thanks")

                    else:
                        print("enter agin") 
                        ##############

                if h == "/":
                    j=float(input("thrid three "))
                    k=(j/f)
                    print(f"answer {k}")
                    m=input("enter agin?(y/n) ")
                    if m == "y":
                        u=input("how to go? +,-,/,* ")
                        if u == "+":
                            l=float(input("fourth "))
                            p=(k+l)
                            print(f"answer {p}")
                        
                        if u == "-":
                            l=float(input("fourth "))
                            p=(k-l)
                            print(f"answer {p}")
                        
                        if u == "*":
                            l=float(input("fourth "))
                            p=(k*l)
                            print(f"answer {p}")
                        
                        if u == "/":
                            l=float(input("fourth "))
                            p=(k/l)
                            print(f"answer {p}")
                        else:
                            print("enter agin")

                    if m == "n":
                        print("thanks")

                    else:
                        print("enter agin")
                else:
                    ("enter agin")
            if g == "n":
                print("thanks")
            else:
                print("enter agin")
 
        else:
            print("enter agin")
    if b == "4":
        c =float(input("first one "))
        d =float(input("secord two "))
        e =input(" +,-,?,*, how to go? ")
        if e == "+":
            r=(c+d)
            print(f"answer {r}")
            q=input("enter agin?(y/n) ")
            if q == "y":
                e=float(input("secord two "))
                a=(" +,-,?,*, how to go? ")
                if a == "+":
                    c=(r+e)
                    print(f"answer {c}")
                    rt=input("enter agin?(y/n) ")
                    if rt == "y":
                        t=float(input("fourth "))
                        er=input(" +,-,?,*, how to go? ")
                        if er == "+":
                            re=(c+t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                      
                        if er == "-":
                            re=(c-t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        if er == "/":
                            re=(c/t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")

                        if er == "*":
                            re=(c*t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        else:
                            print("enter agin")
                    
                    if rt == "n":
                        print("thanks")
                    else:
                        print("enter agin")


                if a == "-":
                    c=(r-e)
                    print(f"answer {c}")
                    rt=input("enter agin?(y/n) ")
                    if rt == "y":
                        t=float(input("fourth "))
                        er=input(" +,-,?,*, how to go? ")
                        if er == "+":
                            re=(c+t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                      
                        if er == "-":
                            re=(c-t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        if er == "/":
                            re=(c/t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")

                        if er == "*":
                            re=(c*t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        else:
                            print("enter agin")
                    
                    if rt == "n":
                        print("thanks")
                    else:
                        print("enter agin")

                if a == "/":
                    c=(r/e)
                    print(f"answer {c}")
                    rt=input("enter agin?(y/n) ")
                    if rt == "y":
                        t=float(input("fourth "))
                        er=input(" +,-,?,*, how to go? ")
                        if er == "+":
                            re=(c+t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                      
                        if er == "-":
                            re=(c-t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        if er == "/":
                            re=(c/t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")

                        if er == "*":
                            re=(c*t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        else:
                            print("enter agin")




                    if rt == "n":
                        print("thanks")
                    else:
                        print("enter agin")
                
                if a == "*":
                    c=(r*e)
                    print(f"answer {c}")
                    rt=input("enter agin?(y/n) ")
                    if rt == "y":
                        t=float(input("fourth "))
                        er=input(" +,-,?,*, how to go? ")
                        if er == "+":
                            re=(c+t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                      
                        if er == "-":
                            re=(c-t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        if er == "/":
                            re=(c/t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")

                        if er == "*":
                            re=(c*t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        else:
                            print("enter agin")


                    if rt == "n":
                        print("thanks")
                    else:
                        print("enter agin")
                
                else:
                    print("thanks")


            if q == "n":
                print("thanks")
            else:
                print("enter agin")
        if e == "-":
            r=(c-d)
            print(f"answer {r}")
            q=input("enter agin?(y/n) ")
            if q == "y":
                e=float(input("secord two "))
                a=(" +,-,?,*, how to go? ")
                if a == "+":
                    c=(r+e)
                    print(f"answer {c}")
                    rt=input("enter agin?(y/n) ")
                    if rt == "y":
                        t=float(input("fourth "))
                        er=input(" +,-,?,*, how to go? ")
                        if er == "+":
                            re=(c+t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                      
                        if er == "-":
                            re=(c-t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        if er == "/":
                            re=(c/t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")

                        if er == "*":
                            re=(c*t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        else:
                            print("enter agin")
                    
                    if rt == "n":
                        print("thanks")
                    else:
                        print("enter agin")


                if a == "-":
                    c=(r-e)
                    print(f"answer {c}")
                    rt=input("enter agin?(y/n) ")
                    if rt == "y":
                        t=float(input("fourth "))
                        er=input(" +,-,?,*, how to go? ")
                        if er == "+":
                            re=(c+t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                      
                        if er == "-":
                            re=(c-t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        if er == "/":
                            re=(c/t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")

                        if er == "*":
                            re=(c*t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        else:
                            print("enter agin")
                    
                    if rt == "n":
                        print("thanks")
                    else:
                        print("enter agin")

                if a == "/":
                    c=(r/e)
                    print(f"answer {c}")
                    rt=input("enter agin?(y/n) ")
                    if rt == "y":
                        t=float(input("fourth "))
                        er=input(" +,-,?,*, how to go? ")
                        if er == "+":
                            re=(c+t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                      
                        if er == "-":
                            re=(c-t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        if er == "/":
                            re=(c/t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")

                        if er == "*":
                            re=(c*t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        else:
                            print("enter agin")




                    if rt == "n":
                        print("thanks")
                    else:
                        print("enter agin")
                
                if a == "*":
                    c=(r*e)
                    print(f"answer {c}")
                    rt=input("enter agin?(y/n) ")
                    if rt == "y":
                        t=float(input("fourth "))
                        er=input(" +,-,?,*, how to go? ")
                        if er == "+":
                            re=(c+t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                      
                        if er == "-":
                            re=(c-t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        if er == "/":
                            re=(c/t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")

                        if er == "*":
                            re=(c*t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        else:
                            print("enter agin")


                    if rt == "n":
                        print("thanks")
                    else:
                        print("enter agin")
                
                else:
                    print("thanks")
        if e == "/":
            r=(c/d)
            print(f"answer {r}")
            q=input("enter agin?(y/n) ")
            if q == "y":
                e=float(input("secord two "))
                a=(" +,-,?,*, how to go? ")
                if a == "+":
                    c=(r+e)
                    print(f"answer {c}")
                    rt=input("enter agin?(y/n) ")
                    if rt == "y":
                        t=float(input("fourth "))
                        er=input(" +,-,?,*, how to go? ")
                        if er == "+":
                            re=(c+t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                      
                        if er == "-":
                            re=(c-t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        if er == "/":
                            re=(c/t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")

                        if er == "*":
                            re=(c*t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        else:
                            print("enter agin")
                    
                    if rt == "n":
                        print("thanks")
                    else:
                        print("enter agin")


                if a == "-":
                    c=(r-e)
                    print(f"answer {c}")
                    rt=input("enter agin?(y/n) ")
                    if rt == "y":
                        t=float(input("fourth "))
                        er=input(" +,-,?,*, how to go? ")
                        if er == "+":
                            re=(c+t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                      
                        if er == "-":
                            re=(c-t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        if er == "/":
                            re=(c/t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")

                        if er == "*":
                            re=(c*t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        else:
                            print("enter agin")
                    
                    if rt == "n":
                        print("thanks")
                    else:
                        print("enter agin")

                if a == "/":
                    c=(r/e)
                    print(f"answer {c}")
                    rt=input("enter agin?(y/n) ")
                    if rt == "y":
                        t=float(input("fourth "))
                        er=input(" +,-,?,*, how to go? ")
                        if er == "+":
                            re=(c+t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                      
                        if er == "-":
                            re=(c-t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        if er == "/":
                            re=(c/t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")

                        if er == "*":
                            re=(c*t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        else:
                            print("enter agin")




                    if rt == "n":
                        print("thanks")
                    else:
                        print("enter agin")
                
                if a == "*":
                    c=(r*e)
                    print(f"answer {c}")
                    rt=input("enter agin?(y/n) ")
                    if rt == "y":
                        t=float(input("fourth "))
                        er=input(" +,-,?,*, how to go? ")
                        if er == "+":
                            re=(c+t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                      
                        if er == "-":
                            re=(c-t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        if er == "/":
                            re=(c/t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")

                        if er == "*":
                            re=(c*t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        else:
                            print("enter agin")


                    if rt == "n":
                        print("thanks")
                    else:
                        print("enter agin")
                
                else:
                    print("thanks")
        if e == "*":
            r=(c*d)
            print(f"answer {r}")
            q=input("enter agin?(y/n) ")
            if q == "y":
                e=float(input("secord two "))
                a=(" +,-,?,*, how to go? ")
                if a == "+":
                    c=(r+e)
                    print(f"answer {c}")
                    rt=input("enter agin?(y/n) ")
                    if rt == "y":
                        t=float(input("fourth "))
                        er=input(" +,-,?,*, how to go? ")
                        if er == "+":
                            re=(c+t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                      
                        if er == "-":
                            re=(c-t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        if er == "/":
                            re=(c/t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")

                        if er == "*":
                            re=(c*t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        else:
                            print("enter agin")
                    
                    if rt == "n":
                        print("thanks")
                    else:
                        print("enter agin")


                if a == "-":
                    c=(r-e)
                    print(f"answer {c}")
                    rt=input("enter agin?(y/n) ")
                    if rt == "y":
                        t=float(input("fourth "))
                        er=input(" +,-,?,*, how to go? ")
                        if er == "+":
                            re=(c+t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                      
                        if er == "-":
                            re=(c-t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        if er == "/":
                            re=(c/t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")

                        if er == "*":
                            re=(c*t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        else:
                            print("enter agin")
                    
                    if rt == "n":
                        print("thanks")
                    else:
                        print("enter agin")

                if a == "/":
                    c=(r/e)
                    print(f"answer {c}")
                    rt=input("enter agin?(y/n) ")
                    if rt == "y":
                        t=float(input("fourth "))
                        er=input(" +,-,?,*, how to go? ")
                        if er == "+":
                            re=(c+t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                      
                        if er == "-":
                            re=(c-t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        if er == "/":
                            re=(c/t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")

                        if er == "*":
                            re=(c*t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        else:
                            print("enter agin")




                    if rt == "n":
                        print("thanks")
                    else:
                        print("enter agin")
                
                if a == "*":
                    c=(r*e)
                    print(f"answer {c}")
                    rt=input("enter agin?(y/n) ")
                    if rt == "y":
                        t=float(input("fourth "))
                        er=input(" +,-,?,*, how to go? ")
                        if er == "+":
                            re=(c+t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                      
                        if er == "-":
                            re=(c-t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        if er == "/":
                            re=(c/t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")

                        if er == "*":
                            re=(c*t)
                            print(f"answer {re}")
                            we=input("enter agin(y/n) ")
                            if we == "y":
                                wq=float(input("fiveth "))
                                rh=input("+,-,?,*, how to go ")
                                if rh == "+":
                                    qe=(rh+re)
                                    print(f"answer {qe}")
                                if rh == "-":
                                    qe=(rh-re)
                                    print(f"answer{qe}")
                                if rh == "/":
                                    qe=(rh/re)
                                    print(f"answer {qe}")
                                if rh == "*":
                                    qe=(rh*re)
                                    print(f"answer {qe}")
                                else:
                                    print("enter agin")
                                
                            if we == "n":
                                print("thanks")
                            else:
                                print("enter agin")
                        
                        else:
                            print("enter agin")


                    if rt == "n":
                        print("thanks")
                    else:
                        print("enter agin")
                
                else:
                    print("thanks")
        else:
            print("enter agin")

    else:
        print("enter agin")

if t == "n":
    print("thanks") 
else:
    print("enter agin")
            
