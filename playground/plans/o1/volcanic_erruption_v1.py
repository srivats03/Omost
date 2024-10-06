

from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description='An illustration of a volcanic eruption.',
    detailed_descriptions=[
        'A side view of a volcano erupting, showing internal and external features.',
        'The volcano is a conical mountain structure situated in the center of the image.',
        'The sky is clear with a bright blue color, featuring a few scattered white clouds.',
        'The ground displays different horizontal layers representing the Earth\'s crust beneath the volcano.',
        'The overall image is educational, aiming to explain the process of a volcanic eruption to a young audience.',
    ],
    tags='volcano, eruption, lava, magma chamber, Earth\'s crust, ash cloud, educational, illustration, diagram, side view, conical shape, layers, clear sky, clouds, mountain',
    HTML_web_color_name='lightgray',
)

# Add the volcano erupting
canvas.add_local_description(
    location='in the center',
    offset='no offset',
    area='a large vertical area',
    distance_to_viewer=5.0,
    description='A volcano erupting.',
    detailed_descriptions=[
        'A conical mountain structure with a crater at the top, located centrally.',
        'Lava is flowing out from the crater and down the sides of the volcano.',
        'The sides of the volcano are rocky and uneven, depicted in shades of brown and gray.',
        'Small patches of green vegetation are present at the base of the volcano.',
    ],
    tags='volcano, mountain, crater, lava flow, conical shape, rocky sides, vegetation, eruption',
    atmosphere='Educational and informative, clearly depicting the erupting volcano.',
    style='Simple and clear illustration suitable for children, with bold outlines and bright colors.',
    quality_meta='High resolution with clear lines and vibrant colors for visual appeal.',
    HTML_web_color_name='sienna',
)

# Add the magma chamber beneath the volcano
canvas.add_local_description(
    location='in the center',
    offset='slightly to the lower',
    area='a medium-sized vertical area',
    distance_to_viewer=6.0,
    description='A magma chamber beneath the volcano.',
    detailed_descriptions=[
        'An oval-shaped chamber depicted underground beneath the volcano.',
        'The magma chamber is filled with molten rock shown in bright reds and oranges.',
        'A conduit connects the magma chamber to the crater at the top of the volcano.',
    ],
    tags='magma chamber, molten rock, underground, conduit, volcanic structure',
    atmosphere='Informative, illustrating the internal structure of the volcano.',
    style='Simplified diagram with clear representation and bright colors to highlight the magma.',
    quality_meta='High resolution with clear depiction of underground features.',
    HTML_web_color_name='red',
)

# Add the Earth's crust layers
canvas.add_local_description(
    location='on the bottom',
    offset='no offset',
    area='a large horizontal area',
    distance_to_viewer=7.0,
    description="Layers of the Earth's crust.",
    detailed_descriptions=[
        'Multiple horizontal layers beneath the volcano representing different strata of the Earth\'s crust.',
        'Each layer is distinguished by different colors such as browns, yellows, and grays.',
        'The layers extend across the bottom of the image, providing a foundation for the volcano.',
    ],
    tags="Earth's crust, geological layers, underground, strata, foundation",
    atmosphere='Educational, depicting the geological layers beneath the surface.',
    style='Simplified with distinct colors for each layer to enhance understanding.',
    quality_meta='High resolution with clear separation and clean lines between layers.',
    HTML_web_color_name='burlywood',
)

# Add lava flowing from the crater
canvas.add_local_description(
    location='in the center',
    offset='slightly to the upper',
    area='a small vertical area',
    distance_to_viewer=4.0,
    description='Lava flowing out of the crater.',
    detailed_descriptions=[
        'Bright red and orange lava emerging from the top crater of the volcano.',
        'The lava flows in streams down the sides of the volcano, depicted with wavy lines.',
    ],
    tags='lava flow, molten rock, eruption, crater, bright colors',
    atmosphere='Dynamic, showing the movement and heat of the lava.',
    style='Bold and bright colors to represent the hot lava vividly.',
    quality_meta='High resolution with smooth gradients and flowing lines.',
    HTML_web_color_name='orangered',
)

# Add an ash cloud rising above the volcano
canvas.add_local_description(
    location='on the top',
    offset='no offset',
    area='a medium-sized vertical area',
    distance_to_viewer=3.0,
    description='An ash cloud rising from the volcano.',
    detailed_descriptions=[
        'A large, dark gray cloud of ash and smoke billowing upwards from the volcano\'s crater.',
        'The ash cloud has swirling patterns to indicate movement and dispersion into the sky.',
    ],
    tags='ash cloud, smoke, eruption, volcanic gases, swirling patterns',
    atmosphere='Dramatic, illustrating the power and impact of the eruption.',
    style='Dark grays with soft edges to depict the ash cloud realistically.',
    quality_meta='High resolution with detailed textures in the cloud.',
    HTML_web_color_name='darkgray',
)

# Add a clear blue sky with clouds
canvas.add_local_description(
    location='on the top',
    offset='slightly to the upper',
    area='a large horizontal area',
    distance_to_viewer=8.0,
    description='A clear blue sky with white clouds.',
    detailed_descriptions=[
        'A bright blue sky filling the background of the upper part of the image.',
        'White, fluffy clouds scattered across the sky, providing a calm backdrop.',
    ],
    tags='sky, clouds, background, blue, white, calm',
    atmosphere='Peaceful, contrasting with the erupting volcano.',
    style='Soft colors and simple shapes for a gentle sky appearance.',
    quality_meta='High resolution with smooth gradients and soft cloud edges.',
    HTML_web_color_name='skyblue',
)

# Add some surrounding landscape
canvas.add_local_description(
    location='on the bottom',
    offset='slightly to the lower',
    area='a medium-sized horizontal area',
    distance_to_viewer=6.5,
    description='Surrounding landscape with trees and greenery.',
    detailed_descriptions=[
        'Green grass and small trees at the base of the volcano.',
        'The landscape is simple, with shades of green to represent vegetation.',
    ],
    tags='landscape, trees, grass, greenery, nature, base of volcano',
    atmosphere='Natural and serene, enhancing the educational aspect.',
    style='Simple and colorful to appeal to children.',
    quality_meta='High resolution with vibrant greens and clear details.',
    HTML_web_color_name='forestgreen',
)