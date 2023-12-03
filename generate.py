from diffusers import AutoPipelineForText2Image
import torch
import random
import tkinter as tk
from tkinter import Button, Label, Entry
from PIL import Image, ImageTk
from plottin import compute_frequencies_percentage

# load that sdxl-turbooo
pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16")
pipe.to("cuda")

# prompt = "A cinematic shot of a baby racoon wearing an intricate italian priest robe."

def generate_brain_wave_prompt(initial_prompt, delta_percent, theta_percent, alpha_percent, beta_percent, gamma_percent):
    """
    :param initial_prompt: Chosen by the user to style his generation
    :param delta_percent: Percentage of Delta brain waves
    :param theta_percent: Percentage of Theta brain waves
    :param alpha_percent: Percentage of Alpha brain waves
    :param beta_percent: Percentage of Beta brain waves
    :param gamma_percent: Percentage of Gamma brain waves
    :return: A brain wave custom prompt string
    """

    # Define the adjective lists for each brain wave type
    delta_adjectives = [
        "Serene", "Sombre", "Ethereal", "Misty", "Gentle",
        "Luminous", "Dreamlike", "Subdued", "Monochromatic", "Fluid"
    ]
    theta_adjectives = [
        "Ethereal", "Fluid", "Mystical", "Surreal", "Hazy",
        "Translucent", "Whimsical", "Melancholic", "Organic", "Soft-focus"
    ]
    alpha_adjectives = [
        "Tranquil", "Harmonious", "Soft", "Fluid", "Luminous",
        "Pastel", "Ethereal", "Dreamy", "Meditative", "Subtle"
    ]
    beta_adjectives = [
        "Vibrant", "Dynamic", "Sharp", "Intense", "Contrasted",
        "Bold", "Geometric", "Detailed", "Saturated", "Energetic"
    ]
    gamma_adjectives = [
        "Intricate", "Vivid", "Radiant", "Dynamic", "Sharp",
        "Synchronized", "Intense", "Pulsating", "Luminous", "Kaleidoscopic"
    ]

    def select_adjectives(adjective_list, percent):
        count = max(1, int(len(adjective_list) * (percent / 100)))
        return random.sample(adjective_list, count)

    # Select adjectives for each brain wave type based on the given percentages
    selected_delta = select_adjectives(delta_adjectives, delta_percent)
    selected_theta = select_adjectives(theta_adjectives, theta_percent)
    selected_alpha = select_adjectives(alpha_adjectives, alpha_percent)
    selected_beta = select_adjectives(beta_adjectives, beta_percent)
    selected_gamma = select_adjectives(gamma_adjectives, gamma_percent)

    # Build the prompt
    # prompt = "Create a paysage drawing with "
    prompt = initial_prompt
    prompt += ", ".join(selected_delta) #+ " for Delta; "
    prompt += ", ".join(selected_theta) #+ " for Theta; "
    prompt += ", ".join(selected_alpha) #+ " for Alpha; "
    prompt += ", ".join(selected_beta) #+ " for Beta; "
    prompt += ", ".join(selected_gamma) #+ " for Gamma."
    
    return prompt


def display_image(window, img_path, img_label_var):
    """
    :param window: The Tkinter window
    :param img_path: Path to the image file
    """
    img = Image.open(img_path)

    # need this to convert to the window
    img_tk = ImageTk.PhotoImage(img)

    # placing it
    if img_label_var:
        img_label_var[0].configure(image=img_tk)
        img_label_var[0].image = img_tk  # Keep a reference!
    else:
        img_label = Label(window, image=img_tk)
        img_label.image = img_tk  # Keep a reference!
        img_label.pack()
        img_label_var.append(img_label)

def generate_image(initial_prompt, img_label_var, delta, theta, alpha, beta, gamma):
    """
    :param initial_prompt: User chosen
    """
    prompt = generate_brain_wave_prompt(initial_prompt, delta, theta, alpha, beta, gamma)
    image = pipe(prompt=prompt, num_inference_steps=1, guidance_scale=0.0).images[0]
    img_path = "yoo.png"
    image.save(img_path)
    display_image(window, img_path, img_label_var)

# Onclick handling
def on_generate_button_click():
    prompt = prompt_entry.get()
    path = data_entry.get()
    data_list = compute_frequencies_percentage(path)
    for d in data_list:
        print(d)
    delta = data_list[0]
    theta = data_list[1]
    alpha = data_list[2]
    beta = data_list[3]
    gamma = data_list[4]

    # delta = delta_percent_entry.get()
    # theta = theta_percent_entry.get()
    # alpha = alpha_percent_entry.get()
    # beta = beta_percent_entry.get()
    # gamma = gamma_percent_entry.get()
    generate_image(prompt, img_label_var, int(delta), int(theta), int(alpha), int(beta), int(gamma))

