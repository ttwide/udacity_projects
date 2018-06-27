# NEWS1.PY

## Design

Newsdata.py creates the three most important reports for a newspaper.  The newspaper has an SQL database with three tables:
* authors
* articles
* log

The program connects the news database, performs SQL queries, and then reports the answers to these questions.

1. What are the most popular three articles of all time?
2. Who are the most popular articles authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Instructions

1. Run news1.py in the command line prompt.
2. A message will display prompting the user to select a query based on the 3
questions above.  
Note:  If the user selects an option other than 1, 2, or 3 query 3 will run to
check for errors by day.
3.  The program will close the database an end.

If the user wants another query they must rerun the program.  
