from PIL import Image
from os import listdir, mkdir, path, system
from rich.console import Console
from rich.theme import Theme


custom_theme = Theme({"success": "green", "error": "bold red"})
cs = Console(theme=custom_theme)
# This program compresses the images in the input folder and saves them in the output folder
if __name__ == "__main__":
    system("cls")
    # Create the output folder if it doesn't exist
    try:
        if not path.exists("images"):
            mkdir("images")
            cs.print(
                f">>>Folder [blue]{path.curdir}/images/ [green]created successfully!",
                style="success",
            )
        if not path.exists("images/compressed"):
            mkdir("images/compressed")
            cs.print(
                f">>>Folder [blue]{path.curdir}/images/compressed/ [green]created successfully!",
                style="success",
            )
    except OSError as e:
        cs.print(f"Error: Creating directory of data ({e})", style="error")

    # Get the input and output paths
    files = []
    input_string = cs.input(
        "[green]-|Enter the path of the image/s you want to compress (intro to default): "
    )
    output_string = cs.input(
        "[green]-|Enter the path of the output folder (intro to default): "
    )
    # Get the quality of the compression
    qlt = int(cs.input("[magenta]-|Enter the quality of the compression (1-10): "))
    cs.print("\n\n")
    # Check if the quality is between 1 and 10
    if qlt > 10:
        qlt = 10
    elif qlt < 1:
        qlt = 1
    # Check if the input and output paths are empty
    if input_string == "":
        input_string = "./images/"
    if output_string == "":
        output_string = "./images/compressed/"

    # Compress the images
    try:
        files = listdir(input_string)  # Get the files
        files = filter(
            lambda x: x.endswith(".jpg") or x.endswith(".png") or x.endswith(".jpeg"),
            files,
        )  # Filter the files
        for file in files:
            new_name = "compressed_" + file
            file_size = path.getsize(input_string + file)
            cs.print(
                "[red]Current File: [blue]"
                + input_string
                + file
                + "\n"
                + "[red]"
                + "Original Size: [blue]"
                + str(round((file_size / 1024) / 1204, 3))
                + " MB"
            )
            img = Image.open(input_string + file)  # Open the image
            img.save(
                output_string + new_name, optimize=True, quality=qlt * 10
            )  # Save the image
            cs.print(
                "[red]New File: [blue]"
                + output_string
                + new_name
                + "\n"
                + "[red]Compressed Size: [blue]"
                + str(round((path.getsize(output_string + new_name) / 1024) / 1204, 3))
                + " MB\n\n"
            )

    except OSError as e:  # If there is an error
        cs.print(
            f"Error: Creating directory of data ({e})", style="error"
        )  # Print the error
    finally:  # If everything is ok
        cs.print("Compression finished!", style="success")  # Print the message
