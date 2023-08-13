import numpy as np
import pickle 
import streamlit as st
loaded_model = pickle.load(open('mh.pkl', 'rb'))
sc = pickle.load(open('sc.pkl', 'rb'))
st.title('Mental Health Prediction')


Age = st.number_input("Age")

self_employed = st.selectbox("Self Employed", ("Yes", "No"))

if self_employed == "Yes":
    self_employed = 1
else:
    self_employed = 0

family_history = st.selectbox("Family History", ("Yes", "No"))

if family_history == "Yes":
    family_history = 1
else:
    family_history = 0

remote_work = st.selectbox("Remote Work", ("Yes", "No"))

if remote_work == "Yes":
    remote_work = 1
else:
    remote_work = 0

tech_company = st.selectbox("Tech Company", ("Yes", "No"))

if tech_company == "Yes":
    tech_company = 1
else:
    tech_company = 0

obs_consequence = st.selectbox("Obs Consequence", ("Yes", "No"))

if obs_consequence == "Yes":
    obs_consequence = 1
else:
    obs_consequence = 0

Gender = st.selectbox("Gender",("Male","Female","Trans","Male leaning androgynous","unsure what your really means"))

if Gender =="Male":
    Gender_male = 1
    Gender_female = 0
    Gender_Trans = 0
    Gender_male_leaning_androgynous = 0
    unsure_what_that_really_means = 0
elif Gender == "Female":
    Gender_male = 0
    Gender_female = 1
    Gender_Trans = 0
    Gender_male_leaning_androgynous = 0
    unsure_what_that_really_means = 0
elif Gender == "Trans":
    Gender_male = 0
    Gender_female = 0
    Gender_Trans = 1
    Gender_male_leaning_androgynous = 0
    unsure_what_that_really_means = 0
elif Gender == "Male leaning androgynous":
    Gender_male = 0
    Gender_female = 0
    Gender_Trans = 0
    Gender_male_leaning_androgynous = 1
    unsure_what_that_really_means = 0
elif Gender == "unsure what your really means":
    Gender_male = 0
    Gender_female = 0
    Gender_Trans = 0
    Gender_male_leaning_androgynous = 0
    unsure_what_that_really_means = 1

work_interfere = st.selectbox("Work Interfere", ('N/A', 'Never', 'Often', 'Rarely', 'Sometimes'))

if work_interfere == 'N/A':
    work_interfere_N_A = 1
    work_interfere_Never = 0
    work_interfere_Often = 0
    work_interfere_Rarely = 0
    work_interfere_Sometimes = 0
elif work_interfere == 'Never':
    work_interfere_N_A = 0
    work_interfere_Never = 1
    work_interfere_Often = 0
    work_interfere_Rarely = 0
    work_interfere_Sometimes = 0
elif work_interfere == 'Often':
    work_interfere_N_A = 0
    work_interfere_Never = 0
    work_interfere_Often = 1
    work_interfere_Rarely = 0
    work_interfere_Sometimes = 0
elif work_interfere == 'Rarely':
    work_interfere_N_A = 0
    work_interfere_Never = 0
    work_interfere_Often = 0
    work_interfere_Rarely = 1
    work_interfere_Sometimes = 0
elif work_interfere == 'Sometimes':
    work_interfere_N_A = 0
    work_interfere_Never = 0
    work_interfere_Often = 0
    work_interfere_Rarely = 0
    work_interfere_Sometimes = 1

no_employees = st.selectbox("No. Employees", ('1-5','6-25','26-100','100-500', '500-1000', 'More than 1000'))
if no_employees=='1-5':
	no_employees_1_5 =1
	no_employees_100_500 = 0
	no_employees_26_100 = 0
	no_employees_500_1000 = 0
	no_employees_6_25 = 0
	no_employees_More_than_1000 = 0
elif no_employees=='100-500':
	no_employees_1_5 =0
	no_employees_100_500 = 1
	no_employees_26_100 = 0
	no_employees_500_1000 = 0
	no_employees_6_25 = 0
	no_employees_More_than_1000 = 0
elif no_employees== '26-100':
	no_employees_1_5 =0
	no_employees_100_500 = 0
	no_employees_26_100 = 1
	no_employees_500_1000 = 0
	no_employees_6_25 = 0
	no_employees_More_than_1000 = 0
elif no_employees== '500-1000':
	no_employees_1_5 =0
	no_employees_100_500 = 0
	no_employees_26_100 = 0
	no_employees_500_1000 = 1
	no_employees_6_25 = 0
	no_employees_More_than_1000 = 0
elif no_employees== '6-25':
	no_employees_1_5 =0
	no_employees_100_500 = 0
	no_employees_26_100 = 0
	no_employees_500_1000 = 0
	no_employees_6_25 = 1
	no_employees_More_than_1000 = 0
elif no_employees== 'More than 1000':
	no_employees_1_5 =0
	no_employees_100_500 = 0
	no_employees_26_100 = 0
	no_employees_500_1000 = 0
	no_employees_6_25 = 0
	no_employees_More_than_1000 = 1
