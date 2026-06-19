from abc import ABC, abstractmethod


class Companion(ABC):
    def __init__(self, name: str, **kwargs):
        self.name = name
        self.level = 1
        super().__init__(**kwargs)

    @abstractmethod
    def unleash_skill(self):
        pass

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Chỉ có thể lai tạo 2 sinh vật cùng loài!")
        return self._merge(other)

    @abstractmethod
    def _merge(self, other):
        pass


class Pet(Companion):
    def __init__(self, name: str, bonus_atk: int = 0, **kwargs):
        super().__init__(name=name, **kwargs)
        self.bonus_atk = bonus_atk

    def unleash_skill(self):
        print(f">> {self.name} gầm gừ: Tấn công kẻ thù, gây {self.bonus_atk} sát thương!")

    def _merge(self, other):
        merged = Pet(f"{self.name} {other.name}", bonus_atk=self.bonus_atk + other.bonus_atk)
        merged.level = self.level + 1
        return merged


class Mount(Companion):
    def __init__(self, name: str, bonus_speed: int = 0, **kwargs):
        super().__init__(name=name, **kwargs)
        self.bonus_speed = bonus_speed

    def unleash_skill(self):
        print(f">> {self.name} hí vang: Tăng tốc độ di chuyển thêm {self.bonus_speed} điểm!")

    def _merge(self, other):
        merged = Mount(f"{self.name} {other.name}", bonus_speed=self.bonus_speed + other.bonus_speed)
        merged.level = self.level + 1
        return merged


class Dragon(Pet, Mount):
    def __init__(self, name: str, bonus_atk: int = 0, bonus_speed: int = 0):
        super().__init__(name=name, bonus_atk=bonus_atk, bonus_speed=bonus_speed)

    def unleash_skill(self):
        print(f">> {self.name} thị uy:")
        print(f"   - Tấn công kẻ thù, gây {self.bonus_atk} sát thương!")
        print(f"   - Tăng tốc độ di chuyển thêm {self.bonus_speed} điểm!")

    def _merge(self, other):
        merged = Dragon(
            f"{self.name} {other.name}",
            bonus_atk=self.bonus_atk + other.bonus_atk,
            bonus_speed=self.bonus_speed + other.bonus_speed,
        )
        merged.level = self.level + 1
        return merged


def show_companions(companions: list):
    print("\n--- ĐỘI HÌNH SINH VẬT ---")
    if not companions:
        print("Chưa có sinh vật nào.")
        return
    for i, c in enumerate(companions, 1):
        tag = type(c).__name__.upper()
        info = f"{i}. [{tag}] {c.name} | Cấp: {c.level}"
        if isinstance(c, Pet):
            info += f" | Atk: +{c.bonus_atk}"
        if isinstance(c, Mount):
            info += f" | Speed: +{c.bonus_speed}"
        print(info)


def summon_companion(companions: list, kind: str):
    name = input("Nhập tên sinh vật: ").strip()
    try:
        if kind == "pet":
            atk = int(input("Nhập bonus_atk: "))
            companions.append(Pet(name, bonus_atk=atk))
        elif kind == "mount":
            spd = int(input("Nhập bonus_speed: "))
            companions.append(Mount(name, bonus_speed=spd))
        elif kind == "dragon":
            atk = int(input("Nhập bonus_atk: "))
            spd = int(input("Nhập bonus_speed: "))
            companions.append(Dragon(name, bonus_atk=atk, bonus_speed=spd))
        print("Triệu hồi thành công!")
    except ValueError:
        print("Chỉ số phải là số nguyên.")


def breed_companions(companions: list):
    show_companions(companions)
    try:
        i1 = int(input("Chọn sinh vật 1 (số thứ tự): ")) - 1
        i2 = int(input("Chọn sinh vật 2 (số thứ tự): ")) - 1
        if not (0 <= i1 < len(companions) and 0 <= i2 < len(companions)):
            print("Số thứ tự không hợp lệ.")
            return
        result = companions[i1] + companions[i2]
        companions.append(result)
        tag = type(result).__name__
        info = f"Cấp {result.level}"
        if isinstance(result, Pet):
            info += f", Atk: {result.bonus_atk}"
        if isinstance(result, Mount):
            info += f", Speed: {result.bonus_speed}"
        print(f">> Lai tạo thành công! Nhận được: {result.name} ({info})")
    except (ValueError, IndexError):
        print("Nhập không hợp lệ.")
    except TypeError as e:
        print(f"Lỗi: {e}")


def battle(companions: list):
    print("\n--- XUẤT CHIẾN ---")
    if not companions:
        print("Không có sinh vật nào trong đội hình.")
        return
    for c in companions:
        c.unleash_skill()


def main():
    companions = [
        Pet("Sói Trắng", bonus_atk=50),
        Mount("Hắc Mã", bonus_speed=20),
    ]

    while True:
        print("\n=== RIKKEI RPG - COMPANION SYSTEM ===")
        print("1. Xem đội hình")
        print("2. Triệu hồi Thú cưng (Pet)")
        print("3. Triệu hồi Thú cưỡi (Mount)")
        print("4. Triệu hồi Rồng Thần (Dragon)")
        print("5. Lai tạo sinh vật")
        print("6. Xuất chiến")
        print("7. Thoát")

        choice = input("Chọn (1-7): ").strip()

        if choice == "1":
            show_companions(companions)
        elif choice == "2":
            summon_companion(companions, "pet")
        elif choice == "3":
            summon_companion(companions, "mount")
        elif choice == "4":
            summon_companion(companions, "dragon")
        elif choice == "5":
            breed_companions(companions)
        elif choice == "6":
            battle(companions)
        elif choice == "7":
            print("Thoát game. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    print("=" * 50)
    print("DEMO CHỐNG BẪY")
    print("=" * 50)


    print("\n[Bẫy 1] Khởi tạo Companion trực tiếp:")
    try:
        c = Companion("Test")
    except TypeError as e:
        print(f"  TypeError: {e}")

    p1 = Pet("Sói Trắng", bonus_atk=50)
    p2 = Pet("Sói Đen", bonus_atk=60)
    m1 = Mount("Ngựa", bonus_speed=10)
    d1 = Dragon("Rồng Lửa", bonus_atk=500, bonus_speed=200)

    print(f"\n[Dragon] bonus_atk={d1.bonus_atk}, bonus_speed={d1.bonus_speed}")

    p3 = p1 + p2
    print(f"\n[Lai tạo] {p3.name} | Cấp {p3.level} | Atk: {p3.bonus_atk}")


    print("\n[Bẫy 2] Lai tạo khác loài (Pet + Mount):")
    try:
        bad = p1 + m1
    except TypeError as e:
        print(f"  TypeError: {e}")

    print("\n[Bẫy 2] Lai tạo với số (Pet + 10):")
    try:
        bad = p1 + 10
    except TypeError as e:
        print(f"  TypeError: {e}")

    print("\n[Đa hình] Xuất chiến:")
    equipped = [p3, m1, d1]
    for companion in equipped:
        companion.unleash_skill()

    print("\n" + "=" * 50)
    print("Vào chương trình chính...")
    print("=" * 50)
    main()