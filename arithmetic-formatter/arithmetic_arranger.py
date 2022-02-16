def arithmetic_arranger(problems, output=None):
    
    str1 = ""
    str2 = ""
    str3 = ""
    str4 = ""
    tester = []
    
    
    if len(problems) > 5:
      return "Error: Too many problems."

    for i in problems:
      tester.append(i.split())
    
    for i in tester:
      
      if len(i[0]) > 4 != True:
        
        return  "Error: Numbers cannot be more than four digits."
      elif len(i[2]) > 4 != True:
        return  "Error: Numbers cannot be more than four digits."
      
      if i[1] != "+" and i[1] != "-":
        
        return "Error: Operator must be '+' or '-'."
        break
      if i[0].isnumeric()==True and i[2].isnumeric()==True:
        continue
      else:
        
        return  "Error: Numbers must only contain digits."
        break
    i = 1
    for q in tester:
      
      
      
      print(i)
      if len(q[0]) > len(q[2]):
        
        off2 = len(q[0])-len(q[2])
        off3 = len(q[0])+2
        
        if i == len(tester):
          str1+="  "+"{}".format(q[0])
          str2+=q[1]+" "+" "*off2+q[2]
          str3+="-"*off3
          t = round(eval(''.join(q)),0)
          
          if t < 0:
              str4+=" "+str(t)
          else:
              str4+="  "+str(t)
        else:
          str1+="  "+"{}".format(q[0])+" "*4
          str2+=q[1]+" "+" "*off2+q[2]+" "*4
          str3+="-"*off3+" "*4
          t = round(eval(''.join(q)),0)
          
          if t < 0:
              str4+=" "+str(t)+" "*4
          else:
              str4+="  "+str(t)+" "*4
      else:
        if i == len(tester):
          off1 = len(q[2])-len(q[0])
          
          off3 = len(q[2])+2
          
          str1+="  "+" "*off1+"{}".format(q[0])
          str2+=q[1]+" "+q[2]
          str3+="-"*off3
          t = round(eval(''.join(q)),0)
          if t < 0:
              str4+=" "+str(t)
          else:
              str4+="  "+str(t)
        else:
          off1 = len(q[2])-len(q[0])
          
          off3 = len(q[2])+2
          
          str1+="  "+" "*off1+"{}".format(q[0])+" "*4
          str2+=q[1]+" "+q[2]+" "*4
          str3+="-"*off3+" "*4
          t = round(eval(''.join(q)),0)
          if t < 0:
              str4+=" "+str(t)+" "*4
          else:
              str4+="  "+str(t)+" "*4
    
      i+=1
    
    if output == True:
      arranged_problems=str1+"\n"+str2+"\n"+str3+"\n"+str4
    else:
      arranged_problems=str1+"\n"+str2+"\n"+str3
    print("FUNC",len(arranged_problems))
    return arranged_problems
# arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
