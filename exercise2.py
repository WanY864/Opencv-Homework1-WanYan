import cv2
import argparse

def on_trackbar(x):
    pass

def main():
    parser = argparse.ArgumentParser( description="Interactive CLAHE by OpenCV trackbars.")

    parser.add_argument( "image", type=str, help="Path for the input image")

    args = parser.parse_args()

    img = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE)

    if img is None:
        raise FileNotFoundError(f"Cannot load image: {args.image}")

    window_name = "Interactive CLAHE"

    cv2.namedWindow(window_name)

    min_grid = 4
    max_grid = 64
    min_clip = 10
    max_clip = 100
    parts = 10.0
    temp = 10

    cv2.createTrackbar( "Grid Size", window_name, min_grid, max_grid, on_trackbar )

    cv2.createTrackbar( "Clip Limit x parts", window_name, min_clip, max_clip, on_trackbar )

    while True:
        
        grid = cv2.getTrackbarPos( "Grid Size", window_name)

        clip_value = cv2.getTrackbarPos( "Clip Limit x parts", window_name)

        grid = max(grid, 1)
        clip_limit = max(clip_value, 1) / parts

        clahe = cv2.createCLAHE( clipLimit=clip_limit, tileGridSize=(grid, grid))

        result = clahe.apply(img)

        cv2.imshow(window_name, result)

        key = cv2.waitKey(temp)

        if key == 27:  # ESC
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
