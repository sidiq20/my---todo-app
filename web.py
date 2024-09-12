import streamlit as st
import functions

# Load todos
todos = functions.get_todos()

# Initialize session state for todos if not already initialized
if 'todos' not in st.session_state:
    st.session_state.todos = todos

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    st.session_state.todos.append(new_todo)
    functions.write_todos(st.session_state.todos)
    st.session_state["new_todo"] = ""  # Clear the input after adding

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

# Display todos
for index, todo in enumerate(st.session_state.todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")
    if checkbox:
        # Remove the todo from the session state list
        st.session_state.todos.pop(index)
        functions.write_todos(st.session_state.todos)
        st.experimental_rerun()  # Re-run to update the app

# Text input for adding new todos
st.text_input(label="", placeholder="Add new todo....", on_change=add_todo, key='new_todo')
