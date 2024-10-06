from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description='A diagram of the Earth, Moon, and Sun demonstrating tidal movements caused by gravitational pull.',
    detailed_descriptions=[
        'The Earth is at the center of the image, shown as a blue and green sphere representing land and oceans.',
        'The Moon is positioned to the right of the Earth, depicted as a smaller grey sphere.',
        'The Sun is placed to the left of the Earth, illustrated as a large yellow sphere emitting rays.',
        'The ocean tides on Earth are exaggerated, showing bulges on the sides facing the Moon and the opposite side.',
        'The background is a dark space with scattered stars, emphasizing the celestial setting.',
        "The overall image explains how the gravitational forces of the Moon and Sun affect Earth's tides.",
    ],
    tags='Earth, Moon, Sun, tides, gravitational pull, ocean bulges, space, diagram, celestial bodies, orbit',
    HTML_web_color_name='black',
)

# Add the Earth with exaggerated ocean bulges
canvas.add_local_description(
    location='in the center',
    offset='no offset',
    area='a large square area',
    distance_to_viewer=5.0,
    description='The Earth with exaggerated ocean bulges.',
    detailed_descriptions=[
        'A blue and green sphere representing the Earth is at the center.',
        'The Earth shows exaggerated ocean bulges on the sides facing the Moon and the opposite side.',
        'Continents are simplified for clarity, focusing on the concept of tides.',
        'The Earth is tilted slightly to show the bulges clearly.',
    ],
    tags='Earth, ocean bulges, tides, blue, green, sphere, continents, exaggerated',
    atmosphere='Educational and informative, suitable for a 10-year-old student.',
    style='Simple and clear diagrammatic style with bold colors.',
    quality_meta='High resolution, clear and easy to understand visuals.',
    HTML_web_color_name='blue',
)

# Add the Moon
canvas.add_local_description(
    location='on the right',
    offset='no offset',
    area='a small square area',
    distance_to_viewer=7.0,
    description='The Moon.',
    detailed_descriptions=[
        'A smaller grey sphere representing the Moon is positioned to the right of the Earth.',
        'The Moon is shown in proportion to the Earth for scale.',
        'The surface of the Moon has subtle craters for realism.',
    ],
    tags='Moon, grey, sphere, craters, satellite',
    atmosphere='Educational and informative.',
    style='Simple and clear, matching the style of the Earth.',
    quality_meta='High resolution, clear depiction of the Moon.',
    HTML_web_color_name='grey',
)

# Add the Sun
canvas.add_local_description(
    location='on the left',
    offset='no offset',
    area='a medium-sized square area',
    distance_to_viewer=7.0,
    description='The Sun emitting rays.',
    detailed_descriptions=[
        'A large yellow sphere representing the Sun is positioned to the left of the Earth.',
        'The Sun emits stylized rays to indicate its brightness.',
        'The Sun is shown larger than the Earth and Moon but adjusted to fit the diagram.',
    ],
    tags='Sun, yellow, sphere, rays, star, brightness',
    atmosphere='Educational and informative.',
    style='Simple and clear, consistent with other elements.',
    quality_meta='High resolution, clear depiction of the Sun.',
    HTML_web_color_name='yellow',
)

# Add the space background
canvas.add_local_description(
    location='in the center',
    offset='no offset',
    area='a large square area',
    distance_to_viewer=10.0,
    description='A dark space background with scattered stars.',
    detailed_descriptions=[
        'The background is a dark space filled with small white stars.',
        'Stars vary slightly in size to create depth.',
        'The space background provides context for the celestial bodies.',
    ],
    tags='space, stars, dark background, celestial, universe',
    atmosphere='Calm and vast, representing outer space.',
    style='Simple and clear, not distracting from the main elements.',
    quality_meta='High resolution, clear but subtle starry background.',
    HTML_web_color_name='black',
)
