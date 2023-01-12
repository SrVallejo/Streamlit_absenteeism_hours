import streamlit as st
import pickle
import datetime
import pandas as pd
from Main_Page import data_set_prediction, reasons_list, education_list
from sklearn.preprocessing import StandardScaler

st.markdown("# Prediction")
st.sidebar.markdown("# Prediction")
form = st.empty()
results = st.empty()


def clustering(height, weight, service_time, hit_target, transportation_expense, 
    work_load, pets, social_smoker, age):
    pass
    #return numero de cluster

#function to get actual season and translate to dataset code (1=winter,2=summer,3=fall,4=spring)
def get_season():
    # get the current day of the year
    doy = datetime.datetime.today().timetuple().tm_yday

    # "day of year" ranges for the northern hemisphere
    spring = range(80, 172)
    summer = range(172, 264)
    fall = range(264, 355)
    # winter = everything else

    if doy in spring:
        season = 4
    elif doy in summer:
        season = 2
    elif doy in fall:
        season = 3
    else:
        season = 1

    return season

#function that process the form to predict and update database with new row
def process_form(education, reason, disciplinary_failure,age, bodyMassIndex,social_drinker,
                social_smoker, sons, pets,distance, service_time, id, height, weight,
                trans_expense, work_load, hit_target):

    #hide the form once the button predict is clicked
    form.empty()

    #clustering function
    clustering(height, weight, service_time, hit_target, trans_expense, 
    work_load, pets, social_smoker, age)


    #### Prediction 

    #create the new row with all the fields for prediction
    x_row = data_set_prediction.head(0)
    
    #Fill the dataset with the data from the form
    #Reason
    x_row.at[0,'Reason for absence'] = reasons_list.index(reason)
    #Day of the week +2 because monday is 2 in dataset, and 0 in weekday function
    x_row.at[0,'Day of the week'] = datetime.datetime.today().weekday()+2 
    #seasons
    season_num = get_season()
    if season_num != 1:
        x_row.at[0,'Seasons_'+str(season_num)] = 1

    
    #transportation expense (substitute by mean)
    x_row.at[0,"Transportation expense"] = trans_expense

    #distance from residence
    if distance < 20: pass
    elif distance < 40: x_row.at[0,"Distance from Residence to Work_mid"] = 1
    else: x_row.at[0,"Distance from Residence to Work_far"] = 1

    #age
    if age < 35: x_row.at[0,"Age_young"] = 1
    elif age >= 45: x_row.at[0,"Age_old"] = 1
    
    #work load (substitute by mean)
    x_row.at[0,"Work load Average/day "] = work_load

    #hit target (substitute by mean)
    x_row.at[0,"Hit target"] = hit_target

    #Disciplinary failure
    x_row.at[0,"Disciplinary failure"] = int(disciplinary_failure)

    #education
    if education != "High school": x_row.at[0,"Education_University"] = 1
    
    #sons
    #the model work with dummies for sons from 0 to 4, so we have to group 4 or more kids in the same column
    if sons > 4: sons = 4
    if sons!= 0: x_row.at[0,"Son_"+str(sons)] = 1

    #social drinker
    x_row.at[0,"Social drinker"] = int(social_drinker)
    #social smoker
    x_row.at[0,"Social smoker"] = int(social_smoker)

    #pet
    if pets == 0: x_row.at[0,"Pet_no"] = 1
    elif pets <= 2: x_row.at[0,"Pet_few"] = 1

    #body mass index
    x_row.at[0, "Body mass index"] = bodyMassIndex

    #Fill the rest of the fields with 0
    x_row = x_row.fillna(0)

    x_row = x_row.drop(["Absenteeism time in hours", "Group Hours"], axis = 1)
    
    #scaling
    # scaler = StandardScaler()
    # scaler.fit_transform(x_row)

    #load model from pickle

    file_path = 'pickle/classifier_Lightgbm.pkl'
    pickled_model = pickle.load(open(file_path, 'rb'))



    #prediction model
    prediction = pickled_model.predict(x_row)

    with results.container():
        st.write(x_row)
        st.write(prediction)

    
    


    


def buildform():
    #all inside a container to hide it when we click on predict.
    with form.container():
        #ID
        id = st.number_input("Employee ID", min_value=0)
        #Reason
        reason = st.selectbox("Reason for absence", reasons_list)
        #Disciplinary failure checkbox
        disciplinary_failure = st.checkbox("Disciplinary Failure")
        #Age
        age = st.slider ("Age",min_value=16,max_value=70)
        #Service time
        service_time = st.slider("Service time (in years)", min_value=0,max_value =70)
        #EDUCATION
        education_opts = ["High school","Graduate","Postgraduate","Master and doctor"]
        education = st.radio("Education", education_opts)
        #Height
        height = st.slider("Height (in cm's)", min_value=100, max_value=250)
        #weight
        weight = st.slider("Weight (in kgm's)", min_value=20, max_value=200)
        #Body weight mass
        bodyMassIndex = st.slider("Body Mass Index",min_value = 10, max_value = 50)
        #Social drinker
        social_drinker = st.checkbox("Social Drinker")
        #Social Smoker
        social_smoker = st.checkbox("Social Smoker")
        #SONS
        sons = st.number_input("Number of sons", min_value=0)
        #PETS
        pets = st.number_input("Number of pets", min_value=0)
        #Distance
        distance = st.slider("Distance from residence to work", min_value=0, max_value = 70)
        #Transportation expense
        trans_expense = st.slider("Transportation expense", min_value=100, max_value=400)
        #work load average day
        work_load = st.slider("Work load (Average/Day)", min_value=200, max_value=400)
        #hit target
        hit_target = st.slider("Hit target", min_value=0, max_value=100)


        if st.button(label= "Predict"):
            process_form(education, reason, disciplinary_failure,age, bodyMassIndex,social_drinker,
                social_smoker, sons, pets,distance, service_time, id, height, weight,
                trans_expense, work_load, hit_target)



#Get date from today (season and day of the week)


buildform()
