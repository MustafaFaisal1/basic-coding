data = [""]
variable = [""]
error =  ["syntax", "variable not found"]
err = -1



def print_statement(stat_pr):
    comp_pr = "print "
    if stat_pr[0:6] == comp_pr:
        if stat_pr[6] == '"':
            if stat_pr[len(stat_pr) - 1] == '"':
                print (stat_pr[7:len(stat_pr) - 1])
            else:
                err = 0
        else:
            count = 0
            found = False
            while count < len(variable):
                if stat_pr[6:len(stat_pr)] == variable[count]:
                    index = count
                    found = True
                count += 1
            if found:
                print (data[index])
            else:
                err = 1

            

def input_statement():
    comp_inp = "input "
    stat_inp =  str(input())
    if stat_inp[0:6] == comp_inp:
        data[0] = str(input())
        variable[0] = stat_inp[6:len(stat_inp)]
    else:
        err = 1



def for_statement(stat_for):
    temp_variable = ""
    comp_for  = "for "
    found_sym = False
    if stat_for[0:4] == comp_for:                     
        count = 4
        while count < len(stat_for) and stat_for[count] != "(":
            if stat_for[count] == "(":
                index = count
                found_sym = True
            count += 1
        if count < len(stat_for):
            err = 0
        if found_sym:
            var = stat_for[4:index]
            if var in variable:
                pos = variable.index(var)
                temp_data = data(pos)
            else:
                temp_variable = var
            counter = 6
            while counter < len(stat_for) and stat_for[counter] != ",":
                if stat_for[counter] == ",":
                    loc = counter
                counter += 1
            if counter < len(stat_for):
                err = 0
            num1 = int(stat_for[6:loc])
            num2 = int(stat_for[loc:len(stat_for)])
            return [num1, num2];
        return "error"
    
stat_for = str(input()) 
stat_pr = str(input())
numbers = for_statement(stat_for)
if numbers != "error":
    for z in range(numbers[0], numbers[1] + 1):
        for_statement(stat_pr)