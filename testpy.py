import re
def arithmetic_arranger(problems):
  for operations in problems :
      
    match = (re.search(r"\+|\-",operations)).start()    
    
  
    #print(operations[0])
    #print(operations[match])
    #print(operations[-1])
    a = operations[0:match]
    b = operations[match+1:]
    c = len(a)
    pos = '{:>'+str(c)+'}'
    sec_pos = '{:<'+str(len(a)-len(b))+'}{:>0}'
    fi_pos=pos+sec_pos
    print(fi_pos.format(a,operations[match],b))

#    return arranged_problems
arithmetic_arranger(["13+1","2344+2","1234+23","345+34"])
