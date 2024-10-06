from lib_omost.canvas import Canvas

# Initialize the canvas
canvas = Canvas()

# Set a global description for the canvas
canvas.set_global_description(
    description='A diagram explaining the formation of a rainbow.',
    detailed_descriptions=[
        'This diagram illustrates the formation of a rainbow.',
        'It features a bright, colorful arc of light, suspended in the air, with rays of sunlight shining through it.',
        'The sunlight is depicted as a beam entering the atmosphere from the top-left corner, splitting into different colors as it passes through water droplets.',
        'These water droplets are shown in various sizes, suspended in the air, creating a prism effect.',
        'The rainbow arc is vibrant, with colors ranging from red to violet, and is positioned in the center of the diagram.',
        'The entire scene is set against a clear blue sky, with a few scattered clouds.',
        'The diagram aims to visually demonstrate the refraction and dispersion of sunlight as it interacts with water droplets, resulting in the formation of a rainbow.',
    ],
    tags='diagram, rainbow formation, sunlight, water droplets, prism effect, colorful arc, refraction, dispersion, bright colors, clear blue sky, scattered clouds, atmospheric, beam of light, suspended in air, visual explanation, educational, science, nature, weather, light physics, optical phenomenon',
    HTML_web_color_name='skyblue',
)

# Add the rainbow arc
canvas.add_local_description(
    name="rainbow",
    location='in the center',
    offset='no offset',
    area='a large vertical area',
    distance_to_viewer=1.0,
    description='The rainbow arc',
    detailed_descriptions=[
        'The central feature of the diagram is a vibrant rainbow arc.',
        'The arc is depicted with bright, vivid colors ranging from red to violet.',
        'The colors are smooth and well-defined, showing the typical gradient of a rainbow.',
        'The arc appears to be suspended in the air, with its base and top slightly curved.',
        'This part of the diagram aims to illustrate the beauty and vividness of a rainbow.',
    ],
    tags='rainbow arc, bright colors, vivid, gradient, suspended, beauty, vividness, central feature, smooth, well-defined, atmospheric',
    atmosphere='Vivid and colorful, capturing the beauty of a rainbow.',
    style='Realistic and detailed, with a focus on the colors and gradient.',
    quality_meta='High-quality depiction with smooth gradients and vivid colors.',
    HTML_web_color_name='gold',
)

# Add sunlight beam
canvas.add_local_description(
    name="Sunlight",
    location='on the top-left',
    offset='slightly to the lower-right',
    area='a small horizontal area',
    distance_to_viewer=2.5,
    description='Sunlight beam',
    detailed_descriptions=[
        'The diagram features a bright beam of sunlight entering from the top-left corner.',
        'The beam is depicted as a concentrated ray of light, symbolizing the source of the rainbow.',
        'This beam is shown splitting into different colors as it passes through the water droplets, illustrating the dispersion of light.',
        'The sunlight is vibrant, with a golden hue, and it creates a sense of warmth and brightness.',
    ],
    tags='sunlight beam, concentrated ray, source of rainbow, dispersion of light, vibrant, golden hue, warmth, brightness, atmospheric, visual explanation',
    atmosphere='Warm and bright, symbolizing the source of the rainbow.',
    style='Realistic with a focus on the light and its dispersion.',
    quality_meta='High-quality depiction with vibrant colors and a sense of warmth.',
    HTML_web_color_name='gold',
)

# Add water droplets
canvas.add_local_description(
    name="droplets",
    location='on the top',
    offset='slightly to the lower-left',
    area='a medium-sized horizontal area',
    distance_to_viewer=3.0,
    description='Water droplets',
    detailed_descriptions=[
        'The diagram includes water droplets suspended in the air.',
        'These droplets are depicted in various sizes, illustrating the different conditions under which a rainbow can form.',
        'The droplets are shown as small, transparent spheres, with light reflecting off their surfaces.',
        'This part of the diagram aims to visually demonstrate how water droplets interact with sunlight, creating the prism effect that forms a rainbow.',
    ],
    tags='water droplets, suspended in air, various sizes, transparent spheres, light reflection, prism effect, atmospheric, visual explanation, formation conditions',
    atmosphere='Clear and transparent, illustrating the interaction with sunlight.',
    style='Detailed and realistic, with a focus on the transparency and light reflection.',
    quality_meta='High-quality depiction with clear and transparent water droplets.',
    HTML_web_color_name='lightcyan',
)

# Add clear blue sky
canvas.add_local_description(
    name="sky",
    location='on the top',
    offset='slightly to the lower-right',
    area='a small horizontal area',
    distance_to_viewer=4.0,
    description='Clear blue sky',
    detailed_descriptions=[
        'The diagram is set against a clear blue sky, which provides a serene and natural backdrop.',
        'The sky is depicted with a smooth gradient of blue hues, ranging from light to deep blue.',
        'A few scattered clouds are also shown, adding to the natural ambiance of the scene.',
        'This part of the diagram aims to create a sense of openness and tranquility, typical of a clear day.',
    ],
    tags='clear blue sky, serene, natural backdrop, smooth gradient, blue hues, scattered clouds, natural ambiance, openness, tranquility, atmospheric',
    atmosphere='Serene and tranquil, providing a natural backdrop.',
    style='Smooth and realistic, with a focus on the gradient and scattered clouds.',
    quality_meta='High-quality depiction with smooth gradients and natural ambiance.',
    HTML_web_color_name='deepskyblue',
)