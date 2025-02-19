from PIL import Image

def divide_image(image_path, output_directory, num_rows):
    # Open the image file
    image = Image.open(image_path)

    # Get the width and height of the image
    width, height = image.size

    # Calculate the height of each section/row
    section_height = height // num_rows

    # Iterate over the rows and save each section
    for row in range(num_rows):
        # Calculate the starting and ending pixel coordinates for the current section
        start_y = row * section_height
        end_y = start_y + section_height

        # Crop the section from the original image
        section = image.crop((0, start_y, width, end_y))

        # Save the section as a new image
        output_path = f"{output_directory}/{page_num}section_{row+1}.jpg"
        section.save(output_path)

        print(f"Section {row+1} saved as {output_path}")

# Example usage
page_num="page1"
image_path = "/Users/joonghochoi/Desktop/fun/OCR/%s.jpg" %(page_num)
output_directory = "/Users/joonghochoi/Desktop/fun/OCR/KTL_work"
num_rows = 5

divide_image(image_path, output_directory, num_rows)