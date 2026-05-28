def calculate_attendance(attendance_list):
    # 1. 合計を計算
    total_attendance = 0
    for count in attendance_list:
        total_attendance += count

    # 2. 平均を計算（空リストは 0）
    if len(attendance_list) > 0:
        average_attendance = total_attendance / len(attendance_list)
    else:
        average_attendance = 0

    # 3. 出力用変数に代入して表示
    total = total_attendance
    average = average_attendance
    print("Total attendance:", total)
    print("Average attendance:", average)

# Sample calls
attendance_numbers = [15, 18, 20, 17, 19]
calculate_attendance(attendance_numbers)

empty_attendance = []
calculate_attendance(empty_attendance)