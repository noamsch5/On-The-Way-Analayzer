import streamlit as st
import os
from src.audio.analyzer import analyze_track
from src.api.youtube import find_similar_tracks
from src.seo.suggestions import generate_description, generate_tags
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    st.title("🎵 On The Way Analyzer")
    st.subheader("EDM Track Analysis & SEO Tool")

    # File uploader
    uploaded_file = st.file_uploader("Upload your EDM track (WAV format)", type=['wav'])

    if uploaded_file:
        st.info("Analyzing your track...")
        
        # Save temporary file
        with open("temp.wav", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        try:
            # Analyze the track
            genre, subgenres, bpm = analyze_track("temp.wav")
            
            # Find similar tracks on YouTube
            similar_tracks = find_similar_tracks(genre)
            
            # Display results in two columns
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Track Analysis")
                st.write(f"**Main Genre:** {genre}")
                st.write(f"**BPM:** {bpm}")
                st.write("**Subgenres:**")
                for subgenre in subgenres:
                    st.write(f"- {subgenre}")
            
            with col2:
                st.subheader("Similar Tracks")
                for track in similar_tracks[:5]:
                    st.write(f"- {track['title']} ({track['channel']})")
            
            # Generate and display SEO content
            st.header("SEO Suggestions")
            
            description = generate_description(
                genre=genre,
                related_tracks=similar_tracks,
                bpm=bpm
            )
            
            tags = generate_tags(
                genre=genre,
                subgenres=subgenres,
                similar_tracks=similar_tracks
            )
            
            st.subheader("YouTube Description")
            st.text_area("Copy this description:", description, height=200)
            
            st.subheader("Recommended Tags")
            st.text_area("Copy these tags:", ", ".join(tags), height=100)
            
        except Exception as e:
            st.error(f"Error analyzing track: {str(e)}")
        
        finally:
            # Cleanup temporary file
            if os.path.exists("temp.wav"):
                os.remove("temp.wav")
    
    st.markdown("---")
    st.markdown("Made with ❤️ for EDM producers")

if __name__ == "__main__":
    main()
