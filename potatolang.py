import random
import math

#findMatching function by Brain Damaged Senko#5942
def findMatching(code, index, start, stop):
    if code[index]==start:
        step=1
    elif code[index]==stop:
        step=-1
    else:
        return index
    depth=step
    while depth!=0:
        index+=step
        if code[index]==start:
            depth+=1
        elif code[index]==stop:
            depth-=1
    return index

def asdflang(program, debug = False):
    program = program.lower()
    memory = []
    pc = 0
    incomment = False
    def stackpop():
        if memory:
            return memory.pop()
        return 0
    while pc < len(program):
        if program[pc:pc+1] == "^":
            if incomment == False:
                incomment = True
            else:
                incomment = False
        if incomment == False:
            if program[pc:pc+1] == "i":
                memory.append(ord(input()[:1]))
            if program[pc:pc+1] == "q":
                string = input()[::-1]
                while string:
                    memory.append(ord(string[:1]))
                    string = string[1:]
            elif program[pc:pc+1] == "o":
                print(chr(stackpop()), end="")
            if program[pc:pc+1] == ",":
                memory.append(int(input()))
            elif program[pc:pc+1] == ".":
                print(stackpop(), end="")
            elif program[pc:pc+1] == "0":
                memory.append(0)
            elif program[pc:pc+1] == "1":
                memory.append(1)
            elif program[pc:pc+1] == "2":
                memory.append(2)
            elif program[pc:pc+1] == "3":
                memory.append(3)
            elif program[pc:pc+1] == "4":
                memory.append(4)
            elif program[pc:pc+1] == "5":
                memory.append(5)
            elif program[pc:pc+1] == "6":
                memory.append(6)
            elif program[pc:pc+1] == "7":
                memory.append(7)
            elif program[pc:pc+1] == "8":
                memory.append(8)
            elif program[pc:pc+1] == "9":
                memory.append(9)
            elif program[pc:pc+1] == "a":
                memory.append(stackpop()+stackpop())
            elif program[pc:pc+1] == "d":
                memory.append(stackpop()/stackpop())
            elif program[pc:pc+1] == "e":
                memory.append(stackpop()**stackpop())
            elif program[pc:pc+1] == "p":
                memory.append(stackpop()+1)
            elif program[pc:pc+1] == "u":
                memory.append(stackpop()-1)
            elif program[pc:pc+1] == "v":
                memory.append(math.sqrt(stackpop()))
            elif program[pc:pc+1] == "s":
                memory.append(stackpop()-stackpop())
            elif program[pc:pc+1] == "g":
                if stackpop() > stackpop():
                    memory.append(1)
                else:
                    memory.append(0)
            elif program[pc:pc+1] == "l":
                if stackpop() == stackpop():
                    memory.append(1)
                else:
                    memory.append(0)
            elif program[pc:pc+1] == "m":
                memory.append(stackpop()*stackpop())
            elif program[pc:pc+1] == "n":
                if stackpop() == 0:
                    memory.append(1)
                else:
                    memory.append(0)
            elif program[pc:pc+1] == "%":
                memory.append(stackpop()%stackpop())
            elif program[pc:pc+1] == "b":
                pc = stackpop()
            elif program[pc:pc+1] == "j":
                memory.append(len(memory))
            elif program[pc:pc+1] == "t":
                memory.append(random.randrange(1,11))
            elif program[pc:pc+1] == "h":
                pc = len(program)
            elif program[pc:pc+1] == "r":
                stackpop()
            elif program[pc:pc+1] == "c":
                place = stackpop()
                memory.append(place)
                memory.append(place)
            elif program[pc:pc+1] == "w":
                if memory[-1] != 0:
                    pc = int(findMatching(program, pc, "w", ":"))
            elif program[pc:pc+1] == "f":
                if memory[-1] == 0:
                    pc = int(findMatching(program, pc, "f", ";"))
            elif program[pc:pc+1] == ":":
                if memory[-1] == 0:
                    pc = int(findMatching(program, pc, "w", ":"))
            elif program[pc:pc+1] == ";":
                if memory[-1] != 0:
                    pc = int(findMatching(program, pc, "f", ";"))
            elif program[pc:pc+1] == "x":
                place = stackpop()
                memory.append(memory[place])
                memory.pop(place)
            elif program[pc:pc+1] == "y":
                place = stackpop()
                a = stackpop()
                memory.insert(place, a)
            elif program[pc:pc+1] == "z":
                a = stackpop()
                b = stackpop()
                memory.append(a)
                memory.append(b)
            elif program[pc:pc+1] == "k":
                pc = program[pc:].find(";")+1
        if debug == True: print(memory)
        pc += 1
asdflang(input(), False)
