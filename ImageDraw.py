#Draws any ASCII passwordcard output as image and saves it as a png file.
import matplotlib.pyplot as plt


def DrawPasswordCard(filename: str):
    
    # Read passwordcard.txt
    with open(filename, "r") as f:
        ascii_example = f.read()

    # Replace $ with \$ to escape it
    ascii_example = ascii_example.replace("$", "\$")

    # Convert ASCII to image
    fig = plt.figure()
    plt.text(0, 0, ascii_example, fontsize=12, family='monospace', usetex=False)
    plt.axis('off')
    plt.savefig("ascii.png", bbox_inches='tight', pad_inches=0)
    plt.close(fig)