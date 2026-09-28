import cv2
import argparse


def main():
    parser = argparse.ArgumentParser( description="Apply CLAHE to a image.")

    parser.add_argument( "image", type=str, help="Path for the input image")

    parser.add_argument( "--grid", type=int, default=8, help="Tile grid size")

    parser.add_argument( "--clip", type=float, default=2.0, help="CLAHE contrast limiting threshold")

    args = parser.parse_args()

    img = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE)

    if img is None:
        raise FileNotFoundError(f"Cannot load image: {args.image}")

    clahe = cv2.createCLAHE( clipLimit=args.clip, tileGridSize=(args.grid, args.grid))

    result = clahe.apply(img)

    cv2.imshow("Original Image", img)
    cv2.imshow("CLAHE Result", result)

    print(f"Grid size: {args.grid} x {args.grid}")
    print(f"Clip limit: {args.clip}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
