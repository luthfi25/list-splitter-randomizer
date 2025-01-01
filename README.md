# list-splitter-randomizer
Python script to split and randomize any integer list into any number of groups.

## Table of Contents
- [Usage](#usage)
- [Webapp](#webapp)
- [Example](#example)
- [Prerequisites](#prerequisites)

## Usage
1. Create a file called **input.txt** and place it in the same folder as **random_split_list.py**.
2. On the first line of **input.txt**, insert a comma-separated list of integers.
3. On the second line of **input.txt**, insert the desired number of groups the list will be divided into.
4. Run the script by typing `python3 random_split_list.py`.

For any troubles or questions, try asking your friendly Copilot for a more detailed and personalized answer :D

## Webapp
You can also use this project as a web application. Access the webapp at [THIS_URL](THIS_URL).

### Instructions
1. Enter a comma-separated list of integers in the "Enter numbers" field.
2. Enter the desired number of groups in the "Enter number of groups" field.
3. Click the "Submit" button to see the randomized groups.
4. Use the "Copy to Clipboard" button to copy the contents of each group.

## Example
**input.txt**:

> ```
> 123,123,123,123
> 2
> ```

**Output**:

> ```
> Total elements to include: 4
> Number of groups: 2
> Max elements for a single group: 2
>
> Group 1
> 123
> 123
>
> Group 2
> 123
> 123
> ```

## Prerequisites
- Python 3.x