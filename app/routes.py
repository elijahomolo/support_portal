from flask import Flask, render_template, flash, redirect, url_for
app = Flask(__name__)
import requests
from app import app
from logic import headers, auth

@app.route('/')
@app.route('/list')
def get_customer_list():
    customer_pages = []
    companies = []
    for i in range(1, 24):
        page = i
        url = 'https://support.anaconda.com/api/v2/companies?page={0}&per_page=100'.format(page)
        response = requests.get(url , headers=headers, auth=auth )
        desk_data = response.json()
        customers = desk_data['_embedded']['entries']
        customer_pages.append(customers)

    customer_list = []
    for page_number in range(len(customer_pages)):
        pages = customer_pages[page_number]
        #print(len(pages))
        for accounts in range(len(pages)):
            customer_list.append(pages[accounts])
            #return(customer_list)
    for a in range(len(customer_list)):
        account = customer_list[a]
        if account.get('name') == "ExxonMobil":
            ExxonMobil = account
            #return(ExxonMobil)

    return render_template('list.html', account=ExxonMobil)
