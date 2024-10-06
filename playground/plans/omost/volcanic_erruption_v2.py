from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description='A diagram explaining volcanic eruption to a 10-year-old student.',
    detailed_descriptions=[
        'The diagram is designed to explain volcanic eruptions in a way that is easy for a 10-year-old student to understand.',
        'It features a simple and colorful illustration that includes key elements such as a volcano, magma, lava, ash, and an eruption.',
        'The diagram is divided into sections to highlight the different stages of a volcanic eruption, from the formation of magma to the eruption itself.',
        'Each stage is depicted with clear and vibrant graphics, accompanied by easy-to-read text that explains the process.',
        'The illustration also includes visual aids like arrows and symbols to help illustrate the movement of magma and lava.',
        'The overall design is friendly and engaging, with a focus on making the complex topic of volcanic eruptions accessible to young learners.',
    ],
    tags='diagram, volcanic eruption, 10-year-old, student, illustration, magma, lava, ash, eruption stages, colorful, easy to understand, key elements, vibrant graphics, text, arrows, symbols, engaging, accessible, young learners, formation, movement',
    HTML_web_color_name='lightgoldenrodyellow',
)

# Add a volcano with an eruption
canvas.add_local_description(
    location='in the center',
    offset='no offset',
    area='a large vertical area',
    distance_to_viewer=1.0,
    description='A volcano with an eruption',
    detailed_descriptions=[
        'The central part of the diagram features a volcano with an eruption happening.',
        'The volcano is depicted as a tall mountain with a wide base, and the eruption shows molten lava and ash clouds rising from the top.',
        'The eruption is illustrated with bright colors to make it stand out, and there are small details like sparks and smoke to add realism.',
        'The lava flows down the sides of the volcano, and the ash clouds spread outwards.',
        'This section is designed to capture the dramatic and powerful nature of a volcanic eruption.',
    ],
    tags='volcano, eruption, molten lava, ash clouds, mountain, bright colors, sparks, smoke, lava flows, dramatic, powerful',
    atmosphere='Dramatic and powerful, capturing the essence of an eruption.',
    style='Illustrative with bright colors and detailed graphics.',
    quality_meta='High-quality illustration with attention to detail.',
    HTML_web_color_name='firebrick',
)

# Add magma forming beneath the volcano
canvas.add_local_description(
    location='on the left',
    offset='slightly to the lower',
    area='a medium-sized vertical area',
    distance_to_viewer=1.5,
    description='Magma forming beneath the volcano',
    detailed_descriptions=[
        'On the left side of the diagram, slightly lower than the center, is an illustration of magma forming beneath the volcano.',
        'The magma is depicted as molten rock with a glowing core, surrounded by hot, glowing minerals.',
        'This section shows the process of magma rising through the Earth’s crust, with arrows indicating the upward flow.',
        'The magma is illustrated with vibrant reds and oranges to represent its heat and molten state.',
        'This part of the diagram aims to explain how magma forms and its journey before it erupts.',
    ],
    tags='magma, molten rock, glowing core, hot minerals, rising, Earth’s crust, arrows, vibrant colors, heat, molten',
    atmosphere='Hot and glowing, emphasizing the heat of magma.',
    style='Scientific with vibrant colors and clear arrows.',
    quality_meta='Detailed illustration with vibrant colors and clear explanations.',
    HTML_web_color_name='darkorange',
)

# Add lava flowing down the sides of the volcano
canvas.add_local_description(
    location='on the right',
    offset='slightly to the upper',
    area='a medium-sized vertical area',
    distance_to_viewer=1.5,
    description='Lava flowing down the sides of the volcano',
    detailed_descriptions=[
        'On the right side of the diagram, slightly higher than the center, is an illustration of lava flowing down the sides of the volcano.',
        'The lava is shown as a continuous stream of molten rock, with glowing edges and a flowing motion.',
        'This section includes arrows to show the direction of the lava flow.',
        'The lava is illustrated with bright reds and oranges to represent its molten state.',
        'This part of the diagram explains how lava flows from the volcano and its characteristics.',
    ],
    tags='lava, flowing, molten rock, glowing edges, continuous stream, arrows, bright colors, molten, characteristics',
    atmosphere='Hot and flowing, highlighting the continuous motion of lava.',
    style='Illustrative with flowing motion and bright colors.',
    quality_meta='High-quality illustration with clear motion and bright colors.',
    HTML_web_color_name='orangered',
)

# Add ash clouds spreading from the eruption
canvas.add_local_description(
    location='on the top',
    offset='slightly to the right',
    area='a small horizontal area',
    distance_to_viewer=2.0,
    description='Ash clouds spreading from the eruption',
    detailed_descriptions=[
        'At the top of the diagram, slightly to the right, is an illustration of ash clouds spreading from the eruption.',
        'The ash clouds are depicted as dark, billowing clouds rising from the top of the volcano.',
        'This section shows the ash clouds dispersing into the air, with arrows indicating the direction of the spread.',
        'The ash clouds are illustrated with dark grays and blacks to represent their density and darkness.',
        'This part of the diagram explains how ash clouds form and spread from the eruption.',
    ],
    tags='ash clouds, spreading, dark clouds, billowing, rising, arrows, dark colors, density, darkness, form, spread',
    atmosphere='Dark and dense, emphasizing the spread of ash clouds.',
    style='Illustrative with dark colors and dispersing motion.',
    quality_meta='High-quality illustration with clear dispersing motion and dark colors.',
    HTML_web_color_name='dimgray',
)

# Add the formation of magma beneath the volcano
canvas.add_local_description(
    location='on the bottom',
    offset='slightly to the left',
    area='a small horizontal area',
    distance_to_viewer=2.0,
    description='The formation of magma beneath the volcano',
    detailed_descriptions=[
        'At the bottom of the diagram, slightly to the left, is an illustration of the formation of magma beneath the volcano.',
        'This section shows the Earth’s crust with molten rock forming beneath it, with arrows indicating the movement of magma.',
        'The magma is illustrated with vibrant reds and oranges to represent its heat and molten state.',
        'This part of the diagram aims to explain the process of magma formation and its journey before it erupts.',
    ],
    tags='magma formation, Earth’s crust, molten rock, arrows, vibrant colors, heat, molten, process, journey, erupts',
    atmosphere='Hot and glowing, emphasizing the formation of magma.',
    style='Scientific with vibrant colors and clear arrows.',
    quality_meta='Detailed illustration with vibrant colors and clear explanations.',
    HTML_web_color_name='darkred',
)