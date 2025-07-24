import streamlit as st

st.set_page_config(
    page_title="Road Damage Detections App",
    page_icon="🛣️",
)

st.image("./resource/banner.png", use_column_width="always")
st.divider()
st.title("Road Damage Detection Application")

st.markdown(
    """
    Introducing our Road Damage Detection App, powered by the YOLOv8 deep learning model trained on Crowdsensing-based Road Damage Detection Challenge 2024 Dataset.
    
    This application is designed to enhance road safety and infrastructure maintenance by swiftly identifying and categorizing various forms of road damage, such as potholes and cracks.

    There is four types of damage that this model can detects such as:
    - Longitudinal Crack
    - Transverse Crack
    - Alligator Crack
    - Potholes

    The model trained on YOLOv8 small model on Japan and India CRDDC2022 dataset.

    You can select the apps from the sidebar to try and experiment with any kind of input **(realtime-webcam, video and images)** depends on your use case.

    #### Documentations and Links
    - Github Project Page [Github](https://github.com/oracl4/RoadDamageDetection)
    - You can reach me on aadilmohamed2911@gmail.com

    #### License and Citations
    - Road Damage Dataset from Crowdsensing-based Road Damage Detection Challenge (CRDDC2024)
    - All rights reserved on YOLOv8 license permits by [Ultralytics](https://github.com/ultralytics/ultralytics) and [Streamlit](https://streamlit.io/) framework
"""
)

st.divider()

st.markdown(
    """
    This project is created by 
    <a href="https://www.linkedin.com/in/aadil-vasheer-job/" target="_blank">Mohamed Aadil A</a>, 
    <a href="https://www.linkedin.com/in/logamithran-balasubramaniam-6160b4283/" target="_blank">Logamithran C B</a>, 
    <a href="https://www.linkedin.com/in/kushal-kumar-venkatesh-448b79325/" target="_blank">Kushal Kumar V</a>, 
    <a href="https://www.linkedin.com/in/nagappan-sp-0a0098301/" target="_blank">Nagappan S P</a>.
    """,
    unsafe_allow_html=True
)

st.markdown("---")
st.markdown("🚧 **SARD**: An AI-powered road damage detection tool to enhance road safety through real-time, image, and video-based detection using YOLOv8.")

st.markdown(
    """
    <p align="center">
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white"/>
        <img src="https://img.shields.io/badge/YOLOv8-FFAD00?style=flat&logo=openai&logoColor=black"/>
        <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white"/>
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p align="center">
        <a href="mailto:aadilmohamed2911@gmail.com"><button style="padding:10px 20px;border-radius:5px;border:none;background-color:#20C997;color:white;">Contact Developer</button></a>
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2025 SARD Team | Developed with ❤️ using Streamlit</p>", unsafe_allow_html=True)
