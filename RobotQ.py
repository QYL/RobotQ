#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
#============================================================================
#
#     FileName: RobotQ.py
#
#      Author: Le.py
#
#      Created: 2012-5-15 21:21:55
#      Version: 1.0.0
#                                                                            
#============================================================================
'''
status = True #initialize，if False then quit
do = -1 
dovalue = True
print''' -*-*-*-*-*-*-*-*-*- I Am RobotQ -*-*-*-*--*-*-*-*-*-

 
                                     
              ** A Production of Le.py **
              
                                                                 
                                                         
-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
'''
while status:

    import os
    if not os.path.exists("C:/question"):
              
        os.mkdir("C:/question")   
            
    def teach(question,answer):
        conPath0 = 'C:/question'
        conPath1 = '/'
        conPath2 = question.lower()+'.txt'
        conPath = conPath0+conPath1+conPath2
        if not os.path.exists(conPath):
            file = open(conPath,'w')  
            file.write(answer)
            file.close()
        else:
            print'The question already exists,do you want to continue?'
            print'''
            1.Yes,let's do it!
            2.No.
    '''
            do = raw_input()
            if int(do) == 1:
                global dovalue
                file = open(conPath,'w')  
                file.write(answer)
                file.close()
                dovalue = True
            elif int(do) == 2:
                dovalue = False
               
    def talk(question):  
        conPath0 = 'C:/question'
        conPath1 = '/'
        conPath2 = question+'.txt'
        conPath = conPath0 + conPath1 + conPath2
        try:
                 os.path.exists(conPath) #Check whether question exists
                 file = open(conPath,'r')
                 for ans in file:
                     print 'QRobot: %s' %ans
                     print''' '''
                     print'''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''
                                                               
                                                  
        except:
                print"I have no idea."
                
    print ''' '''  

    print'''                1.Teach                            
                2.Talk
                3.Quit
         '''
    select = raw_input('Pleaes select a number to continue:')

    
    if int(select) == 1:
        question = raw_input('Question:')
        answer = raw_input('Answer:')
        
        teach(question,answer)
        
        if dovalue == True:
            print('Thank you, dude.')
        elif dovalue == False:
            print('Thank all the same.')
        print('''

''')
    elif int(select) == 2:
        print'''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''
        print''' '''
        question = raw_input('You say:')
        talk(question.lower())
        print'''
'''
 
    elif int(select) == 3:
        status = False
    else:
        print'Sorry to disappoint you, I can not do it.'
