
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

st.title("Palmer's Penguins")
st.subheader('A WebApp by Runesu')
st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')

#data entry set-up

# ----Starting with file upload: Data gathering

penguin_file = st.file_uploader('Select Your Local Penguins CSV')
@st.cache()
def load_file(penguin_file):
	time.sleep(3)
	if penguin_file is not None:
		df = pd.read_csv(penguin_file)
	else:
		df = pd.read_csv('penguin_data.csv')
	return(df)
penguins_df = load_file(penguin_file)


selected_x_var = st.selectbox('What do you want the x variable to be?',['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm','body_mass_g'])
selected_y_var = st.selectbox('What about the y variable?',['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm','body_mass_g'])

# Penguin gender selection

selected_gender = st.selectbox('What gender do you want to filter for?',
['all penguins', 'male penguins', 'female penguins'])
if selected_gender == 'male penguins':
	penguins_df = penguins_df[penguins_df['sex'] == 'male']
elif selected_gender == 'female penguins':
	penguins_df = penguins_df[penguins_df['sex'] == 'female']
else:
	pass



#setting up the plots
sns.set_style('darkgrid')
markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}
fig, ax = plt.subplots()
ax = sns.scatterplot(data = penguins_df, x = selected_x_var,y = selected_y_var, hue = 'species', markers = markers,style = 'species')
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title("Scatterplot of Palmer's Penguins: {}".format(selected_gender))
st.pyplot(fig)