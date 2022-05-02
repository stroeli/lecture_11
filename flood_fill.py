import matplotlib.pyplot as plt

def flood_fill(img, x, y):

    if x < 0 or y < 0 or x > (img.shape[0] - 1) or y > (img.shape[1] - 1):
        return img
    if img[x, y] != 1:
        return img

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(0.1)
    plt.clf()

    if img[x, y] == 1:
        img[x, y] = 2
        flood_fill(img, x + 1, y)
        flood_fill(img, x - 1, y)
        flood_fill(img, x, y + 1)
        flood_fill(img, x, y - 1)
    return img

def main():
    # img = plt.imread("files/img0.png")[:, :, 0]
    img = plt.imread("files/img1.png")[:, :, 0]
    # img = plt.imread("files/img2.png")[:, :, 0]

    img = flood_fill(img, 0, 0)

    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()


if __name__ == "__main__":
    main()
