import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Загружаем датасет
@st.cache_data
def load_data():
    return pd.read_csv(
        "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    )


df = load_data()

st.title("🎢 Анализ пассажиров Титаника")
st.write("Этот дашборд позволяет изучить данные о пассажирах Титаника.")
st.write(df.head())  # Покажем первые строки

selected_class = st.selectbox("Выберите класс билета", df["Pclass"].unique())
filtered_data = df[df["Pclass"] == selected_class]
st.write(filtered_data)

fig, ax = plt.subplots()
sns.countplot(data=df, x="Survived", ax=ax, palette="coolwarm")
ax.set_xticklabels(["Погибли", "Выжили"])
ax.set_title("Выживаемость на Титанике")
st.pyplot(fig)
