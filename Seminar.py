import streamlit as st
import load_model  # Assuming 'load_model' is in a separate module
loaded_model = load_model('phantichdulieu')
def app():
    # Set the app title
    st.title("Phân tích dữ liệu")

    # Add a header for user input
    st.header("Nhập dữ liệu:")

    # Create input fields for user to enter data
    # Replace 'feature_names' with the actual names of your features
    feature_names = ['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure',
                     'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']
    user_inputs = st.number_input(label=feature_names, min_value=0)

    # Check if all input fields have been filled
    if all(user_inputs):
        # Combine user inputs into a single list
        data = [user_input for user_input in user_inputs]

        # Make a prediction using the loaded model
        prediction = loaded_model.predict([data])

        # Display the prediction result
        st.success("Kết quả dự đoán: {}".format(prediction[0]))
    else:
        # Display a message if not all inputs are provided
        st.warning("Vui lòng nhập đầy đủ dữ liệu.")

# Run the Streamlit app
app()
if __name__ == "__main__":
    st.run(app)

