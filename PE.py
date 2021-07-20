#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import PySimpleGUI as sg
import pyodbc
import pandas as pd
conn=pyodbc.connect(r'DRIVER={NetezzaSQL};SERVER=SRVDWHITP04;DATABASE=EDW_SPOKE;UID=akaul;PWD=California@1234;TIMEOUT=0')
crsr=conn.cursor()
layout=[
    [sg.Radio('Subclass', "RADIO1", default=True, key="r1")],
    [sg.Radio('Class', "RADIO1", default=False, key="r2")],
    [sg.Radio('Subdept', "RADIO1", default=False, key="r3")],
    [sg.Text("Enter Subdept",size=(12,0)),sg.Text("Enter Class",size=(12,0)),sg.Text("Enter Subclass")],
#     [sg.Checkbox('', default=True, key="-IN-")],
    
    [sg.InputText(key='input1',size=(14,0)),sg.InputText(key='input2',size=(14,0)),sg.InputText(key='input3',size=(14,0))],
    [sg.Button('Generate',#button_color=sg.TRANSPARENT_BUTTON
              )],
    [sg.Output(size=(50,0),
        key='output1')]
]

window = sg.Window('Price Elasticity', layout,default_element_size=(12, 1),resizable=True)

while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    elif event == 'Generate':
        window['output1'].update(value='')
        try:
#             #SKU
#             r=crsr.execute("""select * from ba_prod..summary_el where sku_display_number = ? """,values['input1']).fetchall()
#             df = pd.DataFrame.from_records(r, columns=[x[0] for x in crsr.description])
#             if df.loc[0,'EL_GLS'] < 1:
#                 print(df.loc[0,'EL_GLS'])
#             else:
#                 print('Insignificant or Invalid Data')
# #             print(values['input1'])
            
            if values['r1']==True:
                #SUBCLASS
                sc=values['input1']+values['input2']+values['input3']
                r=crsr.execute("""select * from ba_prod..subclass_el where sku_style = ? """,sc).fetchall()
                df = pd.DataFrame.from_records(r, columns=[x[0] for x in crsr.description])
                if df.loc[0,'ELASTICITY_GLS'] < 1:
                    print(df.loc[0,'ELASTICITY_GLS'])
                else:
                    print('Insignificant or Invalid Data')
                
            elif values['r2']==True:
                #CLASS
                cl=values['input1']+values['input2']
                r=crsr.execute("""select * from ba_prod..class_el where sku_style = ? """,cl).fetchall()
                df = pd.DataFrame.from_records(r, columns=[x[0] for x in crsr.description])
                if df.loc[0,'ELASTICITY_GLS'] < 1:
                    print(df.loc[0,'ELASTICITY_GLS'])
                else:
                    print('Insignificant or Invalid Data')
                
            elif values['r3']==True:
                #SUBDEPT
                sd=values['input1']
                r=crsr.execute("""select * from ba_prod..subdept_el where sku_style = ? """,sd).fetchall()
                df = pd.DataFrame.from_records(r, columns=[x[0] for x in crsr.description])
                if df.loc[0,'ELASTICITY_GLS'] < 1:
                    print(df.loc[0,'ELASTICITY_GLS'])
                else:
                    print('Insignificant or Invalid Data')
        except:
            print('Invalid Data')

window.close()

