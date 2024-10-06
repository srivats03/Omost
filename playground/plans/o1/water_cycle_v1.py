from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description='A landscape illustrating the Water Cycle.',
    detailed_descriptions=[
        'The scene depicts a natural landscape with mountains, rivers, lakes, and the ocean.',
        'Above, the sky is clear with some clouds forming.',
        'The Sun is shining brightly in the sky.',
        'Water evaporates from the surface of the ocean and lakes.',
        'Clouds form in the sky as water vapor condenses.',
        'Rain falls from the clouds onto the land below.',
        'Water flows from the mountains through rivers back to the ocean.',
        'The overall image represents the continuous movement of water on Earth.',
    ],
    tags='water cycle, landscape, mountains, rivers, lakes, ocean, sky, clouds, sun, evaporation, condensation, precipitation, collection, natural, environment',
    HTML_web_color_name='skyblue',
)

# Add the Sun
canvas.add_local_description(
    name="Sun",
    location='on the top-right',
    offset='no offset',
    area='a small square area',
    distance_to_viewer=10.0,
    description='The bright Sun shining in the sky.',
    detailed_descriptions=[
        'The Sun is bright and yellow, positioned in the top-right corner of the image.',
        'It emits warm rays of light that illuminate the landscape below.',
        'The Sun is a key source of energy driving the water cycle.',
    ],
    tags='Sun, bright, yellow, sky, light, energy, water cycle',
    atmosphere='Warm and bright, symbolizing energy.',
    style='Simple and clear illustration suitable for children.',
    quality_meta='High resolution with vibrant colors.',
    HTML_web_color_name='gold',
)

# Add the Ocean
canvas.add_local_description(
    name="Ocean",
    location='on the bottom-left',
    offset='no offset',
    area='a medium-sized horizontal area',
    distance_to_viewer=7.0,
    description='A large body of water like an ocean or lake.',
    detailed_descriptions=[
        'The ocean stretches across the bottom-left of the image.',
        'Its surface is calm, reflecting the sky above.',
        'Water evaporates from the surface, rising into the sky as water vapor.',
    ],
    tags='ocean, water, surface, evaporation, water vapor, calm',
    atmosphere='Peaceful and expansive, representing the source of evaporation.',
    style='Realistic yet simple to understand for children.',
    quality_meta='High resolution with smooth textures.',
    HTML_web_color_name='deepskyblue',
)

# Add Evaporation
canvas.add_local_description(
    name="Evaporation",
    location='on the bottom-left',
    offset='slightly to the upper',
    area='a small vertical area',
    distance_to_viewer=6.5,
    description='Water vapor rising from the ocean into the sky.',
    detailed_descriptions=[
        'Thin, wispy clouds of water vapor rise from the surface of the ocean.',
        'The water vapor moves upward toward the sky, indicating evaporation.',
        'This represents the process of water turning into vapor due to the Sun\'s heat.',
    ],
    tags='evaporation, water vapor, rising, ocean, heat, Sun',
    atmosphere='Light and airy, showing the movement of water vapor.',
    style='Gentle and illustrative to help children understand.',
    quality_meta='High resolution with subtle details.',
    HTML_web_color_name='white',
)

# Add Clouds
canvas.add_local_description(
    name="Clouds",
    location='on the top',
    offset='no offset',
    area='a medium-sized horizontal area',
    distance_to_viewer=8.0,
    description='White clouds forming in the sky.',
    detailed_descriptions=[
        'Fluffy white clouds are gathered in the sky above the landscape.',
        'They are formed from condensed water vapor.',
        'The clouds are a key part of the water cycle, representing condensation.',
    ],
    tags='clouds, sky, condensation, water vapor, white, fluffy',
    atmosphere='Calm and serene, indicating condensation.',
    style='Soft and appealing to children.',
    quality_meta='High resolution with realistic cloud textures.',
    HTML_web_color_name='lightgray',
)

# Add Precipitation
canvas.add_local_description(
    name="Precipitation",
    location='in the center',
    offset='no offset',
    area='a medium-sized vertical area',
    distance_to_viewer=6.0,
    description='Rain falling from clouds to the land below.',
    detailed_descriptions=[
        'Droplets of rain fall from the clouds towards the land.',
        'The rain represents precipitation, a key stage in the water cycle.',
        'The raindrops are visible as lines or droplets between the clouds and the ground.',
    ],
    tags='rain, precipitation, clouds, droplets, water cycle',
    atmosphere='Refreshing and vital, showing the return of water to Earth.',
    style='Clear and simple to illustrate rain.',
    quality_meta='High resolution with visible raindrops.',
    HTML_web_color_name='cornflowerblue',
)

# Add Mountains
canvas.add_local_description(
    name="Mountains",
    location='on the right',
    offset='no offset',
    area='a medium-sized vertical area',
    distance_to_viewer=7.0,
    description='Tall mountains rising from the land.',
    detailed_descriptions=[
        'High mountains are depicted on the right side of the image.',
        'They have snowy peaks and are the source of rivers.',
        'Water from precipitation flows down the mountains as rivers.',
    ],
    tags='mountains, peaks, snow, rivers, land',
    atmosphere='Majestic and sturdy, representing collection of water.',
    style='Detailed but approachable for children.',
    quality_meta='High resolution with clear mountain features.',
    HTML_web_color_name='darkslategray',
)

# Add Rivers
canvas.add_local_description(
    name="Rivers",
    location='on the bottom-right',
    offset='slightly to the left',
    area='a small vertical area',
    distance_to_viewer=5.5,
    description='Rivers flowing from the mountains to the ocean.',
    detailed_descriptions=[
        'Blue rivers flow from the mountains down towards the ocean.',
        'They wind through the landscape, collecting water from precipitation.',
        'The rivers represent the collection and movement of water back to the ocean.',
    ],
    tags='rivers, water, flow, mountains, collection, ocean',
    atmosphere='Flowing and continuous, showing the movement of water.',
    style='Smooth and clear to illustrate river paths.',
    quality_meta='High resolution with gentle curves.',
    HTML_web_color_name='royalblue',
)