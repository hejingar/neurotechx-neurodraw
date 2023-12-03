# neurotechx-neurodraw

Install :

Create a new python environment (conda or pythonvenv), and install the requirements in requirements.txt (pip install requirements)
Run the generate.py script and enjoy! You'll need to put an initial prompt instruction (or let it blank for full creativity!) and specify the relative or absolute path to your EEG csv data (you can send it raw, we'll clean it for you 🍪)

Open Issue if you have some trouble running it.

NB: For the first run, the install might be excessively long because of the stable diffusion model download (weights around 5gb). You also need at least 6gb of free RAM to use this script in the best condition, otherwise the memory swaps might make the generation a bit longer.
Image generation takes around 2-3s on an entry level user GPU 


Documentation : 
#### Introduction
NeuroDraw is an innovative project that bridges the gap between neuroscience and art, transforming EEG (electroencephalogram) brainwave data into captivating art pieces using cutting-edge AI technology. This project leverages the power of EEG devices to capture the subtle fluctuations in brain activity and employs AI models, specifically Stable Diffusion, to translate these readings into visually stunning artworks. This intersection of science and art offers a unique perspective into the human mind, making the invisible visible and tangible.

#### Concept Overview
- **Objective**: To create a platform where users can visualize their current mental states as art, offering a new way to understand and appreciate the complexities of human brain activity.
- **Target Audience**: Anyone interested in neurofeedback, mental health enthusiasts, art lovers, educators, and researchers in neuroscience.

#### Technical Components
1. **EEG Measuring Devices**:  IDUN Guardian
   - Utilizes non-invasive EEG technology to measure brainwaves in real-time.

2. **AI-Generated Art with Stable Diffusion**:
   - A cutting-edge AI model transforms EEG data into specific visual prompts.
   - Each brainwave type is associated with certain visual elements and styles.
   - The AI generates art pieces that are not only aesthetically pleasing but also scientifically representative of the user's brain activity.

3. **User Interface**:
   - A user-friendly application that integrates EEG reading and art generation.
   - Features include real-time EEG data display, image generation, and the ability to save and share generated art.

#### Use Cases
- **Mental Health Awareness**: Visualizing brain activity can offer insights into one's mental state, potentially aiding in mindfulness and mental health awareness.
- **Educational Tool**: A novel approach for educators to teach about neurology and the science of the brain.
- **Artistic Exploration**: Artists and creators can use this tool to explore new frontiers of art, where science meets creativity.

#### Unique Selling Points
- **Innovative Integration**: One of the first platforms to combine EEG technology with AI-driven art generation.
- **Customizable Experience**: Each art piece is unique, reflecting the individual's specific brain activity at that moment.
- **Scientific and Artistic Merit**: Appeals to both the scientific community for its data representation and the art community for its creative expression.

#### Future Prospects
- **Therapeutic Applications**: Potential use in therapy and relaxation techniques, where users can see and understand the impact of different therapeutic interventions on their brain activity.
- **Collaborations and Exhibitions**: Opportunities for collaborations with artists, galleries, and educational institutions to showcase the intersection of neuroscience and art.
- **Enhanced User Engagement**: Development of features like trend analysis of brain activity over time and integration with virtual reality for a more immersive experience.

#### Conclusion
NeuroDraw stands at the forefront of an exciting fusion of technology, neuroscience, and art. It offers a unique and interactive way for individuals to connect with their mental state, promoting both self-awareness and appreciation for the complexities of the human mind. Through NeuroDraw, we aim to demystify brain activity and make it accessible and engaging for everyone.
