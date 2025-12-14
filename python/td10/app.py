import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Page config
st.set_page_config(
    page_title="CineSearch Pro",
    page_icon="🍿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 700;
        background: linear-gradient(120deg, #f093fb 0%, #f5576c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0;
    }
    
    .hero-subtitle {
        text-align: center;
        color: #888;
        font-size: 1.3rem;
        margin-top: 0;
    }
    
    .movie-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        margin: 1rem 0;
        transition: transform 0.3s;
    }
    
    .movie-card:hover {
        transform: translateY(-5px);
    }
    
    .stat-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .search-box {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# IMDb Scraping Functions
def scrape_imdb_top_movies(pages=1):
    all_movies = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    
    progress = st.progress(0)
    status = st.empty()
    
    for page in range(1, pages + 1):
        status.text(f"🎬 Loading page {page}/{pages}...")
        progress.progress(page / pages)
        
        url = f'https://www.imdb.com/search/title/?groups=top_250&start={1+(page-1)*50}'
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            movies = soup.find_all('div', class_='ipc-metadata-list-summary-item__c')
            
            for movie in movies:
                try:
                    title = movie.find('h3').text.strip()
                    year = movie.find('span', class_='sc-ab348ad5-8')
                    year = year.text.strip() if year else 'Unknown'
                    
                    rating = movie.find('span', class_='ipc-rating-star')
                    rating = rating.text.split()[0] if rating else 'N/A'
                    
                    metadata = movie.find_all('span', class_='sc-ab348ad5-8')
                    duration = metadata[1].text if len(metadata) > 1 else 'N/A'
                    
                    all_movies.append({
                        'Title': title,
                        'Year': year,
                        'Rating': rating,
                        'Duration': duration
                    })
                except:
                    continue
            
            time.sleep(1)
        except Exception as e:
            st.error(f"Error: {e}")
            break
    
    progress.empty()
    status.empty()
    return all_movies

def search_movie_by_name(query):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    search_url = f"https://www.imdb.com/find/?q={query.replace(' ', '+')}&s=tt&ttype=ft"
    
    try:
        response = requests.get(search_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        results = []
        items = soup.find_all('li', class_='ipc-metadata-list-summary-item')[:10]
        
        for item in items:
            try:
                title_tag = item.find('a', class_='ipc-metadata-list-summary-item__t')
                title = title_tag.text if title_tag else 'Unknown'
                link = f"https://www.imdb.com{title_tag['href']}" if title_tag else None
                
                metadata = item.find_all('span', class_='ipc-metadata-list-summary-item__li')
                year = metadata[0].text if metadata else 'Unknown'
                
                # Get detailed info
                if link:
                    time.sleep(0.5)
                    detail_response = requests.get(link, headers=headers, timeout=10)
                    detail_soup = BeautifulSoup(detail_response.content, 'html.parser')
                    
                    rating_tag = detail_soup.find('span', class_='sc-eb51e184-1')
                    rating = rating_tag.text if rating_tag else 'N/A'
                    
                    genre_tags = detail_soup.find_all('span', class_='ipc-chip__text')
                    genres = ', '.join([g.text for g in genre_tags[:3]]) if genre_tags else 'N/A'
                    
                    results.append({
                        'Title': title,
                        'Year': year,
                        'Rating': rating,
                        'Genres': genres,
                        'Link': link
                    })
            except:
                continue
        
        return results
    except Exception as e:
        st.error(f"Search failed: {e}")
        return []

# Sidebar
with st.sidebar:
    st.markdown("### 🎯 Control Panel")
    
    page = st.radio(
        "Navigate:",
        ["🏠 Home", "🔥 Top Movies", "🔍 Search Movies", "📊 Analytics"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### ⚙️ Settings")
    
    if page == "🔥 Top Movies":
        num_pages = st.slider("Pages to load", 1, 5, 2)
        load_btn = st.button("🚀 Load Movies", use_container_width=True, type="primary")
    
    st.markdown("---")
    st.markdown("**📌 Quick Info**")
    st.info("CineSearch Pro helps you discover and analyze movies from IMDb")

# Main Content
if page == "🏠 Home":
    st.markdown('<h1 class="hero-title">🍿 CineSearch Pro</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Your Ultimate Movie Discovery Platform</p>', unsafe_allow_html=True)
    
    st.markdown("##")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="stat-box">
            <h2>🔥</h2>
            <h3>Top Movies</h3>
            <p>Browse IMDb's highest rated films</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-box">
            <h2>🔍</h2>
            <h3>Smart Search</h3>
            <p>Find any movie instantly</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-box">
            <h2>📊</h2>
            <h3>Analytics</h3>
            <p>Visualize movie trends</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("##")
    
    with st.container():
        st.markdown('<div class="search-box">', unsafe_allow_html=True)
        st.markdown("### 🎬 Quick Search")
        quick_search = st.text_input("Search for a movie...", placeholder="Try: Inception, Titanic, Avatar...")
        if st.button("Search Now", type="primary"):
            if quick_search:
                st.session_state['search_query'] = quick_search
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "🔥 Top Movies":
    st.markdown("## 🔥 IMDb Top Rated Movies")
    
    if 'load_btn' in locals() and load_btn:
        with st.spinner("Loading movies..."):
            movies = scrape_imdb_top_movies(num_pages)
        
        if movies:
            df = pd.DataFrame(movies)
            st.session_state['movies_df'] = df
            st.success(f"✅ Loaded {len(movies)} movies!")
    
    if 'movies_df' in st.session_state:
        df = st.session_state['movies_df']
        
        # Stats
        col1, col2, col3, col4 = st.columns(4)
        
        ratings = df[df['Rating'] != 'N/A']['Rating'].astype(float)
        
        col1.metric("🎬 Movies", len(df))
        col2.metric("⭐ Avg Rating", f"{ratings.mean():.2f}")
        col3.metric("🏆 Best", f"{ratings.max():.1f}")
        col4.metric("📊 Lowest", f"{ratings.min():.1f}")
        
        st.markdown("##")
        
        # Filters
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            search = st.text_input("🔎 Filter by title", "")
        with col2:
            sort_by = st.selectbox("Sort by", ["Rating ↓", "Rating ↑", "Year ↓", "Year ↑"])
        with col3:
            min_rating = st.number_input("Min Rating", 0.0, 10.0, 7.0, 0.1)
        
        # Apply filters
        filtered = df.copy()
        
        if search:
            filtered = filtered[filtered['Title'].str.contains(search, case=False, na=False)]
        
        filtered = filtered[
            (filtered['Rating'] != 'N/A') & 
            (filtered['Rating'].astype(float) >= min_rating)
        ]
        
        # Sort
        if "Rating" in sort_by:
            filtered = filtered.sort_values('Rating', ascending="↑" in sort_by)
        elif "Year" in sort_by:
            filtered = filtered.sort_values('Year', ascending="↑" in sort_by)
        
        st.markdown(f"### 📽️ Showing {len(filtered)} movies")
        
        # Display as cards
        for idx, row in filtered.iterrows():
            st.markdown(f"""
            <div class="movie-card">
                <h3>🎬 {row['Title']}</h3>
                <p><strong>Year:</strong> {row['Year']} | <strong>Rating:</strong> ⭐ {row['Rating']} | <strong>Duration:</strong> {row['Duration']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Download
        csv = filtered.to_csv(index=False)
        st.download_button("📥 Download CSV", csv, "movies.csv", "text/csv", use_container_width=True)

elif page == "🔍 Search Movies":
    st.markdown("## 🔍 Search Any Movie")
    
    search_query = st.text_input(
        "Enter movie name:",
        value=st.session_state.get('search_query', ''),
        placeholder="e.g., The Matrix, Interstellar, The Godfather..."
    )
    
    search_button = st.button("🎬 Search", type="primary", use_container_width=True)
    
    if search_button and search_query:
        with st.spinner(f"🔍 Searching for '{search_query}'..."):
            results = search_movie_by_name(search_query)
        
        if results:
            st.success(f"✅ Found {len(results)} results!")
            
            for movie in results:
                with st.container():
                    st.markdown(f"""
                    <div class="movie-card">
                        <h2>🎬 {movie['Title']}</h2>
                        <div style="display: flex; justify-content: space-between; margin-top: 1rem;">
                            <div>
                                <p><strong>📅 Year:</strong> {movie['Year']}</p>
                                <p><strong>⭐ Rating:</strong> {movie['Rating']}/10</p>
                            </div>
                            <div>
                                <p><strong>🎭 Genres:</strong> {movie['Genres']}</p>
                                <a href="{movie['Link']}" target="_blank" style="color: white; text-decoration: underline;">View on IMDb →</a>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Export
            df_results = pd.DataFrame(results)
            csv = df_results.to_csv(index=False)
            st.download_button("📥 Export Results", csv, f"search_{search_query}.csv", use_container_width=True)
        else:
            st.warning("❌ No results found. Try a different search.")

elif page == "📊 Analytics":
    st.markdown("## 📊 Movie Analytics Dashboard")
    
    if 'movies_df' in st.session_state:
        df = st.session_state['movies_df']
        ratings = df[df['Rating'] != 'N/A'].copy()
        ratings['Rating'] = ratings['Rating'].astype(float)
        
        # Charts
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### ⭐ Rating Distribution")
            fig = px.histogram(ratings, x='Rating', nbins=20, color_discrete_sequence=['#f5576c'])
            fig.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### 📅 Movies by Year")
            year_counts = df['Year'].value_counts().sort_index()
            fig = px.line(x=year_counts.index, y=year_counts.values, color_discrete_sequence=['#667eea'])
            fig.update_layout(xaxis_title="Year", yaxis_title="Count", height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        # Top movies
        st.markdown("### 🏆 Top 15 Highest Rated")
        top = ratings.nlargest(15, 'Rating')[['Title', 'Year', 'Rating']]
        
        fig = px.bar(top, x='Rating', y='Title', orientation='h', 
                     color='Rating', color_continuous_scale='Viridis')
        fig.update_layout(height=600, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
        
    else:
        st.warning("⚠️ Load movies first from the 'Top Movies' section!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem;'>
    <h4>🍿 CineSearch Pro</h4>
    <p style='color: #888;'>Built with Python, Streamlit & IMDb | © 2024</p>
</div>
""", unsafe_allow_html=True)