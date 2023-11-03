from gettext import npgettext
import streamlit as st
import pandas as pd 
import numpy as np

#Texto

st.header('Minha dashboard')
st.sidebar.text("Meu texto")

st.markdown("# Meu titulo")

pessoas = [{'Nome': 'Caio', 'Idade' : '20'}]

st.write("Pessoas", pessoas)

# EXIBIÇÃO DE DADOS 

import pandas as pd 
import numpy as np

if st.sidebar.button("Exibir grafico"):
    df = pd.DataFrame(
    np.random.rand(10, 3),
    columns=['Preço', 'Taxa de ocupação', 'Taxa de inadimplência']
)
st.line_chart(df)

