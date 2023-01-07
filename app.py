
import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image


# Loading up the Classification model we created
model = pickle.load(open('job_posting.pkl','rb'))



#Creating Front end of application
app_mode = st.sidebar.radio('Select Page',['Home','Prediction'])   #two pages

if app_mode=='Home':

    html_temp = """
      <div style='background-color: teal; padding:10px'>
      <h2 style='color:white; text-align:center;'>Job Posting Classifier: </h2>
      <h3 style='color:white; text-align:center;'>Real/Fake </h3>
      </div>"""

    st.markdown(html_temp, unsafe_allow_html=True)
    # st.title("Job Posting Classifier: Real/Fake")
    st.image("""https://imagevars.gulfnews.com/2020/09/07/Fake-job-offer_1746917114d_original-ratio.jpg""")


elif app_mode == 'Prediction':

    def add_bg_from_url():
        st.markdown(
            f"""
             <style>
             .stApp {{
                 background-image: url("https://res.cloudinary.com/jerrick/image/upload/c_scale,q_auto/5e68f566ddce58001c542e16.jpg");
                 background-attachment: fixed;
                 background-size: cover
             }}
             </style>
             """,
            unsafe_allow_html=True
        )

    add_bg_from_url()


    st.title('Job Posting Classifier: Real/Fake')
    st.markdown("For predicting if job posting is real/fake please enter the details.")
    st.subheader('Enter the details:')



    telecommuting = st.radio('Is work from home or remote work allowed?', options= ['Yes', 'No'])
    if telecommuting == 'Yes':
        telecommuting = 1
    else:
        telecommuting = 0

    has_company_logo = st.radio('Does the job posting have a company logo?', options= ['Yes', 'No'])
    if has_company_logo == 'Yes':
        has_company_logo = 1
    else:
        has_company_logo = 0

    has_questions = st.radio('Does the job posting have questions?', options= ['Yes', 'No'])
    if has_questions == 'Yes':
        has_questions = 1
    else:
        has_questions = 0


    employment_type = st.selectbox('What is the employment type?',
                                   ('Not Specified', 'Other', 'Part-time', 'Contract','Temporary','Full-time'))
    # Set dummy variables to zero
    employment_type_Not_Specified, employment_type_Other = 0,0
    employment_type_Part_time, employment_type_Contract  = 0,0
    employment_type_Temporary, employment_type_Full_time = 0,0


    if employment_type == 'Not Specified':
        employment_type_Not_Specified = 1
    elif employment_type == 'Other':
        employment_type_Other = 1
    elif employment_type == 'Part-time':
        employment_type_Part_time = 1
    elif employment_type == 'Contract':
        employment_type_Contract = 1
    elif employment_type == 'Temporary':
        employment_type_Temporary = 1
    elif employment_type == 'Full-time':
        employment_type_Full_time = 1




    required_experience = st.selectbox('What is the required experience?',
                                       ('Not Applicable', 'Internship', 'Entry level', 'Mid-Senior level',
                                        'Associate',  'Executive', 'Director'))

    required_experience_Not_Applicable = 0
    required_experience_Internship, required_experience_Entry_level  = 0, 0
    required_experience_Mid_Senior_level, required_experience_Associate = 0, 0
    required_experience_Executive, required_experience_Director  = 0, 0



    if required_experience == 'Not Applicable':
        required_experience_Not_Applicable = 1
    elif required_experience == 'Internship':
        required_experience_Internship = 1
    elif required_experience == 'Entry level':
        required_experience_Entry_level = 1
    elif required_experience == 'Mid-Senior level':
        required_experience_Mid_Senior_level = 1
    elif required_experience == 'Associate':
        required_experience_Associate = 1
    elif required_experience == 'Executive':
        required_experience_Executive = 1
    elif required_experience == 'Director':
        required_experience_Director = 1


    required_education = st.selectbox('What is the required education?',
                                      ('Unspecified', 'Vocational - HS Diploma', 'Some High School Coursework', 'High School or equivalent',
                                        'Some College Coursework Completed', 'Certification', 'Vocational', 'Vocational - Degree', "Bachelor's Degree",
                                        "Master's Degree", 'Associate Degree', 'Professional', 'Doctorate'))

    required_education_Unspecified, required_education_Vocational___HS_Diploma = 0, 0
    required_education_Some_High_School_Coursework, required_education_High_School_or_equivalent  = 0, 0
    required_education_Some_College_Coursework_Completed, required_education_Certification = 0, 0
    required_education_Bachelor_s_Degree, required_education_Master_s_Degree  = 0, 0
    required_education_Vocational, required_education_Vocational___Degree = 0, 0
    required_education_Associate_Degree , required_education_Professional  = 0, 0
    required_education_Doctorate = 0


    if required_education == 'Unspecified':
        required_education_Unspecified = 1
    elif required_education == 'Vocational - HS Diploma':
        required_education_Vocational___HS_Diploma = 1
    elif required_education == 'Some High School Coursework':
        required_education_Some_High_School_Coursework = 1
    elif required_education == 'High School or equivalent':
        required_education_High_School_or_equivalent = 1
    elif required_education == 'Some College Coursework Completed':
        required_education_Some_College_Coursework_Completed = 1
    elif required_education == 'Certification':
        required_education_Certification = 1
    elif required_education == "Bachelor's Degree":
        required_education_Bachelor_s_Degree = 1
    elif required_education == 'Vocational - Degree':
        required_education_Vocational___Degree = 1
    elif required_education == "Master's Degree":
        required_education_Master_s_Degree = 1
    elif required_education == 'Vocational':
        required_education_Vocational = 1
    elif required_education == 'Associate Degree':
        required_education_Associate_Degree = 1
    elif required_education == 'Professional':
        required_education_Professional = 1
    elif required_education == 'Doctorate':
        required_education_Doctorate = 1



    industry = st.selectbox('Please choose which industry the job posting is relevant to',
                            ('Not Specified', 'Marketing and Advertising', 'Computer Software',
                             'Hospital & Health Care', 'Online Media',
                             'Information Technology and Services', 'Financial Services',
                             'Management Consulting', 'Internet',
                             'Telecommunications', 'Consumer Services', 'Construction',
                             'Oil & Energy', 'Education Management',
                             'Health, Wellness and Fitness', 'Insurance', 'E-Learning',
                             'Staffing and Recruiting', 'Human Resources', 'Real Estate',
                             'Automotive', 'Logistics and Supply Chain', 'Design', 'Accounting',
                             'Retail','Others'))
    industry_Not_Specified, industry_Marketing_and_Advertising, industry_Computer_Software = 0, 0, 0
    industry_Hospital___Health_Care, industry_Online_Media, industry_Information_Technology_and_Services  = 0, 0, 0
    industry_Financial_Services, industry_Management_Consulting, industry_Internet = 0, 0, 0
    industry_Telecommunications, industry_Consumer_Services, industry_Construction  = 0, 0, 0
    industry_Oil___Energy, industry_Education_Management, industry_Health__Wellness_and_Fitness = 0, 0, 0
    industry_Insurance, industry_E_Learning, industry_Staffing_and_Recruiting   = 0, 0, 0
    industry_Human_Resources, industry_Real_Estate = 0, 0
    industry_Automotive, industry_Logistics_and_Supply_Chain = 0, 0
    industry_Design, industry_Accounting = 0, 0
    industry_Retail, industry_Others = 0, 0


    if industry == 'Not Specified':
        industry_Not_Specified = 1
    elif industry == 'Marketing and Advertising':
        industry_Marketing_and_Advertising = 1
    elif industry == 'Computer Software':
        industry_Computer_Software = 1
    elif industry == 'Hospital & Health Care':
        industry_Hospital___Health_Care = 1
    elif industry == 'Online Media':
        industry_Online_Media = 1
    elif industry == 'Information Technology and Services':
        industry_Information_Technology_and_Services = 1
    elif industry == 'Financial Services':
        industry_Financial_Services = 1
    elif industry == 'Management Consulting':
        industry_Management_Consulting = 1
    elif industry == 'Internet':
        industry_Internet = 1
    elif industry == 'Telecommunications':
        industry_Telecommunications = 1
    elif industry == 'Consumer Services':
        industry_Consumer_Services = 1
    elif industry == 'Construction':
        industry_Construction = 1
    elif industry == 'Oil & Energy':
        industry_Oil___Energy = 1
    elif industry == 'Education Management':
        industry_Education_Management = 1
    elif industry == 'Health, Wellness and Fitness':
        industry_Health__Wellness_and_Fitness = 1
    elif industry == 'Insurance':
        industry_Insurance = 1
    elif industry == 'E-Learning':
        industry_E_Learning = 1
    elif industry == 'Staffing and Recruiting':
        industry_Staffing_and_Recruiting = 1
    elif industry == 'Human Resources':
        industry_Human_Resources = 1
    elif industry == 'Real Estate':
        industry_Real_Estate = 1
    elif industry == 'Automotive':
        industry_Automotive = 1
    elif industry == 'Logistics and Supply Chain':
        industry_Logistics_and_Supply_Chain = 1
    elif industry == 'Design':
        industry_Design = 1
    elif industry == 'Accounting':
        industry_Accounting = 1
    elif industry == 'Retail':
        industry_Retail = 1
    else:
        industry_Others = 1

    function = st.selectbox('Please choose which umbrella term matches job\'s functionality?',
                            ('Not Specified', 'Marketing', 'Customer Service', 'Sales',
       'Health Care Provider', 'Management', 'Information Technology',
        'Engineering', 'Administrative', 'Design', 'Production',
       'Education', 'Business Development', 'Product Management',
       'Consulting', 'Human Resources', 'Project Management', 'Finance',
       'Accounting/Auditing', 'Art/Creative', 'Quality Assurance',
       'Writing/Editing', 'Other'))

    function_Not_Specified,function_Marketing = 0, 0
    function_Customer_Service, function_Sales = 0, 0
    function_Health_Care_Provider, function_Management = 0, 0
    function_Information_Technology, function_Engineering = 0, 0
    function_Administrative, function_Design = 0, 0
    function_Production, function_Education = 0, 0
    function_Business_Development, function_Project_Management = 0, 0
    function_Consulting, function_Human_Resources   = 0, 0
    function_Product_Management, function_Finance = 0, 0
    function_Accounting_Auditing, function_Art_Creative = 0, 0
    function_Quality_Assurance, function_Writing_Editing = 0, 0
    function_Other = 0

    if function == 'Not Specified':
        function_Not_Specified = 1
    elif function == 'Marketing':
        function_Marketing = 1
    elif function == 'Customer Service':
        function_Customer_Service = 1
    elif function == 'Sales':
        function_Sales = 1
    elif function == 'Health Care Provider':
        function_Health_Care_Provider = 1
    elif function == 'Management':
        function_Management = 1
    elif function == 'Information Technology':
        function_Information_Technology = 1
    elif function == 'Engineering':
        function_Engineering = 1
    elif function == 'Administrative':
        function_Administrative = 1
    elif function == 'Design':
        function_Design = 1
    elif function == 'Production':
        function_Production = 1
    elif function == 'Education':
        function_Education = 1
    elif function == 'Business Development':
        function_Business_Development = 1
    elif function == 'Product Management':
        function_Product_Management = 1
    elif function == 'Consulting':
        function_Consulting = 1
    elif function == 'Human Resources':
        function_Human_Resources = 1
    elif function == 'Project Management':
         function_Project_Management = 1
    elif function == 'Finance':
        function_Finance = 1
    elif function == 'Accounting/Auditing':
        function_Accounting_Auditing = 1
    elif function == 'Art/Creative':
        function_Art_Creative = 1
    elif function == 'Quality Assurance':
        function_Quality_Assurance= 1
    elif function == 'Writing/Editing':
        function_Writing_Editing= 1
    else:
        function_Other= 1


    inputs=[[telecommuting, has_company_logo, has_questions,
       employment_type_Full_time, employment_type_Not_Specified,
       employment_type_Other, employment_type_Part_time,
       employment_type_Temporary, required_experience_Director,
       required_experience_Entry_level, required_experience_Executive,
       required_experience_Internship,
       required_experience_Mid_Senior_level,
       required_experience_Not_Applicable,
       required_education_Bachelor_s_Degree,
       required_education_Certification, required_education_Doctorate,
       required_education_High_School_or_equivalent,
       required_education_Master_s_Degree, required_education_Professional,
       required_education_Some_College_Coursework_Completed,
       required_education_Some_High_School_Coursework,
       required_education_Unspecified, required_education_Vocational,
       required_education_Vocational___Degree,
       required_education_Vocational___HS_Diploma, industry_Automotive,
       industry_Computer_Software, industry_Construction,
       industry_Consumer_Services, industry_Design, industry_E_Learning,
       industry_Education_Management, industry_Financial_Services,
       industry_Health__Wellness_and_Fitness,
       industry_Hospital___Health_Care, industry_Human_Resources,
       industry_Information_Technology_and_Services, industry_Insurance,
       industry_Internet, industry_Logistics_and_Supply_Chain,
       industry_Management_Consulting, industry_Marketing_and_Advertising,
       industry_Not_Specified, industry_Oil___Energy,
       industry_Online_Media, industry_Others, industry_Real_Estate,
       industry_Retail, industry_Staffing_and_Recruiting,
       industry_Telecommunications, function_Administrative,
       function_Art_Creative, function_Business_Development,
       function_Consulting, function_Customer_Service, function_Design,
       function_Education, function_Engineering, function_Finance,
       function_Health_Care_Provider, function_Human_Resources,
       function_Information_Technology, function_Management,
       function_Marketing, function_Not_Specified, function_Other,
       function_Product_Management, function_Production,
       function_Project_Management, function_Quality_Assurance,
       function_Sales, function_Writing_Editing]]

    result = model.predict(inputs)

    # st.markdown("""
    # <style>
    # div.stButton > button:first-child {
    #     background-color: red;
    #     color:black;
    # }
    # # div.stButton > button:hover {
    # #     background-color:black;
    # #     color:red;
    # #     }
    # </style>""", unsafe_allow_html=True)


    # when 'Predict' is clicked, make the prediction and store it
    if st.button('Get Your Prediction'):

            if result == 0:
                st.success('The given job posting is Real')
            else:
                st.error('The given job posting is Fake')
    #st.snow()
    print(inputs)
