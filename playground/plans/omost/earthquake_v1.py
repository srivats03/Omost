from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description='A diagram explaining how earthquakes happen, including epicenter and fault lines.',
    detailed_descriptions=[
        'This diagram provides a clear explanation of how earthquakes occur, focusing on the epicenter and fault lines.',
        'The central part of the diagram features a detailed illustration of the Earth’s crust with tectonic plates in motion.',
        'The epicenter is marked with a red dot, surrounded by concentric circles representing different seismic intensity levels.',
        'Fault lines are depicted as jagged lines running through the tectonic plates, with arrows indicating the direction of plate movement.',
        'The surrounding area includes explanatory text and annotations to highlight the key concepts and processes involved in earthquake formation.',
        'Additional details, such as the stress buildup and sudden release of energy, are also illustrated.',
        'The overall design is educational, with a balanced use of visual elements and text to ensure that the information is conveyed effectively.',
    ],
    tags='diagram, earthquake, epicenter, fault lines, tectonic plates, seismic intensity, plate movement, stress buildup, energy release, educational, illustration, Earth’s crust, motion, concentric circles, arrows, key concepts, processes, explanation, text, annotations',
    HTML_web_color_name='lightgray',
)

# Add the epicenter marked with a red dot.
canvas.add_local_description(
    name="epicenter",
    location='in the center',
    offset='no offset',
    area='a medium-sized square area',
    distance_to_viewer=1.0,
    description='The epicenter marked with a red dot.',
    detailed_descriptions=[
        'The epicenter is depicted as a red dot in the center of the diagram.',
        'This dot represents the point on the Earth’s surface directly above the location where the earthquake occurs.',
        'Surrounding the epicenter are concentric circles, each representing a different seismic intensity level, ranging from low to high.',
        'The concentric circles help to illustrate the varying degrees of impact felt at different distances from the epicenter.',
    ],
    tags='epicenter, red dot, concentric circles, seismic intensity, Earth’s surface, location, earthquake, impact, degrees, distance, illustration, point, center, diagram, explanation, educational, visual element, key concept',
    atmosphere='Educational and focused on explaining key concepts.',
    style='Detailed and clear illustration with balanced use of visual elements.',
    quality_meta='High-quality, educational illustration with clear visual elements.',
    HTML_web_color_name='red',
)

# Add tectonic plates in motion with fault lines.
canvas.add_local_description(
    name="tectonic_plates",
    location='on the bottom',
    offset='slightly to the right',
    area='a large horizontal area',
    distance_to_viewer=1.5,
    description='Tectonic plates in motion with fault lines.',
    detailed_descriptions=[
        'The bottom part of the diagram shows the Earth’s crust with tectonic plates in motion.',
        'These plates are illustrated with different colors and textures to differentiate between them.',
        'Fault lines are depicted as jagged lines running through the plates, with arrows indicating the direction of plate movement.',
        'This section aims to explain the process of plate tectonics and how fault lines form as a result of the movement and interaction between plates.',
    ],
    tags='tectonic plates, motion, Earth’s crust, fault lines, jagged lines, arrows, plate movement, interaction, process, plate tectonics, illustration, diagram, educational, explanation, key concept, textures, colors, movement, interaction, formation',
    atmosphere='Dynamic and educational, focusing on the movement of tectonic plates.',
    style='Illustrative with detailed textures and colors to differentiate between plates.',
    quality_meta='High-quality illustration with detailed textures and colors.',
    HTML_web_color_name='darkslategray',
)

# Add explanatory text and annotations.
canvas.add_local_description(
    name="annotations",
    location='on the top-left',
    offset='slightly to the lower-right',
    area='a small square area',
    distance_to_viewer=2.0,
    description='Explanatory text and annotations.',
    detailed_descriptions=[
        'This section includes explanatory text and annotations that provide additional information about the diagram.',
        'The text explains key concepts such as the formation of earthquakes, the role of fault lines and the epicenter, and the processes involved in plate tectonics.',
        'Annotations are used to highlight specific parts of the diagram, providing a clear and concise explanation of the information presented.',
        'This section is designed to support the visual elements of the diagram and ensure that the viewer understands the key concepts.',
    ],
    tags='explanatory text, annotations, key concepts, formation, earthquakes, fault lines, epicenter, processes, plate tectonics, diagram, illustration, educational, explanation, information, support, visual elements, viewer, understanding, clear, concise',
    atmosphere='Informative and supportive, designed to enhance understanding.',
    style='Clear and concise with supportive annotations.',
    quality_meta='High-quality text and annotations that support the visual elements.',
    HTML_web_color_name='black',
)

# Add stress buildup and sudden release of energy.
canvas.add_local_description(
    name="Stress",
    location='on the right',
    offset='slightly to the lower-left',
    area='a medium-sized vertical area',
    distance_to_viewer=1.2,
    description='Stress buildup and sudden release of energy.',
    detailed_descriptions=[
        'This section of the diagram illustrates the process of stress buildup and the sudden release of energy that occurs during an earthquake.',
        'It includes visual elements such as arrows and waves to represent the buildup of stress and the subsequent release of energy.',
        'This section aims to explain the mechanical processes involved in earthquake formation, providing a detailed and clear representation of the stress and energy dynamics.',
    ],
    tags='stress buildup, energy release, earthquake, visual elements, arrows, waves, stress, energy, dynamics, mechanical processes, formation, diagram, illustration, educational, explanation, key concept, detailed, clear, representation',
    atmosphere='Mechanically dynamic and educational, focusing on stress and energy.',
    style='Illustrative with detailed visual elements to represent stress and energy dynamics.',
    quality_meta='High-quality illustration with detailed visual elements.',
    HTML_web_color_name='darkorange',
)

# Add annotations highlighting key concepts.
canvas.add_local_description(
    name="annotations",
    location='on the bottom-left',
    offset='slightly to the upper-right',
    area='a small square area',
    distance_to_viewer=1.8,
    description='Annotations highlighting key concepts.',
    detailed_descriptions=[
        'This section includes annotations that highlight key concepts and processes involved in earthquake formation.',
        'The annotations are designed to be concise yet informative, providing additional information to support the visual elements of the diagram.',
        'This section aims to enhance the viewer’s understanding by providing clear and specific explanations of the key concepts, such as fault lines, epicenters, and stress buildup.',
    ],
    tags='annotations, key concepts, processes, earthquake formation, concise, informative, additional information, support, visual elements, diagram, illustration, educational, explanation, viewer, understanding, clear, specific, explanations',
    atmosphere='Informative and supportive, enhancing understanding with clear explanations.',
    style='Concise and informative with clear annotations.',
    quality_meta='High-quality annotations that support the visual elements.',
    HTML_web_color_name='dimgray',
)
