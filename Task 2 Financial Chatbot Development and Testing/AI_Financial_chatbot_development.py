#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Reading Financial data with growth percetage and summary (average) of growth percentage


# In[3]:


Financial_data_with_growth_percetage = pd.read_csv('final_financial_data_report.csv')
Average_of_growth_percentage = pd.read_csv('final_financial_data_%summary.csv')


# In[4]:


# Creating a basic Rule-based Logic AI-Driven Chatbot
def financial_chatbot():
    print("\nPlease enter your query")
    user_query = input()

    if user_query == "What is the total revenue?":
        revenue = Financial_data_with_growth_percetage[(Financial_data_with_growth_percetage['Year'] == fiscal_year) & (Financial_data_with_growth_percetage['Company'] == company_input)]['Total Revenue'].values[0]
        return f"The Total Revenue for {company_input} for fiscal year {fiscal_year} is $ {revenue}"
    
    elif user_query == "What is the Net Income?":
        net_income  = Financial_data_with_growth_percetage[(Financial_data_with_growth_percetage['Year'] == fiscal_year) & (Financial_data_with_growth_percetage['Company'] == company_input)]['Net Income'].values[0]
        return f"The Net Income for {company_input} for fiscal year {fiscal_year} is $ {net_income}"
    
    elif user_query == "What is the sum of total assets?":
        total_assets  = Financial_data_with_growth_percetage[(Financial_data_with_growth_percetage['Year'] == fiscal_year) & (Financial_data_with_growth_percetage['Company'] == company_input)]['Total Assets'].values[0]
        return f"The sum of Total Assets for {company_input} for fiscal year {fiscal_year} is $ {total_assets}"
    
    elif user_query == "What is the sum of total liabilities?":
        total_liabilities  = Financial_data_with_growth_percetage[(Financial_data_with_growth_percetage['Year'] == fiscal_year) & (Financial_data_with_growth_percetage['Company'] == company_input)]['Total Liabilities'].values[0]
        return f"The sum of Total Liabilities for {company_input} for fiscal year {fiscal_year} is $ {total_liabilities}"
    
    elif user_query == "What is cash flow from operating activities?":
        cash_ops = Financial_data_with_growth_percetage[(Financial_data_with_growth_percetage['Year'] == fiscal_year) & (Financial_data_with_growth_percetage['Company'] == company_input)]['Cash Flow from Operating Activities'].values[0]
        return f"The Cash Flow from Operating Activities for {company_input} for fiscal year {fiscal_year} is $ {cash_ops}"
    
    elif user_query == "What is the revenue growth(%) ?":
        revenue_growth = Financial_data_with_growth_percetage[(Financial_data_with_growth_percetage['Year'] == fiscal_year) & (Financial_data_with_growth_percetage['Company'] == company_input)]['Revenue Growth (%)'].values[0].round(4)
        return f"The Revenue Growth(%) for {company_input} for fiscal year {fiscal_year} is {revenue_growth}(%)"
    
    elif user_query == "What is the net income growth(%) ?":
        net_income_growth = Financial_data_with_growth_percetage[(Financial_data_with_growth_percetage['Year'] == fiscal_year) & (Financial_data_with_growth_percetage['Company'] == company_input)]['Net Income Growth (%)'].values[0].round(4)
        return f"The Net Income Growth(%) for {company_input} for fiscal year {fiscal_year} is {net_income_growth}(%)"
    
    elif user_query == "What is the assets growth(%) ?":
        assets_growth = Financial_data_with_growth_percetage[(Financial_data_with_growth_percetage['Year'] == fiscal_year) & (Financial_data_with_growth_percetage['Company'] == company_input)]['Assets Growth (%)'].values[0].round(4)
        return f"The Assets Growth(%) for {company_input} for fiscal year {fiscal_year} is {assets_growth}(%)"
    
    elif user_query == "What is the liabilities growth(%) ?":
        liabilities_growth = Financial_data_with_growth_percetage[(Financial_data_with_growth_percetage['Year'] == fiscal_year) & (Financial_data_with_growth_percetage['Company'] == company_input)]['Liabilities Growth (%)'].values[0].round(4)
        return f"The Liabilities Growth(%) for {company_input} for fiscal year {fiscal_year} is {liabilities_growth}(%)"
    
    elif user_query == "What is the cash flow from operations growth(%) ?":
        cash_ops_growth = Financial_data_with_growth_percetage[(Financial_data_with_growth_percetage['Year'] == fiscal_year) & (Financial_data_with_growth_percetage['Company'] == company_input)]['Cash Flow from Operations Growth(%)'].values[0].round(4)
        return f"The Cash Flow from Operations Growth(%) for {company_input} for fiscal year {fiscal_year} is {cash_ops_growth}(%)"
    
    elif user_query == "What is the year by year average revenue growth rate(%)?":
        year_avg_revenue_growth = Average_of_growth_percentage[(Average_of_growth_percentage['Company'] == company_input)]['Revenue Growth (%)'].values[0].round(4)
        return f"The Year By Year Average Revenue Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_revenue_growth}(%)"
     
    elif user_query == "What is the year by year average net income growth rate(%)?":
        year_avg_net_income_growth = Average_of_growth_percentage[(Average_of_growth_percentage['Company'] == company_input)]['Net Income Growth (%)'].values[0].round(4)
        return f"The Year By Year Net Income Revenue Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_net_income_growth}(%)"
    
    elif user_query == "What is the year by year average assets growth rate(%)?":
        year_avg_assets_growth = Average_of_growth_percentage[(Average_of_growth_percentage['Company'] == company_input)]['Assets Growth (%)'].values[0].round(4)
        return f"The Year By Year Average Assets Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_assets_growth}(%)"
    
    elif user_query == "What is the year by year average liabilities growth rate(%)?":
        year_avg_liabilities_growth = Average_of_growth_percentage[(Average_of_growth_percentage['Company'] == company_input)]['Liabilities Growth (%)'].values[0].round(4)
        return f"The Year By Year Average Liabilities Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_liabilities_growth}(%)"
    
    elif user_query == "What is the year by year average cash flow from operations growth rate(%)?":
        year_avg_cash_ops_growth = Average_of_growth_percentage[(Average_of_growth_percentage['Company'] == company_input)]['Cash Flow from Operations Growth(%)'].values[0].round(4)
        return f"The Year By Year Average Cash Flow from Operations Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_cash_ops_growth}(%)" 
    
    else:
        return "Sorry, I cannot provide information on the requested query."


# In[ ]:


# Test the chatbot
while True:
    print("----------------------------------------------------------------------------")
    user_input = input("\nEnter start to start the chatbot session; type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    elif user_input.lower() == "start":
        print("\nHello! Welcome to AI Driven Financial Chatbot!!!")
        print("\nI can help you with your financial queries")
        print("Please select the company name from below: -")
        print("\n1.Microsoft \n2.Tesla \n3.Apple")
        company_input = input("Enter company name : ").capitalize()
        if company_input not in ['Apple', 'Microsoft', 'Tesla']:
            print("Invalid Company Name. Please check and enter correct company name by starting the chatbot session again")
            break
        else:
            print("\nThe data for the fiscal year 2023, 2022, and 2021 is currently available")
            fiscal_year = int(input("The fiscal year for the selected company : "))
            if fiscal_year not in [2023, 2022, 2021]:
                print("Please enter a valid fiscal year by starting the chatbot session again")
                break
    else:
        print("Enter 'start' Properly!!!!! by starting the chatbot session again")
        break
            
        
    response = financial_chatbot()
    print(response)

