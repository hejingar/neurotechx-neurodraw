# neurotechx-neurodraw

Install :

Create a new python environment (conda or pythonvenv), and install the requirements in requirements.txt (pip install requirements)
Run the generate.py script and enjoy! You'll need to put an initial prompt instruction (or let it blank for full creativity!) and specify the relative or absolute path to your EEG csv data (you can send it raw, we'll clean it for you 🍪)

Open Issue if you have some trouble running it.

NB: For the first run, the install might be excessively long because of the stable diffusion model download (weights around 5gb). You also need at least 6gb of free RAM to use this script in the best condition, otherwise the memory swaps might make the generation a bit longer.
Image generation takes around 2-3s on an entry level user GPU 
