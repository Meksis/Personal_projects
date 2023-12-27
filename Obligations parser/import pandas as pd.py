import pandas as pd
import plotly.express as px
import streamlit as st

def main():
    st.title("Отображение данных CSV файла")

    # Загрузка CSV файла
    uploaded_file = st.file_uploader("Выберите CSV файл", type=["csv"])
    if uploaded_file is not None:
        st.success("Файл успешно загружен.")
        df = pd.read_csv(uploaded_file)

        # Отображение содержимого файла
        st.write("Содержимое CSV файла:")
        st.write(df)

        # Отображение линейного графика
        st.subheader("Линейный график:")
        fig = px.line(df, x=df.columns[0], y=df.columns[1:], title="Линейный график")
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()
