import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="Cinema Dashboard",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stMetric {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        backdrop-filter: blur(10px);
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def get_connection():
    return sqlite3.connect('cinema.sqlite', check_same_thread=False)

def load_data(query):
    conn = get_connection()
    return pd.read_sql_query(query, conn)

st.title("🎬 Dashboard Cinema")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3163/3163478.png", width=100)
    st.title("Navigation")
    
    menu = st.radio(
        ["📊 Vue d'ensemble", "🎥 Films", "🎭 Acteurs", "💰 Filmographie", 
         "📈 Statistiques", "➕ Ajouter des données"]
    )
    
    st.markdown("---")
    st.info("💡 Base de données: cinema.sqlite")
    
    if st.button("🔄 Rafraîchir les données"):
        st.cache_data.clear()
        st.rerun()

if menu == "📊 Vue d'ensemble":
    st.header("📊 Vue d'ensemble")
    
    col1, col2, col3, col4 = st.columns(4)
    
    try:
        df_films = load_data("SELECT COUNT(*) as count FROM FILM")
        total_films = df_films['count'].iloc[0]
        
        df_acteurs = load_data("SELECT COUNT(*) as count FROM ACTEUR")
        total_acteurs = df_acteurs['count'].iloc[0]
        
        df_salaires = load_data("SELECT SUM(salaire) as total FROM FILMOGRAPHIE")
        total_salaires = df_salaires['total'].iloc[0] if df_salaires['total'].iloc[0] else 0
        
        df_moy = load_data("SELECT AVG(salaire) as moy FROM FILMOGRAPHIE")
        salaire_moyen = df_moy['moy'].iloc[0] if df_moy['moy'].iloc[0] else 0
        
        with col1:
            st.metric("🎥 Films", total_films)
        with col2:
            st.metric("🎭 Acteurs", total_acteurs)
        with col3:
            st.metric("💰 Total Salaires", f"${total_salaires:,.0f}")
        with col4:
            st.metric("📊 Salaire Moyen", f"${salaire_moyen:,.0f}")
        
        st.markdown("---")
        
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Films par Réalisateur")
            df_real = load_data("""
                SELECT realisateur, COUNT(*) as nombre 
                FROM FILM 
                GROUP BY realisateur 
                ORDER BY nombre DESC
            """)
            if not df_real.empty:
                fig = px.bar(df_real, x='realisateur', y='nombre', 
                           color='nombre',
                           color_continuous_scale='Viridis')
                fig.update_layout(showlegend=False, height=400)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("Aucune donnée disponible")
        
        with col2:
            st.subheader("💵 Top 5 Salaires")
            df_top = load_data("""
                SELECT a.prenom || ' ' || a.nom as acteur, f.salaire, film.titre
                FROM FILMOGRAPHIE f
                JOIN ACTEUR a ON f.idActeur = a.idActeur
                JOIN FILM film ON f.idFilm = film.idFilm
                ORDER BY f.salaire DESC
                LIMIT 5
            """)
            if not df_top.empty:
                fig = px.bar(df_top, x='acteur', y='salaire', 
                           hover_data=['titre'],
                           color='salaire',
                           color_continuous_scale='Plasma')
                fig.update_layout(showlegend=False, height=400)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("Aucune donnée disponible")
        
        st.subheader("🎬 Films Récents")
        df_recent = load_data("""
            SELECT titre, realisateur, annee 
            FROM FILM 
            ORDER BY annee DESC 
            LIMIT 5
        """)
        if not df_recent.empty:
            st.dataframe(df_recent, use_container_width=True, hide_index=True)
        else:
            st.info("Aucun film dans la base")
            
    except Exception as e:
        st.error(f"Erreur lors du chargement des données: {e}")
        st.info("Assurez-vous que la base de données cinema.sqlite existe et contient des données.")

elif menu == "🎥 Films":
    st.header("🎥 Gestion des Films")
    
    search = st.text_input("🔍 Rechercher un film", "")
    
    if search:
        df = load_data(f"""
            SELECT * FROM FILM 
            WHERE titre LIKE '%{search}%' OR realisateur LIKE '%{search}%'
        """)
    else:
        df = load_data("SELECT * FROM FILM ORDER BY annee DESC")
    
    if not df.empty:
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.subheader("📋 Détails d'un film")
        film_id = st.selectbox("Choisir un film:", df['idFilm'].tolist())
        
        if film_id:
            film_details = load_data(f"""
                SELECT f.titre, f.realisateur, f.annee,
                       a.prenom || ' ' || a.nom as acteur,
                       fg.role, fg.salaire
                FROM FILM f
                LEFT JOIN FILMOGRAPHIE fg ON f.idFilm = fg.idFilm
                LEFT JOIN ACTEUR a ON fg.idActeur = a.idActeur
                WHERE f.idFilm = {film_id}
            """)
            
            if not film_details.empty:
                st.write(f"**Titre:** {film_details['titre'].iloc[0]}")
                st.write(f"**Réalisateur:** {film_details['realisateur'].iloc[0]}")
                st.write(f"**Année:** {film_details['annee'].iloc[0]}")
                
                if film_details['acteur'].notna().any():
                    st.write("**Distribution:**")
                    cast_df = film_details[['acteur', 'role', 'salaire']].dropna()
                    st.dataframe(cast_df, use_container_width=True, hide_index=True)
    else:
        st.warning("Aucun film trouvé")

elif menu == "🎭 Acteurs":
    st.header("🎭 Gestion des Acteurs")
    
    search = st.text_input("🔍 Rechercher un acteur", "")
    
    if search:
        df = load_data(f"""
            SELECT * FROM ACTEUR 
            WHERE nom LIKE '%{search}%' OR prenom LIKE '%{search}%'
        """)
    else:
        df = load_data("SELECT * FROM ACTEUR ORDER BY nom")
    
    if not df.empty:
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.subheader("🎬 Filmographie")
        acteur_id = st.selectbox("Choisir un acteur:", df['idActeur'].tolist())
        
        if acteur_id:
            filmo = load_data(f"""
                SELECT f.titre, fg.role, fg.salaire, f.annee
                FROM FILMOGRAPHIE fg
                JOIN FILM f ON fg.idFilm = f.idFilm
                WHERE fg.idActeur = {acteur_id}
                ORDER BY f.annee DESC
            """)
            
            if not filmo.empty:
                st.dataframe(filmo, use_container_width=True, hide_index=True)
                
                total = filmo['salaire'].sum()
                moyenne = filmo['salaire'].mean()
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Films", len(filmo))
                with col2:
                    st.metric("Total Salaires", f"${total:,.0f}")
                with col3:
                    st.metric("Salaire Moyen", f"${moyenne:,.0f}")
            else:
                st.info("Cet acteur n'a joué dans aucun film")
    else:
        st.warning("Aucun acteur trouvé")

elif menu == "💰 Filmographie":
    st.header("💰 Filmographie Complète")
    
    df = load_data("""
        SELECT 
            a.prenom || ' ' || a.nom as Acteur,
            f.titre as Film,
            fg.role as Rôle,
            fg.salaire as Salaire,
            ROUND(fg.salaire * 9, 2) as 'Salaire (DH)'
        FROM FILMOGRAPHIE fg
        JOIN ACTEUR a ON fg.idActeur = a.idActeur
        JOIN FILM f ON fg.idFilm = f.idFilm
        ORDER BY fg.salaire DESC
    """)
    
    if not df.empty:
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Télécharger en CSV",
            data=csv,
            file_name='filmographie.csv',
            mime='text/csv'
        )
    else:
        st.warning("Aucune donnée de filmographie")

