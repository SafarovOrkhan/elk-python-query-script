import subprocess
import re
from datetime import datetime, timedelta

def save_filtered_output_to_file(file_path):

    command = "curl -XGET 'localhost:9200/_cat/indices?v' | column -t"


    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()


    output = output.decode('utf-8')


    lines = output.split('\n')


    filtered_output = '\n'.join(lines[1:])


    with open(file_path, "w") as file:
        file.write(filtered_output)

    print("Filtered output saved to:", file_path)

def extract_third_column_from_file(file_path):

    with open(file_path, "r") as file:
        lines = file.readlines()


    third_column = [line.split()[2] for line in lines]

    return third_column

def extract_index_names_without_date_format(index_names):

    date_pattern = r'\d{4}\.\d{2}\.\d{2}$'


    index_names_without_date = []


    index_names_with_non_formatted = []


    for index_name in index_names:

        if index_name.startswith('.'):
            index_names_with_non_formatted.append(index_name)
            continue


        match = re.search(date_pattern, index_name)
        if match:

            index_name_without_date = index_name[:match.start()]

            if index_name_without_date.endswith('-'):
                index_name_without_date = index_name_without_date[:-1]
            index_names_without_date.append(index_name_without_date)
        else:

            index_names_with_non_formatted.append(index_name)

    index_names_without_date_unique = list(set(index_names_without_date))

    return index_names_without_date_unique, index_names_with_non_formatted


def extract_size_of_matched_element(index_names_without_date_unique, index_number, file_path):

    if index_number < 0 or index_number >= len(index_names_without_date_unique):
        print("Error: Invalid index number.")
        return None


    index_name = index_names_without_date_unique[index_number]
    print("Selected Indice Name : ", index_name)


    sizes_of_matched_element = []


    with open(file_path, "r") as file:
        lines = file.readlines()


    for line in lines:

        parts = line.split()


        if len(parts) >= 9 and index_name in parts[2]:

            size_str = parts[8]

            if size_str.endswith('mb'):

                size_in_mb = float(parts[8].rstrip("mb"))
            elif size_str.endswith('kb'):

                size_in_mb = float(parts[8].rstrip("kb")) * 0.001
            elif size_str.endswith('gb'):

                size_in_mb = float(parts[8].rstrip("gb")) * 1024
            elif size_str.endswith('b'):

                size_in_mb = float(parts[8].rstrip("b")) * 0.000001

            sizes_of_matched_element.append(size_in_mb)

    print("Total number of files : "+str(len(sizes_of_matched_element)))
    return sizes_of_matched_element

def calculate_sum_of_elements(sizes_of_matched_element):

    total_sum = sum(sizes_of_matched_element)
    rounded_average = round(total_sum, 2)
    return rounded_average

def calculate_average_of_elements(sizes_of_matched_element):

    total_sum = sum(sizes_of_matched_element)


    average = total_sum / len(sizes_of_matched_element)


    rounded_average = round(average, 2)

    return rounded_average

def find_index_size_for_today(index_names_without_date_unique, index_name , filtered_output_path):

    today_date = datetime.today().strftime('%Y.%m.%d')

    full_name = index_names_without_date_unique[index_name]+"-"+str(today_date)
    specific_size = None

    with open(filtered_output_path, "r") as file:
        lines = file.readlines()


    for line in lines:

        parts = line.split()


        if len(parts) >= 9 and full_name in parts[2]:

            size_str = parts[8]

            if size_str.endswith('mb'):

                specific_size = float(parts[8].rstrip("mb"))
            elif size_str.endswith('kb'):

                specific_size = float(parts[8].rstrip("kb"))  * 0.001
            elif size_str.endswith('gb'):

                specific_size = float(parts[8].rstrip("gb")) * 1024
            elif size_str.endswith('b'):

                specific_size = float(parts[8].rstrip("b")) * 0.000001
    rounded_average = round(specific_size, 2)

    return rounded_average


def check_index_names_with_non_formatted (index_names_with_non_formatted, index_number, file_path):

    if index_number < 0 or index_number >= len(index_names_with_non_formatted):
        print("Error: Invalid index number.")
        return None


    index_name = index_names_with_non_formatted[index_number]
    print("Selected Indice Name : ", index_name)


    sizes_of_matched_element = None

    with open(file_path, "r") as file:
        lines = file.readlines()


    for line in lines:

        parts = line.split()


        if len(parts) >= 9 and index_name in parts[2]:

            size_str = parts[8]
            if size_str.endswith('mb'):

                size_in_mb = float(parts[8].rstrip("mb"))
            elif size_str.endswith('kb'):

                size_in_mb = float(parts[8].rstrip("kb"))  * 0.001
            elif size_str.endswith('gb'):

                size_in_mb = float(parts[8].rstrip("gb")) * 1024
            elif size_str.endswith('b'):

                size_in_mb = float(parts[8].rstrip("b")) * 0.000001

            print("Indice \""+index_name+"\" size is : "+str(size_in_mb)+" mb")

def calculate_all (file_path):

    sizes_of_matched_element = []


    with open(file_path, "r") as file:
        lines = file.readlines()


    for line in lines:

        parts = line.split()


        if len(parts) >= 9 :

            size_str = parts[8]

            if size_str.endswith('mb'):

                size_in_mb = float(parts[8].rstrip("mb"))
            elif size_str.endswith('kb'):

                size_in_mb = float(parts[8].rstrip("kb")) * 0.001
            elif size_str.endswith('gb'):

                size_in_mb = float(parts[8].rstrip("gb")) * 1024
            elif size_str.endswith('b'):

                size_in_mb = float(parts[8].rstrip("b")) * 0.000001

            sizes_of_matched_element.append(size_in_mb)


    total_sum = sum(sizes_of_matched_element)
    rounded_total = round(total_sum, 2)
    print("==============================")
    print("Total complete size of all indices : "+str(rounded_total)+" mb")
    print("==============================")
