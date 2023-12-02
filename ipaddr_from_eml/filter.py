def remove_empty_brackets_lines(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Remove lines containing only []
    filtered_lines = [line for line in lines if line.strip() != '[]']

    with open(output_file, 'w') as outfile:
        outfile.writelines(filtered_lines)

# Example usage:
input_file_path = 'ipaddr_out.txt'  # Replace with your input file path
output_file_path = 'ipaddr_filtered_out.txt'  # Replace with your desired output file path

remove_empty_brackets_lines(input_file_path, output_file_path)
