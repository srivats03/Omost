from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description="Diagram showing how a rainbow is formed through sunlight and raindrops.",
    detailed_descriptions=[
        "The diagram illustrates the formation of a rainbow when sunlight passes through raindrops.",
        "On the left side, the sun shines brightly, emitting light towards the raindrops on the right.",
        "On the right side, raindrops are falling from a cloud.",
        "An arc-shaped rainbow appears opposite the sun, displaying the sequence of colors.",
        "The background is a light blue sky with scattered clouds.",
        "At the bottom, there is a simple green field.",
    ],
    tags="rainbow, sunlight, raindrops, refraction, reflection, spectrum, colors, sun, clouds, sky, field",
    HTML_web_color_name="skyblue",
)

# Add the sun
canvas.add_local_description(
    name="sun",
    bbox=[0, 0, 20, 20],
    distance_to_viewer=10.0,
    description="A bright sun emitting rays of light.",
    detailed_descriptions=[
        "The sun is in the top-left corner, a bright yellow circle.",
        "It has rays extending outward, representing sunlight.",
        "The sun's rays reach towards the raindrops on the right.",
    ],
    tags="sun, bright, yellow, rays, light, top-left",
    atmosphere="Bright and sunny, providing light for the rainbow.",
    style="Simple and clear, suitable for educational purposes.",
    quality_meta="High resolution with clear lines and bright colors.",
    HTML_web_color_name="yellow",
)

# Add the cloud with raindrops
canvas.add_local_description(
    name="cloud",
    bbox=[70, 0, 20, 20],
    distance_to_viewer=10.0,
    description="A gray cloud with falling raindrops.",
    detailed_descriptions=[
        "A gray cloud is in the top-right corner.",
        "Blue raindrops are falling from the cloud.",
        "The raindrops represent the water droplets that form the rainbow.",
    ],
    tags="cloud, gray, raindrops, blue, top-right",
    atmosphere="Rainy, providing raindrops for the rainbow.",
    style="Simple and clear, suitable for educational purposes.",
    quality_meta="High resolution with clear shapes.",
    HTML_web_color_name="lightgray",
)

# Add the rainbow
canvas.add_local_description(
    name="rainbow",
    bbox=[20, 40, 50, 20],
    distance_to_viewer=5.0,
    description="An arc-shaped rainbow displaying spectrum of colors.",
    detailed_descriptions=[
        "A colorful rainbow arc spans across the middle of the image.",
        "The rainbow shows red, orange, yellow, green, blue, indigo, and violet.",
        "The arc is smooth and vibrant against the sky.",
    ],
    tags="rainbow, arc, colors, spectrum, red, orange, yellow, green, blue, indigo, violet",
    atmosphere="Vibrant and colorful, showcasing the beauty of a rainbow.",
    style="Bright and vivid colors, attracting attention.",
    quality_meta="High resolution with smooth gradients.",
    HTML_web_color_name="violet",
)

# Add light rays from the sun to the raindrops
canvas.add_local_description(
    name="light_rays",
    bbox=[20, 10, 50, 30],
    distance_to_viewer=8.0,
    description="Rays of sunlight traveling from the sun to the raindrops.",
    detailed_descriptions=[
        "Straight lines represent light rays from the sun to the raindrops.",
        "The rays are light yellow lines crossing the image diagonally.",
        "They illustrate how sunlight reaches the raindrops.",
    ],
    tags="light rays, sunlight, lines, yellow",
    atmosphere="Clear depiction of sunlight traveling to the raindrops.",
    style="Simple lines, easy to understand.",
    quality_meta="High resolution with clear, thin lines.",
    HTML_web_color_name="gold",
)

# Add the ground
canvas.add_local_description(
    name="ground",
    bbox=[0, 60, 90, 30],
    distance_to_viewer=10.0,
    description="A simple green field at the bottom of the image.",
    detailed_descriptions=[
        "A flat green field spans the bottom part of the image.",
        "It provides a base for the rainbow.",
    ],
    tags="field, ground, green, bottom",
    atmosphere="Calm and natural, serving as a base for the diagram.",
    style="Simple and solid color.",
    quality_meta="High resolution with even color.",
    HTML_web_color_name="green",
)
