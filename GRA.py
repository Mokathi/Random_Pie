import statistics

def convert_to_degrees(degrees, minutes, seconds):
    return degrees + minutes/60 + seconds/3600

def calculate_stats(data):
    mean = statistics.mean(data)
    variance = statistics.variance(data)
    return mean, variance

student_a = [convert_to_degrees(108, 26, int(x.split("′")[1])) for x in ["108° 26′ 10''", "108° 26′ 10''", "108° 26′ 08''", "108° 26′ 10''", "108° 26′ 10''", "108° 26′ 05''", "108° 26′ 04''", "108° 26′ 10''", "108° 26′ 11''", "108° 26′ 05''"]]
    
student_b = [convert_to_degrees(108, 26, int(x.split("′")[1])) for x in ["108° 26′ 12''", "108° 26′ 11''", "108° 26′ 09''", "108° 26′ 13''", "108° 26′ 12''", "108° 26′ 01''", "108° 26′ 01''", "108° 26′ 11''", "108° 26′ 14''", "108° 26′ 03''"]]

student_a_mean, student_a_variance = calculate_stats(student_a)
student_b_mean, student_b_variance = calculate_stats(student_b)

print(f'Student A: Mean={student_a_mean}, Variance={student_a_variance}')
print(f'Student B: Mean={student_b_mean}, Variance={student_b_variance}')