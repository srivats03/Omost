from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description='A diagram explaining photosynthesis.',
    detailed_descriptions=[
        'The diagram illustrates the process of photosynthesis, showing the conversion of sunlight, water, and carbon dioxide into glucose and oxygen.',
        'The main components include a plant leaf with chloroplasts, sunlight rays, water molecules, carbon dioxide, glucose, and oxygen.',
        'The diagram is designed to be visually engaging and educational, with clear labels and arrows to show the flow of energy and materials.',
        'The background is a simple green to represent a natural environment.',
        'The overall layout is organized to clearly show the steps involved in photosynthesis, with each component having its own section and explanation.',
    ],
    tags='diagram, photosynthesis, plant leaf, chloroplasts, sunlight, water, carbon dioxide, glucose, oxygen, educational, visually engaging, clear labels, arrows, energy flow, natural environment, green background, conversion process, scientific illustration, step-by-step explanation',
    HTML_web_color_name='green',
)

# Add plant leaf with chloroplasts
canvas.add_local_description(
    name="leaf",
    location='in the center',
    offset='no offset',
    area='a medium-sized square area',
    distance_to_viewer=1.0,
    description='Plant leaf with chloroplasts',
    detailed_descriptions=[
        'The central component of the diagram is a plant leaf, showcasing its structure and the presence of chloroplasts.',
        'The leaf is green, indicating the presence of chlorophyll, which is essential for photosynthesis.',
        'The chloroplasts are depicted as small, green organelles scattered throughout the leaf.',
        'The veins of the leaf are also visible, showing the network of tiny blood vessels that distribute nutrients.',
        'The overall appearance is realistic, with intricate details to make the leaf appear lifelike.',
    ],
    tags='plant leaf, chloroplasts, chlorophyll, green, structure, veins, blood vessels, nutrients, realistic, lifelike, detailed',
    atmosphere='Educational and informative, focusing on the plant leaf.',
    style='Realistic and detailed, with intricate features.',
    quality_meta='High-quality, lifelike appearance with detailed features.',
    HTML_web_color_name='green',
)

# Add sunlight rays
canvas.add_local_description(
    name="Sunlight",
    location='on the left',
    offset='slightly to the upper',
    area='a small vertical area',
    distance_to_viewer=1.5,
    description='Sunlight rays',
    detailed_descriptions=[
        'On the left side of the diagram, slightly towards the upper area, are the sunlight rays.',
        'These rays are depicted as bright, yellowish beams of light, symbolizing the energy source for photosynthesis.',
        'The rays are drawn to resemble the sun’s light, with a slight gradient to indicate their intensity.',
        'This component is crucial in illustrating the energy input required for photosynthesis to occur.',
    ],
    tags='sunlight rays, bright, yellowish, beams of light, energy source, gradient, intensity, sun’s light, crucial, illustrating',
    atmosphere='Bright and energetic, symbolizing sunlight.',
    style='Bright and gradient, with a focus on light intensity.',
    quality_meta='High-quality, bright and energetic depiction.',
    HTML_web_color_name='yellow',
)

# Add water molecules
canvas.add_local_description(
    name="Water molecules",
    location='on the right',
    offset='slightly to the lower',
    area='a small vertical area',
    distance_to_viewer=1.5,
    description='Water molecules',
    detailed_descriptions=[
        'On the right side of the diagram, slightly towards the lower area, are the water molecules.',
        'These molecules are represented as small, blue spheres, symbolizing the water required for photosynthesis.',
        'The spheres are grouped together to indicate the amount of water needed.',
        'This component is essential in showing the water input required for the process to occur.',
    ],
    tags='water molecules, small, blue, spheres, water required, grouped, amount, essential, input, process',
    atmosphere='Cool and essential, symbolizing water.',
    style='Simple and blue, with grouped spheres.',
    quality_meta='High-quality, cool and essential depiction.',
    HTML_web_color_name='blue',
)

# Add carbon dioxide
canvas.add_local_description(
    name="Carbon dioxide",
    location='on the top',
    offset='slightly to the left',
    area='a small horizontal area',
    distance_to_viewer=1.75,
    description='Carbon dioxide',
    detailed_descriptions=[
        'At the top of the diagram, slightly to the left, is the carbon dioxide.',
        'This component is depicted as small, grey CO2 molecules, symbolizing the carbon dioxide needed for photosynthesis.',
        'The molecules are drawn in a way that indicates their presence and importance in the process.',
        'This component is crucial in illustrating the role of carbon dioxide in photosynthesis.',
    ],
    tags='carbon dioxide, small, grey, CO2 molecules, needed, presence, importance, process, crucial, illustrating, role',
    atmosphere='Grey and essential, symbolizing carbon dioxide.',
    style='Grey and simple, with CO2 molecules.',
    quality_meta='High-quality, grey and essential depiction.',
    HTML_web_color_name='grey',
)

# Add glucose and oxygen
canvas.add_local_description(
    name="Glucose and oxygen",
    location='on the bottom',
    offset='slightly to the right',
    area='a small horizontal area',
    distance_to_viewer=1.75,
    description='Glucose and oxygen',
    detailed_descriptions=[
        'At the bottom of the diagram, slightly to the right, are the glucose and oxygen produced by photosynthesis.',
        'These components are depicted as small, green glucose molecules and small, white oxygen molecules.',
        'The molecules are drawn in a way that indicates their formation and importance in the process.',
        'This component is crucial in illustrating the output of photosynthesis.',
    ],
    tags='glucose, oxygen, small, green, white, molecules, formation, importance, process, crucial, illustrating, output',
    atmosphere='Green and white, symbolizing glucose and oxygen.',
    style='Green and white, with glucose and oxygen molecules.',
    quality_meta='High-quality, green and white depiction.',
    HTML_web_color_name='white',
)