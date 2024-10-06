from lib_omost.canvas import Canvas

canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description='A simple diagram explaining photosynthesis to a 10-year-old student.',
    detailed_descriptions=[
        'A bright and colorful illustration depicting the process of photosynthesis in a simple and easy-to-understand manner.',
        'The scene includes a green plant absorbing sunlight, water, and carbon dioxide, and producing oxygen.',
        'All elements are depicted in a child-friendly style with vivid colors.',
        'The background is a clear blue sky with a bright sun.',
        'The overall atmosphere is cheerful and educational, aiming to engage young students.',
    ],
    tags='photosynthesis, diagram, plant, sun, water, carbon dioxide, oxygen, simple, child-friendly, bright, colorful, educational',
    HTML_web_color_name='white',
)

# Add a bright sun
canvas.add_local_description(
    location='on the top-right',
    offset='no offset',
    area='a small square area',
    distance_to_viewer=2.0,
    description='A bright yellow sun shining.',
    detailed_descriptions=[
        'A radiant yellow sun located in the top-right corner of the image.',
        'The sun has simple rays extending outward, symbolizing sunlight.',
        'It provides the light energy necessary for the plant\'s photosynthesis.',
    ],
    tags='sun, sunlight, bright, yellow, shining, rays, energy, photosynthesis',
    atmosphere='Bright and cheerful, providing energy to the plant.',
    style='Simple and friendly illustration suitable for children.',
    quality_meta='High resolution with vivid colors and clear details.',
    HTML_web_color_name='yellow',
)

# Add the green plant
canvas.add_local_description(
    location='in the center',
    offset='slightly to the upper',
    area='a medium-sized vertical area',
    distance_to_viewer=3.0,
    description='A green plant with leaves.',
    detailed_descriptions=[
        'A healthy green plant positioned at the center of the image.',
        'The plant has several broad green leaves and a sturdy brown stem.',
        'The leaves are facing upwards, indicating growth and vitality.',
        'The plant symbolizes the main organism performing photosynthesis.',
    ],
    tags='plant, green, leaves, stem, photosynthesis, healthy, growth, vitality',
    atmosphere='Vibrant and lively, representing life and growth.',
    style='Simple and friendly illustration suitable for children.',
    quality_meta='High resolution with vivid colors and clear details.',
    HTML_web_color_name='forestgreen',
)

# Add roots
canvas.add_local_description(
    location='in the center',
    offset='slightly to the lower',
    area='a small vertical area',
    distance_to_viewer=3.0,
    description='Roots of the plant growing down',
    detailed_descriptions=[
        'The plant\'s roots extend downward into the soil.',
        'The roots are shown absorbing water and nutrients.',
        'They branch out to show how they spread through the soil.',
        'The roots are depicted in a way that is easy for children to understand.',
    ],
    tags='roots, plant, absorption, water, nutrients, soil, growth, photosynthesis',
    atmosphere='Essential and foundational, representing the plant\'s uptake of nutrients.',
    style='Simple and friendly illustration suitable for children.',
    quality_meta='High resolution with clear details.',
    HTML_web_color_name='sienna',
)

# Add brown soil
canvas.add_local_description(
    location='on the bottom',
    offset='no offset',
    area='a large horizontal area',
    distance_to_viewer=2.0,
    description='Cross-section of ground showing brown soil',
    detailed_descriptions=[
        'Rich brown soil depicted at the bottom of the image.',
        'The soil is shown in a cross-sectional view, illustrating where the roots grow.',
        'It provides nutrients and support for the plant\'s growth.',
    ],
    tags='soil, ground, brown, earth, nutrients, foundation, plant growth, photosynthesis',
    atmosphere='Stable and nurturing, representing the foundation for plant growth.',
    style='Simple and friendly illustration suitable for children.',
    quality_meta='High resolution with vivid colors and clear details.',
    HTML_web_color_name='saddlebrown',
)

# Add blue water droplets near roots
canvas.add_local_description(
    location='on the bottom',
    offset='no offset',
    area='a small square area',
    distance_to_viewer=4.0,
    description='Blue water droplets near the roots.',
    detailed_descriptions=[
        'Several blue water droplets near the bottom-left, close to the roots.',
        'The droplets represent water being absorbed by the plant.',
    ],
    tags='water, droplets, blue, absorption, roots, plant, photosynthesis',
    atmosphere='Refreshing and essential, representing vital nutrients.',
    style='Simple and friendly illustration suitable for children.',
    quality_meta='High resolution with vivid colors and clear details.',
    HTML_web_color_name='deepskyblue',
)

# Add grey carbon dioxide bubbles
canvas.add_local_description(
    location='on the left',
    offset='slightly to the upper',
    area='a small vertical area',
    distance_to_viewer=7.0,
    description='Grey bubbles representing carbon dioxide entering the leaves.',
    detailed_descriptions=[
        'Small grey bubbles near the leaves on the left side of the plant.',
        'The bubbles are moving towards the leaves, symbolizing absorption.',
    ],
    tags='carbon dioxide, bubbles, grey, absorption, leaves, plant, photosynthesis',
    atmosphere='Vital and necessary, representing gases absorbed by the plant.',
    style='Simple and friendly illustration suitable for children.',
    quality_meta='High resolution with clear details.',
    HTML_web_color_name='lightgrey',
)

# Add red oxygen bubbles
canvas.add_local_description(
    location='on the right',
    offset='slightly to the upper',
    area='a small vertical area',
    distance_to_viewer=7.0,
    description='Red bubbles representing oxygen released from the leaves.',
    detailed_descriptions=[
        'Small red bubbles near the leaves on the right side of the plant.',
        'The bubbles are moving away from the leaves, symbolizing release.',
    ],
    tags='oxygen, bubbles, red, release, leaves, plant, photosynthesis',
    atmosphere='Vital and life-giving, representing gases released by the plant.',
    style='Simple and friendly illustration suitable for children.',
    quality_meta='High resolution with clear details.',
    HTML_web_color_name='tomato',
)

# Add a clear blue sky background
canvas.add_local_description(
    location='on the top',
    offset='no offset',
    area='a large horizontal area',
    distance_to_viewer=1.0,
    description='A clear blue sky.',
    detailed_descriptions=[
        'A bright blue sky filling the background of the image.',
        'The sky is clear with no clouds, emphasizing a sunny day.',
        'It adds to the cheerful and educational atmosphere of the diagram.',
    ],
    tags='sky, blue, clear, background, sunny, cheerful, educational',
    atmosphere='Calm and bright, enhancing the overall positivity.',
    style='Simple and friendly illustration suitable for children.',
    quality_meta='High resolution with vivid colors.',
    HTML_web_color_name='skyblue',
)
