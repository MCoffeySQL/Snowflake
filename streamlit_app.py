import streamlit
import pandas
import requests

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.text('Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#my_fruit_list = my_fruit_list.set_index('Fruit') #change pick list value to fruit name

#display pick list
#fruits_selected = streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index))['Strawberries','Grapes']
#fruits_to_show = my_fruit_list.loc[fruits_selected]     #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html 

#display fruit table
#streamlit.dataframe(my_fruit_list)

#streamlit.header('fruityvice Fruit Advice!')
#fruit_choice = streamlit.text_input('What fruit would oyou like information about?','Kiwi')
#streamlit.write('The user entered',fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)



#take the json version of the response and normalize it
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it the screen as a table
#streamlit.dataframe(fruityvice_normalized)

