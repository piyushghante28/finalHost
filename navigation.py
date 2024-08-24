import streamlit as st
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages

def make_sidebar():
    with st.sidebar:
        
        st.image("bitlock.png", use_column_width=True)


        st.markdown(
        """
        <div style='text-align: center; font-size: 30px; font-weight: bold; font-family: Arial, sans-serif; color: #000000;'>
                🔒 BitLocks 
        </div>
        """,
        unsafe_allow_html=True
        )
        st.write("")
        st.markdown("<h3 style='text-align: center;'>FINAL YEAR PROJECT BY <br> JANHAVI , VAISHNAVI , AVDHOOT , PHILNEHAS , PIYUSH </h3>", unsafe_allow_html=True)

        

        
        
