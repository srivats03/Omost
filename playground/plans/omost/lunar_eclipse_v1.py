from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description='A diagram explaining how a lunar eclipse occurs.',
    detailed_descriptions=[
        'This diagram illustrates the process of a lunar eclipse, which occurs when the Earth, Moon, and Sun align in a straight line.',
        'The diagram features a celestial sphere with the Earth, Moon, and Sun represented as concentric circles.',
        'The Earth is shown with a blue atmosphere, the Moon with a bright, reflective surface, and the Sun with radiant solar flares.',
        'Shadows cast by the Earth onto the Moon are depicted with dark, gradient lines, demonstrating how the Earth blocks the Sun’s light, causing the Moon to appear dark during an eclipse.',
        'Additional details like the lunar phases and the alignment of celestial bodies are included to enhance the understanding of the lunar eclipse.',
    ],
    tags='lunar eclipse, celestial sphere, Earth, Moon, Sun, alignment, concentric circles, blue atmosphere, bright surface, solar flares, shadows, dark lines, gradient, light blocking, lunar phases, celestial bodies, understanding, diagram, illustration, astronomy, space, science',
    HTML_web_color_name='darkslategray',
)

# Add celestial sphere with earth, moon, and sun.
canvas.add_local_description(
    name="Celestial sphere",
    location='in the center',
    offset='no offset',
    area='a large square area',
    distance_to_viewer=1.5,
    description='Celestial sphere with Earth, Moon, and Sun.',
    detailed_descriptions=[
        'The celestial sphere is the central focus of this diagram, featuring concentric circles representing the Earth, Moon, and Sun.',
        'The Earth is depicted with a blue atmosphere, the Moon with a bright, reflective surface, and the Sun with radiant solar flares.',
        'This sphere helps to visualize the alignment of celestial bodies that leads to a lunar eclipse.',
    ],
    tags='celestial sphere, concentric circles, Earth, Moon, Sun, blue atmosphere, bright surface, solar flares, alignment, celestial bodies, visualization, lunar eclipse, astronomy, space, science',
    atmosphere='Astronomical and educational, focusing on celestial alignment.',
    style='Detailed and illustrative, with clear distinctions between celestial bodies.',
    quality_meta='High-quality illustration with clear, distinct features.',
    HTML_web_color_name='midnightblue',
)

# Add shadows cast by the earth.
canvas.add_local_description(
    name="Earth shadow",
    location='on the left',
    offset='slightly to the lower',
    area='a medium-sized vertical area',
    distance_to_viewer=1.0,
    description='Shadows cast by the Earth.',
    detailed_descriptions=[
        'On the left side of the diagram, shadows cast by the Earth onto the Moon are depicted.',
        'These shadows are represented by dark, gradient lines that demonstrate how the Earth blocks the Sun’s light, causing the Moon to appear dark during an eclipse.',
        'This part of the diagram helps to illustrate the cause of the eclipse, showing how the Earth’s shadow falls on the Moon.',
    ],
    tags="shadows, Earth, Moon, dark lines, gradient, light blocking, eclipse, astronomy, celestial alignment, lunar eclipse, science, illustration, visualization, cause, celestial bodies, Earth's shadow",
    atmosphere='Educational and focused on the cause of the eclipse.',
    style='Illustrative with gradient lines to show the shadow effect.',
    quality_meta='High-quality depiction of shadows with gradient effects.',
    HTML_web_color_name='black',
)

# Add lunar phases illustration.
canvas.add_local_description(
    name="Lunar phases",
    location='on the top',
    offset='slightly to the right',
    area='a medium-sized horizontal area',
    distance_to_viewer=2.0,
    description='Lunar phases illustration.',
    detailed_descriptions=[
        'At the top of the diagram, an illustration of lunar phases is included.',
        'This section shows the different stages of the Moon’s appearance as it orbits the Earth, from full moon to new moon.',
        'This part helps to provide context for the lunar eclipse, showing how the alignment of the Earth, Moon, and Sun leads to the eclipse.',
    ],
    tags="lunar phases, Moon, Earth, orbit, full moon, new moon, context, lunar eclipse, alignment, celestial bodies, astronomy, science, illustration, visualization, stages, Moon's appearance",
    atmosphere='Educational and contextual, focusing on lunar phases.',
    style='Illustrative with clear stages and phases of the Moon.',
    quality_meta='High-quality illustration of lunar phases with clear distinctions.',
    HTML_web_color_name='slategray',
)

# Add alignment of celestial bodies.
canvas.add_local_description(
    name="celestial bodies",
    location='on the bottom-right',
    offset='slightly to the upper-left',
    area='a small square area',
    distance_to_viewer=1.75,
    description='Alignment of celestial bodies.',
    detailed_descriptions=[
        'In the bottom-right corner, the alignment of celestial bodies is illustrated.',
        'This section shows the Earth, Moon, and Sun in a straight line, indicating the perfect alignment that leads to a lunar eclipse.',
        'This alignment is crucial for understanding the cause of the eclipse, and it is depicted with clear, illustrative lines.',
    ],
    tags='alignment, celestial bodies, Earth, Moon, Sun, straight line, lunar eclipse, cause, astronomy, science, illustration, visualization, celestial alignment, understanding, diagram',
    atmosphere='Focused and educational, highlighting the alignment.',
    style='Clear and illustrative, with emphasis on alignment.',
    quality_meta='High-quality illustration of celestial alignment.',
    HTML_web_color_name='dimgray',
)