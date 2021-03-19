Time_slots = ["t1", "t2", "t3", "t4"]
Halls = ["A", "B", "C"]
Exams = ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10"]
Schedule = []
reserved = []
Domain = [[time, hall] for time in Time_slots for hall in Halls]
# Just for printing out the conditions
Conditions = ["1. The 1st exam should take place before the third exam",
              "2. The 10th exam occurs after the 9th and 4th exams",
              "3. The 1st, 3rd, and 4th exams should take place in either Hall A or Hall C",
              "4. The 7th, 8th, 9th, and 10th exams should be in either Hall A or Hall B",
              "5. There are no two exams occur at the same place and time"]
# [Exam, Time, Hall]
# [ 0  ,   1 ,   2 ]


def solve(schedule):

    if len(schedule) == 10:
        return schedule

    for exam in Exams:
        if exam in reserved:
            continue

        for value in Domain:
            if valid([exam, value[0], value[1]]):
                schedule.append([exam, value[0], value[1]])
                reserved.append(exam)
                result = solve(schedule)
                # if result != False
                if result:
                    return schedule
                schedule.remove([exam, value[0], value[1]])
                reserved.remove(exam)
        return False


def valid(triple_item):

    # 1.The 1st exam should take place before the third exam
    if triple_item[0] in ["E1", "E3"]:

        # if E3,E1 has a record in the schedule return its time
        # [E1,t1,A] ==> [exam,time,hall]
        exam3_slot = [i[1] for i in Schedule if i[0] == "E3"]
        exam1_slot = [i[1] for i in Schedule if i[0] == "E1"]

        # if E3 in schedule
        if exam3_slot:
            # if the candidate time for E1 > time(E3)
            if Time_slots.index(triple_item[1]) >= Time_slots.index(exam3_slot[0]):
                # then, not valid
                return False
        # if E1 in schedule
        elif exam1_slot:
            # if time(E1) > the candidate time for E3
            if Time_slots.index(exam1_slot[0]) >= Time_slots.index(triple_item[1]):
                # then, not valid
                return False

    # 2.The 10th exam occurs after the 9th and 4th exams
    if triple_item[0] in ["E4", "E9", "E10"]:
        # if Exam has a record in the schedule return its time
        exam4_slot = [i[1] for i in Schedule if i[0] == "E4"]
        exam9_slot = [j[1] for j in Schedule if j[0] == "E9"]
        exam10_slot = [k[1] for k in Schedule if k[0] == "E10"]

        # if E4 in schedule and the candidate is E10
        if exam4_slot and triple_item[0] == "E10":
            # if the candidate time for E10 <= time(E4)
            if Time_slots.index(triple_item[1]) <= Time_slots.index(exam4_slot[0]):
                return False
        # if E9 in schedule and the candidate is E10
        if exam9_slot and triple_item[0] == "E10":
            if Time_slots.index(triple_item[1]) <= Time_slots.index(exam9_slot[0]):
                return False
        # if E10 in schedule and the candidate is E4
        elif exam10_slot and triple_item[0] == "E4":
            # if the candidate time for E10 < time(E4)
            if Time_slots.index(exam10_slot[0]) <= Time_slots.index(triple_item[1]):
                return False
        elif exam10_slot and triple_item[0] == "E9":
            # if the candidate time for E10 < time(E9)
            if Time_slots.index(exam10_slot[0]) <= Time_slots.index(triple_item[1]):
                return False

    # 3.The 1st, 3rd, and 4th exams should take place in either Hall A or Hall C
    if triple_item[0] in ["E1", "E3", "E4"]:
        if triple_item[2] == "B":
            return False

    # 4.The 7th, 8th, 9th, and 10th exams should be in either Hall A or Hall B
    if triple_item[0] in ["E7", "E8", "E9", "E10"]:
        if triple_item[2] == "C":
            return False

    # 5.There are no two exams occur at the same place and time
    for block in Schedule:
        if triple_item[1] == block[1] and triple_item[2] == block[2]:
            return False

    return True


def print_schedule(schedule):
    for condition in Conditions:
        print(condition)
    print("---"*19)
    print("The schedule depending on the previous conditions wil be:")
    for event in schedule:
        print(event[0]+"\t"+event[1]+"\t"+event[2])


solve(Schedule)
print_schedule(Schedule)
