from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description='A diagram explaining Tidal Movements, showing how the gravitational pull of the moon and sun affect the ocean tides, to a 10-year-old student.',
    detailed_descriptions=[
        'The diagram is designed to be simple and easy to understand for a 10-year-old student.',
        'It includes illustrations of the Earth, Moon, and Sun, with arrows showing the gravitational pull.',
        'The ocean is represented by blue waves, and the tides are shown with rising and falling arrows.',
        'The diagram also includes labels and explanations in a clear and concise manner.',
        'The colors are bright and engaging, with a mix of blues and whites to highlight the ocean and space elements.',
        'The overall design is visually appealing and organized, making it easy for young students to follow along and understand the concept of tidal movements.',
    ],
    tags='diagram, tidal movements, gravitational pull, moon, sun, ocean tides, 10-year-old, student, Earth, arrows, blue waves, rising tides, falling tides, labels, explanations, bright colors, blues, whites, ocean, space, visually appealing, organized, concept, understanding',
    HTML_web_color_name='skyblue',
)

# Add illustration of the earth
canvas.add_local_description(
    location='in the center',
    offset='no offset',
    area='a large square area',
    distance_to_viewer=1.0,
    description='Illustration of the Earth',
    detailed_descriptions=[
        'The Earth is depicted as a blue sphere, representing the planet we live on.',
        'It has a few continents and oceans marked with simple lines.',
        'The Earth is positioned centrally to draw attention to its importance in the diagram.',
        'The illustration is colorful and easy to recognize, making it clear for young students.',
    ],
    tags='Earth, blue sphere, continents, oceans, simple lines, colorful, easy to recognize, central position, important, diagram, illustration, student, young, learning, planet, globe, geographical, educational',
    atmosphere='Educational and engaging, designed for young learners.',
    style='Simple and colorful, with a focus on clarity and recognition.',
    quality_meta='High-quality illustration with clear lines and colors.',
    HTML_web_color_name='dodgerblue',
)

# Add illustration of the moon
canvas.add_local_description(
    location='on the top-left',
    offset='no offset',
    area='a medium-sized square area',
    distance_to_viewer=1.5,
    description='Illustration of the Moon',
    detailed_descriptions=[
        'The Moon is illustrated as a small, bright, white sphere, with shadows to give it a three-dimensional look.',
        'It has a few craters marked with simple dots.',
        'The Moon is shown with an arrow pointing towards the Earth, indicating the gravitational pull.',
        'The illustration is clear and easy to understand, with a focus on the concept of the Moon’s influence on the tides.',
    ],
    tags='Moon, white sphere, shadows, three-dimensional, craters, simple dots, arrow, gravitational pull, influence, tides, illustration, clear, easy to understand, concept, educational, student, young, learning, space, celestial body',
    atmosphere='Clear and educational, with a focus on the Moon’s influence.',
    style='Simple and three-dimensional, with clear arrows and shadows.',
    quality_meta='High-quality illustration with clear shadows and arrows.',
    HTML_web_color_name='whitesmoke',
)

# Add illustration of the sun
canvas.add_local_description(
    location='on the top-right',
    offset='no offset',
    area='a medium-sized square area',
    distance_to_viewer=1.5,
    description='Illustration of the Sun',
    detailed_descriptions=[
        'The Sun is illustrated as a bright, yellow circle with rays extending outwards.',
        'The Sun is shown with an arrow pointing towards the Earth, indicating the gravitational pull.',
        'The illustration is vibrant and clear, with a focus on the Sun’s influence on the tides.',
        'The rays are simple and extend outwards to represent the light and heat the Sun emits.',
    ],
    tags='Sun, bright, yellow circle, rays, arrows, gravitational pull, influence, tides, illustration, vibrant, clear, concept, educational, student, young, learning, space, celestial body, light, heat',
    atmosphere='Vibrant and educational, with a focus on the Sun’s influence.',
    style='Simple and vibrant, with clear arrows and rays.',
    quality_meta='High-quality illustration with vibrant colors and clear arrows.',
    HTML_web_color_name='goldenrod',
)

# Add illustration of the ocean tides
canvas.add_local_description(
    location='on the bottom',
    offset='no offset',
    area='a large horizontal area',
    distance_to_viewer=1.0,
    description='Illustration of the Ocean Tides',
    detailed_descriptions=[
        'The ocean tides are illustrated with blue waves, showing rising and falling arrows.',
        'The arrows are simple and easy to understand, indicating the movement of the tides.',
        'The blue waves are colorful and give a sense of motion to the diagram.',
        'The illustration is designed to be visually appealing and easy to follow, making it easy for young students to understand the concept of tidal movements.',
    ],
    tags='ocean tides, blue waves, rising arrows, falling arrows, simple, easy to understand, movement, illustration, colorful, motion, visually appealing, easy to follow, concept, educational, student, young, learning, ocean, tides, diagram',
    atmosphere='Visually appealing and easy to follow, designed for young learners.',
    style='Colorful and dynamic, with rising and falling arrows.',
    quality_meta='High-quality illustration with colorful waves and clear arrows.',
    HTML_web_color_name='deepskyblue',
)
