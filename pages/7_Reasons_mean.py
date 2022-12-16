import streamlit as st
from main_page import data_set
import matplotlib.pyplot as plt
import numpy as np


arr=data_set.groupby(['Reason for absence'])['Absenteeism time in hours'].count()
arr=np.array(arr)

fig, ax = plt.subplots(figsize=(8,8))


table=[
    'No Reason given','Certain infectious and parasitic diseases', 
'Neoplasms', 
'blood-forming organs and involving the immune mechanism', 
'Endocrine, nutritional and metabolic diseases', 
'Mental and behavioural disorders', 
'Diseases of the nervous system', 
'Diseases of the eye and adnexa', 
'Diseases of the ear and mastoid process', 
'Diseases of the circulatory system', 
'Diseases of the respiratory system', 
'Diseases of the digestive system', 
'Diseases of the skin and subcutaneous tissue', 
'Diseases of the musculoskeletal system and connective tissue', 
'Diseases of the genitourinary system',
'Pregnancy, childbirth and the puerperium',
'Certain conditions originating in the perinatal period',
'Congenital malformations, deformations and chromosomal abnormalities', 
'Symptoms, signs and abnormal clinical and laboratory findings', 
'Injury, poisoning and certain other consequences of external causes', 
'Factors influencing health status and contact with health services.',
'patient follow-up',
'medical consultation',
'blood donation',
'laboratory examination',
'unjustified absence',
'physiotherapy',
'dental consultation']
plt.barh(y=np.arange(len(arr)),width=arr,label='No. of employee',color='#00C6C5')
plt.yticks(np.arange(len(arr)),table,rotation=0)
plt.ylabel('Reason of Absence')
plt.xlabel('Count of employee')
plt.title('Reason vs Freq',fontweight='bold')
plt.legend()

for i, v in enumerate(arr):
    ax.text(v+2, i, str(v), color='black',fontweight='bold')

st.pyplot(fig)