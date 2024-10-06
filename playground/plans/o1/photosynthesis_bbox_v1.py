from lib_omost.canvas import Canvas

# # Initialize the canvas
# canvas = Canvas()

# # Set a global description for the canvas
# canvas.set_global_description(
#     description="Diagram explaining photosynthesis.",
#     detailed_descriptions=[
#         "A visual representation of the photosynthesis process in a green plant.",
#         "A bright and clear background illustrating a sunny day.",
#         "Central focus on a plant showing both above-ground and underground parts.",
#         "The sun is positioned in the sky, shining light onto the plant.",
#         "The ground is depicted with visible soil layers.",
#     ],
#     tags="photosynthesis, plant, sun, roots, leaves, ground, sky, sunlight, diagram, educational",
#     HTML_web_color_name="lightblue",
# )

# # Add the sun in the sky
# canvas.add_local_description(
#     bbox=[70, 0, 20, 20],
#     distance_to_viewer=10.0,
#     description="The sun in the sky.",
#     detailed_descriptions=[
#         "A bright yellow sun located in the top right corner.",
#         "Sun rays extending outward in all directions.",
#     ],
#     tags="sun, sunlight, bright, sky, rays, energy",
#     atmosphere="Bright and cheerful.",
#     style="Simple and clear illustration suitable for children.",
#     quality_meta="High resolution with vivid colors and clear shapes.",
#     HTML_web_color_name="yellow",
# )

# # Add the sky with few clouds
# canvas.add_local_description(
#     bbox=[0, 0, 90, 30],
#     distance_to_viewer=9.0,
#     description="A clear sky with a few clouds.",
#     detailed_descriptions=[
#         "Light blue sky serving as the background.",
#         "Soft white clouds scattered across the sky.",
#     ],
#     tags="sky, clouds, background, atmosphere",
#     atmosphere="Calm and serene.",
#     style="Simple and cheerful.",
#     quality_meta="High resolution with smooth gradients.",
#     HTML_web_color_name="skyblue",
# )

# # Add the green plant
# canvas.add_local_description(
#     bbox=[35, 30, 20, 40],
#     distance_to_viewer=5.0,
#     description="A green plant with leaves.",
#     detailed_descriptions=[
#         "A tall plant positioned at the center.",
#         "Multiple green leaves branching out from the stem.",
#         "The stem is brownish-green and sturdy.",
#     ],
#     tags="plant, leaves, stem, green, photosynthesis",
#     atmosphere="Natural and lively.",
#     style="Clear illustration with defined edges.",
#     quality_meta="High resolution with detailed textures.",
#     HTML_web_color_name="green",
# )

# # Add roots extending into the ground
# canvas.add_local_description(
#     bbox=[35, 65, 20, 25],
#     distance_to_viewer=5.0,
#     description="Roots extending into the soil.",
#     detailed_descriptions=[
#         "Brown roots spreading out beneath the plant.",
#         "Roots branching out in different directions.",
#     ],
#     tags="roots, soil, underground, plant",
#     atmosphere="Educational and natural.",
#     style="Simple illustration with clear lines.",
#     quality_meta="High resolution with fine details.",
#     HTML_web_color_name="sienna",
# )

# # Add the ground or soil layers
# canvas.add_local_description(
#     bbox=[0, 65, 90, 25],
#     distance_to_viewer=8.0,
#     description="The ground showing soil layers.",
#     detailed_descriptions=[
#         "Brown soil depicted at the bottom portion.",
#         "Different shades to represent various soil layers.",
#         "Cross-sectional view to display the roots.",
#     ],
#     tags="ground, soil, layers, earth, cross-section",
#     atmosphere="Educational and clear.",
#     style="Simple with distinct color separations.",
#     quality_meta="High resolution with smooth transitions.",
#     HTML_web_color_name="peru",
# )

# # Add water droplets near the roots
# canvas.add_local_description(
#     bbox=[40, 80, 10, 10],
#     distance_to_viewer=6.0,
#     description="Water being absorbed by roots.",
#     detailed_descriptions=[
#         "Small blue droplets near the roots.",
#         "Droplets positioned as if moving towards the roots.",
#     ],
#     tags="water, droplets, absorption, roots",
#     atmosphere="Educational.",
#     style="Simple symbols suitable for children.",
#     quality_meta="High resolution with clear shapes.",
#     HTML_web_color_name="blue",
# )

# # Add carbon dioxide molecules entering the leaves
# canvas.add_local_description(
#     bbox=[15, 40, 20, 10],
#     distance_to_viewer=6.0,
#     description="Carbon dioxide molecules near the leaves.",
#     detailed_descriptions=[
#         "Small gray circles representing carbon dioxide on the left side of the plant.",
#         "Circles positioned as if moving towards the leaves.",
#     ],
#     tags="carbon dioxide, molecules, gas, leaves, intake",
#     atmosphere="Educational.",
#     style="Simple icons appropriate for children.",
#     quality_meta="High resolution with distinct shapes.",
#     HTML_web_color_name="darkgray",
# )

