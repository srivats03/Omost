from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas (starry background)
# canvas.set_global_description(
#     description='A diagram illustrating how the gravitational pull of the moon and sun affects ocean tides on Earth.',
#     detailed_descriptions=[
#         'The Earth is positioned in the center of the image, displaying the blue oceans and the landmasses.',
#         'The oceans on Earth show noticeable bulges on the sides facing the moon and the sun, representing high tides.',
#         'The background is the dark space filled with distant stars, emphasizing the celestial context.',
#         'The moon and the sun are positioned on opposite sides of the Earth, showing their relative positions in space.',
#         'The overall scene is simple and clear, focusing on the relationship between the Earth, moon, and sun in causing tides.',
#     ],
#     tags='Earth, moon, sun, ocean tides, gravitational pull, space, stars, high tide, low tide, diagram, celestial bodies, tidal bulges',
#     HTML_web_color_name='black',
# )

# # Add a low opacity blue oval depicting the ocean
# canvas.add_local_description(
#     location='in the center',
#     offset='no offset',
#     area='a small horizontal area',
#     distance_to_viewer=9.0,  # Maximum distance to place it behind the Earth
#     description='A low opacity blue oval representing the ocean stretched towards the Sun and Moon.',
#     detailed_descriptions=[
#         'A semi-transparent blue oval horizontally stretched across the center of the image.',
#         'The oval extends towards the left and right sides, pointing towards the Sun and Moon respectively.',
#         'The low opacity allows the starry background to be visible through the oval.',
#         'The oval symbolizes the Earth\'s ocean affected by the gravitational pull.',
#     ],
#     tags='ocean, blue oval, low opacity, semi-transparent, stretched, tides, gravitational pull',
#     atmosphere='Educational and clear, focusing on the depiction of ocean tides.',
#     style='Simplified and illustrative, suitable for educational purposes.',
#     quality_meta='High resolution with smooth gradients and transparency effects.',
#     HTML_web_color_name='aqua',
# )

# # Add the Earth in the middle
# canvas.add_local_description(
#     location='in the center',
#     offset='no offset',
#     area='a small square area',
#     distance_to_viewer=8.0,
#     description='The Earth depicted as a simple globe.',
#     detailed_descriptions=[
#         'A simplified illustration of the Earth placed at the center of the image.',
#         'The Earth is shown as a globe with minimal details of continents.',
#         'It is positioned on top of the blue oval, indicating the planet within the ocean depiction.',
#         'The globe is slightly smaller than the blue oval, allowing the oval to be visible around it.',
#     ],
#     tags='Earth, globe, planet, center, simple illustration',
#     atmosphere='Neutral and educational, focusing on Earth\'s position in the diagram.',
#     style='Simplified and clear, suitable for educational purposes.',
#     quality_meta='High resolution with clear edges and minimal details.',
#     HTML_web_color_name='blue',
# )

# # Add the Sun on the left side
# canvas.add_local_description(
#     location='on the left',
#     offset='slightly to the left',
#     area='a small square area',
#     distance_to_viewer=10.0,
#     description='The Sun depicted as a bright yellow circle.',
#     detailed_descriptions=[
#         'A simple bright yellow circle representing the Sun, positioned on the left side, vertically centered.',
#         'The Sun emits subtle rays extending outward, indicating its influence.',
#         'Its size is smaller compared to the Earth to fit the diagram\'s scale.',
#     ],
#     tags='Sun, yellow circle, bright, left side, gravitational pull',
#     atmosphere='Bright and educational, showing the Sun\'s position.',
#     style='Simplified and clear, suitable for educational purposes.',
#     quality_meta='High resolution with smooth edges and bright color.',
#     HTML_web_color_name='yellow',
# )

# # Add the Moon on the right side
# canvas.add_local_description(
#     location='on the right',
#     offset='slightly to the right',
#     area='a small square area',
#     distance_to_viewer=10.0,
#     description='The Moon depicted as a gray circle.',
#     detailed_descriptions=[
#         'A simple gray circle representing the Moon, positioned on the right side, vertically centered.',
#         'The Moon is smaller than the Earth but similar in size to the Sun in the diagram.',
#         'It has subtle crater markings to distinguish it as the Moon.',
#     ],
#     tags='Moon, gray circle, right side, gravitational pull',
#     atmosphere='Calm and educational, showing the Moon\'s position.',
#     style='Simplified and clear, suitable for educational purposes.',
#     quality_meta='High resolution with smooth edges and subtle details.',
#     HTML_web_color_name='lightgray',
# )

canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description='A diagram illustrating how the gravitational pull of the moon and sun affects ocean tides on Earth.',
    detailed_descriptions=[
        'The Earth is positioned in the center of the image, displaying the blue oceans and the landmasses.',
        'The oceans on Earth show noticeable bulges on the sides facing the moon and the sun, representing high tides.',
        'The background is the dark space filled with distant stars, emphasizing the celestial context.',
        'The moon and the sun are positioned on opposite sides of the Earth, showing their relative positions in space.',
        'The overall scene is simple and clear, focusing on the relationship between the Earth, moon, and sun in causing tides.',
    ],
    tags='Earth, moon, sun, ocean tides, gravitational pull, space, stars, high tide, low tide, diagram, celestial bodies, tidal bulges',
    HTML_web_color_name='black',
)

# Add the Earth in the center
canvas.add_local_description(
    location='in the center',
    offset='no offset',
    area='a small square area',
    distance_to_viewer=5.0,
    description='The Earth with visible oceans and landmasses.',
    detailed_descriptions=[
        'The Earth is prominently displayed in the center of the image, showing the blue oceans and green-brown continents.',
        'The oceans exhibit noticeable bulges on the sides facing the Moon and opposite the Moon, representing high tides.',
        'The areas of the Earth perpendicular to the Moon show lower water levels, representing low tides.',
        'The continents are accurately depicted, including recognizable shapes like Africa and Asia.',
        'The Earth\'s atmosphere is subtly visible as a thin blue layer around the planet.',
        'The Earth appears vibrant and detailed, emphasizing the focus on ocean tides influenced by gravitational forces.',
    ],
    tags='Earth, oceans, landmasses, continents, tidal bulges, blue planet, atmosphere, high tide, low tide',
    atmosphere='Educational and clear, focusing on Earth and its oceans.',
    style='Realistic yet simplified for clarity, suitable for educational purposes.',
    quality_meta='High resolution with clear details of Earth\'s surface and oceans.',
    HTML_web_color_name='blue',
)

# Add the Moon on the left side
canvas.add_local_description(
    location='on the left',
    offset='slightly to the left',
    area='a small square area',
    distance_to_viewer=10.0,
    description='The Moon showing its cratered surface.',
    detailed_descriptions=[
        'The Moon is positioned on the left side of the image, displaying its gray, cratered surface.',
        'It appears smaller than the Earth, indicating its relative size and distance.',
        'The Moon is shown fully illuminated, with craters and lunar maria visible.',
        'Its position illustrates its gravitational pull on Earth\'s oceans.',
        'The Moon faces the Earth, emphasizing the connection between the two bodies.',
    ],
    tags='Moon, cratered surface, gray, satellite, celestial body, gravitational pull',
    atmosphere='Calm and educational, focusing on the Moon\'s influence on tides.',
    style='Realistic with simplified details, suitable for educational purposes.',
    quality_meta='High resolution with clear depiction of the Moon\'s surface.',
    HTML_web_color_name='lightgray',
)

# Add the Sun on the right side
canvas.add_local_description(
    location='on the right',
    offset='slightly to the right',
    area='a small square area',
    distance_to_viewer=10.0,
    description='The Sun emitting light and heat.',
    detailed_descriptions=[
        'The Sun is positioned on the right side of the image, depicted as a bright, glowing sphere with a radiant aura.',
        'Solar flares and prominences are subtly illustrated, adding realism to the depiction.',
        'The Sun\'s rays extend outward, filling the right side of the image with warm light.',
        'It appears larger than both the Earth and the Moon, indicating its massive size in the solar system.',
        'The Sun\'s position shows its gravitational influence on Earth\'s tides, although less than the Moon.',
    ],
    tags='Sun, bright, glowing, rays, star, celestial body, gravitational pull',
    atmosphere='Warm and bright, emphasizing the Sun\'s role in tides.',
    style='Simplified and radiant, suitable for educational illustration.',
    quality_meta='High resolution with bright, glowing effects.',
    HTML_web_color_name='yellow',
)