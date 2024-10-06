from lib_omost.canvas import Canvas

# Initialize the canvas
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
    area='a large square area',
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
    offset='no offset',
    area='a medium-sized square area',
    distance_to_viewer=6.0,
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
    offset='no offset',
    area='a large square area',
    distance_to_viewer=7.0,
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