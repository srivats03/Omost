from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description="A diagram illustrating the water cycle.",
    detailed_descriptions=[
        "The scene shows a natural landscape with a body of water, land, and sky.",
        "The sun shines in the sky, warming the water below.",
        "Clouds form in the sky above the water.",
        "Rain falls from the clouds onto the land and water.",
        "Water flows from the land back into the body of water.",
    ],
    tags="water cycle, evaporation, condensation, precipitation, collection, sun, clouds, rain, water, landscape, nature",
    HTML_web_color_name="skyblue",
)

# Add the body of water (collection)
canvas.add_local_description(
    name="water",
    bbox=[0, 60, 90, 30],
    distance_to_viewer=5.0,
    description="A large body of water.",
    detailed_descriptions=[
        "A blue lake at the bottom part of the image.",
        "Calm water surface with slight ripples.",
        "Water reflects the sky and surroundings.",
    ],
    tags="lake, water, blue, calm, reflections, ripples",
    atmosphere="Peaceful and natural.",
    style="Simple and clear, suitable for a diagram.",
    quality_meta="High-quality illustration with clear details.",
    HTML_web_color_name="blue",
)

# Add the hillside (land)
canvas.add_local_description(
    name="hillside",
    bbox=[60, 50, 30, 40],
    distance_to_viewer=5.0,
    description="A green hillside.",
    detailed_descriptions=[
        "Grassy hill on the right side of the image.",
        "Hill slopes down towards the lake.",
        "Trees and plants grow on the hill.",
    ],
    tags="hill, grass, trees, plants, land, green",
    atmosphere="Lush and natural.",
    style="Simple and clear, suitable for a diagram.",
    quality_meta="High-quality illustration with clear details.",
    HTML_web_color_name="green",
)

# Add the sun (energy source)
canvas.add_local_description(
    name="sun",
    bbox=[0, 0, 20, 20],
    distance_to_viewer=10.0,
    description="A bright sun.",
    detailed_descriptions=[
        "Yellow sun in the top left corner.",
        "Sun shines brightly.",
    ],
    tags="sun, bright, yellow, shining",
    atmosphere="Warm and sunny.",
    style="Simple and clear, suitable for a diagram.",
    quality_meta="High-quality illustration with clear details.",
    HTML_web_color_name="yellow",
)

# Add water vapor rising from the lake (evaporation)
canvas.add_local_description(
    name="vapor",
    bbox=[20, 40, 50, 20],
    distance_to_viewer=7.0,
    description="Water vapor rising from the lake.",
    detailed_descriptions=[
        "Light wisps of vapor rising upwards from the lake surface.",
        "Semi-transparent vapor rises towards the sky.",
    ],
    tags="evaporation, water vapor, rising, lake, vapor",
    atmosphere="Light and airy.",
    style="Simple and clear, suitable for a diagram.",
    quality_meta="High-quality illustration with clear details.",
    HTML_web_color_name="white",
)

# Add clouds (condensation)
canvas.add_local_description(
    name="clouds",
    bbox=[30, 10, 30, 20],
    distance_to_viewer=8.0,
    description="Clouds in the sky.",
    detailed_descriptions=[
        "White fluffy clouds above the lake.",
        "Clouds formed from water vapor.",
    ],
    tags="clouds, sky, condensation, fluffy",
    atmosphere="Light and airy.",
    style="Simple and clear, suitable for a diagram.",
    quality_meta="High-quality illustration with clear details.",
    HTML_web_color_name="white",
)

# Add rain falling from the clouds (precipitation)
canvas.add_local_description(
    name="rain",
    bbox=[30, 30, 30, 30],
    distance_to_viewer=6.0,
    description="Rain falling from the clouds.",
    detailed_descriptions=[
        "Droplets of rain falling towards the lake and land.",
        "Rain connects clouds and ground.",
    ],
    tags="rain, precipitation, droplets, falling",
    atmosphere="Refreshing and natural.",
    style="Simple and clear, suitable for a diagram.",
    quality_meta="High-quality illustration with clear details.",
    HTML_web_color_name="lightblue",
)

# Add water flowing back into the lake (runoff)
canvas.add_local_description(
    name="water_to_lake",
    bbox=[60, 60, 30, 20],
    distance_to_viewer=5.0,
    description="Water flowing back into the lake.",
    detailed_descriptions=[
        "Small streams running down the hillside into the lake.",
        "Water collects in the lake, completing the cycle.",
    ],
    tags="collection, runoff, streams, flowing water, hillside",
    atmosphere="Natural and continuous.",
    style="Simple and clear, suitable for a diagram.",
    quality_meta="High-quality illustration with clear details.",
    HTML_web_color_name="blue",
)

# Add water vapor rising from plants (transpiration)
canvas.add_local_description(
    name="plant_vapor",
    bbox=[60, 40, 20, 20],
    distance_to_viewer=7.0,
    description="Water vapor rising from plants.",
    detailed_descriptions=[
        "Light wisps of vapor rising from trees and plants on the hillside.",
        "Represents transpiration from vegetation.",
    ],
    tags="transpiration, plants, water vapor, vegetation",
    atmosphere="Light and airy.",
    style="Simple and clear, suitable for a diagram.",
    quality_meta="High-quality illustration with clear details.",
    HTML_web_color_name="white",
)
