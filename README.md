# Bing-search-scraping-data-from-multiple-queries-from-a-csv-file
Now you can quickly search multiple keywords via input.csv file one by one and save the search result (Title, URLs, etc.) from BING.com respectively and save it in the CSV file.

Here are the steps:

Step 1: Create a csv with headers as following and add your bulk search queries. An example of input.csv would be like this:

**Input.CSV file content**

| Keyword  | URL |
| -------- | --- |
| Facebook | --- |
| Twitter  | --- |
| Etc.     | --- |

Step 2: Make sure to specify the **path for input.csv in line 12 as well as output.csv in line 25**. Make sure to use single quote, e.g. 'D:\\python\\input.csv'

Step 3: Limit the output as per your requirement in line 12 **limit=1**, currently, it's set to 1st result only.

PS: Edit the class in line 20 **.b_algo h2 a**, currently, I am only saving the URL of the search result.

**CSV Output:**

| Keyword | URL |
| -------- | ---------------- |
| Facebook | www.facebook.com |
| Twitter  | www.twitter.com |
