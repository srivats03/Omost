from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description='A diagram explaining a volcanic eruption to a 10-year-old student.',
    detailed_descriptions=[
        'This diagram is designed to explain a volcanic eruption in a way that is easy for a 10-year-old student to understand.',
        'The main focus is on visualizing the process, making it simple and engaging.',
        'The diagram includes illustrations of the Earth\'s interior, magma rising, volcanic activity, and the effects of the eruption.',
        'Each part of the diagram is labeled clearly to help the student understand the different stages of a volcanic eruption.',
        'The colors used are vibrant and appealing to children, with a mix of blues, reds, and greens to represent the Earth and magma.',
        'The background is a simple gradient to keep the focus on the main elements.',
    ],
    tags='diagram, volcanic eruption, explanation, student, 10-year-old, Earth, magma, volcanic activity, illustration, simple, engaging, visual, stages, labels, vibrant colors, blues, reds, greens, gradient background, focus, main elements',
    HTML_web_color_name='lightskyblue',
)

# Add the earth's interior with magma rising.
canvas.add_local_description(
    location='in the center',
    offset='no offset',
    area='a large square area',
    distance_to_viewer=1.5,
    description="The Earth's interior with magma rising.",
    detailed_descriptions=[
        'This part of the diagram shows the Earth\'s interior, with magma rising from the core.',
        'The magma is depicted as a bright red, flowing upwards.',
        'The Earth is illustrated with a blue and green gradient to represent the crust and mantle.',
        'This section aims to explain the source of volcanic eruptions, showing how magma is formed deep within the Earth and rises due to pressure.',
    ],
    tags='Earth, interior, magma, rising, core, bright red, flowing, blue gradient, green gradient, crust, mantle, pressure, source, volcanic eruptions, explanation, illustration, student, 10-year-old, visual, engaging',
    atmosphere='The atmosphere is educational and engaging, designed for young learners.',
    style='The style is simple and colorful, with clear labels and illustrations.',
    quality_meta='High-quality illustration with vibrant colors and clear details.',
    HTML_web_color_name='firebrick',
)

# Add magma rising through the earth's crust.
canvas.add_local_description(
    location='on the left',
    offset='slightly to the upper',
    area='a medium-sized vertical area',
    distance_to_viewer=1.75,
    description="Magma rising through the Earth's crust.",
    detailed_descriptions=[
        'This section illustrates magma rising through the Earth’s crust.',
        'The magma is depicted as a bright red, flowing upwards through the blue and green crust.',
        'This part of the diagram aims to show how the pressure and heat from the magma cause it to rise, eventually leading to a volcanic eruption.',
        'The illustration is designed to be clear and easy to understand, with simple labels and arrows indicating the direction of the magma flow.',
    ],
    tags='magma, rising, Earth’s crust, bright red, flowing, blue crust, green crust, pressure, heat, volcanic eruption, illustration, student, 10-year-old, visual, engaging, clear, labels, arrows, direction, flow',
    atmosphere='The atmosphere is educational and visually engaging.',
    style='The style is simple and colorful, with clear labels and illustrations.',
    quality_meta='High-quality illustration with vibrant colors and clear details.',
    HTML_web_color_name='crimson',
)

# Add volcanic activity with lava flowing.
canvas.add_local_description(
    location='on the right',
    offset='slightly to the lower',
    area='a medium-sized vertical area',
    distance_to_viewer=1.75,
    description='Volcanic activity with lava flowing.',
    detailed_descriptions=[
        'This section of the diagram shows volcanic activity, with lava flowing from the volcano.',
        'The lava is depicted as bright red, flowing down the sides of the volcano.',
        'This part of the diagram aims to illustrate the effects of a volcanic eruption, showing the lava flowing and the ash clouds rising.',
        'The illustration is designed to be visually engaging, with simple labels and arrows indicating the direction of the lava flow and the ash clouds.',
    ],
    tags='volcanic activity, lava, flowing, volcano, bright red, flowing down, sides of volcano, lava flow, ash clouds, rising, illustration, student, 10-year-old, visual, engaging, clear, labels, arrows, direction, flow',
    atmosphere='The atmosphere is educational and visually engaging.',
    style='The style is simple and colorful, with clear labels and illustrations.',
    quality_meta='High-quality illustration with vibrant colors and clear details.',
    HTML_web_color_name='darkred',
)

# Add ash clouds rising from the volcano.
canvas.add_local_description(
    location='on the top',
    offset='slightly to the right',
    area='a medium-sized horizontal area',
    distance_to_viewer=2.0,
    description='Ash clouds rising from the volcano.',
    detailed_descriptions=[
        'This section of the diagram shows ash clouds rising from the volcano.',
        'The ash clouds are depicted as dark gray, rising from the volcano.',
        'This part of the diagram aims to illustrate the effects of a volcanic eruption, showing the ash clouds rising and the impact they have on the environment.',
        'The illustration is designed to be visually engaging, with simple labels and arrows indicating the direction of the ash clouds.',
    ],
    tags='ash clouds, rising, volcano, dark gray, rising from volcano, ash clouds, illustration, student, 10-year-old, visual, engaging, clear, labels, arrows, direction, impact, environment',
    atmosphere='The atmosphere is educational and visually engaging.',
    style='The style is simple and colorful, with clear labels and illustrations.',
    quality_meta='High-quality illustration with vibrant colors and clear details.',
    HTML_web_color_name='gray',
)

# Add the effects of a volcanic eruption.
canvas.add_local_description(
    location='on the bottom',
    offset='slightly to the left',
    area='a medium-sized horizontal area',
    distance_to_viewer=2.0,
    description='The effects of a volcanic eruption.',
    detailed_descriptions=[
        'This section of the diagram shows the effects of a volcanic eruption.',
        'The effects include ash fall, lava flows, and the impact on the environment.',
        'This part of the diagram aims to illustrate the consequences of a volcanic eruption, showing the different ways it can affect the surroundings.',
        'The illustration is designed to be visually engaging, with simple labels and arrows indicating the different effects.',
    ],
    tags='effects, volcanic eruption, ash fall, lava flows, impact, environment, illustration, student, 10-year-old, visual, engaging, clear, labels, arrows, direction, consequences, surroundings',
    atmosphere='The atmosphere is educational and visually engaging.',
    style='The style is simple and colorful, with clear labels and illustrations.',
    quality_meta='High-quality illustration with vibrant colors and clear details.',
    HTML_web_color_name='darkslategray',
)