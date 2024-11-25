import time
import random
import os

def clear_screen():
    """Ekranni tozalash."""
    os.system("cls" if os.name == "nt" else "clear")

def print_road(player_pos, obstacles, level, score):
    """Yo‘lni chizish."""
    road = ["|       |"] * 10
    for obs in obstacles:
        road[obs[1]] = road[obs[1]][:obs[0] + 1] + "#" + road[obs[1]][obs[0] + 2:]
    road[9] = road[9][:player_pos + 1] + "P" + road[9][player_pos + 2:]
    clear_screen()
    for line in road:
        print(line)
    print("=========")
    print(f"Level: {level} | Score: {score}")

def move_obstacles(obstacles):
    """To‘siqlarni pastga siljitish."""
    return [[obs[0], obs[1] + 1] for obs in obstacles if obs[1] < 9]

def check_collision(player_pos, obstacles):
    """To‘qnashuvni tekshirish."""
    for obs in obstacles:
        if obs[1] == 9 and obs[0] == player_pos:
            return True
    return False

def main():
    print("Trafik Rider: Mototsikl Versiyasi")
    print("O‘yinni boshlash uchun ENTER tugmasini bosing!")
    input()

    player_pos = 3  # Mototsiklning boshlang‘ich pozitsiyasi
    obstacles = []  # To‘siqlar ro‘yxati
    score = 0       # Ball
    level = 1       # Boshlang‘ich daraja
    max_score = 150 # G‘alaba uchun kerak bo‘lgan ball

    try:
        while True:
            # Darajalar va tezlikni boshqarish
            if score >= 150:
                clear_screen()
                print("W I N N E R !")
                break
            elif score >= 100:
                level = 3
                speed = 0.2
            elif score >= 50:
                level = 2
                speed = 0.3
            else:
                level = 1
                speed = 0.5

            # To‘siqlarni qo‘shish
            if random.random() < 0.3:  # To‘siq paydo bo‘lish ehtimoli
                obstacles.append([random.randint(1, 5), 0])

            # To‘siqlarni harakatlantirish
            obstacles = move_obstacles(obstacles)

            # To‘qnashuvni tekshirish
            if check_collision(player_pos, obstacles):
                print("To‘qnashuv yuz berdi! O‘yin tugadi!")
                print(f"Jami ball: {score}")
                break

            # Yo‘lni chizish
            print_road(player_pos, obstacles, level, score)

            # Harakat qilish
            print("Harakat: [a] chapga | [d] o‘ngga | [q] chiqish")
            action = input(">>> ").strip().lower()
            if action == "a" and player_pos > 1:
                player_pos -= 1
            elif action == "d" and player_pos < 5:
                player_pos += 1
            elif action == "q":
                print("O‘yin tugadi!")
                break

            score += 1
            time.sleep(speed)  # Tezlikni darajaga qarab boshqarish

    except KeyboardInterrupt:
        print("\nO‘yin to‘xtatildi.")

if __name__ == "__main__":
    main()
