from lib_omost.canvas import Canas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description="A diagram explaining how earthquakes happen, showing fault lines, epicenter, and tectonic plates.",
    detailed_descriptions=[
        "This diagram illustrates the process of how earthquakes occur.",
        "It shows the Earth's crust with tectonic plates and the fault lines where they meet.",
        "The movement of tectonic plates along fault lines is depicted.",
        "An earthquake's focus point beneath the Earth's surface is shown.",
        "The epicenter directly above the focus on the Earth's surface is highlighted.",
        "Seismic waves radiate outward from the epicenter.",
        "The diagram helps explain the relationship between fault lines, epicenters, and earthquakes.",
    ],
    tags="earthquake, diagram, tectonic plates, fault lines, epicenter, focus, seismic waves, Earth's crust, movement, geology",
    HTML_web_color_name="lightblue",
)

# Add the Earth's crust and tectonic plates
canvas.add_local_description(
    name="tectonic_plates",
    bbox=[0, 40, 90, 50],
    distance_to_viewer=5.0,
    description="The Earth's crust with tectonic plates.",
    detailed_descriptions=[
        "The lower half of the diagram shows the Earth's crust as large pieces called tectonic plates.",
        "These plates fit together like a puzzle, covering the Earth's surface.",
        "They are depicted with jagged edges to represent their uneven shapes.",
        "Different colors are used for each plate to distinguish them.",
        "The plates span across the width of the diagram.",
    ],
    tags="Earth's crust, tectonic plates, plates, geology, puzzle pieces, uneven shapes",
    atmosphere="Educational and clear, showing the Earth's crust and plates.",
    style="Simple and illustrative, suitable for young learners.",
    quality_meta="High resolution with clear lines and distinct colors.",
    HTML_web_color_name="sandybrown",
)

# Add fault lines between tectonic plates
canvas.add_local_description(
    name="fault_lines",
    bbox=[0, 40, 90, 50],
    distance_to_viewer=5.0,
    description="Fault lines where tectonic plates meet.",
    detailed_descriptions=[
        "Bold lines between the plates represent fault lines.",
        "These are cracks in the Earth's crust where plates meet.",
        "Fault lines are shown as dark, jagged lines.",
        "They are located where the plates touch each other.",
    ],
    tags="fault lines, cracks, Earth's crust, tectonic plates, geology",
    atmosphere="Clear and informative, highlighting where plates meet.",
    style="Bold lines to emphasize the fault lines.",
    quality_meta="High resolution with clear, bold lines.",
    HTML_web_color_name="black",
)

# Add the earthquake focus point beneath the Earth's surface
canvas.add_local_description(
    name="focus",
    bbox=[45, 55, 5, 5],
    distance_to_viewer=4.0,
    description="The earthquake's focus point below the Earth's surface.",
    detailed_descriptions=[
        "A small point beneath the Earth's surface represents the focus.",
        "It is located along a fault line.",
        "The focus is where the earthquake starts inside the Earth.",
        "It is shown as a bright red dot.",
    ],
    tags="focus, earthquake origin, below surface, starting point, seismic activity",
    atmosphere="Highlighting the origin point of the earthquake.",
    style="Emphasized with brightness or contrast.",
    quality_meta="High resolution with clear depiction of the focus point.",
    HTML_web_color_name="red",
)

# Add the epicenter directly above the focus on the Earth's surface
canvas.add_local_description(
    name="epicenter",
    bbox=[45, 45, 5, 5],
    distance_to_viewer=3.0,
    description="The epicenter on the Earth's surface above the focus.",
    detailed_descriptions=[
        "A point on the Earth's surface directly above the focus represents the epicenter.",
        "It is shown on top of the Earth's crust.",
        "The epicenter is where the earthquake is felt strongest on the surface.",
        "It is depicted as a bright orange dot.",
    ],
    tags="epicenter, Earth's surface, above focus, strongest shaking",
    atmosphere="Emphasizing the point where the earthquake is felt.",
    style="Highlighted to stand out from the surface.",
    quality_meta="High resolution with clear depiction of the epicenter.",
    HTML_web_color_name="orange",
)

# Add seismic waves radiating from the epicenter
canvas.add_local_description(
    name="seismic_waves",
    bbox=[0, 0, 90, 90],
    distance_to_viewer=2.0,
    description="Seismic waves radiating outward from the epicenter.",
    detailed_descriptions=[
        "Curved lines spread out from the epicenter across the Earth's surface.",
        "These lines represent seismic waves spreading out.",
        "The waves are shown as concentric circles or curves.",
        "They indicate how the earthquake's energy travels.",
    ],
    tags="seismic waves, energy, earthquake, radiating, spreading",
    atmosphere="Dynamic representation of the earthquake's energy.",
    style="Curved lines spreading outward.",
    quality_meta="High resolution with clear, smooth lines.",
    HTML_web_color_name="yellow",
)
