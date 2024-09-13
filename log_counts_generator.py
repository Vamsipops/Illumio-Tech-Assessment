import os
import glob

# Define file paths
protocol_file_path = "protocol-numbers.csv"
lookup_file_path = "lookup_data.csv"

# Function to read protocol numbers and create a dictionary
def read_protocol_numbers(file_path):
    protocol_dict = {}
    with open(file_path, 'r') as file:
        # Skip the header
        next(file)
        for line in file:
            keyword, decimal = line.strip().split(',')
            # Convert keyword to lowercase
            protocol_dict[decimal] = keyword.lower()
    return protocol_dict

# Function to read flow log data and count protocol occurrences
def count_protocol_occurrences(file_path, protocol_dict):
    protocol_counts = {}
    with open(file_path, "r") as file:
        for line in file:
            # Split the line into elements
            elements = line.split()
            # Get protocol name from the dictionary and create a tuple
            key = (elements[5], protocol_dict.get(elements[7], 'Unknown'))
            # Increment the count in the dictionary
            protocol_counts[key] = protocol_counts.get(key, 0) + 1
    return protocol_counts

# Function to read lookup data and create a dictionary
def read_lookup_data(file_path):
    lookup_dict = {}
    with open(file_path, 'r') as file:
        # Skip the header
        next(file)
        for line in file:
            dstport, protocol, tag = line.strip().split(',')
            lookup_dict[(dstport, protocol.lower())] = tag.lower()  # Convert tag to lowercase
    return lookup_dict

# Function to count tags based on protocol occurrences and lookup data
def count_tags(protocol_counts, lookup_dict):
    tag_counts = {}
    for key, value in protocol_counts.items():
        tag = lookup_dict.get(key, 'Untagged').lower()  # Convert tag to lowercase
        tag_counts[tag] = tag_counts.get(tag, 0) + value
    return tag_counts

# Function to write counts to a CSV file
def write_counts_to_csv(output_file, tag_counts, protocol_counts):
    # Create a list of dictionaries for tag counts
    tag_counts_list = [{'Tag': tag, 'Count': count} for tag, count in tag_counts.items()]
    # Create a list of dictionaries for protocol counts
    protocol_counts_list = [{'dstport': key[0], 'protocol': key[1], 'count': count} for key, count in protocol_counts.items()]
    # Define the headers for the CSV file
    tag_headers = ['Tag', 'Count']
    protocol_headers = ['Port', 'Protocol', 'Count']

    with open(output_file, 'w') as file:
        # Write the tag counts header
        file.write("Tag counts:\n")
        # Write the tag headers
        file.write(','.join(tag_headers) + '\n')
        # Write the tag counts
        for row in tag_counts_list:
            file.write(f"{row['Tag']},{row['Count']}\n")
        
        # Add a newline between the sections
        file.write('\n')

        # Write the protocol counts header
        file.write("Port/Protocol Combination Counts:\n")
        # Write the protocol headers
        file.write(','.join(protocol_headers) + '\n')
        # Write the protocol counts
        for row in protocol_counts_list:
            file.write(f"{row['dstport']},{row['protocol']},{row['count']}\n")

# Main function to orchestrate the process
def main():
    protocol_dict = read_protocol_numbers(protocol_file_path)
    lookup_dict = read_lookup_data(lookup_file_path)
    
    # Get all log files in the current directory starting with 'log' and ending with '.txt'
    log_files = glob.glob("log*.txt")

    if not log_files:
        print("No log files found to process.")
        return
    
    for log_file in log_files:
        protocol_counts = count_protocol_occurrences(log_file, protocol_dict)
        tag_counts = count_tags(protocol_counts, lookup_dict)
        output_file = f"output_{os.path.splitext(os.path.basename(log_file))[0]}.csv"
        write_counts_to_csv(output_file, tag_counts, protocol_counts)
        print(f"Output file '{output_file}' created successfully.")
    
    #print the message with the number of files processed
    print(f"{len(log_files)} files processed.")

# Run the main function
if __name__ == "__main__":
    main()