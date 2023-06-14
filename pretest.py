import streamlit as st
from css_utilities import format_card_with_css, format_list_with_css
pretest_objectives = ['Test the adequacy of training agenda for the main survey', 
                      'Test the data collection instruments (questionnaires, manuals, forms)',
                        'Test the suitability of the CAPI data collection approach',
                          'Evaluate the competence of personnel',
                            'Assess the workload of field interviewers and biomarker technicians',
                              'Test the adequacy of training procedures for the field personnel', 
                      'Test the adequacy of the planned duration of data collection', 
                      'Evaluate the overall administrative and financial structure and other general logistics issues', 
                      'Test the reliability of the central server data transmission mechanisms and the robustness of the system',
                        'Put in place to monitor the quality of data from the field', 'Test the effectiveness of the publicity and advocacy strategy and data processing strategies'
                        ]

def pretest(pretest_objectives = pretest_objectives):
    format_card_with_css("Pretest")
    st.info(
        """The pretest consisted of classroom training and field practice for interviewers and biomarker technicians. 
       The training took place from December 11, 2021, to January 18, 2022. The objectives of the pretest were 
       to:
        """)
    format_list_with_css(pretest_objectives)
    with st.expander(":blue[Learn more]"):
        st.caption("""
        The pretest training for the survey encompassed comprehensive coverage of questionnaire content, interviewing procedures, and anthropometry practice with children. Field practice took place over a span of two days, following which field teams were deployed to eight counties to pilot the survey tools and procedures. The selection of pretest clusters aimed to represent diverse geographical areas and necessitated the use of different languages. It is important to note that these clusters were not part of the actual 2022 KDHS sample. Following the pretest fieldwork, a debriefing session was conducted to assess any issues that arose. The outcomes of the debriefing informed the finalization of questionnaires, the CAPI program, and field logistics in preparation for the main training and data collection phase.
        """)
