import streamlit as st
from todoist_analytics.frontend.habit_tracker import filter_recurrent_task, get_recurrent_tasks
from todoist_analytics.frontend.plots import calendar_habits_plot


def render():
    st.markdown("# Habit Tracking")
    st.markdown("The side panel filters do not affect this section")
    data = st.session_state["completed_tasks"].copy()
    recurrent_tasks = get_recurrent_tasks(data)
    completed_tasks_habits = filter_recurrent_task(data, recurrent_tasks)
    st.plotly_chart(calendar_habits_plot(completed_tasks_habits), use_container_width=True)
