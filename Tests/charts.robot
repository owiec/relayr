*** Settings ***
Library  Charts.py

*** Test Cases ***
Check if limit parameter works properly
    ${code}  ${message}  get top artist  artists=7
    Should be equal  ${code}  ${200}  ${message}
    Length should be  ${message}[artists][artist]  7

Check if limit parameter cannot be lower than 1
    ${code}  ${message}  get top artist  artists=0
    Should be equal  ${code}  ${200}  ${message}
    Should be equal   ${message}[error]  ${6}
    Should be equal   ${message}[message]  limit param out of bounds (1-1000)