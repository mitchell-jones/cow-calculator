import streamlit as st
import matplotlib.pyplot as plt  # for plotting
import time  # for sleeping
import imageio  # for gif export
import pandas as pd  # for tables
import matplotlib as mpl  # for graphing
from PIL import Image

mpl.rc("figure", dpi=150)
st.set_page_config(layout="wide")

def generate_gif(maxTime):
    images = []
    filename_list = ['Cow Calculator_{}.png'.format(x) for x in range(20, maxTime + 1, 5)]
    filename_list.append(filename_list[-1])
    for filename in filename_list:
        images.append(imageio.imread(filename))
    imageio.mimsave('Cow Calculator from 20 to {}.gif'.format(maxTime), images, duration = .5)

    return 'Cow Calculator from 20 to {}.gif'.format(maxTime)

def update_loop(maxtime, placeholderTable, placeholderGraph, adultCows, babyCows):
    for i in range(20, maxtime + 1, 5):
        # Math
        adultCows.append(adultCows[-1] + (adultCows[-4] // 2))
        babyCows.append((babyCows[-1]) + (adultCows[-1] // 2) - (adultCows[-4] // 2))

        # Render graph
        placeholderGraph.pyplot(render_graph(i, adultCows, babyCows), clear_figure=True)

        # Render Table
        placeholderTable.table(pd.DataFrame({
            'Time': list(range(0, i + 1, 5)),
            'Adult Cows': adultCows,
            'Baby Cows': babyCows}))
        time.sleep(.75)


def render_graph(i, adultCows, babyCows):
    # plt.clf()
    plt.plot(list(range(0, i + 1, 5)), adultCows, label="Full Size Cows")
    plt.plot(list(range(0, i + 1, 5)), babyCows, label="Baby Cows")
    plt.title('Cow Breeding in Minecraft (Time 0 to {})'.format(i))
    plt.xlabel('Minutes')
    plt.ylabel('Cows')
    plt.legend()
    fig1 = plt.gcf()
    # fig1.set_size_inches(1, 1)
    fig1.savefig('Cow Calculator_{}.png'.format(i))
    return fig1


def main():
    st.title('Minecraft Cow Calculator')
    st.write(
        "Breeding 2 adult cows in Minecraft produces a single baby cow. Additionally, adult cows in Minecraft can be bred every 5 minutes, and baby cows grow up in 20 minutes.")
    st.write("Assume that baby cows will be bred in the same minute that they grow up.")
    st.write("Given the starting number of adult cows c, state the number of adult and baby cows at time k in minutes.")

    maxTime = int(st.number_input('How long do you want to breed cows for? (k)', min_value=20, step=5))
    starting_number = int(st.number_input('How many cows do you want to start with? (c)', min_value=2, step=1))

    adultCows = [starting_number for x in range(0, 4)]
    babyCows = [starting_number // 2 + x for x in range(0, 4)]

    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

    with col5:
        goButton = st.button('Start')

    maincol1, maincol2 = st.columns([1, 1])

    with maincol1:
        placeholderTable = st.empty()
    with maincol2:
        placeholderGraph = st.empty()

    if goButton:
        update_loop(maxTime, placeholderTable, placeholderGraph, adultCows, babyCows)

        placeholderTable.table(pd.DataFrame({
            'Time': list(range(0, maxTime + 1, 5)),
            'Adult Cows': adultCows,
            'Baby Cows': babyCows}))

        placeholderGraph.image(generate_gif(maxTime))




if __name__ == '__main__':
    main()
