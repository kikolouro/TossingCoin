from blob import Blob
import random
numberofblobs = 5
chanceofcheating = 0.3
iterations = 100


def main():
    blobs = []
    for i in range(numberofblobs):
        blobs.append(Blob(random.random() < chanceofcheating))
    for i in range(iterations):
        for blob in blobs:
            result = blob.tossCoing()
            if result == "Heads":
                blob.addPoints(1)
    for blob in blobs:

        print( f"Cheating {blob.points}" if blob.ifcheater() else f"{blob.points}" )
main()
