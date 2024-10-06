from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description='A diagram explaining the Water Cycle.',
    detailed_descriptions=[
        'This diagram illustrates the Water Cycle, also known as the Hydrologic Cycle, which describes the continuous journey of water on Earth.',
        'The diagram features various components such as evaporation, condensation, and precipitation, all interconnected to form a circular process.',
        'The main sections are labeled clearly, with arrows and lines indicating the flow of water between them.',
        'The diagram also includes additional elements like clouds, rain, and water bodies to provide a more comprehensive view of the Water Cycle.',
        'The colors used are vibrant and distinct, making it easy to understand the different stages of the cycle.',
        'The overall design is both informative and visually appealing, with a balance between clarity and detail.',
    ],
    tags='Water Cycle, Hydrologic Cycle, diagram, evaporation, condensation, precipitation, water flow, circular process, clouds, rain, water bodies, arrows, lines, labels, vibrant colors, comprehensive view, informative, visually appealing, clarity, detail',
    HTML_web_color_name='lightblue',
)

# Add evaporation stage
canvas.add_local_description(
    name="Evaporation",
    location='in the center',
    offset='no offset',
    area='a medium-sized square area',
    distance_to_viewer=1.5,
    description='Evaporation Stage',
    detailed_descriptions=[
        'The Evaporation Stage is depicted as a large area in the center of the diagram.',
        'It shows water bodies like oceans, lakes, and rivers, with water molecules turning into vapor.',
        'The stage is marked with an upward-pointing arrow to indicate the movement of water from its liquid state to its gaseous state.',
        'The area is colored in a light blue hue to distinguish it from other stages.',
        'The inclusion of water bodies and the vapor rising from them makes this stage visually engaging and easy to understand.',
    ],
    tags='Evaporation Stage, water bodies, oceans, lakes, rivers, water molecules, vapor, upward arrow, light blue, visual engagement, understanding',
    atmosphere='The atmosphere here is educational and engaging.',
    style='The style is informative with clear labels and arrows.',
    quality_meta='High-quality depiction with clear and distinct elements.',
    HTML_web_color_name='lightblue',
)

# Add condensation stage
canvas.add_local_description(
    name="Condensation",
    location='on the top',
    offset='no offset',
    area='a large horizontal area',
    distance_to_viewer=2.0,
    description='Condensation Stage',
    detailed_descriptions=[
        'The Condensation Stage is represented at the top of the diagram, covering a large horizontal area.',
        'This stage illustrates water vapor in the air condensing into tiny droplets, forming clouds.',
        'The area is marked with a downward-pointing arrow to show the transformation of water vapor back into liquid form.',
        'The clouds are depicted with fluffy, white textures to emphasize condensation.',
        'The use of light blue and white colors helps distinguish this stage from others.',
        'The stage is visually appealing with the clouds creating a sense of depth and continuity in the Water Cycle.',
    ],
    tags='Condensation Stage, water vapor, air, tiny droplets, clouds, downward arrow, fluffy textures, light blue, white, visual appeal, depth, continuity',
    atmosphere='The atmosphere is informative and visually appealing.',
    style='The style is clear with distinct textures and colors.',
    quality_meta='High-quality depiction with fluffy textures and clear labels.',
    HTML_web_color_name='white',
)

# Add precipitation stage
canvas.add_local_description(
    name="Precipitation",
    location='on the bottom',
    offset='no offset',
    area='a large horizontal area',
    distance_to_viewer=2.5,
    description='Precipitation Stage',
    detailed_descriptions=[
        'The Precipitation Stage is illustrated at the bottom of the diagram, covering a large horizontal area.',
        'This stage shows water droplets falling from the clouds as rain or snow.',
        'The area is marked with a downward-pointing arrow to indicate the descent of water from the atmosphere back to the Earth.',
        'The rain and snow are depicted with dark blue and white textures, respectively, to signify their forms.',
        'The stage is visually engaging with the rain and snow creating a sense of movement and flow.',
        'The use of distinct colors and textures makes this stage easy to understand and visually appealing.',
    ],
    tags='Precipitation Stage, water droplets, clouds, rain, snow, downward arrow, dark blue, white, visual engagement, movement, flow, understanding, visually appealing',
    atmosphere='The atmosphere is engaging and informative.',
    style='The style is clear with distinct textures and colors.',
    quality_meta='High-quality depiction with clear labels and distinct textures.',
    HTML_web_color_name='darkblue',
)

# Add runoff stage
canvas.add_local_description(
    name="Runoff",
    location='on the left',
    offset='slightly to the lower',
    area='a medium-sized vertical area',
    distance_to_viewer=1.75,
    description='Runoff Stage',
    detailed_descriptions=[
        'The Runoff Stage is depicted on the left side of the diagram, slightly lower than the center.',
        'This stage shows rainwater flowing over land as runoff.',
        'The area is marked with a downward-pointing arrow to indicate the movement of water from the precipitation stage to the land.',
        'The runoff is depicted with a blue hue, showing the water flowing over the land.',
        'The stage is visually engaging with the depiction of water flowing over various terrains.',
        'The use of blue colors and clear labels makes this stage easy to understand and visually appealing.',
    ],
    tags='Runoff Stage, rainwater, land, runoff, downward arrow, blue, visual engagement, terrains, understanding, visually appealing',
    atmosphere='The atmosphere is educational and visually engaging.',
    style='The style is clear with distinct colors and labels.',
    quality_meta='High-quality depiction with clear labels and distinct colors.',
    HTML_web_color_name='blue',
)

# Add infiltration stage
canvas.add_local_description(
    name="Infiltration",
    location='on the right',
    offset='slightly to the upper',
    area='a medium-sized vertical area',
    distance_to_viewer=1.75,
    description='Infiltration Stage',
    detailed_descriptions=[
        'The Infiltration Stage is depicted on the right side of the diagram, slightly upper than the center.',
        'This stage shows rainwater penetrating the soil as infiltration.',
        'The area is marked with a downward-pointing arrow to indicate the movement of water from the precipitation stage into the soil.',
        'The infiltration is depicted with a light blue hue, showing the water seeping into the soil.',
        'The stage is visually engaging with the depiction of water seeping through various soil types.',
        'The use of light blue colors and clear labels makes this stage easy to understand and visually appealing.',
    ],
    tags='Infiltration Stage, rainwater, soil, infiltration, downward arrow, light blue, visual engagement, soil types, understanding, visually appealing',
    atmosphere='The atmosphere is educational and visually engaging.',
    style='The style is clear with distinct colors and labels.',
    quality_meta='High-quality depiction with clear labels and distinct colors.',
    HTML_web_color_name='lightblue',
)