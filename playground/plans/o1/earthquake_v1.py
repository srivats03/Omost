from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description='A diagram showing how earthquakes happen, including the epicenter and fault lines.',
    detailed_descriptions=[
        'A cross-sectional view of the Earth displaying its layers.',
        'The crust at the top, with tectonic plates illustrated.',
        'Fault lines shown where tectonic plates meet and move.',
        'An earthquake focus point located underground along a fault line.',
        'The epicenter marked on the surface directly above the focus point.',
        'Seismic waves depicted radiating outward from the epicenter.',
        'The diagram explains how earthquakes occur due to movements along fault lines.',
        'An educational and clear image suitable for young students.',
    ],
    tags='earthquake, epicenter, fault lines, tectonic plates, seismic waves, Earth layers, crust, mantle, focus, educational, diagram, cross-section',
    HTML_web_color_name='lightgray',
)

# Add Earth's layers
canvas.add_local_description(
    name='Earth layers',
    location='in the center',
    offset='no offset',
    area='a large vertical area',
    distance_to_viewer=10.0,
    description="The Earth's layers shown in cross-section.",
    detailed_descriptions=[
        'A cross-sectional view of the Earth showing layers from crust to mantle.',
        'The crust is the thin, outermost layer at the top.',
        'The mantle lies beneath the crust, thicker and denser.',
        'Layers are colored differently to distinguish them.',
        'Helps visualize the inside structure of the Earth.',
    ],
    tags='Earth, layers, crust, mantle, cross-section, diagram',
    atmosphere='Educational and clear, suitable for young students.',
    style='Simple and colorful illustration.',
    quality_meta='High resolution with clear distinctions between layers.',
    HTML_web_color_name='sienna',
)

# Add tectonic plates
canvas.add_local_description(
    name='Tectonic plates',
    location='on the top',
    offset='no offset',
    area='a medium-sized horizontal area',
    distance_to_viewer=9.0,
    description="Tectonic plates on the Earth's crust.",
    detailed_descriptions=[
        'Pieces of the Earth\'s crust shown as tectonic plates.',
        'Plates fit together like puzzle pieces on the crust.',
        'Fault lines are where these plates meet.',
        'Plates are colored differently to distinguish them.',
        'They float on the mantle beneath.',
    ],
    tags='tectonic plates, crust, fault lines, Earth, diagram',
    atmosphere='Educational and clear.',
    style='Simple illustration showing plates as puzzle pieces.',
    quality_meta='High resolution with distinct plates and fault lines.',
    HTML_web_color_name='lightsteelblue',
)

# Add a fault line
canvas.add_local_description(
    name='Fault line',
    location='in the center',
    offset='slightly to the lower-left',
    area='a medium-sized vertical area',
    distance_to_viewer=9.0,
    description='A fault line where tectonic plates meet.',
    detailed_descriptions=[
        'A crack or line showing where two tectonic plates meet.',
        'Extends from the crust down into the mantle.',
        'Shown as a dark line to distinguish it.',
    ],
    tags='fault line, tectonic plates, Earth, diagram',
    atmosphere='Important for understanding earthquakes.',
    style='Simple line representing the fault.',
    quality_meta='Clear and distinct representation.',
    HTML_web_color_name='darkgray',
)

# Add the earthquake focus point
canvas.add_local_description(
    name='Focus point',
    location='in the center',
    offset='slightly to the lower-left',
    area='a small square area',
    distance_to_viewer=8.0,
    description='The earthquake focus point underground.',
    detailed_descriptions=[
        'A point underground where the earthquake starts.',
        'Located along a fault line beneath the surface.',
        'Shown as a bright spot or star to highlight it.',
        'Indicates the origin of seismic activity.',
    ],
    tags='focus point, earthquake origin, underground, seismic activity',
    atmosphere='Important and highlighted.',
    style='Simple symbol to represent the focus point.',
    quality_meta='Clear and distinct representation.',
    HTML_web_color_name='red',
)

# Add the epicenter on the surface
canvas.add_local_description(
    name='Epicenter',
    location='in the center',
    offset='slightly to the upper-left',
    area='a small square area',
    distance_to_viewer=7.0,
    description='The epicenter on the Earth\'s surface.',
    detailed_descriptions=[
        'Point on the surface directly above the focus point.',
        'Shown as a dot or symbol on the crust.',
        'Represents where the earthquake is felt strongest.',
    ],
    tags='epicenter, earthquake, surface point',
    atmosphere='Highlighted and important.',
    style='Simple symbol to represent the epicenter.',
    quality_meta='Clear and distinct representation.',
    HTML_web_color_name='orange',
)

# Add seismic waves radiating from the epicenter
canvas.add_local_description(
    name='Seismic waves',
    location='in the center',
    offset='no offset',
    area='a large square area',
    distance_to_viewer=6.0,
    description='Seismic waves radiating from the epicenter.',
    detailed_descriptions=[
        'Concentric circles or waves spreading out from the epicenter.',
        'Representing the energy released by the earthquake.',
        'Waves extend across the Earth\'s surface.',
    ],
    tags='seismic waves, earthquake, energy, waves',
    atmosphere='Dynamic and spreading.',
    style='Simple lines or circles to represent waves.',
    quality_meta='Clear and visually understandable.',
    HTML_web_color_name='yellow',
)
