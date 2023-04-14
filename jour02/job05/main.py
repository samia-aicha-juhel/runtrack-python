def calcul(num1, operator, num2):
    if operator == "*":
        return num1*num2 
    if operator == "+":
        return num1+num2
    if operator =="-":
        return num1-num2
    if operator =="/":
        return num1/num2
    if operator =="%":
        return num1%num2
print(calcul(8,"*",9))
print(calcul(8,"+",9))
print(calcul(8,"-",9))
print(calcul(8,"/",9))
print(calcul(8,"%",9))