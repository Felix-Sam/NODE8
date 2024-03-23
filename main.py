import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from database import *


# Create the SQLAlchemy engine and session
SQLALCHEMY_DATABASE_URL = 'sqlite:///./malnutrition.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Streamlit app
def main():
    st.title(":blue[Malnutrition Data Collection Form]")
    classes = ['Malnourish', 'Nourished']
    selected_class = st.sidebar.radio('Select an option', classes)
    st.image('Node8.PNG')
    st.sidebar.header('Data Collection App')
    st.sidebar.image('img.PNG')
    
    st.sidebar.text(f'You selected {selected_class}')

    if selected_class == 'Malnourish':
        st.subheader(f':red[You are Collecting Data for {selected_class} Children]')
        # Input form
        with st.form("user_form"):
            st.subheader("User Information")
            age = st.number_input(":red[Age in months]", min_value=0.0, max_value=150.0, value=0.0, step=0.5, key="age")
            weight = st.number_input(":red[Weight in (kg)]", min_value=0, max_value=1000, step=1, value=0, key="weight")
            height = st.number_input(":red[Height in (cm)]", min_value=0, max_value=3000, value=0, step=1, key="height")
            hand_circumference = st.number_input(":red[Mid Lower Hand Circumference (cm)]", min_value=0, max_value=100, value=0, step=1, key="hand_circumference")
            skin_type = st.selectbox(":red[Select Skin Type]", ['Dry and scaly', 'Rash'], key="skin_type")
            hair_type = st.selectbox(":red[Select Hair Type]", ['Dry flaky scalp', 'Thin sparse hair'], key="hair_type")
            eyes_type = st.selectbox(":red[Select Eye Type]", ['Jaundice', 'Dry sour eyes'], key="eyes_type")
            oedema = st.selectbox(":red[Oedema]", ['yes', 'no'], key="odeama")
            angular_stomatitis = st.selectbox(":red[Angular]", ['yes', 'no'], key="angular_stomatitis")
            cheilosis = st.selectbox(":red[Cheilosis]", ['yes', 'no'],key='cheilosis')
            bowlegs = st.selectbox(":red[Bowlegs]", ['yes', 'no'], key="bowlegs")
            location = st.text_input(":red[Location]", key="location")
            type_of_malnutrition = st.text_input(":red[Type of malnutrition]", key="type_of_malnutrition")
            face_image = st.file_uploader("Face Image", key="face_image")
            if face_image:
                st.image(face_image,width=300,caption='image of a face')
            hair_image = st.file_uploader("Hair Image", key="hair_image")
            if hair_image:
                st.image(hair_image,width=300,caption='image of  hair')
            hands_image = st.file_uploader("Hands Image", key="hands_image")
            if hands_image:
                st.image(hands_image,width=300,caption='image of hands')
            leg_image = st.file_uploader("Leg Image", key="leg_image")
            if leg_image:
                st.image(leg_image,width=300,caption='image of leg')

            submitted = st.form_submit_button("Submit", type='primary')
            if submitted:
                # Validate if all fields are filled
                if not (age and weight and height and hand_circumference and skin_type and hair_type and eyes_type and location and face_image and hair_image and hands_image and leg_image):
                    st.error("Please fill in all the fields")
                    return

                # Save user data to the database
                data = {
                    "age": age,
                    "weight": weight,
                    "height": height,
                    "mid_lower_hand_circumference": hand_circumference,
                    "skin_type": skin_type,
                    "hair_type": hair_type,
                    "eyes_type": eyes_type,
                    "oedema":oedema,
                    "angular_stomatitis":angular_stomatitis,
                    "cheilosis":cheilosis,
                    "bowlegs":bowlegs,
                    "location": location,
                    'type_of_malnutrition':type_of_malnutrition,
                    "face_image": face_image.read() if face_image else None,
                    "hair_image": hair_image.read() if hair_image else None,
                    "hands_image": hands_image.read() if hands_image else None,
                    "leg_image": leg_image.read() if leg_image else None
                }
                with SessionLocal() as session:
                    user = Malnurish_data(**data)
                    session.add(user)
                    session.commit()

                st.success(f"User data saved successfully! to {selected_class} table in the database")
    
    
    
    # For nourish children 
    if selected_class == 'Nourished':
        st.subheader(f'You are Collecting Data for {selected_class} Children')
        # Input form
        with st.form("user_form"):
            st.subheader("User Information")
            age = st.number_input("Age in months", min_value=0.0, max_value=150.0, value=0.0, step=0.5, key="age")
            weight = st.number_input("Weight in (kg)", min_value=0, max_value=1000, step=1, value=0, key="weight")
            height = st.number_input("Height in (cm)", min_value=0, max_value=3000, value=0, step=1, key="height")
            hand_circumference = st.number_input("Mid Lower Hand Circumference (cm)", min_value=0, max_value=100, value=0, step=1, key="hand_circumference")
            skin_type = st.selectbox("Select Skin Type", ['Dry and scaly', 'Rash'], key="skin_type")
            hair_type = st.selectbox("Select Hair Type", ['Dry flaky scalp', 'Thin sparse hair'], key="hair_type")
            eyes_type = st.selectbox("Select Eye Type", ['Jaundice', 'Dry sour eyes'], key="eyes_type")
            oedema = st.selectbox("Oedema", ['yes', 'no'], key="odeama")
            angular_stomatitis = st.selectbox("Angular", ['yes', 'no'], key="angular_stomatitis")
            cheilosis = st.selectbox("Cheilosis", ['yes', 'no'],key='cheilosis')
            bowlegs = st.selectbox("Bowlegs", ['yes', 'no'], key="bowlegs")
            location = st.text_input("Location", key="location")
            face_image = st.file_uploader("Face Image", key="face_image")
            if face_image:
                st.image(face_image,width=300,caption='image of a face')
            hair_image = st.file_uploader("Hair Image", key="hair_image")
            if hair_image:
                st.image(hair_image,width=300,caption='image of  hair')
            hands_image = st.file_uploader("Hands Image", key="hands_image")
            if hands_image:
                st.image(hands_image,width=300,caption='image of hands')
            leg_image = st.file_uploader("Leg Image", key="leg_image")
            if leg_image:
                st.image(leg_image,width=300,caption='image of leg')

            submitted = st.form_submit_button("Submit", type='primary')
            if submitted:
                # Validate if all fields are filled
                if not (age and weight and height and hand_circumference and skin_type and hair_type and eyes_type and location and face_image and hair_image and hands_image and leg_image):
                    st.error("Please fill in all the fields")
                    return

                # Save user data to the database
                data = {
                    "age": age,
                    "weight": weight,
                    "height": height,
                    "mid_lower_hand_circumference": hand_circumference,
                    "skin_type": skin_type,
                    "hair_type": hair_type,
                    "eyes_type": eyes_type,
                    "oedema":oedema,
                    "angular_stomatitis":angular_stomatitis,
                    "cheilosis":cheilosis,
                    "bowlegs":bowlegs,
                    "location": location,
                    "face_image": face_image.read() if face_image else None,
                    "hair_image": hair_image.read() if hair_image else None,
                    "hands_image": hands_image.read() if hands_image else None,
                    "leg_image": leg_image.read() if leg_image else None
                }
                with SessionLocal() as session:
                    user = Nurish_data(**data)
                    session.add(user)
                    session.commit()

                st.success(f"User data saved successfully! to {selected_class} table in the database")
      
if __name__ == "__main__":
    main()