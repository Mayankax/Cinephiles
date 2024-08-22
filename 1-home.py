import streamlit as st
import pandas as pd
from PIL import Image


def main():

	image = Image.open('CinePhile.png')
	st.image(image,width=300)
	st.write("# Welcome to CinePhile!!👋")
	st.write('To a CINEPHILE, movie is not just a form of entertainment as they see films from a more critical point of view.')
	st.write('All the MOVIE LOVERS, this is for you! We are going to entertain you on the basis of movies that we never ever thought of. We are going to recommend movies on the basis of it’s footing that we never thought of but technology make it easy so let’s make a best use of this!')

if __name__ == '__main__':
	main()