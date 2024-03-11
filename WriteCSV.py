import csv
import os

class WriteCSV(object):
    
    def writeIntoCSV(self, decisions, degree):
        if not decisions:
            print(decisions)
            print("No data to write")
            return

        file_path = r'C:\UNI\DataMining\Project\scrapper\YM_Scraper\Scraped_Dataset\dataset.csv'
        file_exists = os.path.isfile(file_path)
        
        with open(file_path, 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['university','state', 'country' , 'major', 'degree', 'mcat', 'gmat', 'lsat', 'toefl speaking', 'toefl listening', 'toefl writing', 'toefl reading', 'ielts speaking', 'ielts listening', 'ielts writting', 'itelts reading', 'gre verbal', 'gre quant', 'gre awa', 'gpa', 'highschool gpa', 'sat', 'act', 'work experience', 'research papers'])
            for decision in decisions:
                # print(decision['gradprofile']['is_undergrad'])
                university = decision['uni_name'] if decision['uni_name'] else ''
                state = decision['uni_state'] if decision['uni_state'] else ''
                country = decision['uni_country'] if decision['uni_country'] else ''
                major = decision['major']["name"] if decision['major']["name"] else ''
                degree = degree
                mcat = decision['gradprofile']["mcat"] if decision['gradprofile']["mcat"] else ''
                gmat = decision['gradprofile']['gmat'] if decision['gradprofile']['gmat'] else ''
                lsat = decision['gradprofile']['lsat'] if decision['gradprofile']['lsat'] else ''
                toefl_speaking = decision['gradprofile']['toefl']['speaking'] if decision['gradprofile']['toefl'] else ''
                toefl_listening = decision['gradprofile']['toefl']['listening'] if decision['gradprofile']['toefl'] else ''
                toefl_writing = decision['gradprofile']['toefl']['writing'] if decision['gradprofile']['toefl'] else ''
                toefl_reading = decision['gradprofile']['toefl']['reading'] if decision['gradprofile']['toefl'] else ''
                ielts_speaking = decision['gradprofile']['ielts']['speaking'] if decision['gradprofile']['ielts'] else ''
                ielts_listening = decision['gradprofile']['ielts']['listening'] if decision['gradprofile']['ielts'] else ''
                ielts_writting = decision['gradprofile']['ielts']['writing'] if decision['gradprofile']['ielts'] else ''
                ielts_reading = decision['gradprofile']['ielts']['reading'] if decision['gradprofile']['ielts'] else ''
                gre_verbal = decision['gradprofile']['gre']['verbal'] if decision['gradprofile']['gre'] else ''
                gre_quant = decision['gradprofile']['gre']['quant'] if decision['gradprofile']['gre'] else ''
                gre_awa = decision['gradprofile']['gre']['awa'] if decision['gradprofile']['gre'] else ''
                gpa = decision['gradprofile']['cgpa'] if decision['gradprofile']['cgpa'] else ''
                highschool_gpa = decision['gradprofile']['high_school_cgpa'] if decision['gradprofile']['high_school_cgpa'] else ''
                sat = decision['gradprofile']['sat'] if decision['gradprofile']['sat'] else ''
                act = decision['gradprofile']['act'] if decision['gradprofile']['act'] else ''
                work_experience = decision['gradprofile']['work_ex_months'] if decision['gradprofile']['work_ex_months'] else 0
                research_papers = decision['gradprofile']['research_papers'] if decision['gradprofile']['research_papers'] else 0
                
                # print(
                #     "University: ", university, "\n",
                #     "State: ", state, "\n",
                #     "Country: ", country, "\n",
                #     "Major: ", major, "\n",
                #     "Degree: ", degree, "\n",
                #     "MCAT: ", mcat, "\n",
                #     "GMAT: ", gmat, "\n",
                #     "LSAT: ", lsat, "\n",
                #     "TOEFL Speaking: ", toefl_speaking, "\n",
                #     "TOEFL Listening: ", toefl_listening, "\n",
                #     "TOEFL Writing: ", toefl_writing, "\n",
                #     "TOEFL Reading: ", toefl_reading, "\n",
                #     "IELTS Speaking: ", ielts_speaking, "\n",
                #     "IELTS Listening: ", ielts_listening, "\n",
                #     "IELTS Writing: ", ielts_writting, "\n",
                #     "IELTS Reading: ", ielts_reading, "\n",
                #     "GRE Verbal: ", gre_verbal, "\n",
                #     "GRE Quant: ", gre_quant, "\n",
                #     "GRE AWA: ", gre_awa, "\n",
                #     "GPA: ", gpa, "\n",
                #     "High School GPA: ", highschool_gpa, "\n",
                #     "SAT: ", sat, "\n",
                #     "ACT: ", act, "\n",
                #     "Work Experience: ", work_experience, "\n",
                #     "Research Papers: ", research_papers, "\n"
                # )
                
                writer.writerow([university, state, country, major, degree, mcat, gmat, lsat, toefl_speaking, toefl_listening, toefl_writing, toefl_reading, ielts_speaking, ielts_listening, ielts_writting, ielts_reading, gre_verbal, gre_quant, gre_awa, gpa, highschool_gpa, sat, act, work_experience, research_papers])