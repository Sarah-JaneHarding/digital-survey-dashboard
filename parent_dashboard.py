import matplotlib.pyplot as plt
import pandas as pd

# Sample parent survey data
# Device ownership
device_data = {'Device': ['Smartphone', 'Tablet', 'Laptop', 'Desktop', 'None'],
               'Count': [40, 15, 25, 10, 10]}
device_df = pd.DataFrame(device_data)

# Independence vs Supervision
independence_data = {'Category': ['Independence', 'Supervised'], 'Count': [60, 40]}
independence_df = pd.DataFrame(independence_data)

# Internet access
internet_access_data = {'Access': ['Yes', 'No'], 'Count': [80, 20]}
internet_access_df = pd.DataFrame(internet_access_data)

# Internet freedom
freedom_data = {'Freedom Level': ['High', 'Medium', 'Low'], 'Count': [30, 50, 20]}
freedom_df = pd.DataFrame(freedom_data)

# Websites/apps usage
usage_data = {'Usage': ['Educational', 'Social Media', 'Entertainment', 'None'], 'Count': [50, 30, 15, 5]}
usage_df = pd.DataFrame(usage_data)

# Generating the visualizations...

# Device Ownership Stacked Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(device_df['Device'], device_df['Count'], color='black')
plt.title('Device Ownership')
plt.xlabel('Device')
plt.ylabel('Number of Parents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('device_ownership.png', format='png')

# Independence vs Supervision Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(independence_df['Count'], labels=independence_df['Category'], autopct='%1.1f%%', startangle=140, colors=['black', 'gray'])
plt.title('Independence vs Supervision')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig('independence_vs_supervision.png', format='png')

# Internet Access Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(internet_access_df['Count'], labels=internet_access_df['Access'], autopct='%1.1f%%', startangle=140, colors=['black', 'gray'])
plt.title('Internet Access')
plt.axis('equal')
plt.savefig('internet_access.png', format='png')

# Internet Freedom Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(freedom_df['Freedom Level'], freedom_df['Count'], color='black')
plt.title('Internet Freedom')
plt.xlabel('Freedom Level')
plt.ylabel('Number of Parents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('internet_freedom.png', format='png')

# Websites/Apps Usage Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(usage_df['Usage'], usage_df['Count'], color='black')
plt.title('Websites/Apps Usage')
plt.xlabel('Usage Type')
plt.ylabel('Number of Parents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('websites_apps_usage.png', format='png')

# Show all plots
plt.show()