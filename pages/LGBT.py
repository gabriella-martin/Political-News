import pandas as pd
import pickle
import streamlit as st
from streamlit_extras.image_in_tables import table_with_images

#styling


with open('resources/styles.css') as f:
    st.markdown(f'<style>{f.read()}</style', unsafe_allow_html=True)

hide_table_row_index = """
            <style>

            thead tr th:first-child {display:none}
            tbody th {display:none}
            
            </style>
            """

#loading data

with open('data/links', 'rb') as l:
    links = pickle.load(l)

with open('data/headlines', 'rb') as h:
    headlines = pickle.load(h)

#start of visual

st.markdown("<h1 style='text-align: center;color: black;'>LGBT</h1>", unsafe_allow_html=True)
select = st.select_slider(label='timeline', options =('Left','Center-left', 'Center', 'Center-right', 'Right'), value = 'Center', label_visibility='collapsed')


if select == 'Center':
    data = {'Source':'https://www.ispa.org.uk/wp-content/uploads/I-News-logo.jpg', 'Headline': headlines[4][0], 'Link': links[0][4][0]}

if select == 'Left':
    data = {'Source':'https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/The_Guardian_2018.svg/2560px-The_Guardian_2018.svg.png', 'Headline': headlines[2][0], 'Link': links[0][2][0]}

if select == 'Right':
    data = {'Source':'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/The_Telegraph_logo.svg/512px-The_Telegraph_logo.svg.png?20171108145520', 'Headline': headlines[1][0], 'Link': links[0][1][0]}

if select == 'Center-left':
    data = {'Source':'https://tonyrobertson.mycouncillor.org.uk/files/2016/03/The-Independent-Logo.gif', 'Headline': headlines[3][0], 'Link': links[0][3][0]}

if select == 'Center-right':
    data = {'Source':'https://1000logos.net/wp-content/uploads/2020/03/The-Times-Logo.png', 'Headline': headlines[0][0], 'Link': links[0][0][0]}


df = (pd.DataFrame(data))


with st.expander('**Principles** ', expanded=False):

    if select == 'Left' or select =='Center-left':
        st.write("The left-wing view on LGBT rights is generally more progressive and inclusive, emphasizing the importance of protecting and advancing the rights and needs of all LGBT individuals, including transgender individuals.  \n   \n Left-wing advocates often argue that there is a long history of discrimination and marginalization of LGBT individuals, and that there is a need for ongoing efforts to promote equality and inclusion. They also stress the importance of recognizing and celebrating the diversity of the LGBT community, and challenging gender and sexuality-based stereotypes.  \n   \n Regarding current transgender issues, the left-wing view is generally supportive of the rights and needs of transgender individuals, and may prioritize transgender rights over other competing interests. Left-wing advocates argue that transgender individuals have historically faced significant barriers to accessing healthcare, education, and employment, and that there is a need for greater protections and support for this vulnerable population.  \n   \n In particular, the left-wing view may advocate for policies such as allowing transgender individuals to use bathrooms and other facilities that correspond to their gender identity, and making it easier for individuals to legally change their gender on official documents. They may also support greater access to gender-affirming healthcare, including hormone replacement therapy and gender confirmation surgery.  \n   \n Overall, the left-wing view on LGBT rights is characterized by a strong commitment to equality and social justice, and an emphasis on promoting the rights and needs of marginalized groups, including transgender individuals.")
    if select == 'Right' or select =='Center-right':
        st.write("The right winged view on LGBT issues varies, but it is generally more socially conservative and may view homosexuality and transgender identities as contrary to traditional values and beliefs. Right winged individuals may hold religious or moral objections to certain aspects of the LGBT rights movement and may believe that traditional gender roles and norms should be upheld.  \n   \n Regarding current transgender issues, some on the right view the push for transgender rights and recognition as a threat to women's spaces and safety, as well as to traditional views of gender and sexuality. They may argue that allowing transgender individuals to use facilities such as restrooms and changing rooms based on their gender identity could lead to privacy violations and even sexual assault. Some on the right also believe that allowing young children to undergo gender transition procedures could be harmful and even constitute child abuse.  \n   \n Overall, the right winged view on LGBT issues tends to prioritize traditional social and cultural norms and may seek to limit the expansion of LGBT rights and recognition. They may view transgender issues as particularly contentious, with concerns about privacy, safety, and morality at the forefront of their arguments.")
    if select == 'Center':
        st.write("The central view on LGBT rights is generally supportive of the rights and needs of LGBT individuals, including transgender individuals, while also recognizing the concerns and perspectives of others. Centrists support equal rights, protections, and opportunities for all individuals regardless of their sexual orientation, gender identity, or expression.  \n   \n Regarding current transgender issues, centrists support the right of transgender individuals to live their lives in a way that is authentic to their gender identity, including the right to access healthcare, education, and employment without discrimination. They also acknowledge the complexity and sensitivity of current debates around transgender issues, which may involve conflicting interests and rights.  \n   \n Therefore, the central view on transgender issues seeks to balance the needs and interests of different groups, promote dialogue and understanding, and ensure that policies and programs are evidence-based and informed by expert advice and consultation with affected groups. Ultimately, the central view on LGBT rights is guided by a commitment to human rights, equality, and dignity for all individuals, regardless of their sexual orientation, gender identity, or expression.")

with st.expander('**Headlines** ', expanded=True):

    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    df_html = table_with_images(df=df, url_columns=('Source',))
    st.markdown(df_html, unsafe_allow_html=True)

    st.write('')


with st.expander('**Video Debates** ', expanded=False):

    st.write('')
    cols = st.columns([0.3,5,5,0.3])
    cols[1].video('https://www.youtube.com/watch?v=IBAD2UuMPjs')

    cols[2].video('https://www.youtube.com/watch?v=TBJGgCHgf5w&t=329s')

    cols[1].video('https://www.youtube.com/watch?v=nDEyQB0Jjkw&t=726s')

    cols[2].video('https://www.youtube.com/watch?v=VaVLaPTMECo&t=606s')