elif menu == "📈 Statistiques":
    st.header("📈 Statistiques Avancées")
    
    tab1, tab2, tab3 = st.tabs(["💰 Salaires", "🎬 Films", "🎭 Acteurs"])
    
    with tab1:
        st.subheader("Distribution des Salaires")
        df_sal = load_data("SELECT salaire FROM FILMOGRAPHIE")
        
        if not df_sal.empty:
            fig = px.histogram(df_sal, x='salaire', nbins=20,
                             title="Distribution des Salaires")
            st.plotly_chart(fig, use_container_width=True)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Min", f"${df_sal['salaire'].min():,.0f}")
            with col2:
                st.metric("Max", f"${df_sal['salaire'].max():,.0f}")
            with col3:
                st.metric("Médiane", f"${df_sal['salaire'].median():,.0f}")
    
    with tab2:
        st.subheader("Films par Année")
        df_annee = load_data("""
            SELECT annee, COUNT(*) as nombre 
            FROM FILM 
            GROUP BY annee 
            ORDER BY annee
        """)
        
        if not df_annee.empty:
            fig = px.line(df_annee, x='annee', y='nombre', markers=True)
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.subheader("Acteurs les Plus Actifs")
        df_actifs = load_data("""
            SELECT a.prenom || ' ' || a.nom as acteur, 
                   COUNT(*) as nombre_films,
                   AVG(fg.salaire) as salaire_moyen
            FROM ACTEUR a
            JOIN FILMOGRAPHIE fg ON a.idActeur = fg.idActeur
            GROUP BY a.idActeur
            ORDER BY nombre_films DESC
            LIMIT 10
        """)
        
        if not df_actifs.empty:
            st.dataframe(df_actifs, use_container_width=True, hide_index=True)

