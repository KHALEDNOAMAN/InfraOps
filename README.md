![InfraOps](https://capsule-render.vercel.app/api?type=waving&color=0:000000,100:1f2937&height=250&section=header&text=InfraOps&fontSize=90&fontColor=ffffff)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/postgresql-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

Data Center Infrastructure Management (DCIM) and Asset Management solution designed for modern IT operations. InfraOps provides comprehensive visibility into your entire hardware ecosystem, from rack placement and power consumption to lifecycle tracking and capacity forecasting.

Our platform unifies asset inventory with change management, ensuring that every deployment, maintenance task, and retirement is properly documented and approved. Built with an API-first approach, it integrates seamlessly with existing monitoring tools and automation pipelines.

By combining real-time metrics with predictive analytics, InfraOps enables proactive capacity planning and helps prevent resource bottlenecks before they impact production workloads.

## Architecture

```
React Dashboard --> FastAPI Backend --> PostgreSQL
                         |
               Capacity Engine + Monitoring
                         |
               Change Management Workflows
```

## Modules
- **Data Center Management**: Visualize floor plans, racks, and environmental data.
- **Asset Inventory**: Track servers, switches, storage, and virtual machines.
- **Lifecycle Tracking**: Manage assets from procurement to disposal.
- **Capacity Planning**: Forecast CPU, RAM, storage, and power usage.
- **Change Management**: ITIL-aligned change request workflows.

## Features
1. Interactive rack elevations
2. Custom asset types and attributes
3. Automated warranty tracking
4. Power and thermal monitoring
5. Predictive capacity alerts
6. Change request approvals
7. Maintenance scheduling
8. Software license compliance
9. VM-to-physical host mapping
10. Network port connections
11. Audit logging
12. Role-based access control
13. RESTful API
14. Dark mode UI
15. Bulk import/export

## Tech Stack
| Component | Technology |
|-----------|------------|
| Frontend | React, TypeScript, Tailwind CSS |
| Backend | FastAPI, Python |
| Database | PostgreSQL |
| Cache | Redis |
| Container | Docker |

## UI Mockups

### Floor Map
```
[Rack A1] [Rack A2] [Rack A3]
[Rack B1] [Rack B2] [Rack B3]
```

### Change Request Workflow
```
Draft -> Pending -> Approved -> In Progress -> Completed
```

## Getting Started
```bash
docker-compose up -d
```

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/assets` | GET | List assets |
| `/api/assets/{id}` | GET | Get asset details |
| `/api/datacenters` | GET | List datacenters |
| `/api/changes` | GET | List change requests |
| *(30+ more endpoints)* | | |

## Environment Variables
See `.env.example`.

## Roadmap
- VMware vSphere integration
- Ansible playbooks
- SNMP monitoring
- Grafana dashboards

## License
MIT
