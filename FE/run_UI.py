import streamlit as st



st.title('Man & Women Fashion Recommender System')

uploaded_file = st.file_uploader("Choose an image")
print(uploaded_file)

if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        # display the file
        display_image = Image.open(uploaded_file)
        resized_img = display_image.resize((200, 200))
        st.image(resized_img)
        # feature extract
        print("testtttt check")
        features = extract_feature(os.path.join("./app/uploads",uploaded_file.name),model)
        #st.text(features)
        # recommendention
        indices = recommend(features,feature_list)
        # show
        col1,col2,col3,col4,col5 = st.columns(5)

        with col1:
            st.image(os.path.join("app", filenames[indices[0][0]]))
        with col2:
            st.image(os.path.join("app", filenames[indices[0][1]]))
        with col3:
            st.image(os.path.join("app", filenames[indices[0][2]]))
        with col4:
            st.image(os.path.join("app", filenames[indices[0][3]]))
        with col5:
            st.image(os.path.join("app", filenames[indices[0][4]]))
    else:
        st.header("[FAILED] Some error occured in file upload")
