from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description='A diagram showing how a lunar eclipse happens, with the Sun, Earth, and Moon aligned in space.',
    detailed_descriptions=[
        'The background is a dark, starry space, providing a backdrop for the celestial bodies.',
        'Stars are scattered across the dark space, twinkling softly.',
        'The Sun, Earth, and Moon are aligned in a straight line, illustrating the lunar eclipse.',
    ],
    tags='lunar eclipse, diagram, Sun, Earth, Moon, space, stars, alignment, celestial bodies, astronomy',
    HTML_web_color_name='black',
)

# Add the Sun
canvas.add_local_description(
    name='Sun',
    location='on the left',
    offset='no offset',
    area='a medium-sized square area',
    distance_to_viewer=5.0,
    description='The Sun, a bright yellow-orange sphere.',
    detailed_descriptions=[
        'The Sun is a large, glowing sphere on the left side of the image.',
        'It is bright yellow-orange in color, radiating light.',
        'Simple rays emanate from the Sun to show its brightness.',
    ],
    tags='Sun, star, bright, yellow, orange, sphere, glowing, light, rays',
    atmosphere='Glowing and radiant, emitting light.',
    style='Simple and clear, suitable for young learners.',
    quality_meta='High resolution with clear edges and bright colors.',
    HTML_web_color_name='yellow',
)

# Add the Earth
canvas.add_local_description(
    name='Earth',
    location='in the center',
    offset='no offset',
    area='a medium-sized square area',
    distance_to_viewer=5.0,
    description='The Earth, a blue and green sphere.',
    detailed_descriptions=[
        'The Earth is a sphere in the center of the image.',
        'It has blue oceans and green continents.',
        'The Earth is between the Sun and the Moon, showing the alignment.',
    ],
    tags='Earth, planet, blue, green, sphere, oceans, continents',
    atmosphere='Calm and steady, representing our planet.',
    style='Simple and clear, suitable for young learners.',
    quality_meta='High resolution with clear depiction of continents and oceans.',
    HTML_web_color_name='blue',
)

# Add the Moon
canvas.add_local_description(
    name='Moon',
    location='on the right',
    offset='no offset',
    area='a small square area',
    distance_to_viewer=5.0,
    description='The Moon, a smaller gray sphere.',
    detailed_descriptions=[
        'The Moon is a smaller sphere on the right side of the image.',
        'It is gray in color, representing the lunar surface.',
        'The Moon is within the Earth’s shadow, illustrating the lunar eclipse.',
    ],
    tags='Moon, satellite, gray, sphere, lunar surface, eclipse',
    atmosphere='Subtle and shadowed, representing the lunar eclipse.',
    style='Simple and clear, suitable for young learners.',
    quality_meta='High resolution with clear depiction.',
    HTML_web_color_name='gray',
)

# Add Earth's Shadow
canvas.add_local_description(
    name='Shadow Cone',
    location='in the center',
    offset='no offset',
    area='a large horizontal area',
    distance_to_viewer=6.0,
    description='A shadow cone extending from the Earth towards the Moon.',
    detailed_descriptions=[
        'A cone-shaped shadow extends from the Earth to the Moon.',
        'The shadow is darker near the Earth and fades towards the Moon.',
        'This shadow illustrates how the Earth blocks sunlight during a lunar eclipse.',
    ],
    tags='Earth’s shadow, shadow cone, lunar eclipse, alignment, shadow',
    atmosphere='Dark and subtle, representing the Earth’s shadow.',
    style='Simple shading to show the shadow cone.',
    quality_meta='High resolution with smooth shading.',
    HTML_web_color_name='dimgray',
)
