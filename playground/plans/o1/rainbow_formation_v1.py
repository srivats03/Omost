from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description='A diagram showing how a rainbow forms when sunlight passes through raindrops.',
    detailed_descriptions=[
        'The diagram illustrates the formation of a rainbow through the interaction of sunlight and raindrops.',
        'On the left side, the sun shines brightly, emitting rays of light towards the right.',
        'Raindrops fall from a cloud on the right side, interacting with the sunlight.',
        'A colorful rainbow arcs across the center of the image, connecting the sun and the raindrops.',
        'The background features a clear blue sky with a few fluffy white clouds.',
        'Below, a simple green field with grass provides a natural base for the scene.',
        'The diagram is designed to help explain the process of rainbow formation in an easy-to-understand way.',
    ],
    tags='rainbow, sunlight, raindrops, refraction, reflection, dispersion, sky, clouds, landscape, diagram, formation, light, nature, weather, science, education',
    HTML_web_color_name='skyblue',
)

# Add the sky
canvas.add_local_description(
    name="Sky",
    location='in the center',
    offset='no offset',
    area='a large square area',
    distance_to_viewer=11.0,
    description='A clear blue sky with fluffy white clouds.',
    detailed_descriptions=[
        'The entire background of the image is filled with a soft blue sky.',
        'Fluffy white clouds are scattered across the sky, adding depth to the scene.',
        'The sky provides a bright and cheerful backdrop for the other elements in the diagram.',
        'The blue color of the sky is consistent and smooth throughout the image.',
    ],
    tags='sky, blue, clouds, background, atmosphere, clear, bright, cheerful, nature',
    atmosphere='Bright and clear, representing a typical sunny day.',
    style='Simple and clean, suitable for an educational diagram.',
    quality_meta='High resolution with smooth gradients and soft colors.',
    HTML_web_color_name='skyblue',
)

# Add the sun
canvas.add_local_description(
    name="Sun",
    location='on the left',
    offset='slightly to the upper',
    area='a small square area',
    distance_to_viewer=10.0,
    description='A bright yellow sun shining.',
    detailed_descriptions=[
        'A bright yellow sun is positioned in the upper-left corner of the image.',
        'The sun is depicted as a simple circle with straight rays extending outward.',
        'Sun rays are drawn as straight lines radiating from the sun towards the center.',
        'The sun provides the light necessary for forming the rainbow in the diagram.',
        'The rays reach toward the raindrops on the right side, illustrating the path of sunlight.',
    ],
    tags='sun, sunlight, bright, shining, yellow, rays, light, circle, source',
    atmosphere='Bright and cheerful, symbolizing the source of light.',
    style='Simple and clear, suitable for an educational diagram.',
    quality_meta='High resolution with clear lines and bright colors.',
    HTML_web_color_name='yellow',
)

# Add the rain cloud
canvas.add_local_description(
    name="Cloud",
    location='on the right',
    offset='slightly to the upper',
    area='a medium-sized vertical area',
    distance_to_viewer=9.0,
    description='A gray cloud with raindrops falling.',
    detailed_descriptions=[
        'A fluffy gray cloud is positioned in the upper-right corner of the image.',
        'From the bottom of the cloud, blue raindrops fall toward the ground below.',
        'The raindrops are teardrop-shaped and evenly spaced.',
        'The cloud represents the source of raindrops needed to form a rainbow.',
        'The raindrops interact with the sunlight to create the colorful rainbow arc.',
    ],
    tags='cloud, rain, raindrops, gray, water, precipitation, fluffy, weather',
    atmosphere='Calm and natural, representing the occurrence of rain.',
    style='Simple and clear, suitable for an educational diagram.',
    quality_meta='High resolution with clear lines and soft colors.',
    HTML_web_color_name='lightgray',
)

# Add the rainbow
canvas.add_local_description(
    name="Rainbow",
    location='in the center',
    offset='no offset',
    area='a large horizontal area',
    distance_to_viewer=8.0,
    description='A bright, colorful rainbow arc.',
    detailed_descriptions=[
        'A vibrant rainbow arcs across the center of the image, stretching from left to right.',
        'The rainbow displays red, orange, yellow, green, blue, indigo, and violet colors in order.',
        'It appears between the sun on the left and the raindrops on the right.',
        'The arc is smooth and symmetrical, representing the natural shape of a rainbow.',
        'The rainbow illustrates the result of sunlight passing through raindrops.',
    ],
    tags='rainbow, colors, arc, sky, spectrum, vibrant, colorful, light',
    atmosphere='Colorful and vivid, showcasing the beauty of nature.',
    style='Clear and vivid, suitable for an educational diagram.',
    quality_meta='High resolution with distinct and bright color bands.',
    HTML_web_color_name='violet',
)

# Add the ground
canvas.add_local_description(
    name="Ground",
    location='on the bottom',
    offset='no offset',
    area='a large horizontal area',
    distance_to_viewer=6.0,
    description='A simple green field with grass.',
    detailed_descriptions=[
        'A flat green field stretches across the bottom of the image, representing the ground.',
        'Short green grass covers the field evenly, adding a touch of nature.',
        'The field provides a natural base for the scene, grounding the elements above.',
        'The green of the grass contrasts with the blue sky and the colorful rainbow.',
    ],
    tags='field, grass, ground, green, landscape, nature, earth, base',
    atmosphere='Calm and natural, representing the earth beneath the sky.',
    style='Simple and clear, suitable for an educational diagram.',
    quality_meta='High resolution with clear lines and natural colors.',
    HTML_web_color_name='green',
)