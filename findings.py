import streamlit as st


def main():
    st.title("Survey Response Rates")

    total_households = 42022
    occupied_households = 38731
    interviewed_households = 37911
    eligible_women = 33879
    interviewed_women = 32156
    eligible_men = 16552
    interviewed_men = 14453

    # Calculate response rates
    household_response_rate = (interviewed_households / occupied_households) * 100
    women_response_rate = (interviewed_women / eligible_women) * 100
    men_response_rate = (interviewed_men / eligible_men) * 100

    st.header("Household Survey Response Rate")
    st.write(f"Total Households: {total_households}")
    st.write(f"Occupied Households: {occupied_households}")
    st.write(f"Interviewed Households: {interviewed_households}")
    st.write(f"Response Rate: {household_response_rate:.2f}%")

    st.header("Women's Survey Response Rate")
    st.write(f"Eligible Women: {eligible_women}")
    st.write(f"Interviewed Women: {interviewed_women}")
    st.write(f"Response Rate: {women_response_rate:.2f}%")

    st.header("Men's Survey Response Rate")
    st.write(f"Eligible Men: {eligible_men}")
    st.write(f"Interviewed Men: {interviewed_men}")
    st.write(f"Response Rate: {men_response_rate:.2f}%")

    # Pie chart
    labels = ['Household Response Rate', "Women's Response Rate", "Men's Response Rate"]
    values = [household_response_rate, women_response_rate, men_response_rate]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    st.header("Response Rates Comparison")
    st.plotly_chart(fig)

    st.header("Response Rates by Questionnaire")
    st.write("Full Questionnaire: 95%")
    st.write("Short Questionnaire: 95%")