benefits = st.selectbox("Benefits",('Yes','No',"Don't know" ))

if benefits == "Don't know":
    benefits_Dont_know = 1
    benefits_No = 0
    benefits_Yes = 0
elif benefits == 'No':
    benefits_Dont_know = 0
    benefits_No = 1
    benefits_Yes = 0
elif benefits == 'Yes':
    benefits_Dont_know = 0
    benefits_No = 0
    benefits_Yes = 1

care_options = st.selectbox("Care Options",('Yes','No','Not sure'))

if care_options == 'No':
    care_options_No = 1
    care_options_Not_sure = 0
    care_options_Yes = 0
elif care_options == 'Not sure':
    care_options_No = 0
    care_options_Not_sure = 1
    care_options_Yes = 0
elif care_options == 'Yes':
    care_options_No = 0
    care_options_Not_sure = 0
    care_options_Yes = 1
    


wellness_program = st.selectbox("Wellness Program", ('Yes','No',"Don't know"))

if wellness_program == "Don't know":
    wellness_program_Dont_know = 1
    wellness_program_No = 0
    wellness_program_Yes = 0
elif wellness_program == 'No':
    wellness_program_Dont_know = 0
    wellness_program_No = 1
    wellness_program_Yes = 0
elif wellness_program == 'Yes':
    wellness_program_Dont_know = 0
    wellness_program_No = 0
    wellness_program_Yes = 1


seek_help = st.selectbox("Seek Help",('Yes','No',"Don't know"))

if seek_help == "Don't know":
    seek_help_Dont_know = 1
    seek_help_No = 0
    seek_help_Yes = 0
elif seek_help == 'No':
    seek_help_Dont_know = 0
    seek_help_No = 1
    seek_help_Yes = 0
elif seek_help == 'Yes':
    seek_help_Dont_know = 0
    seek_help_No = 0
    seek_help_Yes = 1

anonymity = st.selectbox("Anonymity",('Yes','No',"Don't know"))

if anonymity == "Don't know":
    anonymity_Dont_know = 1
    anonymity_No = 0
    anonymity_Yes = 0
elif anonymity == 'No':
    anonymity_Dont_know = 0
    anonymity_No = 1
    anonymity_Yes = 0
elif anonymity == 'Yes':
    anonymity_Dont_know = 0
    anonymity_No = 0
    anonymity_Yes = 1

leave = st.selectbox("Leave",( 'Very easy','Very difficult','Somewhat easy','Somewhat difficult',"Don't know", ))

if leave == "Don't know":
    leave_Dont_know = 1
    leave_Somewhat_difficult = 0
    leave_Somewhat_easy = 0
    leave_Very_difficult = 0
    leave_Very_easy = 0
elif leave == 'Somewhat difficult':
    leave_Dont_know = 0
    leave_Somewhat_difficult = 1
    leave_Somewhat_easy = 0
    leave_Very_difficult = 0
    leave_Very_easy = 0
elif leave == 'Somewhat easy':
    leave_Dont_know = 0
    leave_Somewhat_difficult = 0
    leave_Somewhat_easy = 1
    leave_Very_difficult = 0
    leave_Very_easy = 0
elif leave == 'Very difficult':
    leave_Dont_know = 0
    leave_Somewhat_difficult = 0
    leave_Somewhat_easy = 0
    leave_Very_difficult = 1
    leave_Very_easy = 0
elif leave == 'Very easy':
    leave_Dont_know = 0
    leave_Somewhat_difficult = 0
    leave_Somewhat_easy = 0
    leave_Very_difficult = 0
    leave_Very_easy = 1



mental_health_consequence = st.selectbox("Mental Health Consequence",('Yes','No','Maybe'))

if mental_health_consequence == 'Maybe':
    mental_health_consequence_Maybe = 1
    mental_health_consequence_No = 0
    mental_health_consequence_Yes = 0
elif mental_health_consequence == 'No':
    mental_health_consequence_Maybe = 0
    mental_health_consequence_No = 1
    mental_health_consequence_Yes = 0
elif mental_health_consequence == 'Yes':
    mental_health_consequence_Maybe = 0
    mental_health_consequence_No = 0
    mental_health_consequence_Yes = 1

phys_health_consequence = st.selectbox("Phys Health Consequence",('Yes','No','Maybe'))

if phys_health_consequence == 'Maybe':
    phys_health_consequence_Maybe = 1
    phys_health_consequence_No = 0
    phys_health_consequence_Yes = 0
elif phys_health_consequence == 'No':
    phys_health_consequence_Maybe = 0
    phys_health_consequence_No = 1
    phys_health_consequence_Yes = 0
elif phys_health_consequence == 'Yes':
    phys_health_consequence_Maybe = 0
    phys_health_consequence_No = 0
    phys_health_consequence_Yes = 1

coworkers = st.selectbox("Coworkers",('Yes','No','Some of them'))

