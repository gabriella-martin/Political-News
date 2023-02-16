import streamlit as st
import pandas as pd
from streamlit_extras.image_in_tables import table_with_images
from streamlit_extras.app_logo import add_logo

st.markdown("<h1 style='text-align: center;color: black;'>Racism</h1>", unsafe_allow_html=True)
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style', unsafe_allow_html=True)




select = st.select_slider(label='timeline', options =('Left','Center-left', 'Center', 'Center-right', 'Right'), value = 'Center', label_visibility='collapsed')


import pickle

with open('links', 'rb') as l:
    links = pickle.load(l)

with open('headlines', 'rb') as h:
    headlines = pickle.load(h)



if select == 'Center':
    data = {'Source':'https://www.ispa.org.uk/wp-content/uploads/I-News-logo.jpg', 'Headline': headlines[4][2], 'Link': links[0][4][2]}

if select == 'Left':
    data = {'Source':'https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/The_Guardian_2018.svg/2560px-The_Guardian_2018.svg.png', 'Headline': headlines[2][2], 'Link': links[0][2][2]}

if select == 'Right':
    data = {'Source':'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/The_Telegraph_logo.svg/512px-The_Telegraph_logo.svg.png?20171108145520', 'Headline': headlines[1][2], 'Link': links[0][1][2]}

if select == 'Center-left':
    data = {'Source':'https://tonyrobertson.mycouncillor.org.uk/files/2016/03/The-Independent-Logo.gif', 'Headline': headlines[3][2], 'Link': links[0][3][2]}

if select == 'Center-right':
    data = {'Source':'https://1000logos.net/wp-content/uploads/2020/03/The-Times-Logo.png', 'Headline': headlines[0][2], 'Link': links[0][0][2]}


df = (pd.DataFrame(data))
hide_table_row_index = """
            <style>

            thead tr th:first-child {display:none}
            tbody th {display:none}
            
            </style>
            """


with st.expander('**Principles** ', expanded=False):

    if select == 'Left' or select =='Center-left':
        st.write("The left has a long history of fighting against racism and promoting social justice for marginalized communities. Left-wing ideology views racism as a systemic issue that is deeply ingrained in societal structures, such as education, housing, healthcare, and employment. They believe that racism is not just about individual acts of prejudice or discrimination, but also about unequal access to resources, opportunities, and power.  \n   \n In the left-wing perspective, racism perpetuates social inequality and maintains systems of oppression, particularly for people of color. This systemic approach to racism requires a more comprehensive approach to address its root causes. As a result, left-leaning individuals and organizations often advocate for policies that promote equity and inclusion, such as affirmative action, anti-discrimination laws, and investment in underserved communities.  \n   \n Moreover, the left-wing perspective on racism emphasizes the importance of education and awareness-raising campaigns to combat racism and promote diversity and inclusivity. The left believes that promoting cultural diversity, celebrating different perspectives, and acknowledging the contributions of underrepresented groups in society is key to achieving true social justice.  \n   \n Overall, the left sees racism as a major societal issue that requires collective action and systemic change to overcome. By promoting policies that address racial disparities and raising awareness about the harmful effects of racism, the left seeks to create a more just and equitable society for all.")
    if select == 'Right' or select =='Center-right':
        st.write("The right-winged view on racism can vary depending on the individual or group. Some right-winged individuals or groups may reject the concept of systemic racism, believing that any disparities in society are solely the result of individual actions rather than systemic issues. They may also argue that race-based policies, such as affirmative action, are discriminatory against non-minority groups.  \n   \n Others may argue that racism is a problem but that it is primarily perpetuated by individuals rather than institutional structures. They may advocate for individual responsibility and meritocracy, believing that people should be judged based on their individual abilities and accomplishments rather than their race.  \n   \n In general, the right-winged view on racism tends to prioritize individualism, personal responsibility, and limited government intervention in social and economic issues. They may also emphasize the importance of preserving national identity and cultural traditions.")
    if select == 'Center':
        st.write("Political affiliations can vary widely, and it is difficult to say what a central political affiliation believes about racism. However, many moderate political views acknowledge that racism is a problem and that it is essential to address it through policy and education.  \n   \n In general, a central political view may seek to find common ground and compromise on issues related to racism, seeking to bridge the gap between different ideological perspectives. They may support measures that address issues related to systemic discrimination and bias while also emphasizing the need to respect individual rights and freedoms.  \n   \n A central political view might recognize that racism is a complex issue that cannot be solved by any single policy or solution. They may seek to address racism by promoting diversity, inclusivity, and anti-discrimination in all areas of life, including politics, workplaces, and social settings. They may also prioritize education and awareness campaigns to highlight the negative effects of racism on individuals and society as a whole.  \n   \n Ultimately, the approach taken by a central political view on issues related to racism will depend on a range of factors, including the specific policies and platforms of the group, as well as the views and opinions of individual members. However, central political views often seek to balance the needs of diverse groups and work towards a common goal of a more just and equitable society.")

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
    cols[1].video('https://www.youtube.com/watch?v=_f04LwlshHM')

    cols[2].video('https://www.youtube.com/watch?v=S6rDvbQ-mz4')

    cols[1].video('https://www.youtube.com/watch?v=VspjfNMPHyc&t=9s')

    cols[2].video('https://www.youtube.com/watch?v=yYqlI__PniY')