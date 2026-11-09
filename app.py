from shiny import App, render, reactive, ui
import numpy as np
import time
import io
import matplotlib.pyplot as plt
from ratelimit import debounce

from page_setup import page_setup
from plot_types import ir_plot, nmr_plot

app_ui = page_setup()

def server(input, output, session):
    #@debounce(0.5)
    #@reactive.Calc
        
    @output
    @render.plot
    def plots():
            
       
        try:
            data = np.loadtxt(input.data()[0]['datapath'],delimiter = ',')
        except:
            data = None
#            data = np.loadtxt('test_ir.csv',delimiter = ',')

        plot_type = input.plot_type()
        
        if data is not None:         

            plt.rcParams.update({'font.size': 15}) #change the font size of scale bar
            plt.rcParams["font.family"] = "DejaVu Sans" # change the font
            fig, ax = plt.subplots(1)

            ax.plot(data[:,0],data[:,1], lw=input.lw(), c = input.lc())
            
            colour = input.bg_colour()
            fig.patch.set_facecolor(colour)
            ax.patch.set_facecolor(colour)
            
            if plot_type == "ir":
                ir_plot(fig,ax)
            elif plot_type == "nmr":
                nmr_plot(fig,ax)    
            
        @render.download_button(filename = "output.png")
        def dl_button():
            with io.BytesIO() as buf:
                fig.savefig(buf, format="png")
                yield buf.getvalue()
    
#        return f"{input.action_button()}"
    
    @render.ui
    def page_style():
        colour = input.bg_colour()
        # Injects CSS targeting the main HTML body tag dynamically
        return ui.tags.style(f"body {{ background-color: {colour};  }}") #transition: background-color 0.3s ease;

app = App(app_ui, server)
