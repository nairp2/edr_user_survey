QUESTIONS = [
    {
    'id': 'requesting_agency_organization',
    'type': 'text_input',
    'label': 'What agency or organization is requesting this deployment?'
    },
    {
    'id': 'business_owner',
    'type': 'text_input',
    'label': 'Who is the business owner accountable for your environment?'
    },
    {
    'id': 'technical_poc',
    'type': 'text_input',
    'label': 'Who is the primary implementation contact (Technical POC)?'
    },
    {
    'id': 'environment_platform_name',
    'type': 'text_input',
    'label': 'What is the unique environment or platform name?'
    },
    {
    'id': 'environment_type',
    'type': 'text_input',
    'label': 'What is the environment type (Production, Development, Test, QA, DR, Sandbox)?'
    },
    {
    'id': 'hosting_model',
    'type': 'text_input',
    'label': 'What is the hosting model (On-Premises, Hybrid, Cloud, Colocation)?'
    },
    {
    'id': 'cloud_service_provider',
    'type': 'text_input',
    'label': 'Which cloud service provider is used (AWS, Azure, GCP, OCI, etc.), or is it N/A for on-premises?'
    },
    {
    'id': 'cloud_regions',
    'type': 'text_input',
    'label': 'Which cloud regions (CSP) are hosting the workloads?'
    },
    {
    'id': 'data_classification',
    'type': 'text_input',
    'label': 'What is your data classification (Public, Internal, CUI, PII, PHI, etc.)?'
    },
    {
    'id': 'fisma_fedramp_impact_level',
    'type': 'text_input',
    'label': 'What is your FISMA or FedRAMP impact level (Low, Moderate, High, or N/A)?'
    },
    {
    'id': 'operating_systems_versions',
    'type': 'text_area',
    'label': 'What operating systems (OS types) and versions are being used?'
    },
    {
    'id': 'physical_servers',
    'type': 'text_input',
    'label': 'How many physical servers are in the environment?'
    },
    {
    'id': 'virtual_machines',
    'type': 'text_input',
    'label': 'How many virtual machines are in the environment?'
    },
    {
    'id': 'windows_endpoints',
    'type': 'text_input',
    'label': 'How many Windows desktops or laptops exist?'
    },
    {
    'id': 'linux_endpoints',
    'type': 'text_input',
    'label': 'How many Linux endpoints exist?'
    },
    {
    'id': 'macos_endpoints',
    'type': 'text_input',
    'label': 'How many macOS endpoints exist?'
    },
    {
    'id': 'vdi_citrix_avd_endpoints',
    'type': 'text_input',
    'label': 'How many VDI, Citrix, or AVD endpoints exist?'
    },
    {
    'id': 'container_platform',
    'type': 'text_input',
    'label': 'What container platform is used (OpenShift, Kubernetes, Docker, ECS, Rancher, etc.)?'
    },
    {
    'id': 'kubernetes_distribution',
    'type': 'text_input',
    'label': 'What Kubernetes distribution is used (EKS, AKS, GKE, OpenShift, K3s, upstream)?'
    },
    {
    'id': 'kubernetes_management',
    'type': 'text_input',
    'label': 'Is Kubernetes managed or unmanaged?'
    },
    {
    'id': 'kubernetes_clusters',
    'type': 'text_input',
    'label': 'How many total clusters exist?'
    },
    {
    'id': 'kubernetes_worker_nodes',
    'type': 'text_input',
    'label': 'How many total worker nodes exist?'
    },
    {
    'id': 'kubernetes_control_plane_nodes',
    'type': 'text_input',
    'label': 'How many total control plane nodes exist?'
    },
    {
    'id': 'running_containers',
    'type': 'text_input',
    'label': 'What is the approximate number of running containers?'
    },
    {
    'id': 'kubernetes_namespaces',
    'type': 'text_input',
    'label': 'How many namespaces exist?'
    },
    {
    'id': 'container_registry',
    'type': 'text_input',
    'label': 'Which container registry is used (ECR, ACR, GCR, Harbor, Artifactory, etc.)?'
    },
    {
    'id': 'serverless_services',
    'type': 'text_area',
    'label': 'What serverless services are used (Lambda, Azure Functions, Cloud Run, etc.)?'
    },
    {
    'id': 'existing_edr_platform',
    'type': 'text_input',
    'label': 'What is the existing EDR platform?'
    },
    {
    'id': 'antivirus_solution',
    'type': 'text_input',
    'label': 'What is your current antivirus solution?'
    },
    {
    'id': 'asset_inventory_source',
    'type': 'text_input',
    'label': 'What is the asset inventory source (CMDB, SCCM, Intune, ServiceNow, Tanium, etc.)?'
    },
    {
    'id': 'cmdb_available',
    'type': 'text_input',
    'label': 'Is a CMDB available?'
    },
    {
    'id': 'configuration_management_tool',
    'type': 'text_input',
    'label': 'What configuration management tool is used (Ansible, Puppet, Chef, Salt, etc.)?'
    },
    {
    'id': 'deployment_tool',
    'type': 'text_input',
    'label': 'What deployment tool is used (MECM/SCCM, Intune, Tanium, BigFix, JAMF, scripting)?'
    },
    {
    'id': 'siem_platform',
    'type': 'text_input',
    'label': 'What SIEM platform is used (Splunk, Sentinel, QRadar, Elastic, Chronicle, etc.)?'
    },
    {
    'id': 'proxy_requirements',
    'type': 'text_area',
    'label': 'Is a proxy required, and if so, what are the proxy details?'
    },
    {
    'id': 'crowdstrike_https_connectivity',
    'type': 'text_input',
    'label': 'Can systems reach the CrowdStrike cloud via HTTPS?'
    },
    {
    'id': 'outbound_firewall_restrictions',
    'type': 'text_area',
    'label': 'What outbound firewall restrictions or allowlists are in place?'
    },
    {
    'id': 'mission_critical_assets',
    'type': 'text_area',
    'label': 'Which mission-critical assets/systems require coordination?'
    },
    {
    'id': 'legacy_unsupported_systems',
    'type': 'text_area',
    'label': 'What legacy or unsupported systems exist (unsupported OS, OT, embedded, appliances)?'
    },
    {
    'id': 'approved_exceptions',
    'type': 'text_area',
    'label': 'What approved file, directory, process, or patch exceptions exist? Include justification, approving authority, and expected duration in your response.'
    },
    {
    'id': 'vendor_managed_appliances',
    'type': 'text_area',
    'label': 'What vendor-managed appliances exist where CrowdStrike installation may be restricted? Include vendor, model, support limitations, and contact information.'
    },
    {
    'id': 'total_assets',
    'type': 'text_input',
    'label': 'What is the total number of assets including endpoints, servers, and cloud workloads?'
    },
    {
    'id': 'preferred_deployment_window',
    'type': 'text_input',
    'label': 'What is the preferred deployment window?'
    },
    {
    'id': 'compliance_operational_constraints',
    'type': 'text_area',
    'label': 'What compliance or operational constraints apply?'
    },
    {
    'id': 'additional_notes_comments',
    'type': 'text_area',
    'label': 'Include any additional notes or comments you have pertaining to this EDR Data Call.'
    },
]