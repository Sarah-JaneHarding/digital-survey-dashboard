import matplotlib.pyplot as plt
import numpy as np

# Sample data for the visualizations
# You can replace this data with actual survey data

devices = ['Laptop', 'Tablet', 'Smartphone', 'Desktop', 'None']
device_counts = [25, 15, 30, 10, 5]

independence_labels = ['Independence', 'Supervision']
independence_counts = [40, 60]

internet_access = ['Home', 'School', 'Mobile', 'None']
internet_counts = [50, 20, 25, 5]

web_usage_labels = ['Social Media', 'Educational', 'Gaming', 'News']
web_usage_counts = [40, 30, 20, 10]


# Function to create device ownership bar chart
def plot_device_ownership():
    plt.figure(figsize=(10, 5))
    plt.bar(devices, device_counts, color='black')
    plt.title('Device Ownership')
    plt.xlabel('Devices')
    plt.ylabel('Number of Learners')
    plt.grid(axis='y', linestyle='--', color='grey')
    plt.savefig('device_ownership.png', bbox_inches='tight', dpi=300)
    plt.show()

# Function to create independence vs supervision pie chart
def plot_independence_supervision():
    plt.figure(figsize=(7, 7))
    plt.pie(independence_counts, labels=independence_labels, autopct='%1.1f%%', startangle=140, colors=['black', 'lightgrey'])
    plt.title('Independence vs Supervision')
    plt.savefig('independence_vs_supervision.png', bbox_inches='tight', dpi=300)
    plt.axis('equal')
    plt.show()

# Function to create internet access bar chart
def plot_internet_access():
    plt.figure(figsize=(10, 5))
    plt.bar(internet_access, internet_counts, color='black')
    plt.title('Internet Access')
    plt.xlabel('Access Types')
    plt.ylabel('Number of Learners')
    plt.grid(axis='y', linestyle='--', color='grey')
    plt.savefig('internet_access.png', bbox_inches='tight', dpi=300)
    plt.show()

# Function to create websites/apps usage bar chart
def plot_web_usage():
    plt.figure(figsize=(10, 5))
    plt.bar(web_usage_labels, web_usage_counts, color='black')
    plt.title('Websites/Apps Usage')
    plt.xlabel('Websites/Apps')
    plt.ylabel('Usage (%)')
    plt.grid(axis='y', linestyle='--', color='grey')
    plt.savefig('web_usage.png', bbox_inches='tight', dpi=300)
    plt.show()


# Main function to call the visualization functions
if __name__ == '__main__':
    plot_device_ownership()
    plot_independence_supervision()
    plot_internet_access()
    plot_web_usage()