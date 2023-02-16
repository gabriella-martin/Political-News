
import streamlit as st
import pandas as pd
from streamlit_extras.image_in_tables import table_with_images
from streamlit_extras.app_logo import add_logo

st.markdown("<h1 style='text-align: center;color: black;'>Brexit</h1>", unsafe_allow_html=True)
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style', unsafe_allow_html=True)


st.write("""<style>@import url('https://fonts.googleapis.com/css2?family=Mukta');html, body, [class*="css"]  {  
   font-family: 'Kanit';  
}</style>""", unsafe_allow_html=True)


select = st.select_slider(label='timeline', options =('Left','Center-left', 'Center', 'Center-right', 'Right'), value = 'Center', label_visibility='collapsed')


import pickle

with open('links', 'rb') as l:
    links = pickle.load(l)

with open('headlines', 'rb') as h:
    headlines = pickle.load(h)



if select == 'Center':
    data = {'Source':'https://www.ispa.org.uk/wp-content/uploads/I-News-logo.jpg', 'Headline': headlines[4][3], 'Link': links[0][4][3]}

if select == 'Left':
    data = {'Source':'https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/The_Guardian_2018.svg/2560px-The_Guardian_2018.svg.png', 'Headline': headlines[2][3], 'Link': links[0][2][3]}

if select == 'Right':
    data = {'Source':'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/The_Telegraph_logo.svg/512px-The_Telegraph_logo.svg.png?20171108145520', 'Headline': headlines[1][3], 'Link': links[0][1][3]}

if select == 'Center-left':
    data = {'Source':'https://tonyrobertson.mycouncillor.org.uk/files/2016/03/The-Independent-Logo.gif', 'Headline': headlines[4][3], 'Link': links[0][4][3]}

if select == 'Center-right':
    data = {'Source':'https://1000logos.net/wp-content/uploads/2020/03/The-Times-Logo.png', 'Headline': headlines[0][3], 'Link': links[0][0][3]}


df = (pd.DataFrame(data))
hide_table_row_index = """
            <style>

            thead tr th:first-child {display:none}
            tbody th {display:none}
            
            </style>
            """


with st.expander('**Principles** ', expanded=False):

    if select == 'Left' or select =='Center-left':
        st.write("The left-wing view of Brexit varies among different left-wing political groups and individuals. However, in general, many left-wing politicians and activists opposed Brexit and saw it as a regressive move that could harm workers' rights, social protections, and the economy.  \n   \n One of the key arguments put forward by left-wing critics of Brexit was that leaving the European Union (EU) could lead to a race to the bottom in terms of labor standards and environmental regulations. Some left-wing commentators argued that leaving the EU could lead to a dismantling of these protections and a decline in workers' rights.  \n   \n  Another argument made by some on the left was that Brexit would harm the UK economy, particularly through reduced access to the EU's single market. Many left-wing politicians and activists argued that leaving the single market would damage trade and investment, and potentially lead to job losses and economic instability.  \n   \n  Finally, some on the left saw Brexit as a manifestation of right-wing populism and anti-immigrant sentiment. They argued that the Leave campaign had stoked anti-immigrant sentiment and that Brexit could lead to a reduction in immigration, which would harm the economy and undermine multiculturalism. Overall, the left-wing view of Brexit was generally critical and viewed it as a threat to workers' rights, the economy, and social protections.")
    if select == 'Right' or select =='Center-right':
        st.write("The right-wing view of Brexit also varies among different right-wing political groups and individuals. However, in general, many right-wing politicians and activists supported Brexit and saw it as an opportunity to regain control over the UK's laws, borders, and economy.One of the key arguments put forward by right-wing supporters of Brexit was that leaving the EU would allow the UK to regain its sovereignty and take back control of its laws. They argued that the EU had too much influence over the UK's laws and regulations and that Brexit would allow the UK to create its own laws without interference from the EU.  \n   \n Another argument made by some on the right was that leaving the EU would allow the UK to control its borders and reduce immigration. They argued that immigration had led to pressure on public services and housing and that leaving the EU would allow the UK to limit immigration and prioritize skilled workers.  \n   \n Finally, some on the right saw Brexit as an opportunity to forge new trade deals with countries outside the EU. They argued that the UK would be able to negotiate better trade deals with countries like the US and China and that this would help to boost the economy.  \n   \n Overall, the right-wing view of Brexit was generally supportive and viewed it as an opportunity for the UK to regain control over its laws, borders, and economy.")
    if select == 'Center':
        st.write("The central view on Brexit is a more moderate stance that falls between the more extreme positions taken by the left and the right. Generally speaking, centrists were divided on the issue of Brexit, with some supporting it and others opposing it.  \n   \n One argument made by centrists in favor of Brexit was that it would allow the UK to have more control over its own affairs, while maintaining a close relationship with the EU. They argued that the UK could negotiate a new relationship with the EU that would provide for continued trade and cooperation, while allowing the UK to have greater control over its laws and regulations.  \n   \n On the other hand, some centrists opposed Brexit, arguing that it would be harmful to the UK economy and that the risks of leaving the EU outweighed the potential benefits. They argued that leaving the EU's single market and customs union could lead to increased trade barriers and reduced investment, which could harm UK businesses and the economy more broadly.  \n   \n Overall, the central view on Brexit was characterized by a desire to strike a balance between the benefits of greater autonomy and control, and the potential risks of leaving the EU. While some centrists supported Brexit and others opposed it, many called for a more nuanced and pragmatic approach that would seek to minimize the risks and maximize the benefits of leaving the EU.")

with st.expander('**Headlines** ', expanded=True):

    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    df_html = table_with_images(df=df, url_columns=('Source',))
    st.markdown(df_html, unsafe_allow_html=True)

    st.write('')

# only grab articles from guardian

with st.expander('**Video Debates** ', expanded=False):

    st.write('')
    cols = st.columns([0.3,5,5,0.3])
    cols[1].video('https://www.youtube.com/watch?v=W-fVMIUHmwE')

    cols[2].video('https://www.youtube.com/watch?v=YKCrKtOsPNg')