# scripts-n-things
My collection of experiments and public failings..

monitors_to_csv.py

Usage:

export DD_SITE="datadoghq.com" DD_API_KEY="<API-KEY>" DD_APP_KEY="<APP-KEY>" DD_TAG="TagToSearchFor"

python3 "monitors_to_csv.py"
  
This will output a CSV file containing all monitors matching the tag identified in the DD_TAG system variable.
