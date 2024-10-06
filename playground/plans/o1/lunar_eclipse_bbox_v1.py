from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description="A diagram showing how a lunar eclipse happens.",
    detailed_descriptions=[
        "The Sun, Earth, and Moon are aligned in a straight line.",
        "The Earth is positioned between the Sun and the Moon.",
        "The Earth's shadow falls on the Moon, causing the lunar eclipse.",
        "The Sun is on the left side, emitting light towards the Earth.",
        "The Earth is in the center of the diagram.",
        "The Moon is on the right side, entering the Earth's shadow.",
        "The Earth's umbra and penumbra are depicted.",
        "The background is space with scattered stars.",
        "The overall atmosphere is educational and clear.",
    ],
    tags="lunar eclipse, Sun, Earth, Moon, shadow, umbra, penumbra, alignment, space, astronomy, diagram",
    HTML_web_color_name="black",
)

# Add the Sun
canvas.add_local_description(
    name="Sun",
    bbox=[0, 30, 20, 30],
    distance_to_viewer=10.0,
    description="The Sun emitting light towards the Earth.",
    detailed_descriptions=[
        "Bright yellow Sun on the left side.",
        "Sun with rays extending outward.",
        "Sunlight directed towards the Earth.",
    ],
    tags="Sun, bright, yellow, rays, light, space, star",
    atmosphere="Bright and radiant, illuminating the scene.",
    style="Simple and clear, suitable for educational purposes.",
    quality_meta="High resolution with clear details.",
    HTML_web_color_name="gold",
)

# Add the Earth
canvas.add_local_description(
    name="Earth",
    bbox=[35, 35, 20, 20],
    distance_to_viewer=5.0,
    description="The Earth positioned between the Sun and Moon.",
    detailed_descriptions=[
        "Blue and green Earth in the center.",
        "Displays continents and oceans.",
        "Earth shown as a sphere.",
    ],
    tags="Earth, planet, blue, green, continents, oceans, sphere",
    atmosphere="Calm and educational.",
    style="Detailed but simple, suitable for kids.",
    quality_meta="High resolution with clear continents and oceans.",
    HTML_web_color_name="blue",
)

# Add the Moon
canvas.add_local_description(
    name="Moon",
    bbox=[70, 40, 15, 15],
    distance_to_viewer=5.0,
    description="The Moon entering Earth's shadow.",
    detailed_descriptions=[
        "Gray Moon on the right side.",
        "Moon within Earth's shadow.",
        "Moon surface shows craters.",
    ],
    tags="Moon, satellite, gray, craters, shadow",
    atmosphere="Dimmed due to Earth's shadow.",
    style="Simple and clear.",
    quality_meta="High resolution with visible craters.",
    HTML_web_color_name="lightgray",
)

# Add Earth's shadow (umbra and penumbra)
canvas.add_local_description(
    name="Shadow",
    bbox=[50, 35, 30, 20],
    distance_to_viewer=5.0,
    description="Earth's shadow falling on the Moon.",
    detailed_descriptions=[
        "Cone-shaped shadow extending from Earth to Moon.",
        "Shadow includes darker umbra and lighter penumbra.",
        "Demonstrates how Earth's shadow covers the Moon.",
    ],
    tags="shadow, umbra, penumbra, eclipse, Earth's shadow",
    atmosphere="Demonstrates the shadow effect clearly.",
    style="Clear and illustrative.",
    quality_meta="High resolution with distinct shadow areas.",
    HTML_web_color_name="dimgray",
)

# Add background stars
canvas.add_local_description(
    name="Stars",
    bbox=[0, 0, 90, 90],
    distance_to_viewer=15.0,
    description="Background of space with scattered stars.",
    detailed_descriptions=[
        "Black background dotted with small white stars.",
        "Stars scattered throughout the space.",
        "Creates a space setting for the diagram.",
    ],
    tags="stars, space, background, astronomy",
    atmosphere="Calm and vast.",
    style="Simple and not distracting.",
    quality_meta="High resolution with clear stars.",
    HTML_web_color_name="black",
)