import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu


# Données utilisateurs
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attempts': 0,  # Géré automatiquement
            'logged_in': False,  # Géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attempts': 0,  # Géré automatiquement
            'logged_in': False,  # Géré automatiquement
            'role': 'administrateur'
        }
    }
}

# Authentification
authenticator = Authenticate(
    lesDonneesDesComptes,  # Données des comptes
    "cookie_name",  # Nom du cookie
    "cookie_key",  # Clé du cookie
    30  # Durée du cookie (en jours)
)

# Fonction pour la page d'accueil
def accueil():
    st.title("Bienvenue sur ma page")
    st.write("Vous êtes actuellement sur la page d'accueil.")
    st.image("https://youcancookit.fr/wp-content/uploads/2023/05/Recette-croissant.jpg")

# Fonction pour la page des photos
def photos():
    st.title("Album Photo")
    st.write("Voici vos photos !")

    # Affichage des images
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Un chat")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    with col2:
        st.header("Un chien")
        st.image("https://static.streamlit.io/examples/dog.jpg")
    with col3:
        st.header("Un hibou")
        st.image("https://static.streamlit.io/examples/owl.jpg")

# Authentification
authenticator.login()
s
if st.session_state.get("authentication_status"):
    # Utilisateur authentifié
    authenticator.logout("Déconnexion", key="logout")

    # Barre latérale pour la navigation
    st.sidebar.title("Navigation")
    choix = st.sidebar.radio(
        "Choisissez une page :", 
        options=["Accueil", "Photos"]
    )
    
    # Gestion des pages
    if choix == "Accueil":
        accueil()
    elif choix == "Photos":
        photos()

elif st.session_state.get("authentication_status") is False:
    # Erreur d'authentification
    st.error("L'username ou le password est incorrect.")
else:
    # Champs non remplis
    st.warning("Les champs username et mot de passe doivent être remplis.")