elif menu == "➕ Ajouter des données":
    st.header("➕ Ajouter des Données")
    
    tab1, tab2, tab3 = st.tabs(["🎥 Nouveau Film", "🎭 Nouvel Acteur", "💰 Nouvelle Filmographie"])
    
    conn = get_connection()
    c = conn.cursor()
    
    with tab1:
        st.subheader("Ajouter un Film")
        with st.form("form_film"):
            id_film = st.number_input("ID Film", min_value=1, step=1)
            titre = st.text_input("Titre")
            realisateur = st.text_input("Réalisateur")
            annee = st.number_input("Année", min_value=1900, max_value=2030, value=2024)
            
            if st.form_submit_button("Ajouter"):
                try:
                    c.execute("INSERT INTO FILM VALUES (?, ?, ?, ?)", 
                            (id_film, titre, realisateur, annee))
                    conn.commit()
                    st.success(f"✅ Film '{titre}' ajouté avec succès!")
                    st.cache_data.clear()
                except Exception as e:
                    st.error(f"Erreur: {e}")
    
    with tab2:
        st.subheader("Ajouter un Acteur")
        with st.form("form_acteur"):
            id_acteur = st.number_input("ID Acteur", min_value=1, step=1)
            nom = st.text_input("Nom")
            prenom = st.text_input("Prénom")
            
            if st.form_submit_button("Ajouter"):
                try:
                    c.execute("INSERT INTO ACTEUR VALUES (?, ?, ?)", 
                            (id_acteur, nom, prenom))
                    conn.commit()
                    st.success(f"✅ Acteur '{prenom} {nom}' ajouté avec succès!")
                    st.cache_data.clear()
                except Exception as e:
                    st.error(f"Erreur: {e}")
    
    with tab3:
        st.subheader("Ajouter une Filmographie")
        with st.form("form_filmo"):
            id_acteur_f = st.number_input("ID Acteur", min_value=1, step=1, key="fa")
            id_film_f = st.number_input("ID Film", min_value=1, step=1, key="ff")
            role = st.text_input("Rôle")
            salaire = st.number_input("Salaire ($)", min_value=0, step=1000)
            
            if st.form_submit_button("Ajouter"):
                try:
                    c.execute("INSERT INTO FILMOGRAPHIE VALUES (?, ?, ?, ?)", 
                            (id_acteur_f, id_film_f, role, salaire))
                    conn.commit()
                    st.success("✅ Filmographie ajoutée avec succès!")
                    st.cache_data.clear()
                except Exception as e:
                    st.error(f"Erreur: {e}")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Dashboard Cinema 🎬 | TD N°15 | Développé avec Streamlit</p>",
    unsafe_allow_html=True
)