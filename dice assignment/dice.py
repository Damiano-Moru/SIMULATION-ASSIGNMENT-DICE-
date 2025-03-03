import random

def roll_dice(num_rolls=1000):
    face_counts = {i: 0 for i in range(1, 7)}
    
    for _ in range(num_rolls):
        face = random.randint(1, 6)
        face_counts[face] += 1
    
    print("Face | Count | Percentage")
    print("------------------------")
    for face, count in face_counts.items():
        percentage = (count / num_rolls) * 100
        print(f"  {face}   |  {count}   |  {percentage:.1f}%")
if __name__ == "__main__":

    roll_dice()