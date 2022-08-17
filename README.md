# Mine-app
**This is a app based on streamlit to help me control my life**
## The features 

## The introduction on Database
This app use Deta as the database.  
Until now, there are three databases.
- schedule_md
  >This database is used to store the schedule of each day in md.  
  > key : date of iso format.  
  > value : the schedule of that day.
- record_md
    >This database is used to store the record of each day as in md.  
  > key : date of iso format.  
  > value : the record of that day.  
- attention_md
    > This database is used to store the attention in md.  
  > key : only one key. ' attention'  
  > value : all attentions.