from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description="A space background filled with stars.",
    detailed_descriptions=[
        "The background is a deep, dark space with numerous stars scattered throughout.",
        "Stars of varying sizes and brightness create a sense of depth and vastness.",
        "Some stars are small and twinkling, while others are larger and more luminous.",
        "The overall color palette is dark navy blue transitioning to black.",
    ],
    tags="space, stars, dark, navy blue, twinkling, luminous, vast, background",
    HTML_web_color_name="midnightblue",
)

# Add Earth with tidal bulges
canvas.add_local_description(
    bbox=[30, 30, 30, 30],
    distance_to_viewer=5.0,
    description="Planet Earth with tidal bulges.",
    detailed_descriptions=[
        "Earth is centered in the image, showing blue oceans and green continents.",
        "On opposite sides of Earth, subtle bulges represent high tides.",
        "The tidal bulges are aligned along the axis pointing toward and away from the Moon.",
        "White clouds are scattered over the Earth's surface.",
        "A thin, light blue atmosphere surrounds the planet.",
    ],
    tags="Earth, oceans, continents, tidal bulges, high tides, clouds, atmosphere, planet",
    atmosphere="Calm and educational, focusing on Earth's features.",
    style="Realistic and detailed illustration of Earth.",
    quality_meta="High resolution with accurate colors and sharp details.",
    HTML_web_color_name="blue",
)

# Add the Moon orbiting Earth
canvas.add_local_description(
    bbox=[65, 40, 15, 15],
    distance_to_viewer=6.0,
    description="The Moon orbiting Earth.",
    detailed_descriptions=[
        "A smaller sphere representing the Moon is positioned to the right of Earth.",
        "The Moon appears in shades of gray with visible craters and texture.",
        "It is smaller than Earth, illustrating the relative size difference.",
        "The Moon's position indicates its gravitational influence on Earth's tides.",
    ],
    tags="Moon, gray, craters, orbit, satellite, Earth's moon, smaller",
    atmosphere="Informative, highlighting the Moon's relation to Earth.",
    style="Realistic with detailed textures on the Moon's surface.",
    quality_meta="High resolution with clear surface details.",
    HTML_web_color_name="lightgray",
)

# Add the Sun in the background
canvas.add_local_description(
    bbox=[0, 0, 30, 30],
    distance_to_viewer=7.0,
    description="A portion of the Sun in the background.",
    detailed_descriptions=[
        "The Sun is partially visible in the upper left corner.",
        "It is depicted as a bright, glowing sphere with fiery textures.",
        "Radiating rays extend outward, blending into the space background.",
        "The Sun is larger than both Earth and Moon but appears further away.",
    ],
    tags="Sun, bright, glowing, yellow, orange, rays, background, star",
    atmosphere="Warm and radiant, indicating the Sun's presence.",
    style="Vibrant depiction of the Sun with glowing effects.",
    quality_meta="High resolution with vivid colors and light effects.",
    HTML_web_color_name="gold",
)
