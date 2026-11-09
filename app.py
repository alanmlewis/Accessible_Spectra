from shiny import App, render, reactive, ui
import numpy as np
import time
import matplotlib.pyplot as plt
from ratelimit import debounce

from page_setup import page_setup

app_ui = page_setup()

def server(input, output, session):
    #@debounce(0.5)
    #@reactive.Calc
        
    @output
    @render.plot
    def plots():
            
            #data = None
            #while data is None:
            #    try:
            #        data = np.loadtxt(input.data()[0]['datapath'],delimiter = ',')
            #    except:
            #        time.sleep(0.5)
            data = np.loadtxt(input.data()[0]['datapath'],delimiter = ',')
            
            plt.rcParams.update({'font.size': 15}) #change the font size of scale bar
            plt.rcParams["font.family"] = "DejaVu Sans" # change the font
            fig,axs = plt.subplots(1)
            axs.plot(data[:,0],data[:,1])
            
    @render.ui
    def page_style():
        color = input.bg_colour()
        # Injects CSS targeting the main HTML body tag dynamically
        return ui.tags.style(f"body {{ background-color: {color}; transition: background-color 0.3s ease; }}")

app = App(app_ui, server)
