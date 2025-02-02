import cv2


def annotate_license_plate(input_path, output_path):
    try:

        image = cv2.imread(input_path)
        if image is None:
            raise FileNotFoundError("Could not load the image. Check the file path.")

        height, width = image.shape[:2]

        x1, y1 = int(width * 0.21), int(height * 0.20)
        x2, y2 = int(width * 0.78), int(height * 0.97)

        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 6)

        text = "RAH972U"
        text_x, text_y = int(width * 0.68), int(height * 0.19)
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale, thickness = 1.5, 4
        text_color = (0, 255, 0)

        overlay = image.copy()
        (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)
        cv2.rectangle(
            overlay, (text_x - 5, text_y - text_height - 5),
            (text_x + text_width + 5, text_y + 5), (0, 0, 0), -1
        )

        cv2.addWeighted(overlay, 0.5, image, 0.5, 0, image)

        cv2.putText(image, text, (text_x, text_y), font, font_scale, text_color, thickness)

        cv2.imwrite(output_path, image)

        return image
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    input_image = "assignment-001-given.jpg"
    output_image = "result.jpg"

    result = annotate_license_plate(input_image, output_image)

    if result is not None:
        cv2.imshow("Annotated License Plate", result)
        print("Press any key to close the image and save the result.")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(f"Annotated image saved at {output_image}.")
    else:
        print("Failed to annotate the image.")


if __name__ == "__main__":
    main()
