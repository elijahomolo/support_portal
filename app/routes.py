from flask import Flask, render_template, flash, redirect, url_for
app = Flask(__name__)
import requests
from app import app
from logic import headers, auth

@app.route('/')
@app.route('/list')
def get_customer_list():
    customer_list = []
    customer_pages = []
    companies = []
    account = ''

    for i in range(1, 24):
        page = i
        url = 'https://support.anaconda.com/api/v2/companies?page={0}&per_page=100'.format(page)
        response = requests.get(url , headers=headers, auth=auth )
        desk_data = response.json()
        customers = desk_data['_embedded']['entries']
        customer_pages.append(customers)

    for page_number in range(len(customer_pages)):
        pages = customer_pages[page_number]
        #print(len(pages))
        for accounts in range(len(pages)):
            accounts = pages[accounts]
            custom_fields = accounts.get('custom_fields')
            anaconda_subscription_level = custom_fields.get('anaconda_subscription_level')

            if anaconda_subscription_level == "Anaconda Enterprise" or anaconda_subscription_level == "Implementation":
                customer_list.append(accounts)

    for item in customer_list:
        case_url = 'https://support.anaconda.com' + item.get('_links')['cases']['href']
        case_response = requests.get(case_url , headers=headers, auth=auth )
        case_data = case_response.json()
        ticket_count = case_data.get('total_entries')
        item['ticket_count'] = ticket_count



    return render_template('list.html', customer_list=customer_list, account=account)
