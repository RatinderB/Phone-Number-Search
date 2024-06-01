# Phone Number Search Script

This Python script searches for phone numbers in files within a specified directory and its subdirectories.

## Usage

1. Clone or download the repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using Python:

    ```sh
    python phone_search.py <directory> [--pattern <pattern>]
    ```

    - `<directory>`: The directory to search for phone numbers.
    - `--pattern <pattern>` (optional): The regex pattern to search for phone numbers. Default pattern: `\b\d{3}-\d{3}-\d{4}\b`.

4. The script will search for phone numbers in files within the specified directory and its subdirectories and print the phone numbers found.

## Example

Search for phone numbers in the `unzipped_content` directory using a custom pattern:

```sh
python phone_search.py unzipped_content --pattern r'\b\d{3}\.\d{3}\.\d{4}\b'
