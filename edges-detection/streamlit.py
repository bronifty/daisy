import streamlit as st
from PIL import Image, ImageOps

def st_ui():
    '''
    Function running the Streamlit UI.
    Doesn't return anything.
    '''
    
    st.set_page_config(layout = "wide")
    st.title("Compute edges")

    user_image = st.sidebar.file_uploader("Load your own image")
    if user_image is not None:
        im = Image.open(user_image)
        imagegray = ImageOps.grayscale(im)
        image = np.array(imagegray).astype(np.float32)
    
    else:
        im = scipy.misc.face()
        image = misc.face(gray=True).astype(np.float32)

    st.header("Original image")
    st.image(im)

    final = compute_deriv(image)
    
    st.header("Edge image")
    st.image(final)

if __name__ == "__main__":
    st_ui()