# # Add oxygen molecules exiting the leaves
# canvas.add_local_description(
#     bbox=[55, 40, 20, 10],
#     distance_to_viewer=6.0,
#     description="Oxygen molecules near the leaves.",
#     detailed_descriptions=[
#         "Small light green circles representing oxygen on the right side of the plant.",
#         "Circles positioned as if moving away from the leaves.",
#     ],
#     tags="oxygen, molecules, gas, leaves, release",
#     atmosphere="Educational.",
#     style="Simple icons appropriate for children.",
#     quality_meta="High resolution with distinct shapes.",
#     HTML_web_color_name="lightgreen",
# )

# # Add glucose representation inside the plant
# canvas.add_local_description(
#     bbox=[38, 50, 14, 10],
#     distance_to_viewer=5.0,
#     description="Glucose represented inside the plant.",
#     detailed_descriptions=[
#         "Small orange hexagons inside the stem.",
#         "Represents glucose being produced within the plant.",
#     ],
#     tags="glucose, sugar, energy, plant, production",
#     atmosphere="Educational.",
#     style="Simple symbols suitable for children.",
#     quality_meta="High resolution with clear shapes.",
#     HTML_web_color_name="orange",
# )

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description="Diagram showing how photosynthesis works in plants.",
    detailed_descriptions=[
        "Plant under the sun, illustrating photosynthesis.",
        "Plant absorbs sunlight, carbon dioxide, and water.",
        "Produces oxygen and glucose.",
        "Clear sky background, sun shining.",
        "Soil at bottom with roots absorbing water.",
    ],
    tags="photosynthesis, plant, sun, water, carbon dioxide, oxygen, glucose, roots, soil, leaves, chlorophyll",
    HTML_web_color_name="lightblue",
)

# Add the sun
canvas.add_local_description(
    name="sun",
    bbox=[70, 0, 20, 20],
    distance_to_viewer=10.0,
    description="Bright sun in top right corner.",
    detailed_descriptions=[
        "Yellow circle with rays extending outward.",
        "Provides sunlight to the plant.",
    ],
    tags="sun, bright, shining, sunlight, energy",
    atmosphere="Bright, providing energy.",
    style="Simple and clear.",
    quality_meta="High resolution, bright colors.",
    HTML_web_color_name="yellow",
)

# Add the plant
canvas.add_local_description(
    name="plant",
    bbox=[35, 30, 20, 40],
    distance_to_viewer=5.0,
    description="Green plant in center.",
    detailed_descriptions=[
        "Stem with several green leaves.",
        "Leaves facing the sun.",
    ],
    tags="plant, leaves, green, stem, chlorophyll",
    atmosphere="Healthy, absorbing sunlight.",
    style="Simple, suitable for kids.",
    quality_meta="High resolution, vivid green.",
    HTML_web_color_name="green",
)

# Add the roots
canvas.add_local_description(
    name="roots",
    bbox=[35, 70, 20, 20],
    distance_to_viewer=6.0,
    description="Roots in soil below plant.",
    detailed_descriptions=[
        "Roots extend into brown soil.",
        "Absorbing water from soil.",
    ],
    tags="roots, soil, water absorption, nutrients",
    atmosphere="Underground, absorbing water.",
    style="Clear focus on roots.",
    quality_meta="High resolution, clear roots.",
    HTML_web_color_name="saddlebrown",
)

# Add water droplets
canvas.add_local_description(
    name="water",
    bbox=[30, 70, 10, 20],
    distance_to_viewer=7.0,
    description="Blue water droplets near roots.",
    detailed_descriptions=[
        "Blue droplets represent water.",
        "Positioned near roots in soil.",
    ],
    tags="water, droplets, absorption, roots",
    atmosphere="Shows water absorption.",
    style="Simple, using blue droplets.",
    quality_meta="High resolution, clear droplets.",
    HTML_web_color_name="blue",
)

# Add carbon dioxide
canvas.add_local_description(
    name="carbon_dioxide",
    bbox=[25, 20, 20, 20],
    distance_to_viewer=8.0,
    description="CO2 molecules near leaves.",
    detailed_descriptions=[
        "Small grey circles represent CO2.",
        "Near leaves on left side.",
    ],
    tags="carbon dioxide, CO2, gas, leaves, absorption",
    atmosphere="Shows CO2 absorption.",
    style="Simple, grey circles.",
    quality_meta="High resolution, clear CO2.",
    HTML_web_color_name="gray",
)

# Add oxygen
canvas.add_local_description(
    name="oxygen",
    bbox=[55, 20, 20, 20],
    distance_to_viewer=8.0,
    description="Oxygen molecules leaving leaves.",
    detailed_descriptions=[
        "Small red circles represent oxygen.",
        "Near leaves on right side.",
    ],
    tags="oxygen, O2, gas, leaves, release",
    atmosphere="Shows oxygen release.",
    style="Simple, red circles.",
    quality_meta="High resolution, clear oxygen.",
    HTML_web_color_name="red",
)