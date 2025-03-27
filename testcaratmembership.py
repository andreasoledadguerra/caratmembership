import streamlit as st

# Function to apply a custom background and font
def set_styles(theme: str):
    if theme == "Light":
        css = """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
            
            body {
                background-color: #f0f8ff; /* AliceBlue background */
                color: #000;
                font-family: 'Roboto', sans-serif;
            }
            .stButton>button {
                background-color: #007bff;
                color: #fff;
                border: none;
                font-family: 'Roboto', sans-serif;
            }
        </style>
        """
    elif theme == "Dark":
        css = """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
            
            body {
                background: linear-gradient(to bottom, #121212, #1d1d1d);
                color: #fff;
                font-family: 'Roboto', sans-serif;
            }
            .stButton>button {
                background-color: #444;
                color: #fff;
                border: none;
                font-family: 'Roboto', sans-serif;
            }
        </style>
        """
    elif theme == "Image":
        css = """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
            
            body {
                background: url('https://source.unsplash.com/random/1920x1080') no-repeat center center fixed;
                background-size: cover;
                color: #fff;
                font-family: 'Roboto', sans-serif;
            }
            .stButton>button {
                background-color: rgba(0, 0, 0, 0.7);
                color: #fff;
                border: none;
                font-family: 'Roboto', sans-serif;
            }
        </style>
        """
    else:
        css = ""  # Default styling
    
    # Inject the CSS into the Streamlit app
    st.markdown(css, unsafe_allow_html=True)

# Main Streamlit app
def main():
    st.set_page_config(page_title="Custom Fonts and Backgrounds", layout="wide")

    # Sidebar settings
    st.sidebar.title("Customize Theme")
    theme = st.sidebar.radio("Background Theme", ["Light", "Dark", "Image"], index=0)

    # Apply the selected styles
    set_styles(theme)

    # Main content
    st.title("Customizing Background and Font in Streamlit")
    st.write("Switch between different themes for the app background and font styles.")
    st.button("Click Me!")

if __name__ == "__main__":
    main()

