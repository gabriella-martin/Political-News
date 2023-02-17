import streamlit as st

st.markdown("<h1 style='text-align: center;color: black;'>Moral Foundations Quiz</h1>", unsafe_allow_html=True)

# introductory text with link

with st.sidebar:
    st.write('### Part 1 Scale')
    st.write('0: Not at all relevant')
    st.write('1: Not very relevant')
    st.write('2: Slightly relevant')
    st.write('3: Somewhat relevant')
    st.write('4: Very relevant')
    st.write('5: Extremely relevant')
    st.write('---')
    st.write('### Part 2 Scale')
    st.write('0: Strongly disagree')
    st.write('1: Moderately disagree')
    st.write('2: Slightly disagree')
    st.write('3: Slightly agree')
    st.write('4: Moderately agree')
    st.write('5: Strongly agree')

care_foundation = ['emotionally', 'weak', 'cruel', 'compassion', 'animal', 'kill']
fairness_foundation = ['treated', 'unfairly', 'rights', 'fairly', 'justice', 'rich']
loyalty_foundation = ['lovecountry', 'betray', 'loyalty','history', 'family', 'team']
authority_foundation = ['respect', 'traditions', 'chaos', 'kidrespect', 'sexroles', 'soldier']
purity_foundation = ['decency', 'disgusting', 'god', 'harmlessdg', 'unnatural', 'chastity']

with st.expander(label = 'Please Read the Preamble', expanded=False):

    st.write("Jonathan Haidt is a social psychologist who has written extensively about morality and its role in human behavior. One of his key insights is that people's moral beliefs and values are often shaped by a combination of innate tendencies, cultural norms, and personal experiences.")
    st.write("Jonathan Haidt's book 'The Righteous Mind: Why Good People Are Divided by Politics and Religion' provides a framework for understanding how moral values and intuitions shape political beliefs. According to Haidt, there are six foundations of morality that are common to all human societies, but they are weighted differently across the political spectrum. The six moral foundations are:")
    st.write("According to Haidt, everyone is attempting to do what they think is right morally, even though it may not be what others would do or what society as a whole might consider to be the 'right' thing. This is because people have different moral foundations, which are the underlying principles that shape their moral judgments.")
    st.write("Haidt has identified (empirically verified) six basic moral foundations that are common to all societies: care/harm, fairness/cheating, loyalty/betrayal, authority/subversion and sanctity/degradation. Different individuals and cultures place varying degrees of emphasis on each of these foundations, and this can lead to moral disagreements and conflicts.")

    st.write('1.	**Care/harm**: This foundation is based on the principle of compassion and the desire to care for others, especially those who are vulnerable or in need.')
    st.write('2.	**Fairness/cheating**: This foundation is based on the principle of justice and the desire for equal treatment and opportunity.')
    st.write('3.	**Loyalty/betrayal**: This foundation is based on the principle of loyalty and the importance of in-group loyalty and patriotism.')
    st.write('4.	**Authority/subversion**: This foundation is based on the principle of respect for authority and tradition, and the desire for order and stability.')
    st.write('5.	**Sanctity/degradation**: This foundation is based on the principle of sanctity and the desire for purity and cleanliness, and the disgust for things that are impure or polluting.')
    st.write('')
    st.write("For example, someone who places a high value on the sanctity foundation might believe that it is morally wrong to engage in certain behaviors that others might consider harmless or even beneficial. Conversely, someone who places a high value on the liberty foundation might believe that individual freedom is paramount and that certain restrictions on behavior are morally unacceptable.")
    st.write("Haidt's insight is that people often act in accordance with their moral foundations, even when doing so conflicts with the moral foundations of others. This can lead to misunderstandings, disagreements, and conflicts. However, by understanding the moral foundations of others and acknowledging their validity, it is possible to bridge these divides and find common ground.")
    st.write('')
st.write('### Part 1')
st.write('**Prompt**: When you decide whether something is right or wrong, to what extent are the following considerations relevant to your thinking? Please rate each statement using this scale:')
st.write('')
st.write('0: **Not at all relevant**: This consideration has nothing to do with my judgments of right and wrong')
st.write('1: **Not very relevant**')
st.write('2: **Slightly relevant**')
st.write('3: **Somewhat relevant**')
st.write('4: **Very relevant**')
st.write('5: **Extremely Relevant**: This is one of the most important factors when I judge right and wrong')
st.write('')
st.write('')

