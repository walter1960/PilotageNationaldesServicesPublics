import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard David Analysis", layout="wide")
st.title("Pilotage National des Services Publics")

# Chargement de ma dataset finale netoyee : togo_dataset_final_propre.csv
@st.cache_data
def load_data():
    df = pd.read_csv('../dataset_final/togo_dataset_final_propre.csv')
    df['date_demande'] = pd.to_datetime(df['date_demande'])
    return df

df = load_data()

#FILTRES DYNAMIQUES
st.sidebar.header("Filtres")
date_range = st.sidebar.date_input("Période", [])
commune_opt = st.sidebar.multiselect("Commune", df['commune'].unique(), default=df['commune'].unique())
type_doc = st.sidebar.selectbox("Type de Document", ["Tous"] + list(df['type_document'].unique()))

# Application des filtres
mask = df['commune'].isin(commune_opt)
if type_doc != "Tous":
    mask &= (df['type_document'] == type_doc)
df_filtered = df[mask]
# Remove rows with NaN values in key columns to avoid processing errors
df_filtered = df_filtered.dropna(subset=['delai_traitement_jours', 'personnel_capacite_jour', 'commune_id'])


st.header("1. Vue Globale")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Délai Moyen (Jours)", f"{df_filtered['delai_traitement_jours'].mean():.1f}")
kpi2.metric("Taux de Conformité", f"{(df_filtered['statut_demande'] == 'Traitee').mean()*100:.1f}%")
kpi3.metric("Capacité Totale", f"{df_filtered['personnel_capacite_jour'].sum():.0f}")
kpi4.metric("Volume Demandes", len(df_filtered))

# Évolution temporelle
fig_line = px.line(df_filtered.groupby('date_demande').size().reset_index(name='Volume'), 
                   x='date_demande', y='Volume', title="Évolution des demandes")
st.plotly_chart(fig_line, use_container_width=True)

# VUE OPÉRATIONNELLE PAR CENTRE
st.markdown("---")
st.header("2. Performance Opérationnelle par Centre")
col_bar, col_pie = st.columns(2)

with col_bar:
    # Capacité vs Réel
    fig_op = px.bar(df_filtered.groupby('centre_id')['personnel_capacite_jour'].max().reset_index(), 
                    x='centre_id', y='personnel_capacite_jour', title="Capacité Installée par Centre")
    st.plotly_chart(fig_op)

with col_pie:
    fig_type = px.pie(df_filtered, names='type_centre', title="Répartition des Centres")
    st.plotly_chart(fig_type)

#  VUE TERRITORIALE 
st.markdown("---")
st.header("3. Analyse Territoriale & Accessibilité")

# Heatmap par commune
geo_data = df_filtered.groupby('commune').agg({'demande_id': 'count', 'population': 'max'}).reset_index()
geo_data.columns = ['commune', 'demandes', 'population']
geo_data['Demandes_par_habitant'] = geo_data['demandes'] / geo_data['population']

fig_geo = px.bar(geo_data, x='commune', y='Demandes_par_habitant', 
                 color='Demandes_par_habitant', title="Pression de la demande par Commune")
st.plotly_chart(fig_geo, use_container_width=True)

st.info("NB : Les zones qui ont une forte barre de couleur sombre indiquent des zones potentiellement sous-desservies.")