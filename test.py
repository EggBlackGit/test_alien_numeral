constSymbol = {
  "A": 1,
  "B": 5,
  "Z": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "R": 1000
}

def doProcess(input):
    result = 0
    for idx, i in enumerate(input):
        if i not in constSymbol:
            print('Plase enter \nA:1\nB:2\nZ:10\nL:50\nC:100\nD:500\nR:1000')
            return
            
        if idx<(len(input)-1):
            if constSymbol[input[idx]]>=constSymbol[input[idx+1]]:
                result += constSymbol[i]
            else:
               result -= constSymbol[i]
        else:
            result += constSymbol[i]
    return result

def main():
    print("------------------------------------------------")
    inputUser = str(input('Enter your input:'))
    print("------------------------------------------------")
    result = doProcess(inputUser)
    if result : print("result:",result)
    print("------------------------------------------------")

if __name__=="__main__":
    main()