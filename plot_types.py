import matplotlib.pyplot as plt

def ir_plot(fig,ax):
    ax.set_xlabel("Wavenumber / cm$^{-1}$")
    ax.set_ylabel("Transmittance / %")
    
def nmr_plot(fig,ax):
    ax.set_xlabel("ppm")
#    ax.set_ylabel("Transmittance / %")
    ax.set_yticks([])
