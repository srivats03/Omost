from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description='A diagram illustrating the process of photosynthesis in a plant.',
    detailed_descriptions=[
        'Vibrant green plant in the center showing photosynthesis.',
        'Sun shines brightly, providing energy for the plant.',
        'Carbon dioxide absorbed by the leaves.',
        'Water absorbed by the roots from the soil.',
        'Oxygen released into the air from the leaves.',
        'Clear blue sky with a few fluffy clouds in the background.',
        'Rich brown soil showing roots absorbing water.',
    ],
    tags='photosynthesis, plant, sun, sunlight, carbon dioxide, oxygen, water, roots, leaves, energy, process, diagram, illustration, absorption, release, air, soil, sky, clouds',
    HTML_web_color_name='lightgreen',
)

# Add the sun shining brightly.
canvas.add_local_description(
    name='sun',
    location='on the top-right',
    offset='no offset',
    area='a medium-sized square area',
    distance_to_viewer=10.0,
    description='Bright yellow sun shining.',
    detailed_descriptions=[
        'Bright yellow sun on the top-right corner.',
        'Sun rays extend outward to the plant.',
        'Sun glowing warmly against blue sky.',
    ],
    tags='sun, sunlight, bright, yellow, glowing, energy, sky',
    atmosphere='Bright and cheerful, providing energy for the plant.',
    style='Simple and clear illustration, suitable for children.',
    quality_meta='High resolution with vivid colors and defined shapes.',
    HTML_web_color_name='yellow',
)

# Add a green plant with leaves and roots.
canvas.add_local_description(
    name='plant',
    location='in the center',
    offset='no offset',
    area='a large vertical area',
    distance_to_viewer=5.0,
    description='Green plant with leaves and roots.',
    detailed_descriptions=[
        'Vibrant green plant in the center.',
        'Plant has broad green leaves.',
        'Roots extend downward into soil.',
        'Sturdy stem supports the leaves.',
    ],
    tags='plant, leaves, roots, stem, green, photosynthesis, absorption',
    atmosphere='Healthy and vibrant, actively undergoing photosynthesis.',
    style='Detailed yet simple, clear depiction of plant structure.',
    quality_meta='High resolution with clear lines and bright colors.',
    HTML_web_color_name='forestgreen',
)

# Add rich brown soil showing roots.
canvas.add_local_description(
    name='soil',
    location='on the bottom',
    offset='no offset',
    area='a large horizontal area',
    distance_to_viewer=5.0,
    description='Rich brown soil showing roots.',
    detailed_descriptions=[
        'Dark brown soil at the bottom.',
        'Roots visible within the soil.',
        'Small water droplets near the roots.',
    ],
    tags='soil, roots, water, absorption, brown, earth',
    atmosphere='Nurturing and fertile, supporting plant growth.',
    style='Textured depiction of soil with visible roots.',
    quality_meta='High resolution with detailed textures.',
    HTML_web_color_name='saddlebrown',
)

# Add small bubbles representing carbon dioxide entering leaves.
canvas.add_local_description(
    name='carbon_dioxide',
    location='on the left',
    offset='slightly to the upper-right',
    area='a small square area',
    distance_to_viewer=5.0,
    description='Small bubbles representing carbon dioxide entering leaves.',
    detailed_descriptions=[
        'Small light grey bubbles near leaves on the left side.',
        'Bubbles represent carbon dioxide molecules.',
        'Moving toward the leaves.',
    ],
    tags='carbon dioxide, gas, bubbles, absorption, leaves',
    atmosphere='Subtle, indicating gas absorption by the plant.',
    style='Simple illustrations of gas molecules as bubbles.',
    quality_meta='Clear and minimalistic representation.',
    HTML_web_color_name='lightgray',
)

# Add small bubbles representing oxygen exiting leaves.
canvas.add_local_description(
    name='oxygen',
    location='on the right',
    offset='slightly to the upper-left',
    area='a small square area',
    distance_to_viewer=5.0,
    description='Small bubbles representing oxygen exiting leaves.',
    detailed_descriptions=[
        'Small light blue bubbles near leaves on the right side.',
        'Bubbles represent oxygen molecules.',
        'Moving away from the leaves.',
    ],
    tags='oxygen, gas, bubbles, release, leaves',
    atmosphere='Subtle, indicating gas release by the plant.',
    style='Simple illustrations of gas molecules as bubbles.',
    quality_meta='Clear and minimalistic representation.',
    HTML_web_color_name='lightblue',
)

# Add water droplets being absorbed by roots.
canvas.add_local_description(
    name='water',
    location='on the bottom-left',
    offset='no offset',
    area='a small vertical area',
    distance_to_viewer=5.0,
    description='Water droplets being absorbed by roots.',
    detailed_descriptions=[
        'Small blue droplets near roots in the soil.',
        'Droplets represent water being absorbed.',
        'Moving toward the roots.',
    ],
    tags='water, absorption, roots, droplets, soil',
    atmosphere='Nurturing, showing hydration of the plant.',
    style='Simple depiction of water droplets.',
    quality_meta='Clear and minimalistic representation.',
    HTML_web_color_name='blue',
)

# Add a clear blue sky with few fluffy clouds.
canvas.add_local_description(
    name='sky',
    location='on the top',
    offset='no offset',
    area='a large horizontal area',
    distance_to_viewer=10.0,
    description='Clear blue sky with few fluffy clouds.',
    detailed_descriptions=[
        'Light blue sky fills the background.',
        'Small fluffy white clouds scattered in the sky.',
        'Sky provides a calm backdrop.',
    ],
    tags='sky, clouds, blue, background, atmosphere',
    atmosphere='Calm and clear, indicating a sunny day.',
    style='Simple and bright depiction of the sky.',
    quality_meta='High resolution with soft colors.',
    HTML_web_color_name='skyblue',
)