""""
1. Add Applicant: Allow the admissions office to add new applicants to the system. Each applicant should have a unique identifier (e.g., application number) and attributes such as name, GPA, SAT score, and list of extracurricular activities.
2. Analyze Applicant Data: Analyze applicant data to identify qualified candidates based on specific criteria (e.g., GPA threshold, SAT score threshold, participation in certain extracurricular activities).
3. Generate Admissions Decision: Determine admissions decisions (e.g., accepted, waitlisted, rejected) for each applicant based on the analysis of their data.
4. Generate Admissions Report: Generate a report listing all applicants along with their admissions decisions. Additionally, provide statistics on the number of applicants accepted, waitlisted, and rejected.
5. Exit: Provide an option for the user to exit the program.

Requirements 
1. Utilize while loops and for loops to iteratively process applicant data.
2. Utilize lists and 2D lists to store applicant information and manage applicant data.
3. Implement list methods to add, update, and retrieve data from lists.
4. Implement nested loops as necessary for analyzing applicant data and generating reports.
5. Ensure the program is modular and well-organized for ease of understanding and future modifications.
6. Provide clear output messages to indicate the admissions decision for each applicant and summarize the admissions report.
"""

class Applicant:
    def __init__(self,app_num,name, GPA, SAT_score, extracurr) -> None:
        self.app_num = app_num
        self.name = name
        self.GPA = GPA
        self.SAT_score = SAT_score
        self.extracurr = extracurr
        self.decision = None


def add_app (applicants):
    try:
        app_num = int(input("Enter you application number: "))
        name = input("Enter applicant name: ")
        gpa = float (input("Enter GPA: "))
        sat_score = int(input("Enter SAT score: "))
        extracurr = input("Enter extracurricular activities (comma-separated): ").split(',')

        new_app = Applicant(app_num, name, gpa, sat_score,extracurr)
        applicants.append(new_app)
    
    except ValueError:
        print("Invalid Input.")

def analyze_app(applicants):
    gpa_threshold = 3.0
    sat_threshold = 1000
    disered_extracurr = "negotiation"

    for applicant in applicants:
        if applicant.GPA >= gpa_threshold and applicant.SAT_score >= sat_threshold:
            if disered_extracurr in [x.strip() for x in applicant.extracurr]:
                applicant.decision = "Accepted"

            else:
                applicant.decision = "Waitlisted"
        else:
            applicant.decision = "Rejected"
    print(f"Applicant decision is: {applicant.decision}")


def gen_repo (applicants):
    accepted_count = 0
    waitlisted_count =0
    rejected_count =0

    print("\n Admission Report: ")
    print(
        "{:<10} {:<20} {:<10} {:<10} {:<10}".format(
            "App No.", "Name", "GPA", "SAT", "Decision"
        )
    )
    print("-" * 60)

    for applicant in applicants:

        print(
            "{:10} {:<20} {:<10.2f} {:<10} {:<10}".format(
                applicant.app_num,
                applicant.name,
                applicant.GPA,
                applicant.SAT_score,
                applicant.decision,
            )
        )
        if applicant.decision == "Accepted":
            accepted_count += 1
        elif applicant.decision == "Waitlisted":
            waitlisted_count += 1
        elif applicant.decision == "Rejected":
            rejected_count += 1
    print("-" * 60)
    print( f"Accepted: {accepted_count}, Waitlisted: {waitlisted_count}, Rejected: {rejected_count}\n" )


def main():
    applicants = []

    while True:
        print("\n Welcom to Admission System")
        print("1. Add applicant")
        print("2. Analyze Applicant Data")
        print("3. Generate Report")
        print("4. Exit")

        option = input("Choose an option: ")

        if option == '1':
            add_app(applicants)
        
        elif option == '2':
            analyze_app(applicants)

        elif option =='3':
            gen_repo(applicants)
        
        elif option == '4':
            print ("SEE YOU SOON .. ")
            break
        else:
            print ("Invalid input")

if __name__ == "__main__" :
    main()
