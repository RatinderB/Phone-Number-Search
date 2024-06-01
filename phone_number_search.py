import os
import re
import logging
import argparse

def setup_logger():
    logger = logging.getLogger('phone_search')
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

def search_phone_numbers(directory, pattern):
    phone_pattern = re.compile(pattern)
    for folder, sub_folders, files in os.walk(directory):
        for f in files:
            file_path = os.path.join(folder, f)
            try:
                with open(file_path, 'r') as search_file:
                    for line in search_file:
                        phone_numbers = phone_pattern.findall(line)
                        for phone_number in phone_numbers:
                            logger.info(phone_number)
            except (IOError, OSError) as e:
                logger.error(f'Error opening/reading file {file_path}: {e}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search for phone numbers in files.')
    parser.add_argument('directory', type=str, help='The directory to search in.')
    parser.add_argument('--pattern', type=str, default=r'\b\d{3}-\d{3}-\d{4}\b', help='The regex pattern to search for.')

    args = parser.parse_args()
    
    logger = setup_logger()
    
    # Debugging output to ensure the pattern is correctly interpreted
    logger.info(f'Using pattern: {args.pattern}')
    
    search_phone_numbers(args.directory, args.pattern)