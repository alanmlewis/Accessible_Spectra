from shiny import ui
from descriptions import desc

def page_setup():

    choices = {'ir': "IR Plot",
               'nmr': "NMR Plot"}
               
    bg_choices = {"#aebbff": "Blue",
               "#ffe4a9": "Yellow"}
               
    # Define the main user interface layout using a fluid page that scales with the browser width
    app_ui = ui.page_fluid(
    
        # Dynamic CSS tag injector, NOT SURE HOW THIS WORKS YET!
        ui.output_ui("page_style"),
        
        # Create a wrapper HTML div container
        ui.div(
            # Apply CSS to center-align the main application title formatted with Markdown
            {"style": "text-align: center;"},
            ui.markdown("# **Accessible Visualisations**"),
        ),
        # Create a horizontal row layout to contain the input and output columns
        ui.row(
            # First column: Width 3 out of 12 grid units (Inputs)
            ui.column(
                3,
                
                ui.input_file("data", "Upload your csv file here", accept=[".csv"], multiple=False),
                
                # Section header for Visualisation Options
                ui.markdown("### Visualisation Options"),
                
                # Dropdown menu for plot type
                ui.tooltip(
                    ui.input_select(
                        "plot_type", "Plot Type", choices, multiple = False
                    ),
                    desc["T"],
                ),
                
                # Dropdown menu for bg colour
                ui.tooltip(
                    ui.input_select(
                        "bg_colour", "Background Colour", bg_choices, multiple = False
                    ),
                    desc["T"],
                ),
                
                # Temperature slider (ID: 'T', Range: 100 to 500 K, Default: 298, Step: 1) wrapped in a tooltip
                ui.tooltip(
                    ui.input_slider(
                        "T", "Temperature (K)", 100, 500, 298, step=1
                    ),
                    desc["T"],
                ),
                # Scan Rate text input field (ID: 'v', Default: 100) wrapped in a tooltip
                ui.tooltip(
                    ui.input_text("v", "Scan Rate (mV/s)", 100), desc["v"]
                ),
                # Checkbox group for toggling peak visual features (ID: 'peaks', Options: peak_choices) wrapped in a tooltip
                #ui.tooltip(
                #    ui.input_checkbox_group("peaks", "Show:", peak_choices),
                #    desc["peaks"],
                #),
                # Radio buttons to select which species concentration profile to render (ID: 'C_spe', Options: choices)
                #ui.input_radio_buttons("C_spe", "Show concentration of:", choices),
                
            ),
            
            # Second column: Width 9 out of 12 grid units (Main plot container displaying generated graphs at a fixed height of 1500px)
            ui.column(9, ui.output_plot("plots", height="800px")),
            
            
        ),
        
        #style = f"background-color: {input.bg_colour()};"
    )
    
    return app_ui
