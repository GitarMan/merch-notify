from bs4 import BeautifulSoup
import subprocess

# Change these variables
project_path = '/PATH/TO/PROJECT/'
url = 'https://TOPLEVELDOMAIN.com/collections/COMEDIAN?sort_by=created-descending'

# You will have to experiment to find the selector that retrieves the data you want.
# For context, the site this was built for uses Shopify. I haven't tested it, but there's a good chance this selector, or something similar, will work with other Shopify stores.
with open(project_path + "source.html") as source:
    soup = BeautifulSoup(source, features="lxml").find_all('div', {'class': 'h4 grid-view-item__title'})

with open(project_path + 'product_list') as product_list:
    old_list = product_list.read().splitlines()

new_list = []
for y in soup:
    new_list.append(y.string)

product_list = open(project_path + 'product_list', 'a')
for z in new_list:
    if (z not in old_list):
        print("New Item: " + z )
        product_list.write( '\n' + z )
        command = 'notify-send --urgency=critical "New Merch!" "' + url + '\n\n' + z + '"'
        subprocess.run([ command ], shell=True)
product_list.close()
