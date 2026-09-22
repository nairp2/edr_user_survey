QUESTIONS = [
    {
        'id': 'uses_dashboard_data',
        'type': 'multiselect',
        'label': 'Do you use data from the Tableau dashboards in your work?',
        'options': [
        'Yes',
        'No'
        ]
    },
    {
        'id': 'knows_basic_dashboard',
        'type': 'multiselect',
        'label': 'Do you know what dashboard to go to for basic content?',
        'options': [
        'Yes',
        'No'
        ]
    },
    {
        'id': 'dashboard_login_frequency',
        'type': 'multiselect',
        'label': 'How frequently do you log into the Tableau dashboards?',
        'options': [
        'All day, every day',
        'Once a day',
        'Once a week',
        'Once a month'
        ]
    },
    {
        'id': 'top_dashboard_data',
        'type': 'multiselect',
        'label': 'Please rank the top 3 types of data from the dashboards that you use the most.',
        'options': [
        'Vulnerability',
        'Master Device Records',
        'POAMs',
        'Data Quality',
        'KEVs',
        'Other'
        ]
        },
    {
        'id': 'dashboard_questions_answered',
        'type': 'text_area',
        'label': 'What questions are answered with the dashboard data? (Also let us know which dashboard you find it in.)'
    },
    {
        'id': 'desired_dashboard_metrics',
        'type': 'text_area',
        'label': 'What data or metrics would you want to see in the dashboards? (Please be specific.)'
    },
    {
        'id': 'dashboard_access_method',
        'type': 'multiselect',
        'label': 'How do you personally access data from the dashboards?',
        'options': [
        'I have Tableau access',
        'I see an attachment in an email',
        'I hear about the data in a meeting/Slack',
        'Other'
        ]
    },
    {
        'id': 'learned_dashboard_access',
        'type': 'multiselect',
        'label': 'How did you learn to access this data?',
        'options': [
        'Demo',
        'Confluence',
        'User Guide Tab',
        'Colleague',
        'Other'
        ]
    },
    {
        'id': 'preferred_training',
        'type': 'text_area',
        'label': 'For you, what is the best type of training for learning and understanding risk metrics and risk data?'
    },
    {
        'id': 'dashboard_access_barriers',
        'type': 'text_area',
        'label': 'What do you find are the barriers to access?'
    },
    {
        'id': 'preferred_visuals',
        'type': 'multiselect',
        'label': 'What visuals help you understand the data most clearly?',
        'options': [
        'Pie Charts',
        'Tables',
        'Bar Charts',
        'Area Charts',
        'Other'
        ]
    },
    {
        'id': 'monitor_size_resolution',
        'type': 'text_input',
        'label': 'What size monitor do you use for viewing data? (i.e. Mobile phone, iPad, desktop/laptop) Please include resolution.'
    },
    {
        'id': 'dashboard_speed_rating',
        'type': 'slider',
        'label': 'How quickly (in terms of speed/latency) do you find the dashboards to load? Please rank on a scale of 1-6 with 1 being frustratingly slow and 6 being remarkably fast.',
        'options': [
        '1 - Frustratingly slow',
        '2',
        '3',
        '4',
        '5',
        '6 - Remarkably fast'
        ]
    },
    {
        'id': 'slow_dashboard_issue',
        'type': 'text_input',
        'label': 'If you answered 1 or 2 to the question above regarding speed, which dashboard did you have an issue loading?'
    },
    {
        'id': 'preferred_download_format',
        'type': 'multiselect',
        'label': 'What format is most useful to you for viewing or downloading the dashboards?',
        'options': [
        'PDF',
        'Data (CSV file)',
        'Cross Tab',
        'Screenshots',
        'PowerPoint',
        'Other'
        ]
    },
    {
        'id': 'future_dashboard_improvement',
        'type': 'text_area',
        'label': 'Future Iterations: What is one improvement you’d like to see with the dashboards?'
    },
    {
        'id': 'missing_dashboard_functionality',
        'type': 'text_area',
        'label': 'What feature would you like in the dashboards that you feel is a necessity or missing functionality?'
    },
    {
        'id': 'alternative_reporting_tool',
        'type': 'text_input',
        'label': 'If you weren’t using Tableau, what other medium or tool would be useful to view your reports?'
    }
]