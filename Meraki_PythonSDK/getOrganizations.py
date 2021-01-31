import csv
from datetime import datetime
import os

import meraki

# Either input your API key below by uncommenting line 10 and changing line 16 to api_key=API_KEY,
# or set an environment variable (preferred) to define your API key. The former is insecure and not recommended.
# For example, in Linux/macOS:  export MERAKI_DASHBOARD_API_KEY=093b24e85df15a3e66f1fc359f4c48493eaa1b73
# API_KEY = '093b24e85df15a3e66f1fc359f4c48493eaa1b73'


def main():
    # Instantiate a Meraki dashboard API session
    dashboard = meraki.DashboardAPI(
        api_key='066877fd75bd549c08944b759b4613df7182da22',
        base_url='https://api-mp.meraki.com/api/v0/',
        output_log=True,
        log_file_prefix=os.path.basename(__file__)[:-3],
        log_path='',
        print_console=False
    )

    # Get list of organizations to which API key has access
    organizations = dashboard.organizations.getOrganizations()
    
    # Iterate through list of orgs
    for org in organizations:
        print(f'\nAnalyzing organization {org["name"]}:')
        org_id = org['id']
        print(org_id)

        # Get list of networks in organization
        try:
            networks = dashboard.organizations.getOrganizationNetworks(org_id)
        except meraki.APIError as e:
            print(f'Meraki API error: {e}')
            print(f'status code = {e.status}')
            print(f'reason = {e.reason}')
            print(f'error = {e.message}')
            continue
        except Exception as e:
            print(f'some other error: {e}')
            continue
        
        print(networks)
       


if __name__ == '__main__':
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    print(f'\nScript complete, total runtime {end_time - start_time}')