window = tk.Tk()
window.title("Brain Wave Image Generator")

# Sweet user entry
prompt_label = tk.Label(window, text="Enter your initial prompt")
prompt_label.pack()
prompt_entry = Entry(window)
prompt_entry.pack()

data_label = tk.Label(window, text="Enter the path to your EEG csv data")
data_label.pack()
data_entry = tk.Entry(window)
data_entry.pack()

# theta_percent_entry = tk.Entry(window)
# theta_percent_entry.pack()

# alpha_percent_entry = tk.Entry(window)
# alpha_percent_entry.pack()

# beta_percent_entry = tk.Entry(window)
# beta_percent_entry.pack()

# gamma_percent_entry = tk.Entry(window)
# gamma_percent_entry.pack()

#to keep a reference so we can remove it
img_label_var = []

# sweet button
generate_button = Button(window, text="Generate Image", command=on_generate_button_click)
generate_button.pack()

# Run the application
window.mainloop()





# prompt = generate_brain_wave_prompt(5, 5, 10, 35, 45)

# delta = {
#     1: {'Serene': 'Calm, peaceful, and untroubled.'},
#     2: {'Sombre': 'Dark, dull in color, or muted, suggesting depth and introspection.'},
#     3: {'Ethereal': 'Light, airy, and otherworldly, evoking a sense of peace and tranquility.'},
#     4: {'Misty': 'Soft and indistinct, like a fog or haze, creating a soothing effect.'},
#     5: {'Gentle': 'Soft, tender, and mild in appearance.'},
#     6: {'Luminous': 'Subtly glowing, with a soft and calming light.'},
#     7: {'Dreamlike': 'Resembling a dream; surreal and unreal.'},
#     8: {'Subdued': 'Not bright, intense, or sharp; toned down.'},
#     9: {'Monochromatic': 'Consisting of one color or shades of one color, evoking simplicity and calm.'},
#     10: {'Fluid': 'Smooth and flowing, without sharp edges or abrupt changes.'}
# }

# gamma = {
#     1: {'Intricate': 'Highly detailed and complex.'},
#     2: {'Vivid': 'Strikingly bright or intense in color.'},
#     3: {'Radiant': 'Emitting light or energy; bright and shining.'},
#     4: {'Dynamic': 'Characterized by constant change, activity, or progress.'},
#     5: {'Sharp': 'Clearly defined or well-focused.'},
#     6: {'Synchronized': 'Exhibiting harmony and a well-ordered arrangement.'},
#     7: {'Intense': 'Very strong, deep, or concentrated in quality.'},
#     8: {'Pulsating': 'Throbbing or vibrating with energy.'},
#     9: {'Luminous': 'Emitting or reflecting light; glowing.'},
#     10: {'Kaleidoscopic': 'Continually changing in pattern or colors, complex and varied.'}
# }

# theta = {
#     1: {'Ethereal': 'Light, airy, and otherworldly, suggesting a dreamlike quality.'},
#     2: {'Fluid': 'Flowing and smooth, like water or gentle movement.'},
#     3: {'Mystical': 'Suggesting a sense of mystery or the supernatural.'},
#     4: {'Surreal': 'Beyond the ordinary or realistic, dreamlike.'},
#     5: {'Hazy': 'Indistinct or blurred, creating a sense of softness.'},
#     6: {'Translucent': 'Partially transparent, allowing light to pass through softly.'},
#     7: {'Whimsical': 'Playful or fanciful, often in an imaginative way.'},
#     8: {'Melancholic': 'Slightly somber or reflective, evoking deep emotions.'},
#     9: {'Organic': 'Natural forms and shapes, reminiscent of living things.'},
#     10: {'Soft-focus': 'Gently blurred, creating a calming and soothing effect.'}
# }

# beta = {
#     1: {'Vibrant': 'Bright and full of energy.'},
#     2: {'Dynamic': 'Indicating movement or activity.'},
#     3: {'Sharp': 'Clear, well-defined, and focused.'},
#     4: {'Intense': 'Strong and vivid in appearance.'},
#     5: {'Contrasted': 'Showing stark differences in color or light, creating a clear distinction.'},
#     6: {'Bold': 'Striking and prominent.'},
#     7: {'Geometric': 'Characterized by crisp, precise lines and shapes.'},
#     8: {'Detailed': 'Rich in details and intricate patterns.'},
#     9: {'Saturated': 'Deep, rich colors.'},
#     10: {'Energetic': 'Giving a sense of energy and liveliness.'}
# }