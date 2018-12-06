#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 21:38:31 2018

@author: vmpe
"""

#Converter from  sdl to dlc

#Return a .dlc file from a .sdl file

############ File to convert
name_file = input()
path = '{0}.sdl'.format(name_file)

######################### SEND TO HELL #########################################
##### Esta función sirve para sacar el número N del action parameter de RAND
def take_number(a):
    
    if len(a) == 4:
        snum = '{}{}'.format(a[1],a[2])
        return int(snum)

    else:
        return int(a[1])
############################## send to hell ####################################


# States dictionary, first variable in state 
types_states = { 'MOVE':8, 'SPIN':9, 'SETT':'A','DELT':'B', 'RAND':'C', 'LOOK':'D', 'WAIT':'E'}
# Parameters dictionary, given the word return the number to convert
action_parameters = {'RIGHT': 1, 'BACK':2, 'LEFT':3, 'EMPTY':0, 'OBSTACLE':1, 'DOCK':2, 
                    'DROID':3, 'N':'n-1', 'LABEL1':{'T': 0, 'L':4}, 'LABEL2':{'T': 1, 'L':5},
                    'LABEL3':{'T': 2, 'L':6}, 'LABEL4':{'T': 3, 'L':7}, '-':0}

super_list = []
list_line = []
super_list1 = []

list_line1 = [] # State types list.
success = []
fails = []
action = []


########### Open the file and make a list
########### with all the lines
with open(path, 'r') as sdl_file:
    
    for line in sdl_file:
        list_line = line.split()
        super_list.append(list_line)
        
        
############# Get the number of the state type and put it
############# in a list. 
for i in range(len(super_list)):
    list_line1.append(types_states.get(super_list[i][0]))
    

########### Second column: Take second number and convert to
########### hexadecimal with three digits
for i in range(len(super_list)):
    #if super_list[i][1] == '-':
    #    super_list[i][1] = 0
    hexa_simple = format(int(super_list[i][1]), 'x').upper()
    if len(hexa_simple) == 1:
        hexa_final = '00{0}'.format(hexa_simple)
    if len(hexa_simple) == 2:
        hexa_final = '0{0}'.format(hexa_simple)
    if len(hexa_simple) == 3:
        hexa_final = '{0}'.format(hexa_simple)

    success.append(hexa_final)

########## Third column: 
for i in range(len(super_list)):
    if super_list[i][2] == '-':
        super_list[i][2] = 0
    fails.append(format(int(super_list[i][2]), 'x').upper())
#print(fails) 


############# ACTION PARAMETERS
##TAG1
for i in range(len(super_list)):
    if super_list[i][3] == 'LABEL1':
        if super_list[i][0] == 'LOOK':
            action.append(action_parameters.get('LABEL1').get('L'))
        else:
            action.append(action_parameters.get('LABEL1').get('T'))

##TAG2
    elif super_list[i][3] == 'LABEL2':
        if super_list[i][0] == 'LOOK':
            action.append(action_parameters.get('LABEL2').get('L'))
        else:
            action.append(action_parameters.get('LABEL2').get('T'))
    
##TAG3
    elif super_list[i][3] == 'LABEL3':
        if super_list[i][0] == 'LOOK':
            action.append(action_parameters.get('LABEL3').get('L'))
        else:
            action.append(action_parameters.get('LABEL3').get('T'))  
        
##TAG4
    elif super_list[i][3] == 'LABEL4':
        if super_list[i][0] == 'LOOK':
            action.append(action_parameters.get('LABEL4').get('L'))
        else:
            action.append(action_parameters.get('LABEL4').get('T'))
            
#    elif super_list[i][3].startswith('['):
#    num = take_number(super_list[i][3])
#        action.append(format(num - 1, 'x').upper())
    elif super_list[i][0] == 'RAND':
        
        action.append(format(int(super_list[i][3]) - 1, 'x').upper())
        
    
    else:
        action.append(action_parameters.get(super_list[i][3]))
        
print(action)
    
        
#        print(list_line)
    

    
#    linea = sdl_file.readline()
#    list_line = linea.split()
#    tipo, success, fail, parameter = list_line  