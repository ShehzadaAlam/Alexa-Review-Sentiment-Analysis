#Author: Shehzada

import pickle
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence

def main():
    maxlen=100
    st.title('Alexa Sentiment Classifier')
    review_description = st.text_area('Review Description:')
    prediction  = st.button('Sentiment Prediction')
    with open('tokeniing_text.pkl', 'rb') as fid:
        tokenizer = pickle.load(fid)
    sentiment_model = load_model('customize_conv_network.h5')


    if prediction and review_description != '':
        description = [review_description]
        pred = sentiment_model.predict(sequence.pad_sequences(tokenizer.texts_to_sequences(description),maxlen=maxlen))  
        if pred>0.5:
            st.success(f'The sentiment is positive')
        else:
            st.error(f'The sentiment is negative')
    elif prediction and review_description == '':
        st.warning('Please enter your review')

    

if __name__=='__main__':
    main()
