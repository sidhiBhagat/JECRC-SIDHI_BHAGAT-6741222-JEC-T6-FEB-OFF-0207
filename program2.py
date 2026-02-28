class Solution:

    def subject_average(self, students):
        subject_total = {}
        subject_count = {}
        ## Write your code here and don't forget to add return keyword
        for student in students:
            marks = student["marks"]

            for subject, score in marks.items():
                if subject in subject_total:
                    subject_total[subject] += score
                    subject_count[subject] += 1
                else:
                    subject_total[subject] = score
                    subject_count[subject] = 1
        #Average
        subject_avg = {}
        for subject in subject_total:
            subject_avg[subject] = subject_total[subject] / subject_count[subject]

        # Find highest average
        highest_subject = max(subject_avg, key=subject_avg.get)

        return subject_avg, highest_subject