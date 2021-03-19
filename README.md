# Smart-Exam-Scheduler
Smart-Exam-Scheduler
This project builds a Smart-Exam-Scheduler based on a specific conditions.
As an input we have:
1. Time_slots = {t1,t2,t3,t4}
2. Available_halls = {A,B,C}
3. Intended_exams = {E1,E2,E3,E4,E5,E6,E7,E8,E9,E10}
4. Conditions:   1. The 1st exam should take place before the third exam.

                 2. The 10th exam occurs after the 9th and 4th exams.

                 3. The 1st, 3rd, and 4th exams should take place in either Hall A or Hall C.

                 4. The 7th, 8th, 9th, and 10th exams should be in either Hall A or Hall B.

                 5. There are no two exams occur at the same place and time.

This project is solved by using backtracking algorithm.