if coworkers == 'No':
    coworkers_No = 1
    coworkers_Some_of_them = 0
    coworkers_Yes = 0
elif coworkers == 'Some of them':
    coworkers_No = 0
    coworkers_Some_of_them = 1
    coworkers_Yes = 0
elif coworkers == 'Yes':
    coworkers_No = 0
    coworkers_Some_of_them = 0
    coworkers_Yes = 1

supervisor = st.selectbox("Supervisor",('Yes','No','Some of them'))

if supervisor == 'No':
    supervisor_No = 1
    supervisor_Some_of_them = 0
    supervisor_Yes = 0
elif supervisor == 'Some of them':
    supervisor_No = 0
    supervisor_Some_of_them = 1
    supervisor_Yes = 0
elif supervisor == 'Yes':
    supervisor_No = 0
    supervisor_Some_of_them = 0
    supervisor_Yes = 1

mental_health_interview = st.selectbox("Mental Health Interview",('Yes','No','Maybe'))

if mental_health_interview == 'Maybe':
    mental_health_interview_Maybe = 1
    mental_health_interview_No = 0
    mental_health_interview_Yes = 0
elif mental_health_interview == 'No':
    mental_health_interview_Maybe = 0
    mental_health_interview_No = 1
    mental_health_interview_Yes = 0
elif mental_health_interview == 'Yes':
    mental_health_interview_Maybe = 0
    mental_health_interview_No = 0
    mental_health_interview_Yes = 1

phys_health_interview = st.selectbox("Physical Health Interview",('Yes','No','Maybe'))

if phys_health_interview == 'Maybe':
    phys_health_interview_Maybe = 1
    phys_health_interview_No = 0
    phys_health_interview_Yes = 0
elif phys_health_interview == 'No':
    phys_health_interview_Maybe = 0
    phys_health_interview_No = 1
    phys_health_interview_Yes = 0
elif phys_health_interview == 'Yes':
    phys_health_interview_Maybe = 0
    phys_health_interview_No = 0
    phys_health_interview_Yes = 1

mental_vs_physical = st.selectbox("Mental vs Physical",('Yes','No',"Don't know"))

if mental_vs_physical == "Don't know":
    mental_vs_physical_Dont_know = 1
    mental_vs_physical_No = 0
    mental_vs_physical_Yes = 0
elif mental_vs_physical == 'No':
    mental_vs_physical_Dont_know = 0
    mental_vs_physical_No = 1
    mental_vs_physical_Yes = 0
elif mental_vs_physical == 'Yes':
    mental_vs_physical_Dont_know = 0
    mental_vs_physical_No = 0
    mental_vs_physical_Yes = 1


if st.button('Test Results'):
	classifier = loaded_model.predict(sc.transform([[Age, self_employed, family_history, remote_work, tech_company, obs_consequence, Gender_male, Gender_female, Gender_Trans, Gender_male_leaning_androgynous, unsure_what_that_really_means, work_interfere_N_A, work_interfere_Never, work_interfere_Often, work_interfere_Rarely, work_interfere_Sometimes, no_employees_1_5, no_employees_6_25, no_employees_26_100, no_employees_100_500, no_employees_500_1000, no_employees_More_than_1000, benefits_Dont_know, benefits_No, benefits_Yes, care_options_No, care_options_Not_sure, care_options_Yes, wellness_program_Dont_know, wellness_program_No, wellness_program_Yes, seek_help_Dont_know, seek_help_No, seek_help_Yes, anonymity_Dont_know, anonymity_No, anonymity_Yes, leave_Dont_know, leave_Somewhat_difficult, leave_Somewhat_easy, leave_Very_difficult, leave_Very_easy, mental_health_consequence_Maybe, mental_health_consequence_No, mental_health_consequence_Yes, phys_health_consequence_Maybe, phys_health_consequence_No, phys_health_consequence_Yes, coworkers_No, coworkers_Some_of_them, coworkers_Yes, supervisor_No, supervisor_Some_of_them, supervisor_Yes, mental_health_interview_Maybe, mental_health_interview_No, mental_health_interview_Yes, phys_health_interview_Maybe, phys_health_interview_No, phys_health_interview_Yes, mental_vs_physical_Dont_know, mental_vs_physical_No, mental_vs_physical_Yes]]))

	if classifier == 0:
		st.write("<span style='font-size: 30px;'>SAFE!</span>", unsafe_allow_html=True)
		st.write("<span style='font-size: 30px;'>THE PERSON IS NOT AFFECTED BY MENTAL HEALTH</span>", unsafe_allow_html=True)
	else:
		st.write("<span style='font-size: 30px;'>UNSAFE!</span>", unsafe_allow_html=True)
		st.write("<span style='font-size: 30px;'>THE PERSON IS AFFECTED BY MENTAL HEALTH</span>", unsafe_allow_html=True)	

st.write("NOTE: This is only for Educational Purpose")
st.write("<span style='font-size: 15px;'>Founder: *Santhosh Reddy Padala*</span>", unsafe_allow_html=True)


