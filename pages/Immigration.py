
import streamlit as st
import pandas as pd
from streamlit_extras.image_in_tables import table_with_images
from streamlit_extras.app_logo import add_logo

st.markdown("<h1 style='text-align: center;color: black;'>Immigration</h1>", unsafe_allow_html=True)
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style', unsafe_allow_html=True)





select = st.select_slider(label='timeline', options =('Left','Center-left', 'Center', 'Center-right', 'Right'), value = 'Center', label_visibility='collapsed')


import pickle

with open('links', 'rb') as l:
    links = pickle.load(l)

with open('headlines', 'rb') as h:
    headlines = pickle.load(h)



if select == 'Center':
    data = {'Source':'https://www.ispa.org.uk/wp-content/uploads/I-News-logo.jpg', 'Headline': headlines[4][1], 'Link': links[0][4][1]}

if select == 'Left':
    data = {'Source':'https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/The_Guardian_2018.svg/2560px-The_Guardian_2018.svg.png', 'Headline': headlines[2][1], 'Link': links[0][2][1]}

if select == 'Right':
    data = {'Source':'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/The_Telegraph_logo.svg/512px-The_Telegraph_logo.svg.png?20171108145520', 'Headline': headlines[1][1], 'Link': links[0][1][1]}

if select == 'Center-left':
    data = {'Source':'https://tonyrobertson.mycouncillor.org.uk/files/2016/03/The-Independent-Logo.gif', 'Headline': headlines[3][1], 'Link': links[0][3][1]}

if select == 'Center-right':
    data = {'Source':'https://1000logos.net/wp-content/uploads/2020/03/The-Times-Logo.png', 'Headline': headlines[0][1], 'Link': links[0][0][1]}


df = (pd.DataFrame(data))
hide_table_row_index = """
            <style>

            thead tr th:first-child {display:none}
            tbody th {display:none}
            
            </style>
            """


with st.expander('**Principles** ', expanded=False):

    if select == 'Left' or select =='Center-left':
        st.write("The left-wing view of immigration varies among different left-wing political groups and individuals. However, in general, many left-wing politicians and activists view immigration as a positive force that can bring cultural diversity and economic benefits to a society.  \n   \n One argument put forward by left-wing supporters of immigration is that it can help to fill gaps in the labor market, particularly in sectors such as healthcare, education, and hospitality. They argue that immigrants often take on jobs that are vital to the economy but are less attractive to native-born workers, and that without immigration, many businesses would struggle to find enough workers.  \n   \n Another argument made by some on the left is that immigration can enrich a society's cultural diversity and contribute to social progress. They argue that the mixing of different cultures can lead to greater tolerance, understanding, and innovation, and that a society that is more open to immigration is likely to be more dynamic and resilient.  \n   \n Finally, some on the left view immigration as a human right and argue that it is the responsibility of more prosperous countries to welcome refugees and migrants who are fleeing poverty, persecution, and conflict. They argue that in many cases, the countries that receive the most immigrants have a moral obligation to provide support and assistance to those who have been forced to leave their homes.  \n   \n Overall, the left-wing view of immigration is generally positive and emphasizes the economic and social benefits of welcoming immigrants to a society. Left-wing politicians and activists often call for policies that prioritize the rights and welfare of immigrants, while also addressing the concerns of native-born workers and communities.")
    if select == 'Right' or select =='Center-right':
        st.write("The right-wing view of immigration is generally focused on limiting and controlling the number of immigrants coming into a country. Many right-wing politicians and activists believe that high levels of immigration can have negative impacts on a country's economy, social cohesion, and national security.  \n   \n One of the key arguments put forward by right-wing supporters of restricting immigration is that it can lead to pressure on public services and housing. They argue that a large influx of immigrants can increase demand for housing, healthcare, and other public services, which can put a strain on resources and lead to longer waiting times for citizens.  \n   \n Another argument made by some on the right is that immigration can have a negative impact on social cohesion. They argue that a large influx of immigrants can lead to cultural clashes and divisions within society, which can undermine social harmony and lead to tensions.  \n   \n Finally, some on the right view immigration as a threat to national security. They argue that an open-door immigration policy can make it easier for terrorists and criminals to enter a country, and that immigration controls are necessary to protect the safety and security of citizens.  \n   \n Overall, the right-wing view of immigration is characterized by a focus on controlling and limiting the number of immigrants entering a country, in order to protect the economy, social cohesion, and national security.")
    if select == 'Center':
        st.write("The central view on immigration is also a more moderate stance that falls between the more extreme positions taken by the left and the right. Centrists generally support controlled and managed immigration, with an emphasis on managing the economic, social, and cultural impacts of migration.  \n   \n Centrists often recognize the economic benefits of immigration, such as filling labor shortages, providing skills and expertise, and contributing to economic growth. At the same time, they also acknowledge the potential challenges of immigration, such as pressures on public services, social cohesion, and cultural integration.  \n   \n Therefore, the central view on immigration generally supports a balanced and pragmatic approach that seeks to maximize the benefits of immigration while minimizing its negative impacts. This may include measures such as controlling the number and type of migrants allowed into the country, ensuring that migrants have the skills and qualifications needed to contribute to the economy, and investing in language and cultural programs to support integration.  \n   \n In addition, centrists often support a humane and compassionate approach to asylum seekers and refugees, recognizing the importance of providing protection to those fleeing persecution and conflict. They may also advocate for international cooperation and support for countries experiencing high levels of migration or displacement, in order to address the root causes of migration and promote global stability and security.")

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
    cols[1].video('https://www.youtube.com/watch?v=RmQftvdYT-8')

    cols[2].video('https://www.youtube.com/watch?v=XSCaLcjGUro')

    cols[1].video('https://www.youtube.com/watch?v=jZA34onP-ZA')

    cols[2].video('https://www.youtube.com/watch?v=G0SpzIIHEaE&t=190s')