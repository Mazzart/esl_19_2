## Phone Assistant to search for a phone number

This is a simple program that returns a list up to 10 phone numbers from a database based on the user's input.
The user enters the first digits which must contain a phone number. Then the program looks for phone numbers 
that match to the input and returns list of them.

#### Usage:
Run the phone assistant:\
`$ python3 phone_assistant.py user_digits`

Run to get help messages:\
`$ python3 phone_assistant.py -h`

#### Tests:
Run tests:\
`$ pytest test_phone_assistant.py`

Run tests in verbose mode:\
`$ pytest -v test_phone_assistant.py`

Run tests in verbose mode and print to stdout:\
`$ pytest -v -s test_phone_assistant.py`

Run to see our custom fixtures:\
`$ pytest --fixtures`