with st.expander('**Part 1**: Click to expand', expanded=False):
    with st.form("part 1"):

        st.write('')
        st.markdown("<p style='text-align: center;color: black;'>1: Whether or not someone suffered emotionally</p>", unsafe_allow_html=True)
        emotionally = st.slider('Q1 Relevancy', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>2: Whether or not some people were treated differently than others</p>", unsafe_allow_html=True)
        treated = st.slider('Q2 Relevancy', min_value=0, max_value=5, label_visibility='collapsed')
        
        st.markdown("<p style='text-align: center;color: black;'>3: Whether or not someone’s action showed love for his or her country</p>", unsafe_allow_html=True)
        lovecountry = st.slider('Q3 Relevancy', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>4: Whether or not someone showed a lack of respect for authority </p>", unsafe_allow_html=True)
        respect =st.slider('Q4 Relevancy', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>5: Whether or not someone violated standards of purity and decency </p>", unsafe_allow_html=True)
        decency = st.slider('Q5 Relevancy', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>6: Whether or not someone was good at math </p>", unsafe_allow_html=True)
        math = st.slider('Q6 Relevancy', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>7: Whether or not someone cared for someone weak or vulnerable </p>", unsafe_allow_html=True)
        weak =st.slider('Q7 Relevancy', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>8: Whether or not someone acted unfairly </p>", unsafe_allow_html=True)
        unfairly = st.slider('Q8 Relevancy', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>9: Whether or not someone did something to betray his or her group </p>", unsafe_allow_html=True)
        betray = st.slider('Q9 Relevancy', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>10: Whether or not someone conformed to the traditions of society  </p>", unsafe_allow_html=True)
        traditions = st.slider('Q10 Relevancy', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>11: Whether or not someone did something disgusting </p>", unsafe_allow_html=True)
        disgusting = st.slider('Q11 Relevancy', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>12: Whether or not someone was cruel </p>", unsafe_allow_html=True)
        cruel = st.slider('Q12 Relevancy', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>13: Whether or not someone was denied his or her rights </p>", unsafe_allow_html=True)
        rights = st.slider('Q13 Relevancy', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>14: Whether or not someone showed a lack of loyalty </p>", unsafe_allow_html=True)
        loyalty = st.slider('Q14 Relevancy', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>15: Whether or not an action caused chaos or disorder </p>", unsafe_allow_html=True)
        chaos = st.slider('Q15 Relevancy', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>16: Whether or not someone acted in a way that God would approve of </p>", unsafe_allow_html=True)
        god = st.slider('Q16 Relevancy', min_value=0, max_value=5, label_visibility='collapsed')




        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write('Thanks for submitting, please now do part 2')

st.write('### Part 2')
st.write('**Prompt**: Please read the following sentences and indicate your agreement or disagreement using the following scale:')
st.write('')
st.write('0: **Strongly disagree**')
st.write('1: **Moderately disagree**')
st.write('2: **Slightly disagree**')
st.write('3: **Slightly agree**')
st.write('4: **Moderately agree**')
st.write('5: **Strongly agree**')
st.write('')
st.write('')

with st.expander('**Part 2**: Click to expand', expanded=False):
    with st.form("part 2"):
        st.markdown("<p style='text-align: center;color: black;'>1: Compassion for those who are suffering is the most crucial virtue</p>", unsafe_allow_html=True)
        compassion = st.slider('Q16', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>2: When the government makes laws, the number one principle should be ensuring that everyone is treated fairly</p>", unsafe_allow_html=True)
        fairly = st.slider('Q17', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>3: I am proud of my country’s history</p>", unsafe_allow_html=True)
        history = st.slider('Q18', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>4: Respect for authority is something all children need to learn</p>", unsafe_allow_html=True)
        kidrespect = st.slider('Q19', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>5: People should not do things that are disgusting, even if no one is harmed</p>", unsafe_allow_html=True)
        harmlessdg = st.slider('Q20', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>6: It is better to do good than to do bad</p>", unsafe_allow_html=True)
        good = st.slider('Q21', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>7: One of the worst things a person could do is hurt a defenseless animal</p>", unsafe_allow_html=True)
        animal = st.slider('Q22', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>8: Justice is the most important requirement for a society</p>", unsafe_allow_html=True)
        justice = st.slider('Q23', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>9: People should be loyal to their family members, even when they have done something wrong</p>", unsafe_allow_html=True)
        family = st.slider('Q25', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>10: Men and women each have different roles to play in society</p>", unsafe_allow_html=True)
        sexroles = st.slider('Q26', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>11: I would call some acts wrong on the grounds that they are unnatural</p>", unsafe_allow_html=True)
        unnatural = st.slider('Q27', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>12: It can never be right to kill a human being</p>", unsafe_allow_html=True)
        kill = st.slider('Q28', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>13: I think it’s morally wrong that rich children inherit a lot of money while poor children inherit nothing</p>", unsafe_allow_html=True)
        rich = st.slider('Q29', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>14: It is more important to be a team player than to express oneself</p>", unsafe_allow_html=True)
        team = st.slider('Q30', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>15: If I were a soldier and disagreed with my commanding officer’s orders, I would obey anyway because that is my duty</p>", unsafe_allow_html=True)
        soldier = st.slider('Q31', min_value=0, max_value=5, label_visibility='collapsed')

        st.markdown("<p style='text-align: center;color: black;'>16: Chastity is an important and valuable virtue</p>", unsafe_allow_html=True)
        chastity = st.slider('Q32', min_value=0, max_value=5, label_visibility='collapsed')


        submitted_2 = st.form_submit_button("Submit")

if submitted_2:
    

    care_average =round((emotionally+weak+cruel+animal+kill+compassion)/6)


    fairness_average = round((rights+unfairly+treated+justice+fairly+rich)/6)
    loyalty_average= round((loyalty+betray+lovecountry+team+history+family)/6)
    authority_average = round((traditions+respect+chaos+sexroles+soldier+kidrespect)/6)
    purity_average = round((disgusting+decency+god+harmlessdg+unnatural+chastity)/6)
    compute_progressivism = round(((care_average+fairness_average)/2 - (loyalty_average+authority_average+purity_average)/3),2)

    st.write('### Your Results')
    st.slider(label='your score', label_visibility='collapsed', min_value = -1.00, max_value=1.00, value=compute_progressivism)
    st.write('Your moral beliefs are most congruent with the:')
    if compute_progressivism <= -0.75:
        st.write('**Far Left Political Sphere**')
        st.write('Based on the results of the quiz you took, it appears that you have a left-wing political perspective. From a left-wing perspective, there is typically a stronger emphasis on the Care/Harm and Fairness/Cheating foundations. This means that you may prioritize policies and actions that promote the well-being of others and reduce harm, and that you value fairness and equality.  \n   \n As a left-leaning individual, you may also value the Loyalty/Betrayal and Authority/Subversion foundations to some degree, but you tend to be more skeptical of these values than those on the right. You may be more likely to challenge authority and traditional hierarchies, and to be critical of institutions that you see as oppressive or unjust. Similarly, while you may value loyalty to certain groups or causes, you are also more likely to prioritize individual autonomy and freedom.  \n   \n Finally, as a left-leaning individual, you may be less likely to place importance on the Sanctity/Degradation foundation. While you may still value cleanliness and health, you may be more likely to question or reject traditional notions of purity or religious morality.')
        st.write('**Usage of the App for you**')
        st.write('To use the app effectively as a left-winged reader, you can start by selecting a topic that you are interested in. Once you have chosen a topic, the app will present you with a range of articles from diverse political viewpoints. While it may be tempting to read only those articles that align with your pre-existing beliefs, the app encourages you to engage with opposing viewpoints and challenge your assumptions. By doing so, you can develop a more well-rounded understanding of the issue and be better equipped to engage in informed and respectful political discussions. When reading articles from different perspectives, see if you can spot the moral foundations present.')
    elif compute_progressivism <= -0.5:
        st.write('**Left Political Sphere**')
        st.write('Based on the results of the quiz you took, it appears that you have a left-wing political perspective. From a left-wing perspective, there is typically a stronger emphasis on the Care/Harm and Fairness/Cheating foundations. This means that you may prioritize policies and actions that promote the well-being of others and reduce harm, and that you value fairness and equality.  \n   \n As a left-leaning individual, you may also value the Loyalty/Betrayal and Authority/Subversion foundations to some degree, but you tend to be more skeptical of these values than those on the right. You may be more likely to challenge authority and traditional hierarchies, and to be critical of institutions that you see as oppressive or unjust. Similarly, while you may value loyalty to certain groups or causes, you are also more likely to prioritize individual autonomy and freedom.  \n   \n Finally, as a left-leaning individual, you may be less likely to place importance on the Sanctity/Degradation foundation. While you may still value cleanliness and health, you may be more likely to question or reject traditional notions of purity or religious morality.')
        st.write('**Usage of the App for you**')
        st.write('To use the app effectively as a left-winged reader, you can start by selecting a topic that you are interested in. Once you have chosen a topic, the app will present you with a range of articles from diverse political viewpoints. While it may be tempting to read only those articles that align with your pre-existing beliefs, the app encourages you to engage with opposing viewpoints and challenge your assumptions. By doing so, you can develop a more well-rounded understanding of the issue and be better equipped to engage in informed and respectful political discussions. When reading articles from different perspectives, see if you can spot the moral foundations present.')
    elif compute_progressivism <= -0.25:
        st.write('**Center-Left Political Sphere **')
        st.write('Based on the results of the quiz you took, it appears that you have a left-wing political perspective. From a left-wing perspective, there is typically a stronger emphasis on the Care/Harm and Fairness/Cheating foundations. This means that you may prioritize policies and actions that promote the well-being of others and reduce harm, and that you value fairness and equality.  \n   \n As a left-leaning individual, you may also value the Loyalty/Betrayal and Authority/Subversion foundations to some degree, but you tend to be more skeptical of these values than those on the right. You may be more likely to challenge authority and traditional hierarchies, and to be critical of institutions that you see as oppressive or unjust. Similarly, while you may value loyalty to certain groups or causes, you are also more likely to prioritize individual autonomy and freedom.  \n   \n Finally, as a left-leaning individual, you may be less likely to place importance on the Sanctity/Degradation foundation. While you may still value cleanliness and health, you may be more likely to question or reject traditional notions of purity or religious morality.')
        st.write('**Usage of the App for you**')
        st.write('To use the app effectively as a left-winged reader, you can start by selecting a topic that you are interested in. Once you have chosen a topic, the app will present you with a range of articles from diverse political viewpoints. While it may be tempting to read only those articles that align with your pre-existing beliefs, the app encourages you to engage with opposing viewpoints and challenge your assumptions. By doing so, you can develop a more well-rounded understanding of the issue and be better equipped to engage in informed and respectful political discussions. When reading articles from different perspectives, see if you can spot the moral foundations present.')
    elif compute_progressivism >= 0.25:
        st.write('**Center-Right Political Sphere**')
        st.write('Based on the results of the quiz you look, it appears that you have a right-wing political perspective. In terms of loyalty, you may believe that people should be loyal to their family, country, and religion. This may manifest in your political beliefs through a desire for strong national security, a focus on traditional family values, and a belief in the importance of preserving cultural traditions.  \n   \n You may also place a high value on respect for authority and tradition. You may believe in the importance of law and order, and the need for strict rules and regulations to ensure social stability. Additionally, you may be more likely to respect the authority of leaders and institutions, and may be skeptical of calls for radical change or social upheaval.  \n   \n In terms of sanctity, you may believe in the importance of cleanliness, purity, and sanctity, and be opposed to behaviors or actions that you consider impure or polluting. This can manifest in your political beliefs through a focus on issues such as family values, sexual morality, and opposition to things like drug use, pornography, or other forms of behavior that you consider immoral.')
        st.write('**Usage of the App for you**')
        st.write('To use the app effectively as a right-winged reader, you can start by selecting a topic that you are interested in. Once you have chosen a topic, the app will present you with a range of articles from diverse political viewpoints. While it may be tempting to read only those articles that align with your pre-existing beliefs, the app encourages you to engage with opposing viewpoints and challenge your assumptions. By doing so, you can develop a more well-rounded understanding of the issue and be better equipped to engage in informed and respectful political discussions. When reading articles from different perspectives, see if you can spot the moral foundations present.')
    elif compute_progressivism >= 0.5:
        st.write('**Right Political Sphere**')
        st.write('Based on the results of the quiz you look, it appears that you have a right-wing political perspective. In terms of loyalty, you may believe that people should be loyal to their family, country, and religion. This may manifest in your political beliefs through a desire for strong national security, a focus on traditional family values, and a belief in the importance of preserving cultural traditions.  \n   \n You may also place a high value on respect for authority and tradition. You may believe in the importance of law and order, and the need for strict rules and regulations to ensure social stability. Additionally, you may be more likely to respect the authority of leaders and institutions, and may be skeptical of calls for radical change or social upheaval.  \n   \n In terms of sanctity, you may believe in the importance of cleanliness, purity, and sanctity, and be opposed to behaviors or actions that you consider impure or polluting. This can manifest in your political beliefs through a focus on issues such as family values, sexual morality, and opposition to things like drug use, pornography, or other forms of behavior that you consider immoral.')
        st.write('**Usage of the App for you**')
        st.write('To use the app effectively as a right-winged reader, you can start by selecting a topic that you are interested in. Once you have chosen a topic, the app will present you with a range of articles from diverse political viewpoints. While it may be tempting to read only those articles that align with your pre-existing beliefs, the app encourages you to engage with opposing viewpoints and challenge your assumptions. By doing so, you can develop a more well-rounded understanding of the issue and be better equipped to engage in informed and respectful political discussions. When reading articles from different perspectives, see if you can spot the moral foundations present.')
    elif compute_progressivism >=0.75:
        st.write('**Far Right Political Sphere**')
        st.write('Based on the results of the quiz you look, it appears that you have a right-wing political perspective. In terms of loyalty, you may believe that people should be loyal to their family, country, and religion. This may manifest in your political beliefs through a desire for strong national security, a focus on traditional family values, and a belief in the importance of preserving cultural traditions.  \n   \n You may also place a high value on respect for authority and tradition. You may believe in the importance of law and order, and the need for strict rules and regulations to ensure social stability. Additionally, you may be more likely to respect the authority of leaders and institutions, and may be skeptical of calls for radical change or social upheaval.  \n   \n In terms of sanctity, you may believe in the importance of cleanliness, purity, and sanctity, and be opposed to behaviors or actions that you consider impure or polluting. This can manifest in your political beliefs through a focus on issues such as family values, sexual morality, and opposition to things like drug use, pornography, or other forms of behavior that you consider immoral.')
        st.write('**Usage of the App for you**')
        st.write('To use the app effectively as a right-winged reader, you can start by selecting a topic that you are interested in. Once you have chosen a topic, the app will present you with a range of articles from diverse political viewpoints. While it may be tempting to read only those articles that align with your pre-existing beliefs, the app encourages you to engage with opposing viewpoints and challenge your assumptions. By doing so, you can develop a more well-rounded understanding of the issue and be better equipped to engage in informed and respectful political discussions. When reading articles from different perspectives, see if you can spot the moral foundations present.')
    else:
        st.write('**Central Political Sphere**')
        st.write("Based on the results of the quiz you look, it appears that you have a centrist political perspective. In terms of moral foundations, you may value the principle of care and compassion, believing that it's important to help and care for those who are vulnerable or in need. You may also value the principle of fairness and justice, believing that everyone should be treated equally and have equal opportunities. Additionally, you may value the principle of liberty and individual rights, believing that people should be free to make their own choices without undue interference.  \n   \n While you may not place as much emphasis on the moral foundations of loyalty, authority, and sanctity, you still recognize their importance in certain situations. You may believe in the importance of loyalty to family and friends, respect for legitimate authority, and the need for cleanliness and purity in certain contexts.  \n   \n Overall, your political beliefs are likely influenced by a desire to balance the moral foundations and find a middle ground between competing values. By understanding these moral foundations, we can better understand why people hold the political beliefs that they do, and perhaps find ways to bridge the ideological divide.")
        st.write('To use the app effectively as a centrist reader, you can start by selecting a topic that you are interested in. Once you have chosen a topic, the app will present you with a range of articles from diverse political viewpoints. While it may be tempting to read only those articles that align with your pre-existing beliefs, the app encourages you to engage with opposing viewpoints and challenge your assumptions. By doing so, you can develop a more well-rounded understanding of the issue and be better equipped to engage in informed and respectful political discussions. When reading articles from different perspectives, see if you can spot the moral foundations present.')



