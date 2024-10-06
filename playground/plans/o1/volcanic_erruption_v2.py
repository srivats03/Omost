
from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description='A diagram showing a volcanic eruption.',
    detailed_descriptions=[
        'At the center of the image is a volcano erupting with lava and ash.',
        'The volcano is shown in cross-section to reveal the magma chamber beneath.',
        'Lava is flowing down the sides of the volcano in bright red and orange streams.',
        'Ash and smoke are billowing from the top of the volcano into the sky.',
        'Underneath the volcano, the Earth\'s crust and mantle are visible in layers.',
        'The magma chamber is depicted beneath the volcano, filled with molten rock.',
        'The background is a clear blue sky with a few white clouds.',
        'The ground around the volcano has rocks and green vegetation.',
    ],
    tags='volcano, eruption, lava, ash, magma chamber, cross-section, Earth layers, crust, mantle, diagram, educational, rocks, vegetation, sky, clouds',
    HTML_web_color_name='saddlebrown',
)

# Add the erupting volcano
canvas.add_local_description(
    location='in the center',
    offset='no offset',
    area='a large vertical area',
    distance_to_viewer=5.0,
    description='An erupting volcano shown in cross-section.',
    detailed_descriptions=[
        'The volcano is centrally placed, displayed in cross-section to show internal structures.',
        'Bright red and orange lava is erupting from the top and flowing down the sides.',
        'The sides are brown and textured to represent rock and earth.',
        'Glowing lava streams flow down the volcano\'s slopes.',
    ],
    tags='volcano, eruption, cross-section, lava, rock, earth, glowing streams',
    atmosphere='Dynamic and educational, illustrating the eruption process.',
    style='Simple and clear, suitable for a 10-year-old student.',
    quality_meta='High resolution with clear lines and vibrant colors.',
    HTML_web_color_name='sienna',
)

# Add the magma chamber beneath the volcano
canvas.add_local_description(
    location='in the center',
    offset='slightly to the lower',
    area='a medium-sized square area',
    distance_to_viewer=6.0,
    description='A magma chamber filled with molten rock beneath the volcano.',
    detailed_descriptions=[
        'Directly below the volcano is the magma chamber, shown in bright reds and oranges.',
        'It appears as a large cavity filled with molten rock, connected to the volcano above.',
    ],
    tags='magma chamber, molten rock, beneath volcano, cavity',
    atmosphere='Informative, showing the source of the volcanic eruption.',
    style='Simple and clear, suitable for a 10-year-old student.',
    quality_meta='High resolution with clear lines and bright colors.',
    HTML_web_color_name='red',
)

# Add the Earth's crust and mantle layers
canvas.add_local_description(
    location='on the bottom',
    offset='no offset',
    area='a large horizontal area',
    distance_to_viewer=7.0,
    description='Layers of the Earth\'s crust and mantle beneath the volcano.',
    detailed_descriptions=[
        'At the bottom, the Earth\'s layers are shown in cross-section.',
        'A thin brown crust layer sits above the thicker mantle.',
        'The mantle is depicted in shades of orange and brown below the crust.',
    ],
    tags='Earth layers, crust, mantle, cross-section, layers',
    atmosphere='Educational, illustrating the Earth\'s structure beneath the volcano.',
    style='Simple and clear, suitable for a 10-year-old student.',
    quality_meta='High resolution with distinct layers and clear lines.',
    HTML_web_color_name='darkorange',
)

# Add ash and smoke billowing from the volcano
canvas.add_local_description(
    location='on the top',
    offset='no offset',
    area='a medium-sized vertical area',
    distance_to_viewer=4.0,
    description='Ash and smoke cloud rising from the volcano.',
    detailed_descriptions=[
        'Above the volcano, a large cloud of ash and smoke billows upward.',
        'The cloud is in shades of gray and black, spreading out at the top.',
    ],
    tags='ash cloud, smoke, eruption, billowing',
    atmosphere='Dynamic, showing the eruption\'s impact on the atmosphere.',
    style='Simple and clear, suitable for a 10-year-old student.',
    quality_meta='High resolution with contrasting colors and clear lines.',
    HTML_web_color_name='dimgray',
)

# Add ground with rocks and vegetation
canvas.add_local_description(
    location='on the bottom',
    offset='slightly to the upper',
    area='a medium-sized horizontal area',
    distance_to_viewer=6.0,
    description='Ground around the volcano with rocks and vegetation.',
    detailed_descriptions=[
        'Around the base, the ground has rocks and green vegetation like grass and bushes.',
        'This depicts the natural environment surrounding the volcano.',
    ],
    tags='ground, rocks, vegetation, environment, grass, bushes',
    atmosphere='Natural, showing the surroundings of the volcano.',
    style='Simple and clear, suitable for a 10-year-old student.',
    quality_meta='High resolution with natural colors and clear lines.',
    HTML_web_color_name='forestgreen',
)

# Add a clear sky with a few clouds
canvas.add_local_description(
    location='on the top',
    offset='slightly to the upper',
    area='a large horizontal area',
    distance_to_viewer=8.0,
    description='A clear blue sky with a few white clouds.',
    detailed_descriptions=[
        'Behind the ash cloud, a blue sky is visible at the top.',
        'There are a few white, fluffy clouds in the sky.',
    ],
    tags='sky, clouds, blue, background, fluffy',
    atmosphere='Calm and clear, contrasting with the eruption.',
    style='Simple and clear, suitable for a 10-year-old student.',
    quality_meta='High resolution with soft colors and clear lines.',
    HTML_web_color_name='skyblue',
)
