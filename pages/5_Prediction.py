import streamlit as st
import pickle
import datetime
from Main_Page import data_set, reasons_list

st.markdown("# Prediction")
st.sidebar.markdown("# Prediction")
form = st.empty()

#reason, Day of the week, seasons, transportation expense, distance from residence, Age, Work load, Hit target
#disciplinary failure, education, son, social drinker, social smoker, pet, body mass index,  

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

def predict(education, reason, disciplinary_failure,age, bodyMassIndex,social_drinker,social_smoker, sons, pets):
    form.empty()
    #create the new row

    new_row = []
    #Reason
    new_row.append(reasons_list.index(reason))
    #Day of the week +2 because monday is 2 in dataset, and 0 in weekday function
    new_row.append(datetime.datetime.today().weekday()+2)
    #seasons
    new_row.append(get_season())
    form.write(new_row)

def buildform():
    with form.container():
        #EDUCATION
        education_opts = ["High school","Graduate","Postgraduate","Master and doctor"]
        education = st.radio("Education", education_opts)
        #Reason
        reason = st.selectbox("Reason for absence", reasons_list)
        #Distance?

        #Expense?
        #Disciplinary failure checkbox
        disciplinary_failure = st.checkbox("Disciplinary Failure")
        #Age
        age = st.slider ("Age",min_value=16,max_value=70)
        #Body weight mass
        bodyMassIndex = st.slider("Body Mass Index",min_value = 10, max_value = 50)
        #Social drinker
        social_drinker = st.checkbox("Social Drinker")
        #Social Smoker
        social_smoker = st.checkbox("Social Smoker")
        #SONS
        sons = st.number_input("Number of sons")
        #PETS
        pets = st.number_input("Number of pets")


        if st.button(label= "Predict"):
            predict(education, reason, disciplinary_failure,age, bodyMassIndex,social_drinker,social_smoker, sons, pets)



#Get date from today (season and day of the week)


buildform()




#pickled_model = pickle.load(open('model.pkl', 'rb'))
file_path = 'pickle\classifier_Gradient Boosting.pkl'
pickled_model = pickle.load(open(file_path, 'rb'))