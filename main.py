from appFunctions import save_filtered_output_to_file
from appFunctions import extract_third_column_from_file
from appFunctions import extract_index_names_without_date_format
from appFunctions import extract_size_of_matched_element
from appFunctions import calculate_sum_of_elements
from appFunctions import calculate_average_of_elements
from appFunctions import find_index_size_for_today
from appFunctions import check_index_names_with_non_formatted
from appFunctions import calculate_all
file_path = "./filtered_output.txt"
save_filtered_output_to_file(file_path)


index_names = extract_third_column_from_file(file_path)


index_names_without_date, index_names_with_date_format = extract_index_names_without_date_format(index_names)
print("=========[ Indice Names with Date IS NOT Formatted ]========= (use 'u' prefix for these values)")
for index, wrongname in enumerate(index_names_with_date_format):
    print(f"Index {index}: {wrongname}")
print("=========[ Indice Names with Date IS Formatted ]=============")
for index, name in enumerate(index_names_without_date):
    print(f"Index {index}: {name}")

print("--------------------------")
user_input = input("Enter the index number: ")

if user_input.startswith('u'):

    number_part = user_input[1:]

    if number_part.isdigit():

        index_number = int(number_part)
        print("Extracted index number:", index_number)
        check_index_names_with_non_formatted(index_names_with_date_format, index_number, 'filtered_output.txt')
    else:
        print("Error: Input contains non-digit characters after 'u'.")
elif (user_input.lower() == "all"):
    calculate_all('filtered_output.txt')
else:
    if user_input.isdigit():

        index_number = int(user_input)
        print("==============[ Calculating ... ]==============")

        sizes_of_matched_element = extract_size_of_matched_element(index_names_without_date, index_number, 'filtered_output.txt')


        sum_of_elements = calculate_sum_of_elements(sizes_of_matched_element)
        average_of_elements = calculate_average_of_elements(sizes_of_matched_element)
        today_size_of_element = find_index_size_for_today(index_names_without_date, index_number , 'filtered_output.txt')
        print("Total size of indices of \""+index_names_without_date[index_number]+"\" : "+str(sum_of_elements)+" mb")
        print("Average size of indices of \""+index_names_without_date[index_number]+"\" : "+str(average_of_elements)+" mb")
        print(index_names_without_date[index_number]+" for today is : "+str(today_size_of_element)+" mb")
    else:
        print("Error! . Exiting ...")
